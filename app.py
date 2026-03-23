import streamlit as st
import streamlit.components.v1 as components

# 1. PENGATURAN HALAMAN
st.set_page_config(page_title="Laporan Dana Desa Kopyah", layout="centered")

# 2. JUDUL DAN KONTEN APLIKASI
st.title("📊 Transparansi Dana Desa Kopyah")
st.write("Selamat datang di aplikasi pelaporan dana desa. Di sini Anda dapat melihat rincian penggunaan anggaran secara transparan.")

# --- Bagian isi aplikasi Anda (Contoh) ---
st.info("Gunakan kolom di bawah untuk memberikan saran atau masukan kepada admin.")
# ------------------------------------------

# 3. BAGIAN KOLOM KOMENTAR (DISQUS)
st.divider()
st.subheader("💬 Masukan & Komentar Publik")

# Nama unik dari akun Disqus Anda
disqus_shortname = "dana-desa-kopyah" 

# Kode HTML untuk memanggil Disqus
disqus_html = f"""
    <div id="disqus_thread"></div>
    <script>
        var disqus_config = function () {{
            this.page.url = window.location.origin;
            this.page.identifier = "dana-desa-kopyah-main"; 
        }};
        (function() {{
            var d = document, s = d.createElement('script');
            s.src = 'https://{disqus_shortname}.disqus.com/embed.js';
            s.setAttribute('data-timestamp', +new Date());
            (d.head || d.body).appendChild(s);
        }})();
    </script>
    <noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
"""

# Menampilkan kolom komentar di aplikasi Streamlit
components.html(disqus_html, height=600, scrolling=True)
