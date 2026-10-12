"""
Aplikasi Antarmuka Pengguna Streamlit: Perbandingan Pola Penalaran Kognitif Agen.
Mendukung pembacaan otomatis dataset Kaggle all-data.csv (4.846 baris).
© 2026 Muryan Awaludin. Seluruh hak cipta dilindungi undang-undang.
"""
import streamlit as st
import pandas as pd
import json
import os
from config import CONFIG
from agent.reasoning_patterns import CognitiveReasoningEngine

st.set_page_config(
    page_title=CONFIG.APP_TITLE,
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Market Intelligence Agent: Cognitive Reasoning Engine")
st.caption("Eksplorasi Perbandingan Pola Kognitif: ReAct, Reflexion, dan Tree of Thoughts Berbasis Dataset Finansial Kaggle")

# Fungsi Pemuatan Data Robust (Menangani latin-1, No Header, Kolom Terbalik)
@st.cache_data
def load_dataset(file_path: str) -> pd.DataFrame:
    if not os.path.exists(file_path):
        # Fallback jika berkas belum diletakkan di folder data/
        st.warning(f"Berkas {file_path} tidak ditemukan. Menggunakan sampel darurat.")
        return pd.DataFrame({
            "Sentence": [
                "Operating profit rose to EUR 13.1 mn from EUR 9.4 mn in the first quarter of 2026.",
                "Workforce reduction of 15% announced due to declining retail demand.",
                "Net sales remained flat at EUR 45.2 mn."
            ],
            "Sentiment": ["positive", "negative", "neutral"]
        })
    
    try:
        # Percobaan baca dengan utf-8
        df = pd.read_csv(file_path, encoding="utf-8", header=None)
    except (UnicodeDecodeError, Exception):
        # Fallback standar Kaggle FinancialPhraseBank: encoding latin-1
        df = pd.read_csv(file_path, encoding="latin-1", header=None)

    # Deteksi dan normalisasi kolom: pastikan nama kolom adalah Sentence dan Sentiment
    if df.shape[1] >= 2:
        # Cek apakah kolom pertama berisi nilai sentimen
        sample_col0 = str(df.iloc[0, 0]).strip().lower()
        if sample_col0 in ["positive", "negative", "neutral", "sentiment"]:
            # Jika baris pertama header kebetulan terbawa, hapus
            if sample_col0 == "sentiment":
                df = df.iloc[1:].reset_index(drop=True)
            df = df.rename(columns={0: "Sentiment", 1: "Sentence"})
        else:
            df = df.rename(columns={0: "Sentence", 1: "Sentiment"})
            
    # Pastikan data bersih dari spasi berlebih
    df["Sentiment"] = df["Sentiment"].astype(str).str.strip().str.lower()
    df["Sentence"] = df["Sentence"].astype(str).str.strip()
    return df[["Sentence", "Sentiment"]]

df_news = load_dataset(CONFIG.DATA_PATH)

# Inisialisasi State Hasil Analisis
if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = None

# Sidebar: Navigasi dan Pemilihan 4.846 Kalimat
with st.sidebar:
    st.header("📊 Dataset Sentimen Finansial")
    st.markdown(f"Total Data Terbaca: **{len(df_news):,} baris**")
    
    # Filter Sentimen untuk memudahkan pemilihan data
    sentiment_filter = st.radio(
        "Filter Berdasarkan Kategori Sentimen:",
        ["Semua", "Positive", "Negative", "Neutral"],
        horizontal=True
    )
    
    # Penerapan filter
    if sentiment_filter != "Semua":
        filtered_df = df_news[df_news["Sentiment"] == sentiment_filter.lower()].reset_index()
    else:
        filtered_df = df_news.reset_index()

    # Opsi Pencarian Kata Kunci
    search_query = st.text_input("🔍 Cari kata kunci (opsional):", placeholder="misal: profit, sales, loss...")
    if search_query:
        filtered_df = filtered_df[filtered_df["Sentence"].str.contains(search_query, case=False, na=False)].reset_index(drop=True)

    st.markdown(f"Data ditampilkan: **{len(filtered_df):,} baris**")

    if len(filtered_df) > 0:
        selected_row_idx = st.selectbox(
            "Pilih Baris Kalimat Berita:",
            range(len(filtered_df)),
            format_func=lambda i: f"[{filtered_df.iloc[i]['Sentiment'].upper()}] {filtered_df.iloc[i]['Sentence'][:40]}..."
        )
        
        current_sentence = filtered_df.iloc[selected_row_idx]["Sentence"]
        ground_truth = filtered_df.iloc[selected_row_idx]["Sentiment"]
    else:
        current_sentence = "Tidak ada kalimat yang sesuai filter."
        ground_truth = "-"

    btn_execute = st.button("🚀 Jalankan Penalaran Multi-Pola", type="primary", use_container_width=True, disabled=(len(filtered_df) == 0))

    st.divider()
    st.markdown("**Detail Kalimat Terpilih:**")
    st.info(current_sentence)
    st.markdown(f"**Ground Truth Label:** `{ground_truth.upper()}`")
    
    st.divider()
    st.markdown("© 2026 **Muryan Awaludin**  \nHak Cipta Dilindungi.")

# Area Kerja Utama
if btn_execute and len(filtered_df) > 0:
    with st.spinner("Mengeksekusi pola ReAct, Reflexion, dan Tree of Thoughts..."):
        st.session_state.analysis_result = CognitiveReasoningEngine.analyze_all_patterns(current_sentence)

if st.session_state.analysis_result is not None:
    result = st.session_state.analysis_result

    tab_react, tab_reflexion, tab_tot, tab_summary = st.tabs([
        "⚡ 1. Pola ReAct", 
        "🔄 2. Pola Reflexion", 
        "🌳 3. Pola Tree of Thoughts",
        "📊 4. Matriks Komparasi Kognitif"
    ])

    # Tab 1: ReAct
    with tab_react:
        st.subheader("Pola ReAct (Reasoning and Acting)")
        st.markdown("*Menghubungkan penalaran bertahap dengan grounding telemetri pasar secara langsung.*")
        
        for step in result.react_steps:
            with st.container(border=True):
                st.markdown(f"**Iterasi Langkah {step.step_number}**")
                st.markdown(f"🧠 **Thought:** *{step.thought}*")
                st.markdown(f"⚡ **Action:** `{step.action}` | Parameter: `{json.dumps(step.action_input)}`")
                st.markdown("🔬 **Observation Lingkungan:**")
                st.code(step.observation, language="json")
                
        st.success(f"**Keputusan Akhir ReAct:** {result.react_verdict}")

    # Tab 2: Reflexion
    with tab_reflexion:
        st.subheader("Pola Reflexion (Self-Correction via Verbal Critique)")
        st.markdown("*Menguji evaluasi heuristik dan memperbaiki asumsi yang keliru antar-percobaan.*")
        
        for trial in result.reflexion_trials:
            with st.container(border=True):
                st.markdown(f"**Percobaan Kognitif {trial.trial_number} (Evaluator Score: {trial.critique_score})**")
                st.markdown(f"📝 **Analisis:** {trial.initial_analysis}")
                st.warning(f"💡 **Verbal Self-Reflection:** {trial.reflection}")
                st.markdown(f"✨ **Hasil Refleksi:** {trial.refined_analysis}")
                
        st.success(f"**Keputusan Akhir Reflexion:** {result.reflexion_verdict}")

    # Tab 3: Tree of Thoughts
    with tab_tot:
        st.subheader("Pola Tree of Thoughts (Pencarian Pohon Non-Linier)")
        st.markdown("*Mengeksplorasi cabang keputusan alternatif, estimasi skor kelayakan, dan pemangkasan.*")
        
        root = result.tot_tree
        st.markdown(f"📍 **Akar Masalah:** `{root.hypothesis}`")
        
        col_branches = st.columns(len(root.children))
        for idx, child in enumerate(root.children):
            with col_branches[idx]:
                box_icon = "🟢" if child.status == "SELECTED" else "🔴"
                st.markdown(f"### {box_icon} Cabang {idx+1}")
                st.markdown(f"**Hipotesis:** {child.hypothesis}")
                st.markdown(f"**Skor Kelayakan:** `{child.evaluation_score}`")
                st.markdown(f"**Status Evaluasi:** `{child.status}`")
                
                if child.children:
                    st.markdown("**Sub-cabang Turunan:**")
                    for sub in child.children:
                        sub_icon = "✅" if sub.status == "SELECTED" else "❌"
                        st.caption(f"{sub_icon} {sub.hypothesis} (Skor: {sub.evaluation_score})")
                        
        st.success(f"**Keputusan Akhir Tree of Thoughts:** {result.tot_verdict}")

    # Tab 4: Ringkasan & Matriks Komparasi
    with tab_summary:
        st.subheader("Matriks Perbandingan Output Penalaran")
        summary_table = pd.DataFrame([
            {"Paradigma": "ReAct", "Rekomendasi Keputusan": result.react_verdict, "Kelebihan": "Grounding langsung ke API/Tools eksternal"},
            {"Paradigma": "Reflexion", "Rekomendasi Keputusan": result.reflexion_verdict, "Kelebihan": "Koreksi mandiri berbasis memori trial lampau"},
            {"Paradigma": "Tree of Thoughts", "Rekomendasi Keputusan": result.tot_verdict, "Kelebihan": "Evaluasi multiskip dan pemangkasan cabang keliru"}
        ])
        st.dataframe(summary_table, use_container_width=True, hide_index=True)
else:
    st.info("Pilih data berita finansial pada bilah samping lalu tekan **'Jalankan Penalaran Multi-Pola'** untuk memulai simulasi.")

st.divider()
st.caption(CONFIG.AUTHOR_COPYRIGHT)