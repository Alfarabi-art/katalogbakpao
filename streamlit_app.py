import streamlit as st

# =========================================
# CONFIG
# =========================================

st.set_page_config(
    page_title="Katalog Bakpao Ceu Mumun",
    page_icon="🥟",
    layout="wide"
)

# =========================================
# VIDEO BACKGROUND
# =========================================

VIDEO_URL = "https://raw.githubusercontent.com/Alfarabi-art/bakpao/main/bg.mp4"

st.markdown(f"""
<style>

.stApp {{
    background: transparent;
}}

video {{
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
    top:0;
    left:0;
    width:100%;
    height:100%;
    background: rgba(0,0,0,0.60);
    z-index:-1;
}}

.block-container {{
    padding-top: 2rem;
}}

h1,h2,h3,h4,h5,h6,p,label,span {{
    color:white !important;
}}

.catalog-card {{
    background: rgba(255,255,255,0.10);
    border-radius: 30px;
    padding: 22px;
    backdrop-filter: blur(14px);
    border: 1px solid rgba(255,255,255,0.25);
    margin-bottom: 30px;
    transition: 0.35s;
    box-shadow: 0 8px 30px rgba(0,0,0,0.25);
}}

.catalog-card:hover {{
    transform: translateY(-8px) scale(1.02);
    background: rgba(255,255,255,0.16);
    box-shadow: 0 15px 40px rgba(0,0,0,0.35);
}}

.contact-box {{
    background: rgba(255,255,255,0.12);
    border-radius: 30px;
    padding: 35px;
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.2);
    text-align: center;
}}

.stButton button {{
    width:100%;
    border-radius:18px;
    border:none;
    background:#25D366;
    color:white;
    font-weight:bold;
    padding:16px;
    font-size:18px;
}}

</style>

<video autoplay muted loop>
    <source src="{VIDEO_URL}" type="video/mp4">
</video>

<div class="overlay"></div>

""", unsafe_allow_html=True)

# =========================================
# HEADER
# =========================================

st.markdown("""
<div style='text-align:center; padding:20px 0 40px 0;'>

<h1 style='
font-size:70px;
font-weight:bold;
margin-bottom:10px;
background: linear-gradient(to right, #ffd54f, #ffffff);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
'>
🥟 Katalog Bakpao Ceu Mumun
</h1>

<h3 style='
font-size:24px;
color:white;
font-weight:400;
'>
Bakpao lembut • Isi melimpah • Cocok untuk reseller & keluarga
</h3>

<p style='
font-size:18px;
color:#eeeeee;
max-width:700px;
margin:auto;
line-height:1.8;
'>
Nikmati bakpao premium dengan berbagai pilihan rasa favorit.
Dibuat fresh setiap hari menggunakan bahan berkualitas dan cocok untuk camilan,
acara keluarga, reseller, maupun usaha kuliner.
</p>

</div>
""", unsafe_allow_html=True)

# =========================================
# DATA PRODUK
# =========================================

produk = [
    {
        "nama": "Bakpao Coklat",
        "harga": "Rp 5.000",
        "deskripsi": "Bakpao lembut dengan isian coklat premium yang lumer di mulut.",
        "gambar": "images/cokelat.jpg"
    },

    {
        "nama": "Bakpao Ayam",
        "harga": "Rp 7.000",
        "deskripsi": "Isi ayam gurih dengan bumbu spesial yang nikmat dan mengenyangkan.",
        "gambar": "images/ayam.jpg"
    },

    {
        "nama": "Bakpao Kacang",
        "harga": "Rp 5.000",
        "deskripsi": "Isian kacang hijau manis dengan tekstur lembut dan legit.",
        "gambar": "images/kacang.jpg"
    },

    {
        "nama": "Bakpao Kentang",
        "harga": "Rp 5.000",
        "deskripsi": "Bakpao isi kentang creamy dengan rasa gurih yang khas.",
        "gambar": "images/kentang.jpg"
    }
]

# =========================================
# KATALOG PRODUK
# =========================================

st.write("")
st.markdown("## ✨ Menu Favorit Hari Ini")

cols = st.columns(2)

for index, item in enumerate(produk):

    with cols[index % 2]:

        st.markdown(
            '<div class="catalog-card">',
            unsafe_allow_html=True
        )

        st.image(
            item["gambar"],
            use_container_width=True
        )

        st.markdown(f"""
        <div style='padding-top:10px;'>

        <h2 style='
        font-size:32px;
        margin-bottom:5px;
        color:white;
        '>
        {item['nama']}
        </h2>

        <h3 style='
        color:#ffd54f;
        font-size:28px;
        margin-bottom:15px;
        '>
        {item['harga']}
        </h3>

        <p style='
        font-size:18px;
        line-height:1.8;
        color:#f1f1f1;
        '>
        {item['deskripsi']}
        </p>

        <div style='
        margin-top:20px;
        padding:10px 18px;
        border-radius:14px;
        background:rgba(255,255,255,0.12);
        display:inline-block;
        font-size:15px;
        font-weight:bold;
        color:white;
        '>
        ⭐ Best Seller
        </div>

        </div>
        """, unsafe_allow_html=True)

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )

# =========================================
# TESTIMONI
# =========================================

st.write("")
st.markdown("## 💬 Testimoni Pelanggan")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="catalog-card">
    <h3>⭐️⭐️⭐️⭐️⭐️</h3>
    <p>
    "Bakpaonya lembut banget dan isiannya banyak. Anak-anak suka semua!"
    </p>
    <h4>- Rina</h4>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="catalog-card">
    <h3>⭐️⭐️⭐️⭐️⭐️</h3>
    <p>
    "Cocok buat jualan lagi. Reseller saya banyak yang repeat order."
    </p>
    <h4>- Dedi</h4>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="catalog-card">
    <h3>⭐️⭐️⭐️⭐️⭐️</h3>
    <p>
    "Rasa premium tapi harga tetap ramah di kantong."
    </p>
    <h4>- Salsa</h4>
    </div>
    """, unsafe_allow_html=True)

# =========================================
# CONTACT PERSON
# =========================================

st.write("")
st.markdown("## 📞 Contact Person")

st.markdown("""
<div class="contact-box">

<h2>🥟 Bakpao Ceu Mumun</h2>

<h3>
📱 WhatsApp: 08xxxxxxxxxx
</h3>

<h3>
📍 Alamat: Isi alamat usaha kamu
</h3>

<p>
Melayani reseller, acara keluarga, snack box, dan pesanan harian.
</p>

</div>
""", unsafe_allow_html=True)

# =========================================
# WHATSAPP BUTTON
# =========================================

wa_link = "https://wa.me/628xxxxxxxxxx"

st.link_button(
    "📲 Pesan Sekarang via WhatsApp",
    wa_link,
    use_container_width=True
)
