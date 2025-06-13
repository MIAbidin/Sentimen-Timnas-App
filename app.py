import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import pandas as pd
import matplotlib.pyplot as plt

# Fungsi untuk memuat pipeline model
@st.cache_resource
def load_pipeline(model_path):
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    return pipeline("sentiment-analysis", model=model, tokenizer=tokenizer, return_all_scores=True)

# Path model
model_paths = {
    "DistilBERT": "irfan36/distilBERT-multilingual-sentiment",
    "IndoBERT": "irfan36/indoBERT-sentiment",
    "IndoRoBERTa": "irfan36/indoRoBERTa-sentiment",
}


# Pemetaan label output model ke Bahasa Indonesia
label_map = {
    "LABEL_0": "Positif",
    "LABEL_1": "Netral",
    "LABEL_2": "Negatif"
}

# Pemetaan label output model ke Bahasa Inggris
label_map_eng = {
    "LABEL_0": "positive",
    "LABEL_1": "neutral",
    "LABEL_2": "negative"
}

# Load semua pipeline
pipelines = {name: load_pipeline(path) for name, path in model_paths.items()}

# Judul
st.title("📊 Analisis Sentimen")

# Input teks
text_input = st.text_area("📝 Masukkan teks untuk dianalisis:")

# Tombol Analisis
if st.button("🔍 Analisis"):
    if not text_input.strip():
        st.warning("⚠️ Teks tidak boleh kosong.")
    else:
        st.subheader("📈 Hasil Analisis Sentimen")
        confidence_scores = {}
        labels_predicted = {}
        labels_predicted_eng = {}

        cols = st.columns(len(pipelines))
        for i, (name, pipe) in enumerate(pipelines.items()):
            with cols[i]:
                with st.spinner(f"🔄 Memproses dengan {name}..."):
                    result = pipe(text_input)[0]
                    best = max(result, key=lambda x: x['score'])
                    label = label_map.get(best['label'], best['label'])
                    label_eng = label_map_eng.get(best['label'], best['label'])
                    score = best['score']
                    labels_predicted[name] = label
                    labels_predicted_eng[name] = label_eng
                    confidence_scores[name] = score
                    st.success(f"✅ **{name}**")
                    st.metric(label="Label", value=label)
                    st.metric(label="Confidence", value=f"{score:.4f}")

        # Grafik perbandingan confidence
        st.subheader("📊 Grafik Perbandingan Confidence")
        fig, ax = plt.subplots()
        models = list(confidence_scores.keys())
        scores = list(confidence_scores.values())
        colors = ['green' if labels_predicted[m] == 'Positif' else 'orange' if labels_predicted[m] == 'Netral' else 'red' for m in models]

        bars = ax.bar(models, scores, color=colors)
        ax.set_ylim(0, 1)
        ax.set_ylabel("Confidence Score")
        ax.set_title("Confidence Tiap Model")

        for bar in bars:
            height = bar.get_height()
            ax.annotate(f'{height:.2f}', xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 5), textcoords="offset points", ha='center', va='bottom')

        st.pyplot(fig)

        # Simpan input ke dataset (pakai label Inggris dari IndoBERT)
        try:
            new_row = pd.DataFrame([[text_input, labels_predicted_eng["IndoBERT"]]], columns=["text", "label"])
            new_row.to_csv("dataset.tsv", sep="\t", index=False, header=False, mode="a")
            st.success("📝 Teks berhasil disimpan ke dataset.")
        except Exception as e:
            st.error(f"❌ Gagal menyimpan ke dataset: {e}")

# Tampilkan dataset di bawah
st.markdown("---")
st.subheader("📄 Dataset Sentimen")

try:
    df = pd.read_csv("dataset.tsv", sep="\t", header=None, names=["text", "label"])

    # Mapping untuk dropdown
    label_filter_map = {
        "Semua": None,
        "Positif": "positive",
        "Netral": "neutral",
        "Negatif": "negative"
    }

    # Dropdown filter
    filter_label = st.selectbox("🔎 Filter berdasarkan label:", options=list(label_filter_map.keys()))

    # Terapkan filter jika dipilih
    if label_filter_map[filter_label]:
        df_filtered = df[df["label"].str.lower() == label_filter_map[filter_label]]
    else:
        df_filtered = df

    st.dataframe(df_filtered.reset_index(drop=True))
except Exception as e:
    st.error("❌ Gagal memuat dataset. Pastikan `dataset.tsv` tersedia dan formatnya benar.")