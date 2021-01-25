function btnsubmit() {
  var BaseURL = 'http://127.0.0.1:5000'
   var postRequest = new XMLHttpRequest();
    postRequest.withCredentials= true;
   postRequest.open("POST", BaseURL + '/message/change_message');
   message=document.getElementById('new').value;
    var postData = {
        'message': String(message)        
    }
   postRequest.setRequestHeader("Content-type", "application/json")
   postRequest.send(JSON.stringify(postData))
   postRequest.onreadystatechange = function() {
    if (postRequest.readyState == 4) {
    if (postRequest.status == 200) { 
        console.log(postRequest.responseText)
        alert('修改成功喽')
        window.location.href="留言板个人界面.html"
       } 
        else 
       { confirm(postRequest.responseText)}
       }
    }
}
function cancel(){
  window.location.href="留言板个人界面.html"
}
