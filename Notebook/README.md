# Sentimen-Timnas-App: Analisis Sentimen Komentar Instagram Timnas Indonesia

📊 *Analisis komentar publik terhadap Timnas Indonesia selama Piala Asia 2023 menggunakan model Transformer berbahasa Indonesia.*

---

## 📌 Deskripsi Proyek

Proyek ini merupakan implementasi dari penelitian yang bertujuan untuk menganalisis opini publik terhadap performa **Tim Nasional Indonesia** selama **Piala Asia 2023** melalui komentar di akun Instagram resmi [@timnasindonesia](https://instagram.com/timnasindonesia).

Tiga model Transformer digunakan untuk klasifikasi sentimen:  
- **IndoBERT**  
- **IndoRoBERTa**  
- **DistilBERT Multilingual**

Hasil menunjukkan bahwa model **IndoBERT** memberikan akurasi terbaik dalam mengklasifikasikan komentar menjadi tiga sentimen: **positif**, **netral**, dan **negatif**.

---

## 📥 Dataset

- **Sumber**: Komentar dari akun Instagram @timnasindonesia dengan tagar #GarudaDiPialaAsia
- **Jumlah awal**: 21.045 komentar
- **Setelah preprocessing**: 17.150 komentar
- **Label**: Positif (37.1%), Netral (36.6%), Negatif (26.3%) – dilabeli secara manual

---

## 🔧 Preprocessing

Langkah-langkah pembersihan data:
- Cleaning text (hapus emoji, angka, URL, simbol)
- Case folding
- Normalisasi kata tidak baku
- Tokenisasi
- Stopword removal
- Stemming (Sastrawi)

📍 Implementasi: [`Preprocessing.ipynb`](Notebook/Preprocessing.ipynb)

---

## 🤖 Model yang Digunakan

| Model                  | Deskripsi                                                                                                              |
|------------------------|------------------------------------------------------------------------------------------------------------------------|
| [**IndoBERT**](https://huggingface.co/indobenchmark/indobert-large-p1)               | Pretrained BERT Bahasa Indonesia dari IndoNLU *(Wilie et al., 2020)*                                       |
| [**IndoRoBERTa**](https://huggingface.co/flax-community/indonesian-roberta-base)   | Varian BERT dengan optimisasi RoBERTa: dynamic masking dan tanpa Next Sentence Prediction *(RoBERTa-style)* |
| [**DistilBERT Multilingual**](https://huggingface.co/distilbert-base-multilingual-cased) | Model distilled ringan dari Multilingual BERT; cocok untuk resource terbatas                                 |
---

## 🧪 Pelatihan dan Evaluasi

- Teknik **fine-tuning** dengan 3 variasi learning rate: `1e-5`, `3e-6`, `5e-5`
- **Early stopping** untuk menghindari overfitting
- Evaluasi menggunakan:
  - Accuracy
  - Precision
  - Recall
  - F1-Score
  - Confusion Matrix

📍 Implementasi: [`Training.ipynb`](Notebook/Training.ipynb)

---

## 📊 Hasil Evaluasi

| Model      | LR    | Accuracy | F1-Score | Precision | Recall |
|------------|-------|----------|----------|-----------|--------|
| IndoBERT   | 5e-5  | 73.62%   | 72.42%   | 74.77%    | 71.76% |
| IndoRoBERTa| 5e-5  | 72.33%   | 71.75%   | 71.69%    | 71.82% |
| DistilBERT | 5e-5  | 71.05%   | 70.20%   | 70.10%    | 70.36% |

- **IndoBERT** unggul secara keseluruhan
- **IndoRoBERTa** stabil dan efisien
- **DistilBERT** cocok untuk sistem dengan keterbatasan sumber daya

---

## 📚 Referensi Utama

- Wilie, B., et al. (2020). *IndoNLU: Benchmark and Resources for Evaluating Indonesian NLP*.  
- Liu, Z., Lin, Y., & Sun, M. (2020). *Representation Learning for Natural Language Processing*. Springer.
- Devlin, J., et al. (2019). *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding*.

---

## 🚀 Cara Menjalankan Proyek di Google Colab

Ikuti langkah-langkah berikut untuk menjalankan analisis sentimen komentar Instagram terhadap Timnas Indonesia:

---

### 1️⃣ Buka Notebook Google Colab

Klik salah satu tautan berikut sesuai tahap yang ingin dijalankan:

- 📦 [Preprocessing.ipynb](https://colab.research.google.com/drive/1O-lG1FitF32T73rPx3GoysM5_p-llhxg?usp=sharing) – Membersihkan dan mempersiapkan data  
- 🤖 [Training.ipynb](https://colab.research.google.com/drive/1tKnNImRVQVYyuaf5YQHWQM9tX_mO33tp?usp=sharing) – Melatih dan mengevaluasi model Transformer

---

### 2️⃣ Hubungkan ke GPU

1. Klik `Runtime` → `Change runtime type`
2. Pilih **Hardware accelerator**: `GPU`
3. Klik `Save`

---

### 3️⃣ Jalankan Seluruh Notebook

1. Tekan tombol ▶️ di kiri atas (atau `Runtime > Run all`)
2. Tunggu hingga seluruh sel selesai dijalankan secara berurutan

> 📌 Catatan:
> - Proses training model memerlukan waktu dan memori, pastikan runtime tetap aktif.
> - Pastikan internet stabil saat menggunakan Hugging Face model.

---

### 4️⃣ Simpan Hasil (Opsional)

Untuk menyimpan model, prediksi, atau output lainnya:
- Tambahkan sel di akhir notebook untuk menyimpan ke Google Drive atau unduh manual dari panel `Files`.

Contoh menyimpan model:
```python
from google.colab import drive
drive.mount('/content/drive')
model.save_pretrained('/content/drive/MyDrive/Model-Sentimen-Timnas')
```

## ✍️ Penulis

**Muhammad Irfan Abidin**  
L200210021 – Universitas Muhammadiyah Surakarta  
📝 Skripsi: *Analisis Sentimen terhadap Timnas Indonesia di Piala Asia 2023 dengan Model Transformer Berbahasa Indonesia*

---

> "Sepak bola bukan hanya permainan — ia adalah suara rakyat. Analisis sentimen membantu kita mendengarkannya." ⚽🇮🇩
