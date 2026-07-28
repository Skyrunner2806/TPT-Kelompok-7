from flask import Flask, render_template, Response, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor
import cv2

# ================== KONFIGURASI ==================

# Konfigurasi 3 Kamera
RTSP_URL_1 = "rtsp://admin:TPT2025!@167.205.48.183/"
RTSP_URL_2 = "rtsp://admin:TPT2025!@167.205.48.184/"
RTSP_URL_3 = "rtsp://admin:TPT2025!@167.205.48.185/"

DB_CONFIG = {
    "host": "localhost",
    "dbname": "postgres",
    "user": "postgres",
    "password": "123fikar",
    "port": 5432,
}

TABLE_NAME = "parking_occupancy"

# =================================================

app = Flask(__name__, static_folder="Photo")

# ---------- Helper DB ----------

def get_conn():
    return psycopg2.connect(**DB_CONFIG)

# ---------- API: data terbaru ----------

@app.route("/api/latest_status")
def api_latest_status():
    query = f"""
        SELECT ts, occupied, empty, total_slots
        FROM {TABLE_NAME}
        ORDER BY ts DESC
        LIMIT 1;
    """
    with get_conn() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(query)
            row = cur.fetchone()

    if not row:
        return jsonify({"ok": False, "message": "No data"}), 200

    return jsonify({
        "ok": True,
        "ts": row["ts"].isoformat(),
        "occupied": row["occupied"],
        "empty": row["empty"],
        "total_slots": row["total_slots"],
    })

# ---------- API: data grafik hari ini ----------

@app.route("/api/occupancy_today")
def api_occupancy_today():
    query = f"""
        SELECT ts, occupied
        FROM {TABLE_NAME}
        WHERE ts::date = CURRENT_DATE
        ORDER BY ts DESC
        LIMIT 200
    """
    with get_conn() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(query)
            rows = cur.fetchall()

    rows.reverse()

    data = {
        "labels": [r["ts"].isoformat() for r in rows],
        "occupied": [r["occupied"] for r in rows],
    }
    return jsonify({"ok": True, "data": data})

# ---------- API: analisis jam crowded ----------

@app.route("/api/crowded_hour_today")
def api_crowded_hour_today():
    query = f"""
        SELECT date_trunc('hour', ts) AS hour,
               AVG(occupied::float) AS avg_occupied
        FROM {TABLE_NAME}
        WHERE ts::date = CURRENT_DATE
        GROUP BY hour
        HAVING COUNT(*) > 2
        ORDER BY avg_occupied DESC
        LIMIT 1;
    """
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            row = cur.fetchone()

    if not row:
        return jsonify({"ok": False, "message": "Belum cukup data hari ini."})

    crowded_dt, avg_occ = row
    hour_str = crowded_dt.strftime("%H:%M")
    return jsonify({
        "ok": True,
        "hour": hour_str,
        "avg_occupied": float(avg_occ),
    })

# ---------- API: heatmap crowded ----------

@app.route("/api/weekly_heatmap")
def api_weekly_heatmap():
    query = f"""
        SELECT
            EXTRACT(hour FROM ts)::int AS hour,
            AVG(occupied::float / NULLIF(total_slots, 0)) AS avg_ratio
        FROM {TABLE_NAME}
        WHERE ts >= NOW() - INTERVAL '7 days'
        GROUP BY hour
        ORDER BY hour;
    """
    with get_conn() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(query)
            rows = cur.fetchall()

    data = []
    for r in rows:
        hour = r["hour"]
        avg_ratio = r["avg_ratio"]
        if avg_ratio is None:
            avg_ratio = 0.0
        data.append({"hour": hour, "avg_ratio": float(avg_ratio)})

    return jsonify({"ok": True, "data": data})

# ---------- Streaming CCTV (MJPEG) Helper ----------

def gen_frames(rtsp_url):
    """Generator frame untuk URL RTSP spesifik"""
    cap = cv2.VideoCapture(rtsp_url)
    
    # Optional: Set buffer size agar latency rendah
    try:
        cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
    except:
        pass

    if not cap.isOpened():
        print(f"[ERROR] Gagal membuka RTSP: {rtsp_url}")
        # Return frame hitam atau error image jika mau
        return

    while True:
        success, frame = cap.read()
        if not success:
            break

        # Resize agar ringan di browser (opsional, sesuaikan)
        frame = cv2.resize(frame, (640, 360))

        ret, buffer = cv2.imencode(".jpg", frame)
        if not ret:
            continue
        jpg_bytes = buffer.tobytes()

        yield (b"--frame\r\n"
               b"Content-Type: image/jpeg\r\n\r\n" + jpg_bytes + b"\r\n")

    cap.release()

# ---------- Routes untuk 3 Kamera ----------

@app.route("/video_feed_1")
def video_feed_1():
    return Response(gen_frames(RTSP_URL_1),
                    mimetype="multipart/x-mixed-replace; boundary=frame")

@app.route("/video_feed_2")
def video_feed_2():
    return Response(gen_frames(RTSP_URL_2),
                    mimetype="multipart/x-mixed-replace; boundary=frame")

@app.route("/video_feed_3")
def video_feed_3():
    return Response(gen_frames(RTSP_URL_3),
                    mimetype="multipart/x-mixed-replace; boundary=frame")

# ---------- Halaman utama ----------

@app.route("/")
def index():
    return render_template("index.html")

# ---------- Main ----------

if __name__ == "__main__":
    # Threaded=True penting agar bisa stream multi-kamera sekaligus
    app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)