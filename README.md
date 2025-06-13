# Sentimen Timnas App

Aplikasi web untuk analisis sentimen terhadap komentar publik tentang Tim Nasional Sepak Bola Indonesia. Aplikasi ini dibangun dengan Streamlit dan menggunakan model deep learning berbasis Transformer.

🌐 **Live Demo**: [timnas-sentiment-analysis.streamlit.app](https://timnas-sentiment-analysis.streamlit.app/)

---

## 🎯 Tujuan

Menganalisis opini publik terhadap performa, potensi, dan kebijakan seputar Timnas Indonesia melalui teks komentar.

---

## 🧠 Model yang Digunakan

Model-model telah dilatih ulang (fine-tuned) untuk tugas klasifikasi sentimen dalam bahasa Indonesia:

| Nama Model | Deskripsi |
|-----------|-----------|
| [`irfan36/distilBERT-multilingual-sentiment`](https://huggingface.co/irfan36/distilBERT-multilingual-sentiment) | Model ringan berbasis DistilBERT, mendukung berbagai bahasa |
| [`irfan36/indoBERT-sentiment`](https://huggingface.co/irfan36/indoBERT-sentiment) | Model IndoBERT untuk klasifikasi sentimen bahasa Indonesia |
| [`irfan36/indoRoBERTa-sentiment`](https://huggingface.co/irfan36/indoRoBERTa-sentiment) | Model RoBERTa yang diadaptasi khusus untuk bahasa Indonesia |

---

## ⚙️ Cara Menjalankan Lokal

1. Clone repositori:
   ```bash
   git clone https://github.com/MIAbidin/Sentimen-Timnas-App.git
   cd Sentimen-Timnas-App

2. Instal dependensi:
   ```bash
   pip install -r requirements.txt

3. Jalankan aplikasi:
   ```bash
   streamlit run app.py

## 📄 Dokumentasi Lengkap

Silakan buka file [Notebook/me.md](.Notebook/me.md) untuk melihat dokumentasi lengkap proyek ini, termasuk deskripsi, hasil eksperimen, dan panduan penggunaan Google Colab.
