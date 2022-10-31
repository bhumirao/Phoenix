function validate()
{
    var username=document.getElementById("username") .value;
    var password=document.getElementById("password").value;
    if(username=="admin"&& password=="user")
    { 
        alert("login succesfully"); 
    }
    else
    { 
        alert("login failed");
    } 
}