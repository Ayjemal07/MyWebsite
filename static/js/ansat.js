function validate_first_name()
{
    let first_name = document.getElementsByName("fname"); 
    if (first_name[0].value=="")
    {
        alert("Your first name cannot be empty");
    }
}

function validate_last_name()
{
    let last_name = document.getElementsByName("lname"); 
    if (last_name[0].value=="")
    {
        alert("Your last name cannot be empty");
    }
}