import streamlit as st
import pandas as pd
import os

# =========================================
# CONFIG
# =========================================
st.set_page_config(page_title="Dashboard Dana Desa", layout="wide")

# =========================================
# CUSTOM CSS
# =========================================
st.markdown("""
<style>
body {
    background-color: #0e1117;
}
.card {
    padding: 20px;
    border-radius: 15px;
    background: linear-gradient(145deg, #1f2937, #111827);
    box-shadow: 0 0 15px rgba(0,0,0,0.5);
    text-align: center;
}
.title {
    font-size: 28px;
    font-weight: bold;
}
.sub {
    color: #9ca3af;
}
.review-box {
    padding:15px;
    border-radius:10px;
    margin-bottom:10px;
    background:#1f2937;
}
</style>
""", unsafe_allow_html=True)

# =========================================
# HEADER
# =========================================
st.markdown("""
<div style="display:flex; align-items:center; gap:15px;">
    <img src="https://imgs.click/img/03/23/2026/photo_2026-03-24_02-07-34.jpg" width="80">
    <div>
        <div class="title">Dashboard Transparansi Dana Desa</div>
        <div class="sub">Monitoring real-time anggaran & pembangunan desa</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# =========================================
# DATA
# =========================================
data_desa = {
    "Kegiatan": ["Jalan Lingkungan","UMKM Desa","BLT Dana Desa","Posyandu"],
    "Anggaran": [300000000,45000000,90000000,35000000],
    "Terpakai": [145000000,20000000,90000000,10000000],
    "Progress": [100,45,100,25],
    "Status": ["Selesai","Berjalan","Selesai","Perencanaan"]
}

df = pd.DataFrame(data_desa)
df["Sisa"] = df["Anggaran"] - df["Terpakai"]

# =========================================
# KPI
# =========================================
total = df["Anggaran"].sum()
used = df["Terpakai"].sum()
sisa = total - used

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(f"""<div class="card"><h3>💰 Total Dana</h3><h2>Rp {total:,}</h2></div>""", unsafe_allow_html=True)
with c2:
    st.markdown(f"""<div class="card"><h3>📉 Terpakai</h3><h2>Rp {used:,}</h2></div>""", unsafe_allow_html=True)
with c3:
    st.markdown(f"""<div class="card"><h3>🏦 Sisa Kas</h3><h2>Rp {sisa:,}</h2></div>""", unsafe_allow_html=True)

st.markdown("---")

# =========================================
# PROGRESS
# =========================================
st.subheader("📊 Progress Proyek")

for i in range(len(df)):
    st.write(f"{df['Kegiatan'][i]} ({df['Status'][i]})")
    st.progress(df["Progress"][i] / 100)

st.markdown("---")

# =========================================
# TABEL
# =========================================
st.subheader("📋 Detail Anggaran")
st.dataframe(df, use_container_width=True)

# =========================================
# KOMENTAR + RATING (FINAL)
# =========================================
st.markdown("---")
st.subheader("⭐️ Penilaian & Komentar Warga")

file_komen = "komentar.csv"

# AUTO DATA AWAL
if not os.path.exists(file_komen):
    data_awal = pd.DataFrame([
        ["Budi - Jakarta", 5, "Sekarang transparansi dana desa jauh lebih jelas, semua pengeluaran terlihat rapi dan terbuka."],
        ["Siti - Surabaya", 5, "Dengan sistem ini, dana desa terasa lebih aman dan tidak ada lagi keraguan dari masyarakat."],
        ["Andi - Bandung", 5, "Sangat membantu! Informasi anggaran jadi mudah dipantau, semoga terus konsisten transparan."]
    ], columns=["Nama","Rating","Komentar"])

    data_awal.to_csv(file_komen, index=False)

# INPUT USER
nama = st.text_input("Nama")
rating = st.slider("Rating", 1, 5, 5)
komentar = st.text_area("Komentar")

if st.button("Kirim Komentar"):
    if nama and komentar:
        df_komen = pd.read_csv(file_komen)
        new = pd.DataFrame([[nama, rating, komentar]], columns=["Nama","Rating","Komentar"])
        df_komen = pd.concat([df_komen, new], ignore_index=True)
        df_komen.to_csv(file_komen, index=False)
        st.success("✅ Komentar tersimpan!")
    else:
        st.warning("⚠️ Isi semua field")
        # TAMPILKAN KOMENTAR
st.markdown("### 💬 Semua Komentar")

df_komen = pd.read_csv(file_komen)

for i in range(len(df_komen)):
    stars = "⭐️" * int(df_komen["Rating"][i])
    st.markdown(f"""
    <div class="review-box">
        <b>{df_komen["Nama"][i]}</b><br>
        <span style="color:gold;">{stars}</span><br>
        <span style="color:#ddd;">{df_komen["Komentar"][i]}</span>
    </div>
    """, unsafe_allow_html=True)

# KOMENTAR TERBAIK
st.markdown("### 🌟 Komentar Terbaik (5⭐️)")

terbaik = df_komen[df_komen["Rating"] == 5]

for i in range(len(terbaik)):
    st.success(f"⭐️ {terbaik['Nama'].iloc[i]}: {terbaik['Komentar'].iloc[i]}")
