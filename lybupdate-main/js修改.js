function sub() {
  var BaseURL = 'http://127.0.0.1:5000'
   var postRequest = new XMLHttpRequest();
   postRequest.withCredentials= true;
   postRequest.open("POST", BaseURL + '/users/set_my_information');
   nickname=document.getElementById('nickname').value;
   gender=document.getElementById('gender').value;
   age = document.getElementById('age').value;
    var postData = {
        'age':age, 
        'gender':gender,
        'nickname': String(nickname)
        
           
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
