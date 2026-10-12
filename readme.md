# 🧠 Market Intelligence Agent: Cognitive Reasoning Engine

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://agentic-market-intelligence.streamlit.app)
[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/muryanawaludin/agentic_market_intelligence.git)
[![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-brightgreen)](https://www.python.org/)

> **Bab 2: Pola Penalaran Agen — ReAct, Reflexion, dan Tree of Thoughts**  
> *Implementasi praktis modul penalaran kognitif multi-pola untuk analisis sentimen dan intelijen pasar modal berbasis dataset Kaggle.*

---

## 🚀 Live Demo Aplikasi

Uji langsung cara agen bernalar dan membandingkan 3 pola kognitif tanpa perlu instalasi lokal:

👉 **[KLIK DI SINI UNTUK DEMO APLIKASI](https://agentic-market-intelligence.streamlit.app)**  
*(Repositori GitHub: [muryanawaludin/agentic_market_intelligence](https://github.com/muryanawaludin/agentic_market_intelligence.git))*

---

## ⚡ 3 Pola Penalaran Kognitif yang Dibandingkan

Aplikasi ini mendemonstrasikan bagaimana sebuah agen AI memecahkan ambiguitas berita keuangan menggunakan 3 paradigma berpikir tingkat lanjut:

| Pola Penalaran | Cara Kerja | Keunggulan Utama |
| :--- | :--- | :--- |
| **⚡ ReAct** *(Reason + Act)* | *Thought $\to$ Action $\to$ Observation* | Memvalidasi berita secara real-time dengan tool telemetri pasar & metrik DCF. |
| **🔄 Reflexion** | Evaluasi diri verbal (*Self-Critique*) | Mengoreksi kesalahan analisis tahap awal secara rekursif antar-percobaan (*multi-trial*). |
| **🌳 Tree of Thoughts** | Eksplorasi pohon keputusan non-linier | Mengevaluasi cabang hipotesis pasar, memberi skor heuristik, dan memangkas (*pruning*) skenario keliru. |

---

## 📊 Sumber Dataset

Proyek ini menggunakan data riil dari **Kaggle Financial Sentiment Analysis** (*FinancialPhraseBank*):
* **Ukuran Data:** 4.846 baris kalimat berita pasar modal.
* **Fitur:** Pencarian kata kunci dinamis dan filter sentimen (*Positive*, *Negative*, *Neutral*).

---

## 🛠️ Panduan Menjalankan Cepat (3 Langkah)

```bash
# 1. Kloning repositori
git clone https://github.com/muryanawaludin/agentic_market_intelligence.git
cd agentic_market_intelligence

# 2. Pasang dependensi
pip install -r requirements.txt

# 3. Jalankan aplikasi di browser
streamlit run app.py
```

Aplikasi langsung terbuka di `http://localhost:8501`.

---

## 📁 Struktur Direktori

```text
agentic_market_intelligence/
├── data/
│   └── all-data.csv              # Dataset Kaggle (4.846 entri berita finansial)
├── agent/
│   ├── schema.py                 # Struktur model data Pydantic
│   ├── tools.py                  # Simulator perkakas indikator pasar
│   └── reasoning_patterns.py    # Logika kognitif ReAct, Reflexion, dan ToT
├── config.py                     # Konfigurasi sistem
├── requirements.txt              # Dependensi Python
└── app.py                        # Dasbor visualisasi Streamlit
```

---

## 👨‍💻 Penulis & Peneliti

**Muryan Awaludin, S.Kom., M.Kom.**  
Dosen, Peneliti Kecerdasan Buatan & Konsultan Teknologi Informasi  
GitHub: [@muryanawaludin](https://github.com/muryanawaludin)

---

## ⚖️ Hak Cipta

© 2026 **Muryan Awaludin**. Seluruh hak cipta dilindungi undang-undang.  
*Materi ini merupakan bagian dari buku **Rekayasa Agentic AI**.*