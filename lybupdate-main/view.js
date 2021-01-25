window.onload = function() {
  var BaseURL = 'http://127.0.0.1:5000'
  var getRequest = new XMLHttpRequest()
  getRequest.withCredentials= true;
  username = document.getElementById('username')
  nickname = document.getElementById('nickname')
  age = document.getElementById('age')
  gender = document.getElementById('gender')
  getRequest.open('GET', BaseURL + '/users/show_my_homepage') 
  getRequest.send()
  getRequest.onreadystatechange = function() {
    if (getRequest.readyState == 4)
     {  if (getRequest.status == 200) 
     {  console.log(getRequest.responseText)
        var myObj = JSON.parse(getRequest.responseText);
        var a='用户名:'
        var b='昵称：'
        var c='年龄:'
        var d='性别:'
        document.getElementById("username").innerHTML = a+myObj.username;
        document.getElementById("nickname").innerHTML = b+myObj.nickname;
        document.getElementById("age").innerHTML = c+myObj.age;
        document.getElementById("gender").innerHTML = d+myObj.gender;
     } 
      else {alert(getRequest.responseText)
     }
    }
 }
}
