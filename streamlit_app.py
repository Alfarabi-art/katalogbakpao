import streamlit as st

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Bakpao Ceu Mumun",
    page_icon="🥟",
    layout="wide"
)

# =====================================================
# VIDEO BACKGROUND
# =====================================================

VIDEO_URL = "https://raw.githubusercontent.com/Alfarabi-art/bakpao/main/bg.mp4"

st.markdown(f"""
<style>

video {{
    position: fixed;
    right: 0;
    bottom: 0;
    min-width: 100%;
    min-height: 100%;
    object-fit: cover;
    z-index: -2;
}}

.video-overlay {{
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,0.45);
    z-index: -1;
}}

.stApp {{
    background: transparent;
}}

</style>

<video autoplay muted loop playsinline>
    <source src="{VIDEO_URL}" type="video/mp4">
</video>

<div class="video-overlay"></div>

""", unsafe_allow_html=True)

# =========================
# DATA PRODUK
# =========================
produk = [
    {
        "nama": "Bakpao Coklat",
        "harga": "Rp 5.000",
        "deskripsi": "Bakpao lembut dengan isian coklat premium yang lumer di mulut.",
        "gambar": "https://raw.githubusercontent.com/Alfarabi-art/katalogbakpao/main/images/cokelat.jpg"
    },
    {
        "nama": "Bakpao Ayam",
        "harga": "Rp 7.000",
        "deskripsi": "Isi ayam gurih dengan bumbu spesial yang nikmat dan mengenyangkan.",
        "gambar": "https://raw.githubusercontent.com/Alfarabi-art/katalogbakpao/main/images/ayam.jpg"
    },
    {
        "nama": "Bakpao Kacang",
        "harga": "Rp 5.000",
        "deskripsi": "Bakpao lembut dengan isian kacang manis yang halus, legit, dan nikmat di setiap gigitan.",
        "gambar": "https://raw.githubusercontent.com/Alfarabi-art/katalogbakpao/main/images/kacang.jpg"
    },
    {
        "nama": "Bakpao Kentang",
        "harga": "Rp 5.000",
        "deskripsi": "Bakpao empuk dengan isian kentang gurih yang lembut dan bikin ketagihan.",
        "gambar": "https://raw.githubusercontent.com/Alfarabi-art/katalogbakpao/main/images/kentang.jpg"
    },
    {
        "nama": "Bakpao Unti Kelapa",
        "harga": "Rp 5.000",
        "deskripsi": "Perpaduan kelapa manis tradisional dengan aroma yang harum dan cita rasa khas rumahan.",
        "gambar": "https://raw.githubusercontent.com/Alfarabi-art/katalogbakpao/main/images/kelapa.jpg"
    }
]

# =========================
# CSS
# =========================
st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.main {
    background: transparent;
    padding-top: 10px;
}

.block-container {
    padding-top: 1rem;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.title {
    text-align: center;
    font-size: 60px;
    font-weight: bold;
    color: white;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    font-size: 22px;
    color: #eeeeee;
    margin-bottom: 50px;
}

.card {
    background: rgba(255,255,255,0.10);
    backdrop-filter: blur(14px);
    border: 1px solid rgba(255,255,255,0.18);
    border-radius: 25px;
    overflow: hidden;
    margin-bottom: 30px;
    box-shadow: 0 8px 28px rgba(0,0,0,0.30);
    transition: 0.3s;
    min-height: 540px;
}

.card:hover {
    transform: translateY(-5px);
}

.card img {
    width: 100%;
    height: 250px;
    object-fit: cover;
}

.card-body {
    padding: 24px;
}

.nama-produk {
    font-size: 34px;
    font-weight: bold;
    color: white;
}

.harga {
    font-size: 28px;
    color: #FFD54F;
    font-weight: bold;
    margin-top: 10px;
}

.deskripsi {
    color: #eeeeee;
    margin-top: 15px;
    font-size: 17px;
    line-height: 1.8;
    min-height: 90px;
}

.badge {
    display: inline-block;
    margin-top: 20px;
    background: rgba(255,255,255,0.15);
    color: white;
    padding: 10px 18px;
    border-radius: 14px;
    font-weight: bold;
}

.contact-title {
    color: white;
    font-size: 48px;
    font-weight: bold;
    margin-top: 60px;
    margin-bottom: 30px;
}

.contact-box {
    background: rgba(255,255,255,0.10);
    backdrop-filter: blur(16px);
    border-radius: 28px;
    padding: 50px 35px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.20);
    box-shadow: 0 8px 30px rgba(0,0,0,0.30);
}

