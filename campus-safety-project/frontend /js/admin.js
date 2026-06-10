fetch("http://127.0.0.1:5000/reports")
.then(r=>r.json())
.then(data=>{

data.forEach(d=>{
if(d.is_sos==1){
alert("🚨 URGENT SOS ISSUE RECEIVED!");
}
});

let table=document.getElementById("t");

table.innerHTML = `
<thead>
<tr>
<th>ID</th>
<th>Type</th>
<th>Severity</th>
<th>Date</th>
<th>Time</th>
<th>SOS</th>
<th>Status</th>
<th>Action</th>
</tr>
</thead>
<tbody></tbody>
`;

let body = table.querySelector('tbody');

function severityClass(value){
  const sev = (value||'medium').toLowerCase();
  if(sev==='low') return 'severity-low';
  if(sev==='medium') return 'severity-medium';
  if(sev==='high') return 'severity-high';
  if(sev==='critical') return 'severity-critical';
  return 'severity-medium';
}

data.forEach(d=>{
  const severityVal = d.severity || 'medium';
  body.innerHTML += `
<tr style="${d.is_sos==1 ? 'background:#ffe5e5' : ''}">
<td>${d.id}</td>
<td>${d.type}</td>
<td><span class="${severityClass(severityVal)}">${severityVal}</span></td>
<td>${d.date||'-'}</td>
<td>${d.time||'-'}</td>
<td>${d.is_sos==1 ? '🚨' : ''}</td>
<td>${d.status || '-'}</td>
<td><button onclick="res(${d.id})">✔</button></td>
</tr>`;
});
});

function res(id){
fetch("http://127.0.0.1:5000/update/"+id,{method:"PUT"})
.then(()=>location.reload());
}