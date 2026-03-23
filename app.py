import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# 1. Judul & Header (KODE ASLI ANDA)
st.set_page_config(page_title="Transparansi Dana Desa", layout="centered")
st.title("🏡 Sistem Transparansi Dana Desa")
st.markdown("Portal pemantauan anggaran desa untuk warga.")
st.divider()

# 2. Data Anggaran (KODE ASLI ANDA)
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

# 3. Ringkasan Kas Desa (KODE ASLI ANDA)
total_dana = df['Anggaran (Rp)'].sum()
total_terpakai = df['Terpakai (Rp)'].sum()
sisa_kas = total_dana - total_terpakai

c1, c2 = st.columns(2)
with c1:
    st.info(f"**Total Dana Desa:** \nRp {total_dana:,}")
with c2:
    st.success(f"**Sisa Kas Saat Ini:** \nRp {sisa_kas:,}")

st.divider()

# 4. Tabel Rinci (KODE ASLI ANDA)
st.subheader("📋 Rincian Pengeluaran & Proyek")
st.table(df)

# 5. Interaksi Warga / Kolom Komentar (FITUR BARU)
st.divider()
st.subheader("💬 Masukan & Komentar Publik")
st.caption("Gunakan kolom di bawah untuk memberikan saran atau masukan kepada admin secara publik.")

# Konfigurasi Disqus
disqus_shortname = "dana-desa-kopyah" 

disqus_html = f"""
    <div id="disqus_thread"></div>
    <script>
        var disqus_config = function () {{
            this.page.url = window.location.origin;
            this.page.identifier = "dana-desa-kopyah-final-banget"; 
        }};
        (function() {{
            var d = document, s = d.createElement('script');
            s.src = 'https://{disqus_shortname}.disqus.com/embed.js';
            s.setAttribute('data-timestamp', +new Date());
            (d.head || d.body).appendChild(s);
        }})();
    </script>
"""

# Menampilkan Disqus
components.html(disqus_html, height=600, scrolling=True)
