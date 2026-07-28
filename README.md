# TPT Kelompok 7 - Web Dashboard Monitoring

Branch ini berisi aplikasi antarmuka web (*Web Dashboard*) berbasis **Flask** untuk memvisualisasikan status parkir dan informasi profil kelompok **TPT Kelompok 7**.

---

## 📂 Struktur Direktori

```text
web_dashboard/
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

---

## 📦 Library yang Dibutuhkan

Aplikasi ini membutuhkan beberapa library Python berikut:

* **Flask** — digunakan sebagai framework untuk menjalankan aplikasi web.
* **mysql-connector-python** — digunakan untuk menghubungkan aplikasi Flask dengan database MySQL.

Install seluruh library yang dibutuhkan dengan menjalankan perintah berikut pada terminal:

```bash
pip install flask mysql-connector-python
```

Pastikan Python dan `pip` sudah terinstal pada komputer sebelum menjalankan perintah tersebut.

---

## ▶️ Menjalankan Web Dashboard

Masuk ke direktori `web_dashboard`:

```bash
cd web_dashboard
```

Kemudian jalankan aplikasi Flask:

```bash
python app.py
```

Setelah server berhasil berjalan, buka alamat yang ditampilkan pada terminal melalui browser untuk mengakses **Web Dashboard Monitoring TPT Kelompok 7**.
