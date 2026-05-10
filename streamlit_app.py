import streamlit as st

# =========================================
# CONFIG
# =========================================
st.set_page_config(
    page_title="Katalog Bakpao Ceu Mumun",
    layout="wide"
)

# =========================================
# VIDEO BACKGROUND
# =========================================
VIDEO_URL = "https://raw.githubusercontent.com/Alfarabi-art/bakpao/main/bg.mp4"

# =========================================
# CSS
# =========================================
st.markdown(f"""
<style>

header {{
    visibility: hidden;
}}

[data-testid="stToolbar"] {{
    display: none;
}}

.block-container {{
    padding-top: 2rem;
    max-width: 1400px;
}}

.video-bg {{
    position: fixed;
    right: 0;
    bottom: 0;
    min-width: 100%;
    min-height: 100%;
    object-fit: cover;
    z-index: -2;
}}

.overlay {{
    position: fixed;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,0.45);
    top: 0;
    left: 0;
    z-index: -1;
}}

.title {{
    text-align: center;
    color: white;
    font-size: 68px;
    font-weight: bold;
    margin-top: 20px;
}}

.subtitle {{
    text-align: center;
    color: #eeeeee;
    font-size: 24px;
    margin-bottom: 60px;
}}

.card {{
    background: rgba(255,255,255,0.10);
    backdrop-filter: blur(14px);
    border: 1px solid rgba(255,255,255,0.18);
    border-radius: 25px;
    overflow: hidden;
    margin-bottom: 35px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.35);
}}

.card-body {{
    padding: 24px;
}}

.nama {{
    font-size: 34px;
    font-weight: bold;
    color: white;
}}

.harga {{
    font-size: 28px;
    color: #FFD54F;
    font-weight: bold;
    margin-top: 10px;
}}

.deskripsi {{
    color: #eeeeee;
    margin-top: 15px;
    font-size: 17px;
    line-height: 1.8;
}}

.badge {{
    display: inline-block;
    margin-top: 20px;
    background: rgba(255,255,255,0.15);
    color: white;
    padding: 10px 18px;
    border-radius: 14px;
    font-weight: bold;
}}

.contact-box {{
    background: rgba(255,255,255,0.10);
    backdrop-filter: blur(14px);
    border: 1px solid rgba(255,255,255,0.18);
    border-radius: 30px;
    padding: 50px;
    text-align: center;
    margin-top: 60px;
    margin-bottom: 50px;
}}

.contact-title {{
    color: white;
    font-size: 48px;
    font-weight: bold;
}}

.contact-info {{
    color: #eeeeee;
    font-size: 24px;
    margin-top: 15px;
}}

.contact-desc {{
    color: #dddddd;
    font-size: 18px;
    margin-top: 20px;
}}

.wa-btn {{
    display: inline-block;
    margin-top: 35px;
    background: #25D366;
    color: white !important;
    padding: 16px 34px;
    border-radius: 18px;
    text-decoration: none;
    font-size: 20px;
    font-weight: bold;
}}

</style>

<video autoplay muted loop class="video-bg">
    <source src="{VIDEO_URL}" type="video/mp4">
</video>

<div class="overlay"></div>

""", unsafe_allow_html=True)

# =========================================
# DATA PRODUK
# =========================================
produk = [

    {
        "nama": "Bakpao Coklat",
        "harga": "Rp 5.000",
        "gambar": "images/cokelat.jpg",
        "deskripsi": "Bakpao lembut dengan isian coklat premium yang lumer di mulut."
    },

    {
        "nama": "Bakpao Ayam",
        "harga": "Rp 7.000",
        "gambar": "images/ayam.jpg",
        "deskripsi": "Isi ayam gurih dengan bumbu spesial yang nikmat dan mengenyangkan."
    },

    {
        "nama": "Bakpao Kacang Hijau",
        "harga": "Rp 5.000",
        "gambar": "images/kacang.jpg",
        "deskripsi": "Bakpao lembut dengan isian kacang hijau manis yang halus dan legit."
    },

    {
        "nama": "Bakpao Unti Kelapa",
        "harga": "Rp 5.000",
        "gambar": "images/kelapa.jpg",
        "deskripsi": "Perpaduan kelapa manis tradisional dengan aroma pandan yang khas."
    },

    {
        "nama": "Bakpao Kentang",
        "harga": "Rp 5.000",
        "gambar": "images/kentang.jpg",
        "deskripsi": "Bakpao empuk dengan isian kentang gurih creamy yang lezat."
    }

]

# =========================================
# HEADER
# =========================================
st.markdown("""
<div class="title">
🥟 Bakpao Ceu Mumun
</div>

<div class="subtitle">
Bakpao homemade lembut, halal, dan cocok untuk reseller maupun acara keluarga
</div>
""", unsafe_allow_html=True)

# =========================================
# PRODUK
# =========================================
col1, col2 = st.columns(2, gap="large")

for i, item in enumerate(produk):

    target = col1 if i % 2 == 0 else col2

    with target:

        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.image(
            item["gambar"],
            use_container_width=True
        )

        st.markdown(f"""
        <div class="card-body">

            <div class="nama">
                {item['nama']}
            </div>

            <div class="harga">
                {item['harga']}
            </div>

            <div class="deskripsi">
                {item['deskripsi']}
            </div>

            <div class="badge">
                ⭐ Best Seller
            </div>

        </div>
        </div>
        """, unsafe_allow_html=True)

# =========================================
# CONTACT
# =========================================
st.markdown("""
<div class="contact-box">

    <div class="contact-title">
        🥟 Bakpao Ceu Mumun
    </div>

    <div class="contact-info">
        📱 WhatsApp: 0895701152656
    </div>

    <div class="contact-info">
        📍 Bandung, Jawa Barat
    </div>

    <div class="contact-desc">
        Melayani reseller, snack box, acara keluarga, arisan, dan pesanan harian.
    </div>

    <a class="wa-btn"
       href="https://wa.me/62895701152656"
       target="_blank">

       📲 Pesan Sekarang via WhatsApp

    </a>

</div>
""", unsafe_allow_html=True)
