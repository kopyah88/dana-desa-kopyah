import streamlit as st
import pandas as pd

st.set_page_config(page_title="Transparansi Dana Desa", layout="centered")
st.title("🏡 Sistem Transparansi Dana Desa")
st.markdown("Portal pemantauan anggaran desa untuk warga.")
st.divider()

# MEMBACA DATA DARI FILE CSV
try:
    df = pd.read_csv('data.csv')
    
    # Perhitungan Otomatis
    df['Sisa Saldo'] = df['Anggaran (Rp)'] - df['Terpakai (Rp)']
    total_dana = df['Anggaran (Rp)'].sum()
    total_terpakai = df['Terpakai (Rp)'].sum()
    sisa_kas = total_dana - total_terpakai

    # Tampilan Atas
    c1, c2 = st.columns(2)
    with c1:
        st.info(f"**Total Dana Desa:** \nRp {total_dana:,}")
    with c2:
        st.success(f"**Sisa Kas Saat Ini:** \nRp {sisa_kas:,}")

    st.divider()
    st.subheader("📋 Rincian Pengeluaran & Proyek")
    st.table(df)

except Exception as e:
    st.error("Gagal membaca data. Pastikan file data.csv sudah ada.")

st.divider()
st.subheader("💬 Aspirasi Warga")
with st.form("aspirasi"):
    nama = st.text_input("Nama")
    pesan = st.text_area("Pesan")
    if st.form_submit_button("Kirim"):
        st.success("Terkirim!")
