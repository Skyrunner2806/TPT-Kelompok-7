# TPT Kelompok 7 - Smart Parking & CCTV Occupancy Detection

Projek Tugas TPT Kelompok 7 untuk sistem deteksi okupansi slot parkir berbasis **Computer Vision** menggunakan **YOLO** dan *stream* CCTV multi-kamera.

Sistem mendeteksi kendaraan pada area parkir, menentukan status slot **occupied** atau **empty**, kemudian menyimpan data okupansi ke database **PostgreSQL**.

---

## 📌 Web Dashboard

Kode Web Dashboard berada pada branch terpisah:

[`web-dashboard`](https://github.com/Skyrunner2806/TPT-Kelompok-7/tree/web-dashboard)

Branch tersebut berisi aplikasi Flask untuk menampilkan data okupansi parkir dari PostgreSQL.

---

## 📂 Struktur File

```text
TPT-Kelompok-7/
├── main_yolo_db.py        # Deteksi okupansi + PostgreSQL
├── masking.py             # Pembuatan area slot parkir
├── test_cctv.py           # Pengujian stream CCTV
├── slots_cctv_3cam.json   # Koordinat slot parkir
└── yolo11m.pt             # YOLO weight
```

---

## 📦 Library

Install library yang dibutuhkan:

```bash
pip install opencv-python ultralytics numpy psycopg2-binary
```

Library utama:

* `opencv-python` — membaca dan menampilkan stream CCTV
* `ultralytics` — menjalankan YOLO
* `numpy` — pemrosesan koordinat
* `psycopg2-binary` — koneksi PostgreSQL

---

## 📹 Konfigurasi CCTV

Sistem menggunakan tiga CCTV melalui protokol RTSP:

```python
RTSP_URL_1 = "rtsp://admin:TPT2025!@167.205.48.183/"
RTSP_URL_2 = "rtsp://admin:TPT2025!@167.205.48.184/"
RTSP_URL_3 = "rtsp://admin:TPT2025!@167.205.48.185/"
```

Pastikan komputer terhubung ke:

```text
ITB Hotspot
```

agar CCTV dapat diakses.

---

## 🗄️ PostgreSQL

Program menggunakan PostgreSQL untuk menyimpan data okupansi parkir.

Konfigurasi database:

```python
DB_CONFIG = {
    "host": "localhost",
    "dbname": "postgres",
    "user": "postgres",
    "password": "YOUR_POSTGRESQL_PASSWORD",
    "port": 5432,
}
```

Nama tabel:

```text
parking_occupancy
```

Tabel akan dibuat secara otomatis oleh program dengan struktur:

```sql
CREATE TABLE IF NOT EXISTS parking_occupancy (
    id SERIAL PRIMARY KEY,
    ts TIMESTAMPTZ NOT NULL,
    occupied INTEGER,
    empty INTEGER,
    total_slots INTEGER
);
```

Data yang disimpan:

* `ts` — waktu pencatatan
* `occupied` — jumlah slot terisi
* `empty` — jumlah slot kosong
* `total_slots` — total slot parkir

---

## 🔗 YOLO Weight

Download model YOLO melalui:

[Google Drive - YOLO Weight](https://drive.google.com/file/d/1zl6Q-xGrWpqpw4ZiR-_JcxVLCTxwkNiy/view?usp=sharing)

Letakkan file `yolo11m.pt` pada folder utama projek.

---

## 🚀 Cara Menjalankan

### 1. Clone Repository

```bash
git clone https://github.com/Skyrunner2806/TPT-Kelompok-7.git
cd TPT-Kelompok-7
```

### 2. Install Library

```bash
pip install opencv-python ultralytics numpy psycopg2-binary
```

### 3. Pastikan PostgreSQL aktif

Sesuaikan password PostgreSQL pada `DB_CONFIG`.

### 4. Hubungkan ke ITB Hotspot

Pastikan ketiga CCTV dapat diakses.

### 5. Jalankan Program

```bash
python main_yolo_db.py
```

Jika database berhasil terhubung:

```text
[INFO] DB Connected.
```

Ketika data berhasil disimpan:

```text
[DB SAVED] Total: ... | Occ: ... | Empty: ...
```

Tekan `ESC` untuk menghentikan program.

---

## 🔄 Alur Sistem

```text
CCTV
  ↓
RTSP Stream
  ↓
OpenCV
  ↓
YOLO Detection
  ↓
Parking Slot Occupancy
  ↓
PostgreSQL
  ↓
Web Dashboard
```

---

## 👥 TPT Kelompok 7

**Smart Parking & CCTV Occupancy Detection**

Computer Vision • YOLO • CCTV • PostgreSQL • Flask
