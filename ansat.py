from flask import Flask
from flask import request
from flask import session
from flask import redirect 
import mysql.connector

# connect to the MySQL server
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="ansat"
)

# create a cursor object
mycursor = mydb.cursor()

app = Flask(__name__)
app.secret_key="your_secret_bs"
DOCT='<!Doctype html>'

HEAD = """
    <head> 
        <title>Ansat | Home </title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
    </head>
    """
BODY_START = "<body>"
BODY_END = "</body>"

buttons=f"""
<div class="col">
    <div class="col-4">
        <div id="simple-list-example" class="d-flex flex-column gap-2 simple-list-example-scrollspy text-center">
        <a class="p-1 rounded" href="/logout">Log Out</a>
        <a class="p-1 rounded" href="/poststuff?postid=job">Post a job</a>
        <a class="p-1 rounded" href="/poststuff?postid=repair">Post a repair</a>
        </div>
    </div>
</div>"""

def create_navigation_bar():
    if session.get('logged_in')==True:
        username=session.get("username")
        login_html = f"""
        <a class="btn btn-primary" href="/myprofile">Hello {username}</a>
        """
    else:
        login_html = """
            <a class="btn btn-primary" href="/login" role="button">Login</a>
        """

    return f"""
        <nav class="navbar bg-dark" data-bs-theme="dark">
            <div class="container">
                <a class="navbar-brand" href="#">Ansat</a>
                <ul class="nav">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="/">Home</a>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" data-bs-toggle="dropdown" href="#" role="button" aria-expanded="false">Services</a>
                        <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="/jobs">Jobs</a></li>
                        <li><a class="dropdown-item" href="#">Real Estate</a></li>
                        <li><a class="dropdown-item" href="/repairs">Repairs</a></li>
                        <li><a class="dropdown-item" href="#">Whatever</a></li>
                        </ul>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Buy/Sell Products</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Connect with your community</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/contactUs">Contact Us</a>
                        </li>
                </ul>
                <form class="d-flex" role="search">
                    <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
                    <button class="btn btn-primary" type="submit">Search</button>
                </form>
                {login_html}
            </div>
        </nav>
        """

@app.route('/')
def home():
    carousel = """    
    <div id="carouselExample" class="carousel slide">
        <div class="carousel-inner">
        <div class="carousel-item active">
            <img src="static/clem.jpg" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
            <img src="static/mount.jpg" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
            <img src="static/ocean.jpg" class="d-block w-100" alt="...">
        </div>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
        </button>
    </div>
    """
    return DOCT + "<html>" + HEAD + BODY_START + create_navigation_bar() + carousel + BODY_END + "</html>"

@app.route('/jobs')
def jobs():
    # execute a select query
    mycursor.execute("SELECT ID, job_title, job_des, user_id FROM jobpost")
    # fetch the results
    results = mycursor.fetchall()

    list_of_cards = []
    for row in results:
        list_of_cards.append(f"""
        <div class="col">
            <div class="card" style="width: 18rem;">
                <div class="card-body">
                    <h5 class="card-title">{row[1]}</h5>
                    <p class="card-text">{row[2]}</p>
                    <a href="/jobDescription?job_id={row[0]}&user_id={row[3]}" class="btn btn-primary">Read More</a>
                </div>
            </div>
        </div>
        """)
    j=''.join(list_of_cards)
    cards =f"""
    <div class="container">
        <div class="row">
            {j}
        </div>
    </div>
    """
    return DOCT + "<html>" + HEAD + BODY_START + create_navigation_bar() + cards + BODY_END + "</html>"

@app.route('/jobDescription',methods=['GET'])
def jobdes():
    description=""
    job_id=request.args.get('job_id',None)
    #query for jobID
    mycursor.execute(f"Select job_title from jobpost where ID='{job_id}';")
    jobidgrab = mycursor.fetchall()
    for job in jobidgrab:
        job_title=job[0]
    user_id=request.args.get('user_id',None)
    #query for names
    mycursor.execute(f"Select first_name, last_name from login where user_id='{user_id}';")
    displayname = mycursor.fetchall()
    for name in displayname:
        first_name=name[0]
        last_name=name[1]
    description=f"""
        <div class="container">
            <h1>{job_title} posted by {first_name} {last_name}</h1>
        </div>
    """     
    return DOCT + "<html>" + HEAD+ BODY_START + create_navigation_bar() + description + BODY_END + "</html>"

