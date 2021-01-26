window.onload = function() {
  var BaseURL = 'http://127.0.0.1:5000'
  var getRequest = new XMLHttpRequest()
  getRequest.withCredentials= true;
  getRequest.open('GET', BaseURL + '/users/show_all_message') 
  getRequest.send()
  getRequest.onreadystatechange = function() {
    if (getRequest.readyState == 4)
     {  if (getRequest.status == 200) 
     {  console.log(getRequest.responseText)
        var a = getRequest.response;
        var all = JSON.parse(getRequest.responseText);
        for(var i = 0; i <a.length; i++)
        {var b=all[i].nickname;
          var c=all[i].message;
          document.getElementsByClassName("bubble_other").style.display ="block"; 
         document.getElementById("str1").innerHTML=c;        
         document.getElementById("username_other").innerHTML=b;
        }
     } 
      else {alert(getRequest.responseText)
     }
    }
 }
}
