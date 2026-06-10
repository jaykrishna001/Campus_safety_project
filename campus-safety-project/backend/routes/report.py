from flask import Blueprint, request, jsonify
import sqlite3, os

report_bp = Blueprint('report', __name__)

UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@report_bp.route('/report', methods=['POST'])
def report():
    data = request.form
    photo = request.files.get('photo')
    filename = ""

    if photo:
        filename = os.path.join(UPLOAD_FOLDER, photo.filename)
        photo.save(filename)

    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute('''
    INSERT INTO complaints(type,description,location,date,time,photo,is_sos,severity)
    VALUES(?,?,?,?,?,?,?,?)
    ''', (
        data.get('type'),
        data.get('description'),
        data.get('location'),
        data.get('date'),
        data.get('time'),
        filename,
        int(data.get('is_sos',0)),
        data.get('severity', 'medium')
    ))

    conn.commit()
    conn.close()

    return jsonify({"status":"success"})