@app.route('/contactUs', methods=['GET', 'POST'])
def contactUs():
    error_string=""
    anotherErr=""
    if request.form.get('fname',None) != None:
        if request.form.get('fname',None).isalpha():
            fname=request.form['fname']
        else:
            fname=""
            error_string =f"""
            <div class="alert alert-danger" role="alert">
                Your name cannot be a digit
            </div>"""
    else:
        fname=""
    if request.form.get('lname',None) != None:
        lname=request.form['lname']
    else:
        lname=""
    if request.form.get('Gender',None) !=None:
        Gender=request.form['Gender']
    else:
        Gender=""
        if request.form.get('form_submit')=='yes':
            anotherErr=f"""
            <div class="alert alert-danger" role="alert">
                Please select a gender to proceed
            </div>"""
    if request.form.get('email',None) != None:
        email=request.form['email']
    else:
        email=""
    if request.form.get('phone ',None) != None:
        phone=request.form['phone']
    else:
        phone=""
    if request.form.get('Country',None) !=None:
        Country=request.form['Country']
    else:
        Country=""
    if request.form.getlist('interest',None)!=None:
        inter=request.form.getlist('interest')
        interest=','.join(inter)
    else:
        interest=""
    if request.form.get('questions',None) != None:
        questions=request.form['questions']
    else:
        questions=""

    if fname != "" and Gender!="":
        f=open(f"{fname}.txt", "w")
        print((fname+' '+lname + ' ' +email+' '+phone+' '+questions +' '+Gender +' ' +Country),file=f)
        f.close()

    if fname!="" and interest!="":
        f=open(f"{fname}.txt", "w")
        print((fname+' '+lname + ' ' +email+' '+phone+' '+questions +' '+Gender +' ' +Country+ ' '+interest),file=f)
        f.close()

    contact_form=f"""
    <div class="container">
        <div class="row">
            {error_string}
            {anotherErr}
            <form action="" method="post">
                Welcome to Ansat. Please provide information below and we will get back to you as soon as possible.
                <div class="mb-3">
                <label for="fname" class="form-label">Your First Name</label>
                <input type="text" class="form-control" id="fname" name="fname">
                </div>
                <div class="mb-3">
                <label for="lname" class="form-label">Last Name</label>
                <input type="text" class="form-control" id="lname" name="lname">
                </div>
                <div class="mb-3">
                <label for="phone" class="form-label">Select Gender: </label>
                </div>
                <div class="form-check form-check-inline">
                    <input class="form-check-input" type="radio" name="Gender" id="Gender1" value="Female">
                    <label class="form-check-label" for="inlineRadio1">Female</label>
                </div>
                <div class="form-check form-check-inline">
                    <input class="form-check-input" type="radio" name="Gender" id="Gender2" value="Male">
                    <label class="form-check-label" for="inlineRadio2">Male</label>
                </div>
                <div class="mb-3">
                <label for="email" class="form-label">Email address</label>
                <input type="email" class="form-control" id="email" aria-describedby="emailHelp" name="email">
                <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
                </div>
                <div class="mb-3">
                <label for="phone" class="form-label">Your Phone Number</label>
                <input type="text" class="form-control" id="phone" name="phone">
                </div>
                <div class="mb-3">
                <label for="Country" class="form-label">Please select your country of residence </label>
                <select class="form-select" multiple aria-label="multiple select example" name=Country>
                    <option selected value="USA">USA</option>
                    <option value="CANADA">CANADA</option>
                    <option value="MEXICO">MEXICO</option>
                    <option value="UK">UK</option>
                </select>
                </div>
                <label for="Interest" class="form-label">What services are you interested in? </label>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" value="Jobs" name="interest" id="flexCheckChecked" checked>
                    <label class="form-check-label" for="flexCheckChecked">
                        Jobs
                    </label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" value="Repairs" name="interest" id="flexCheckChecked" checked>
                    <label class="form-check-label" for="flexCheckChecked">
                        Repairs
                    </label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" value="Real Estate" name="interest" id="flexCheckChecked" checked>
                    <label class="form-check-label" for="flexCheckChecked">
                        Real Estate
                    </label>
                </div>
                <div class="mb-3">
                <label for="questions" class="form-label">Write your questions/concerns here</label>
                <textarea class="form-control" id="questions" name="questions" rows="3"></textarea>
                </div>
                <button type="submit" name="form_submit" value="yes" class="btn btn-primary">Submit</button>
            </form>
        </div>
    </div>
    """
    return DOCT + "<html>" + HEAD + BODY_START + create_navigation_bar() + contact_form + BODY_END + "</html>"


