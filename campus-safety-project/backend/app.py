from flask import Flask
from flask_cors import CORS
from routes.report import report_bp
from routes.admin import admin_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(report_bp)
app.register_blueprint(admin_bp)

app.run(debug=True)