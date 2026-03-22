import streamlit as st
import pandas as pd

# 1. Judul & Header
st.set_page_config(page_title="Transparansi Dana Desa", layout="centered")
st.title("🏡 Sistem Transparansi Dana Desa")
st.markdown("Portal pemantauan anggaran desa untuk warga.")
st.divider()

# 2. Data Anggaran (Simulasi Database Kecil)
# Dalam prakteknya, data ini bisa diambil dari file Excel atau Google Sheets
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

df = pd.DataFrame(data_desa)
df['Sisa Saldo'] = df['Anggaran (Rp)'] - df['Terpakai (Rp)']

# 3. Ringkasan Kas Desa
total_dana = df['Anggaran (Rp)'].sum()
total_terpakai = df['Terpakai (Rp)'].sum()
sisa_kas = total_dana - total_terpakai

c1, c2 = st.columns(2)
with c1:
    st.info(f"**Total Dana Desa:** \nRp {total_dana:,}")
with c2:
    st.success(f"**Sisa Kas Saat Ini:** \nRp {sisa_kas:,}")

st.divider()

# 4. Tabel Rincian Pengeluaran
st.subheader("📋 Rincian Pengeluaran & Proyek")
st.table(df) # Menggunakan table agar mudah dibaca di layar HP

# 5. Fitur "Locking" Sederhana (Catatan Admin)
with st.sidebar:
    st.header("🔑 Akses Admin")
    st.write("Gunakan area ini untuk mengunci laporan bulanan.")
    bulan = st.selectbox("Pilih Bulan Laporan", ["maret"])
    if st.button("Kunci & Arsipkan"):
        st.warning(f"Laporan bulan {bulan} telah dikunci dan dikirim ke sistem kabupaten.")

# 6. Interaksi Warga
st.divider()
st.subheader("💬 Tanya Jawab / Aspirasi Warga")
with st.form("aspirasi"):
    nama = st.text_input("Nama Warga / Dusun")
    pesan = st.text_area("Ingin bertanya soal anggaran apa?")
    submit = st.form_submit_button("Kirim Aspirasi")
    if submit:
        st.success("Terima kasih, Pak/Bu. Aspirasi Anda telah masuk ke catatan desa.")
