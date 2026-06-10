let isSOS = 0;

function toggleSOS(){
  const locationInput = prompt("🚨 SOS call: where are you currently located? (e.g., Building 5, Main Gate)");
  if(!locationInput){
    alert("SOS cancelled: location is required.");
    return;
  }

  isSOS = 1;
  alert(`🚨 SOS ACTIVATED\nLocation: ${locationInput}\nHelp will be provided in 5 minutes.`);

  // Optionally store location in global state for submitForm
  window.sosLocation = locationInput;
}

function submitForm(){

let formData = new FormData();

formData.append("type", document.getElementById("type").value);
formData.append("description", document.getElementById("desc").value);
formData.append("location", document.getElementById("loc").value);
formData.append("date", document.getElementById("date").value);
formData.append("time", document.getElementById("time").value);
formData.append("severity", document.getElementById("severity").value);
formData.append("is_sos", isSOS);

fetch("http://127.0.0.1:5000/report",{
method:"POST",
body:formData
})
.then(res=>res.json())
.then(()=>{
alert("✅ Complaint Submitted");
location.reload();
})
.catch(()=>alert("Error submitting"));
}