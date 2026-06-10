🛡️ Campus Shield
Anonymous Campus Safety & Issue Reporting System

Campus Shield is a web-based platform designed to provide students with a safe and accessible way to report campus-related issues anonymously. The system enables students to submit complaints regarding harassment, bullying, racism, safety concerns, and infrastructure problems while allowing administrators to monitor, prioritize, and resolve reported incidents through a centralized dashboard.

🎯 Problem Statement

Many students hesitate to report sensitive issues due to fear of exposure, lack of awareness, or complicated reporting processes. This leads to unresolved concerns affecting campus safety and well-being.

Campus Shield addresses this challenge by providing:

Anonymous issue reporting
SOS emergency alerts
Centralized complaint management
Priority-based issue handling
Faster administrative response
🚀 Features
Student Portal
Submit complaints anonymously
Report multiple issue categories
Add description and location details
Select date and time of incident
Upload supporting evidence (optional)
Emergency SOS reporting
Admin Dashboard
Secure Admin Login
View all submitted complaints
Highlight SOS reports
Mark issues as resolved
Track complaint status
Monitor campus safety trends
📂 Project Structure

Campus-Shield/
│
├── backend/
│   ├── app.py
│   ├── database.db
│   ├── models/
│   │   └── db_setup.py
│   └── routes/
│       ├── admin.py
│       └── report.py
│
├── frontend/
│   ├── index.html
│   ├── login.html
│   ├── admin.html
│   └── js/
│       ├── app.js
│       ├── login.js
│       └── admin.js
│
└── README.md

🛠️ Technologies Used
Frontend
HTML5
CSS3
JavaScript
Backend
Python
Flask
Flask-CORS
Database
SQLite
⚙️ Installation & Setup
1. Clone Repository
git clone https://github.com/yourusername/campus-shield.git
2. Navigate to Backend
cd backend
3. Install Dependencies
pip install flask flask-cors
4. Create Database
python models/db_setup.py
5. Run Backend Server
python app.py

Server will start at:

http://127.0.0.1:5000

6. Run Frontend

Open:

frontend/index.html

or run using VS Code Live Server.

🔑 Admin Credentials
Username: admin
Password: 1234
📋 Complaint Categories
Harassment
Bullying
Racism
Safety Issues
Infrastructure Issues
Other Campus Concerns
🚨 SOS Feature

The SOS feature allows students to flag urgent incidents requiring immediate attention.

When an SOS report is submitted:

The complaint is highlighted in the dashboard
Administrators receive an urgent notification
High-priority handling is enabled
🎓 Sustainable Development Goals (SDGs)

This project supports:

SDG 5 – Gender Equality

Promotes a safer environment for all students.

SDG 10 – Reduced Inequalities

Provides equal access to reporting mechanisms.

SDG 16 – Peace, Justice and Strong Institutions

Encourages transparency, accountability, and institutional responsiveness.

🔮 Future Enhancements
Email Notifications
Real-Time Alerts
AI-Based Complaint Classification
Data Analytics Dashboard
Mobile Application
Role-Based Authentication
Complaint Tracking System
👨‍💻 Team Project

Developed as a Hackathon Project to improve campus safety through technology-driven reporting and response systems.

Project Name

Campus Shield

"Your Voice. Your Safety. Your Campus." 🛡️🚨

GitHub Description (Short)

Campus Shield is a Flask-based anonymous campus safety reporting platform that enables students to report issues securely while providing administrators with a centralized dashboard for monitoring, prioritizing, and resolving complaints. 🚨🛡️
