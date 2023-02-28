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


def create_navigation_bar():
    if session.get('logged_in')==True:
        username=session.get("username")
        login_html = f"""
        <a class="btn btn-primary" href="#">Hello {username}</a>
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
    mycursor.execute("SELECT * FROM jobs")
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
                    <a href="/jobDescription?job_id={row[0]}" class="btn btn-primary">Read More</a>
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
    job_id=request.args.get('job_id', None)
    if job_id:
        f=open(request.args.get('job_id'), 'r')
        desc=f.read()
        f.close()
        description=f"""
            <div class="container">
                <h1>{job_id}</h1>
                <p>{desc}</p>
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
    mycursor.execute("SELECT * FROM repairs")
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
        f=open(request.args.get('repid'), 'r')
        desc=f.read()
        f.close()
        description=f"""
        <div class="container">
            <h1>{repid}</h1>
            <p>{desc}</p>
        </div>
        """
    return DOCT + "<html>" + HEAD+ BODY_START + create_navigation_bar() + description + BODY_END + "</html>"

@app.route('/login',methods=['GET', 'POST'])
def login():
    error_string=""
    logm=""
    mycursor.execute("Select username from login")
    result_usernmame=mycursor.fetchall()
    mycursor.execute("Select passwords from login")
    result_passwords=mycursor.fetchall()
    username=request.form.get('username',result_usernmame)
    password=request.form.get('password',result_passwords)
    if username and password:
        logm=f""" <div> You are logged in! </div>"""
        session['logged_in']=True
        session['username']=username
        return redirect("/")
    else:
        username=""
        password=""
        if request.form.get('form_submit')=="yes":
            error_string =f"""
            <div class="alert alert-danger" role="alert">
                Credentials are not correct! Please try again.
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
        </form>
    """
    return DOCT + "<html>" + HEAD+ BODY_START + create_navigation_bar() + form + BODY_END + "</html>"



    