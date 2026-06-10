from flask import Blueprint, request, jsonify
import sqlite3

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin/login', methods=['POST'])
def login():
    data = request.json
    if data['username']=="admin" and data['password']=="1234":
        return jsonify({"status":"success"})
    return jsonify({"status":"fail"})

@admin_bp.route('/reports')
def reports():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM complaints")
    rows = cur.fetchall()
    conn.close()

    data=[]
    for r in rows:
        data.append({
            "id":r[0],
            "type":r[1],
            "description":r[2],
            "location":r[3],
            "date":r[4],
            "time":r[5],
            "severity":r[8] if len(r) > 8 else 'medium',
            "is_sos":r[7],
            "status":r[10] if len(r) > 10 else r[9]
        })
    return jsonify(data)

@admin_bp.route('/update/<int:id>', methods=['PUT'])
def update(id):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("UPDATE complaints SET status='Resolved' WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return jsonify({"msg":"done"})

@admin_bp.route('/stats')
def stats():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    # Total reports
    cur.execute("SELECT COUNT(*) FROM complaints")
    total = cur.fetchone()[0]

    # Pending reports
    cur.execute("SELECT COUNT(*) FROM complaints WHERE status='Pending'")
    pending = cur.fetchone()[0]

    # Resolved reports
    cur.execute("SELECT COUNT(*) FROM complaints WHERE status='Resolved'")
    resolved = cur.fetchone()[0]

    # SOS reports
    cur.execute("SELECT COUNT(*) FROM complaints WHERE is_sos=1")
    sos = cur.fetchone()[0]

    conn.close()

    return jsonify({
        "total": total,
        "pending": pending,
        "resolved": resolved,
        "sos": sos
    })