.contact-name {
    color: white;
    font-size: 56px;
    font-weight: bold;
    margin-bottom: 25px;
}

.contact-text {
    color: #f1f1f1;
    font-size: 30px;
    margin-bottom: 18px;
}

.contact-desc {
    color: #eeeeee;
    font-size: 22px;
    margin-top: 25px;
    line-height: 1.8;
}

div.stLinkButton > a {
    background: linear-gradient(135deg, #25D366, #128C7E);
    color: white !important;
    font-size: 24px;
    font-weight: bold;
    border-radius: 18px;
    padding: 18px 24px;
    text-align: center;
    border: none;
    box-shadow: 0 8px 25px rgba(0,0,0,0.3);
    transition: 0.3s;
}

div.stLinkButton > a:hover {
    transform: scale(1.03);
    background: linear-gradient(135deg, #2EEB75, #17A589);
    color: white !important;
}

@media (max-width: 768px) {

    .title {
        font-size: 38px;
        line-height: 1.2;
    }

    .subtitle {
        font-size: 18px;
        padding: 0 10px;
    }

    .nama-produk {
        font-size: 28px;
    }

    .harga {
        font-size: 24px;
    }

    .deskripsi {
        font-size: 15px;
        line-height: 1.6;
    }

    .card img {
        height: 220px;
    }

    .contact-title {
        font-size: 34px;
        text-align: center;
    }

    .contact-name {
        font-size: 38px;
    }

    .contact-text {
        font-size: 22px;
    }

    .contact-desc {
        font-size: 18px;
    }

    div.stLinkButton > a {
        font-size: 18px !important;
        padding: 14px 18px !important;
    }

    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown('<div class="main">', unsafe_allow_html=True)

st.markdown("""
<div class="title">
🥟 Bakpao Ceu Mumun
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="subtitle">
Bakpao homemade lembut, halal, dan cocok untuk reseller maupun acara keluarga
</div>
""", unsafe_allow_html=True)

# =========================
# PRODUK
# =========================
col1, col2 = st.columns(2, gap="large")

for i, item in enumerate(produk):

    html = f"""
    <div class="card">
        <img src="{item['gambar']}">
        <div class="card-body">
            <div class="nama-produk">{item['nama']}</div>
            <div class="harga">{item['harga']}</div>
            <div class="deskripsi">{item['deskripsi']}</div>
            <div class="badge">⭐ Best Seller</div>
        </div>
    </div>
    """

    if i % 2 == 0:
        col1.markdown(html, unsafe_allow_html=True)
    else:
        col2.markdown(html, unsafe_allow_html=True)

# =========================
# CONTACT PERSON
# =========================
st.markdown("""
<div class="contact-title">
📞 Contact Person
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="contact-box">

<div class="contact-name">
🥟 Bakpao Ceu Mumun
</div>

<div class="contact-text">
📱 WhatsApp: 0882-1309-5215
</div>

<div class="contact-text">
📍 Babakan Pasar, Bogor Tengah
</div>

<div class="contact-desc">
Melayani reseller, acara keluarga, snack box, dan pesanan harian.
</div>

</div>
""", unsafe_allow_html=True)

# JARAK TOMBOL
st.markdown(
    "<div style='margin-top:45px;'></div>",
    unsafe_allow_html=True
)

# LINK WA
wa_link = "https://wa.me/6288213095215"

st.link_button(
    "📲 Pesan Sekarang via WhatsApp",
    wa_link,
    use_container_width=True
)

st.markdown("</div>", unsafe_allow_html=True)
