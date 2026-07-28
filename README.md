# TPT Kelompok 7 - Smart Parking & CCTV Occupancy Detection

Projek Tugas TPT Kelompok 7 untuk sistem deteksi okupansi slot parkir berbasis visi komputer (*Computer Vision*) dan pemrosesan *stream* CCTV multi-kamera menggunakan model YOLO.

---

## 📌 Informasi Penting (Web Dashboard)
> **Catatan:** Kode dan instruksi untuk menjalankan Web Dashboard interaktif berada di branch tersendiri (**`web-dashboard`**).
> 
> Silakan beralih ke branch [`web-dashboard`](https://github.com/Skyrunner2806/TPT-Kelompok-7/tree/web-dashboard) untuk melihat tampilan dashboard web, aset foto, serta panduan menjalankan server Flask.

---

## 📂 Struktur File di Branch `main`

* `main_yolo_db` : Skrip utama deteksi okupansi slot parkir menggunakan YOLO terhubung ke sistem database.
* `masking` : Tool/skrip anotasi untuk pembuatan *mask* / slot zona parkir berbasis RTSP.
* `test_cctv` : Skrip pengujian dan visualisasi *streaming* multi-view dari beberapa kamera CCTV.
* `slots_cctv_3cam.json` : File konfigurasi koordinat/titik slot parkir untuk 3 sudut kamera CCTV.

---

## 🔗 Model YOLO Weight
Model bobot (*weights*) YOLO dapat diunduh melalui link Google Drive berikut:
* **Download YOLO Weight File:** [Google Drive Link](https://drive.google.com/file/d/1zl6Q-xGrWpqpw4ZiR-_JcxVLCTxwkNiy/view?usp=sharing)

---

## 🚀 Cara Menjalankan

1. **Clone Repositori:**
   ```bash
   git clone [https://github.com/Skyrunner2806/TPT-Kelompok-7.git](https://github.com/Skyrunner2806/TPT-Kelompok-7.git)
   cd TPT-Kelompok-7
2. **Library yang dibutuhkan:**
   ```bash
   pip install opencv-python ultralytics numpy mysql-connector-python
3. **Unduh model yang dubutuhkan:**
   ```bash
   Unduh file bobot YOLO dari link Google Drive di atas dan letakkan di dalam folder utama projek.
4. Jalankan Skrip Utama:
   ```bash
   Jalankan Skrip Utama:
