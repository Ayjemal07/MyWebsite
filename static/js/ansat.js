function validate_first_name()
{
    let first_name = document.getElementsByName("fname"); 
    if (first_name[0].value==="")
    {
        alert("Your first name cannot be empty");
    }
}

function validate_last_name()
{
    let last_name = document.getElementsByName("lname"); 
    let js_error = document.getElementById("js_error_display");
    if (last_name[0].value=="")
    {       
        js_error.innerHTML = '<div class="alert alert-danger" role="alert">Your last name cannot be empty</div>';
    }
    else
    {
        js_error.innerHTML = '';
    }
}


function validate_gender() {
    let gender_input = document.getElementsByName("Gender");
    let GenderError = '<div class="alert alert-danger" role="alert">Please select a gender</div>';
    if (gender_input[0].value === "") {
        let js_error = document.getElementById("js_error_display");
        js_error.innerHTML = GenderError
    } else {
        GenderError.textContent = "";
    }
  }


function validate_email(){
    let email_address=document.getElementsByName("email");
    let js_error = document.getElementById("js_error_display");

    if (email_address[0].value=="")
    {       
        js_error.innerHTML = '<div class="alert alert-danger" role="alert">You cannot proceed without email address</div>';
    }
    else if (!isValidEmailAddress(email_address[0].value))
    {
        js_error.innerHTML = '<div class="alert alert-danger" role="alert">Invalid email address. Please enter a valid email address ending in @mail.com</div>';
    }
    else
    {
        js_error.innerHTML = '';
    }
}

function isValidEmailAddress(email) {
    var regex = /^[a-zA-Z0-9_\-\.]+@mail\.com$/;
    return regex.test(email);
}

function validate_phone_number(){
    let phone_number=document.getElementsByName("phone");
    let js_error = document.getElementById("js_error_display");
    if (!phone_number[0].value) 
    {       
        js_error.innerHTML = '<div class="alert alert-danger" role="alert">Your phone number cannot be empty</div>';
    }
    
    if (!/^\d{10}$/.test(parseInt(phone_number[0].value))) {
        js_error.innerHTML = '<div class="alert alert-danger" role="alert">Your phone number must be ten digitsy</div>';
      }

}

//   function validate_last_name_country("lname","Country"){

    
//   }

