from flask import Flask
from flask import request

app = Flask(__name__)
DOCT='<!Doctype html>'

HEAD = """
    <head> 
        <title>Ansat | Home </title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
    </head>
    """
BODY_START = "<body>"
NAVIGATION_BAR = """
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
    </div>
</nav>
"""
BODY_END = "</body>"

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
    return DOCT + "<html>" + HEAD + BODY_START + NAVIGATION_BAR + carousel + BODY_END + "</html>"

@app.route('/jobs')
def jobs():
    cards="""
    <div class="container">
        <div class="row">
            <div class="col">
                <div class="card" style="width: 18rem;">
                    <div class="card-body">
                        <h5 class="card-title">Job title</h5>
                        <p class="card-text">Job description</p>
                        <a href="#" class="btn btn-primary">Read More</a>
                    </div>
                </div>
            </div>
            <div class="col">
                <div class="card" style="width: 18rem;">
                    <div class="card-body">
                        <h5 class="card-title">Job title</h5>
                        <p class="card-text">Job description</p>
                        <a href="#" class="btn btn-primary">Read More</a>
                    </div>
                </div>
            </div>
            <div class="col">
                <div class="card" style="width: 18rem;">
                    <div class="card-body">
                        <h5 class="card-title">Job title</h5>
                        <p class="card-text">Job description</p>
                        <a href="#" class="btn btn-primary">Read More</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """
    return DOCT + "<html>" + HEAD + BODY_START + NAVIGATION_BAR + cards + BODY_END + "</html>"

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
    if request.form.get('questions',None) != None:
        questions=request.form['questions']
    else:
        questions=""
    if fname != "" and Gender!="":
        f=open(f"{fname}.txt", "w")
        print((fname+' '+lname + ' ' +email+' '+phone+' '+questions +' '+Gender +' ' +Country),file=f)
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
                <div class="mb-3">
                <label for="questions" class="form-label">Write your questions/concerns here</label>
                <textarea class="form-control" id="questions" name="questions" rows="3"></textarea>
                </div>
                <button type="submit" name="form_submit" value="yes" class="btn btn-primary">Submit</button>
            </form>
        </div>
    </div>
    """
    return DOCT + "<html>" + HEAD + BODY_START + NAVIGATION_BAR + contact_form + BODY_END + "</html>"


@app.route('/repairs')
def repairs():
    rep="""
    <div class="container">
        <div class="row">
            <div class="col">
                <div class="card" style="width: 18rem;">
                    <div class="card-body">
                        <h5 class="card-title">Electronics repair</h5>
                        <p class="card-text">Job description</p>
                        <a href="#" class="btn btn-primary">Read More</a>
                    </div>
                </div>
            </div>
            <div class="col">
                <div class="card" style="width: 18rem;">
                    <div class="card-body">
                        <h5 class="card-title">Plumbing</h5>
                        <p class="card-text">Job description</p>
                        <a href="#" class="btn btn-primary">Read More</a>
                    </div>
                </div>
            </div>
            <div class="col">
                <div class="card" style="width: 18rem;">
                    <div class="card-body">
                        <h5 class="card-title">Handymans</h5>
                        <p class="card-text">Description</p>
                        <a href="#" class="btn btn-primary">Read More</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """
    return DOCT + "<html>" + HEAD + BODY_START + NAVIGATION_BAR + rep + BODY_END + "</html>"