@app.route('/repairs')
def repair():
    # execute a select query
    mycursor.execute("SELECT ID, repair_title, repair_des FROM repairpost")
    # fetch the results
    results = mycursor.fetchall()
    list_of_r=[]
    for i in results:
        list_of_r.append(f"""
        <div class="col">
            <div class="card" style="width: 18rem;">
                <div class="card-body">
                    <h5 class="card-title">{i[1]}</h5>
                    <p class="card-text">{i[2]}</p>
                    <a href="/repairDescription?repid={i[0]}" class="btn btn-primary">Read More</a>
                </div>
            </div>
        </div>""")
    j=''.join(list_of_r)
    cards =f"""
    <div class="container">
        <div class="row">
            {j}
        </div>
    </div>
    """
    return DOCT + "<html>" + HEAD + BODY_START + create_navigation_bar() + cards + BODY_END + "</html>"

@app.route('/repairDescription',methods=['GET'])
def repDes():
    repid=request.args.get('repid',None)
    if repid:
        description=f"""
        <div class="container">
            <h1>{repid}</h1>
        </div>
        """
    return DOCT + "<html>" + HEAD+ BODY_START + create_navigation_bar() + description + BODY_END + "</html>"

@app.route('/login',methods=['GET', 'POST'])
def login():
    error_string=""
    logm=""
    user_count = 0
    username=request.form.get('username',None)
    password=request.form.get('password',None)
    if username and password:
        mycursor.execute(f"Select username, passwords from login where username='{username}' and passwords='{password}';")
        logs = mycursor.fetchall()
        for l in logs:
            user_count += 1
        if user_count == 1:
            logm=f""" <div> You are logged in! </div>"""
            session['logged_in']=True
            session['username']=username
            mycursor.execute(f"Select user_id from login where username='{username}';")
            useridgrab=mycursor.fetchall()
            for i in useridgrab:
                user_id=i[0]
            session['user_id']=user_id
            return redirect("/")
        else:
            error_string =f"""
            <div class="alert alert-danger" role="alert">
                Credentials are not correct! Please try again.
            </div>"""
    else:
        if request.form.get('form_submit')=="yes":
            error_string =f"""
            <div class="alert alert-danger" role="alert">
                Please fill the form with username and password!
            </div>"""
    form=f"""
    <div class="container">
        {error_string}
        {logm}
        <form action="" method="post">
            <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Username</label>
                <input type="text" class="form-control" id="exampleInputEmail1" name="username" aria-describedby="emailHelp">
            </div>
            <div class="mb-3">
                <label for="exampleInputPassword1" class="form-label">Password</label>
                <input type="password" class="form-control" id="exampleInputPassword1" name="password">
            </div>
            <button type="submit" name="form_submit" value="yes" class="btn btn-primary">Submit</button>
            <a class="btn btn-primary" href="/signup" role="button">Sign Up</a>
        </form>
    """
    return DOCT + "<html>" + HEAD+ BODY_START + create_navigation_bar() + form + BODY_END + "</html>"



@app.route('/signup',methods=['GET', 'POST'])
def signup():
    # If the form (2 fields, username and password) is submitted
    #   accept username and password from the form and run an Insert query to store in the database
    #   redirect to /login page
    # else:
    #    show the form again
    error_string=""
    logm=""
    errorm=""
    username=request.form.get('username',None)
    password=request.form.get('password',None)
    if username and password:
        try:
            mycursor.execute(f"INSERT INTO login (username, passwords) VALUES ('{username}','{password}');")
            if mycursor.rowcount > 0:
                logm=f""" <div> You have successfully signed up </div>"""
            mydb.commit()
            return redirect("/login")
        except mysql.connector.errors.IntegrityError:
            errorm =f""" <div class="alert alert-danger" role="alert"> This username is taken, please try again! </div>"""
    else:
        if request.form.get('form_submit')=="yes":
            error_string =f"""
            <div class="alert alert-danger" role="alert">
                Please fill the required fields in order to sign up!
            </div>"""
    form=f"""
    <div class="container">
        {error_string}
        {logm}
        {errorm}
        <form action="" method="post">
            <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label"> Please select a unique username</label>
                <input type="text" class="form-control" id="exampleInputEmail1" name="username" aria-describedby="emailHelp">
            </div>
            <div class="mb-3">
                <label for="exampleInputPassword1" class="form-label">Create a password</label>
                <input type="password" class="form-control" id="exampleInputPassword1" name="password">
            </div>
            <button type="submit" name="form_submit" value="yes" class="btn btn-primary">Sign up</button>
        </form>
    """
    return DOCT + "<html>" + HEAD+ BODY_START + create_navigation_bar() + form + BODY_END + "</html>"

