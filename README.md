# TPT Kelompok 7 - Web Dashboard Monitoring

Branch ini berisi aplikasi antarmuka web (*Web Dashboard*) berbasis **Flask** untuk memvisualisasikan status okupansi parkir dan informasi profil kelompok **TPT Kelompok 7**.

Data okupansi parkir diperoleh dari program utama `main_yolo_db.py` dan disimpan ke dalam database **PostgreSQL**, kemudian ditampilkan melalui Web Dashboard.

---

## 📂 Struktur Direktori

```text
TPT-Kelompok-7/
├── main_yolo_db.py            # Deteksi okupansi parkir + PostgreSQL
│
└── web-dashboard/
    ├── app.py                 # Server utama Flask
    ├── templates/
    │   └── index.html         # Antarmuka Dashboard HTML
    └── Photo/                 # Aset gambar profil & logo
        ├── Alpha Novrigian_13322042.png
        ├── Hizb Rafilza R.S_13322008.png
        ├── Zulfikar Firmanto_13322098.png
        ├── Logo_ITB.png
        └── Logo_TF.png
```

File Web Dashboard berada pada:

```text
TPT-Kelompok-7/web-dashboard
```

---

## 📦 Library yang Dibutuhkan

Install library yang dibutuhkan menggunakan:

```bash
pip install flask psycopg2-binary
```

Library utama:

* **Flask** — menjalankan aplikasi Web Dashboard.
* **psycopg2-binary** — menghubungkan Flask dengan database PostgreSQL.

Pastikan Python, `pip`, dan PostgreSQL sudah terinstal sebelum menjalankan aplikasi.

---

## ▶️ Menjalankan Sistem

Sistem dijalankan dalam dua tahap.

### 1. Jalankan Program Deteksi Parkir

Dari direktori utama repository:

```bash
cd TPT-Kelompok-7
```

Jalankan:

```bash
python main_yolo_db.py
```

Program ini akan:

* membaca *stream* CCTV;
* melakukan deteksi kendaraan menggunakan YOLO;
* menentukan jumlah slot `occupied` dan `empty`;
* menyimpan data okupansi ke PostgreSQL.

Pastikan program ini tetap berjalan selama Web Dashboard digunakan.

---

### 2. Jalankan Web Dashboard

Buka terminal baru, kemudian masuk ke direktori:

```bash
cd TPT-Kelompok-7/web-dashboard
```

Jalankan Flask:

```bash
python app.py
```

Setelah server berhasil berjalan, buka alamat yang ditampilkan pada terminal melalui browser.

Contoh:

```text
http://127.0.0.1:5000
```

Web Dashboard akan mengambil data okupansi dari PostgreSQL dan menampilkan status parkir secara visual.

---

## 🔄 Alur Sistem

```text
CCTV
  ↓
main_yolo_db.py
  ↓
YOLO Detection
  ↓
PostgreSQL
  ↓
app.py
  ↓
Web Dashboard
```

---

## 👥 TPT Kelompok 7

**Smart Parking & CCTV Occupancy Monitoring**

YOLO • PostgreSQL • Flask • Web Dashboard
