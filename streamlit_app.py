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
    background: rgba(0,0,0,0.55);
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
    border-radius: 25px;
    padding: 20px;
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.2);
    margin-bottom: 25px;
    transition: 0.3s;
}}

.catalog-card:hover {{
    transform: translateY(-5px);
    background: rgba(255,255,255,0.15);
}}

.contact-box {{
    background: rgba(255,255,255,0.12);
    border-radius: 25px;
    padding: 30px;
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.2);
    text-align: center;
}}

.stButton button {{
    width:100%;
    border-radius:15px;
    border:none;
    background:#25D366;
    color:white;
    font-weight:bold;
    padding:14px;
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
<h1 style='font-size:60px;'>🥟 Katalog Bakpao Ceu Mumun</h1>
<h3>Bakpao lembut, isi melimpah, cocok untuk reseller & keluarga</h3>
""", unsafe_allow_html=True)

# =========================================
# DATA PRODUK
# =========================================

produk = [
    {
        "nama": "Bakpao Coklat",
        "harga": "Rp 5.000",
        "deskripsi": "Bakpao lembut dengan isian coklat manis premium yang lumer di mulut.",
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
    },

    {
        "nama": "Bakpao Unti Kelapa",
        "harga": "Rp 5.000",
        "deskripsi": "Kelapa manis tradisional dengan aroma khas yang lezat.",
        "gambar": "images/kelapa.jpg"
    }
]

# =========================================
# KATALOG PRODUK
# =========================================

st.write("")
st.markdown("## 🛒 Daftar Produk")

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
        <h2>{item['nama']}</h2>
        <h3 style='color:#ffd54f;'>
        {item['harga']}
        </h3>

        <p style='font-size:17px;'>
        {item['deskripsi']}
        </p>
        """, unsafe_allow_html=True)

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )

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