@app.route('/myprofile')
def prof():
    t=f"""
    <div class="container">
        <div class="row">
            {buttons}
        </div>
    </div>"""
    return DOCT + "<html>" + HEAD+ BODY_START + create_navigation_bar() + t + BODY_END + "</html>"


@app.route('/logout')
def log():
    session.clear()
    return redirect("/")

@app.route('/poststuff',methods=['GET','POST'])
def post():
    count=0
    succ=""
    error=""
    #job params
    job_title=request.form.get('job_title',None)
    job_des=request.form.get('job_des',None) 
    jobsal=request.form.get('jobsal',None) 
    job_exp=request.form.get('job_exp',None) 
    job_duration=request.form.get('job_duration',None)
    user_id=session.get("user_id")
    #repair parans
    repair_title=request.form.get('repair_title',None)
    repair_des=request.form.get('repair_des',None) 
    repair_pay=request.form.get('repair_pay',None) 
    rep_address=request.form.get('rep_address',None)
    if request.form.get('job_submit')=='yes':
        mycursor.execute(f"Select job_title from jobpost WHERE job_title='{job_title}';")
        postresult = mycursor.fetchall()
        for i in postresult:
            count+=1
        if count==0:
            mycursor.execute(f"INSERT into jobpost (job_title, job_des, jobsal, job_exp, job_duration, user_id) values ('{job_title}', '{job_des}', '{jobsal}', '{job_exp}','{job_duration}',{user_id});")
            mydb.commit()
            succ="<div> You have successfully posted a job post </div>"
        else:
            error=f"""
            <div class="alert alert-danger" role="alert">
                A job with the same title already exists please try again!
            </div>"""
    elif request.form.get('repair_submit')=='yes':
        mycursor.execute(f"INSERT into repairpost (repair_title, repair_des, repair_pay, rep_address) values ('{repair_title}', '{repair_des}', '{repair_pay}','{rep_address}');")
        mydb.commit()
        succ="<div> You have successfully posted a repair post </div>"
    posta=""
    postid=request.args.get('postid', None)
    if postid=="job":
        posta=f"""
        <div class="col">
        <form action="" method="post">
            <div class="mb-3">
                <label for="exampleFormControlInput1" class="form-label">Job Title</label>
                <input type="text" class="form-control" id="exampleFormControlInput1" name="job_title">
            </div>
            <div class="mb-3">
                <label for="exampleFormControlTextarea1" class="form-label">Job description</label>
                <textarea class="form-control" id="exampleFormControlTextarea1" name="job_des" rows="3"></textarea>
            </div>
            <div class="mb-3">
                <label for="exampleFormControlInput1" class="form-label">Salary</label>
                <input type="text" class="form-control" id="exampleFormControlInput1" name="jobsal">
            </div>
            <div class="mb-3">
                <label for="exampleFormControlInput1" class="form-label">Experience</label>
                <input type="text" class="form-control" name="job_exp" id="exampleFormControlInput1">
            </div>
            <div class="mb-3">
                <label for="exampleFormControlInput1" class="form-label">Duration</label>
                <input type="text" class="form-control" name="job_duration" id="exampleFormControlInput1">
            </div>
            <button type="submit" name="job_submit" value="yes" class="btn btn-primary">Submit</button>
        </form>
        </div>"""
            
    elif postid=="repair":
        posta=f"""  
        <div class="col">
        <form action="" method="post">
            <div class="mb-3">
                <label for="exampleFormControlInput1" class="form-label">Repair Title</label>
                <input type="text" class="form-control" name="repair_title" id="exampleFormControlInput1">
            </div>
            <div class="mb-3">
                <label for="exampleFormControlTextarea1" class="form-label">Repair description</label>
                <textarea class="form-control" id="exampleFormControlTextarea1" name="repair_des" rows="3"></textarea>
            </div>
            <div class="mb-3">
                <label for="exampleFormControlInput1" class="form-label">Pay</label>
                <input type="text" class="form-control" name="repair_pay" id="exampleFormControlInput1">
            </div>
            <div class="mb-3">
                <label for="exampleFormControlInput1" class="form-label">Address</label>
                <input type="text" class="form-control" name="rep_address" id="exampleFormControlInput1">
            </div>
            <button type="submit" name="repair_submit" value="yes" class="btn btn-primary">Submit</button>
        </form>
        </div>"""
    ht=f"""
    <div class="container">
        <div class="row">
            {buttons}{succ}{error}{posta}
        </div>
    </div>"""
    return DOCT + "<html>" + HEAD+ BODY_START + create_navigation_bar() + ht + BODY_END + "</html>"


    