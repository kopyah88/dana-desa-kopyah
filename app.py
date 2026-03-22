import streamlit as st
import pandas as pd

# 1. Judul Utama
st.set_page_config(page_title="Transparansi Dana Desa", layout="centered")
st.title("🏡 Sistem Transparansi Dana Desa")
st.markdown("Portal pemantauan anggaran desa untuk warga.")
st.divider()

# 2. DATA DESA (Hati-hati saat mengubah angka di sini)
data_desa = {
    "Kegiatan / Proyek": [
        "Pembangunan Jalan Lingkungan",
        "Pemberdayaan UMKM Desa",
        "Pemberian BLT Dana Desa",
        "Renovasi Posyandu"
    ],
    "Anggaran (Rp)": [300000000, 45000000, 90000000, 35000000],
    "Terpakai (Rp)": [145000000, 20000000, 90000000, 10000000],
    "Progres Fisik": ["100%", "45%", "100%", "25%"],
    "Status": ["Selesai", "Berjalan", "Selesai", "Perencanaan"]
}

# 3. Pengolahan Data Otomatis
df = pd.DataFrame(data_desa)
total_dana = df['Anggaran (Rp)'].sum()
total_terpakai = df['Terpakai (Rp)'].sum()
sisa_kas = total_dana - total_terpakai

# 4. Tampilan Ringkasan Atas
c1, c2 = st.columns(2)
with c1:
    st.info(f"**Total Dana Desa:** \nRp {total_dana:,}")
with c2:
    st.success(f"**Sisa Kas Saat Ini:** \nRp {sisa_kas:,}")

st.divider()

# 5. Tampilan Tabel
st.subheader("📋 Rincian Pengeluaran & Proyek")
st.table(df)

# 6. Fitur Aspirasi
st.divider()
st.subheader("💬 Tanya Jawab / Aspirasi Warga")
with st.form("aspirasi"):
    nama = st.text_input("Nama Warga / Dusun")
    pesan = st.text_area("Ingin bertanya soal anggaran apa?")
    if st.form_submit_button("Kirim Aspirasi"):
        st.success("Terima kasih, Pak/Bu. Aspirasi Anda telah masuk ke catatan desa.")
