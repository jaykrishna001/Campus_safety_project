function login(){

fetch("http://127.0.0.1:5000/admin/login",{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({
username:document.getElementById("user").value,
password:document.getElementById("pass").value
})
})
.then(res=>res.json())
.then(data=>{
if(data.status==="success"){
window.location.href="admin.html";
}else{
alert("❌ Wrong Login");
}
})
.catch(()=>alert("Server Error"));
}