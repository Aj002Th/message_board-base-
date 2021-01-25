var TurnToLogin = () => {
	document.getElementById('form_login_div').style.display = "block";
	document.getElementById('form_register_div').style.display = "none";
}
var TurnToRegister = () => {
	document.getElementById('form_register_div').style.display = "block";
	document.getElementById('form_login_div').style.display = "none";
}
function regist() {
  var BaseURL = 'http://127.0.0.1:5000'
   var postRequest = new XMLHttpRequest();
   postRequest.withCredentials= true;
   postRequest.open("POST", BaseURL + '/users');
   username=document.getElementById('username').value;
   password = document.getElementById('password').value;
    var postData = {
        'username': username,
        'password': String(password)
        
    }
   postRequest.setRequestHeader("Content-type", "application/json")
   postRequest.send(JSON.stringify(postData))
   postRequest.onreadystatechange = function() {
    if (postRequest.readyState == 4) {
    if (postRequest.status == 200) { 
        console.log(postRequest.responseText)
        window.location.href="留言板!!!.html";
       } 
        else 
       { confirm(postRequest.responseText)}
       }
    }
}
function turnin() {
  var BaseURL = 'http://127.0.0.1:5000'
   var postRequest = new XMLHttpRequest();
   postRequest.withCredentials= true; 
   postRequest.open("POST", BaseURL + '/session');
   username=document.getElementById('user').value;
   password = document.getElementById('pass').value;
    var postData = {
        'username': username,
        'password': String(password)
        
    }
   postRequest.setRequestHeader("Content-type", "application/json")
   postRequest.send(JSON.stringify(postData))
   postRequest.onreadystatechange = function() {
    if (postRequest.readyState == 4) {
    if (postRequest.status == 200) { 
        console.log(postRequest.responseText)
        window.location.href="留言板个人界面.html";
       } 
        else 
       { confirm(postRequest.responseText)}
       }
    }
}
