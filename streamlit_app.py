import streamlit as st

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Katalog Bakpao Ceu Mumun",
    page_icon="🥟",
    layout="wide"
)

# =========================
# DATA PRODUK
# =========================
produk = [
    {
        "nama": "Bakpao Coklat",
        "harga": "Rp 5.000",
        "deskripsi": "Bakpao lembut dengan isian coklat premium yang lumer di mulut.",
        "gambar": "https://images.unsplash.com/photo-1547592180-85f173990554?q=80&w=1200&auto=format&fit=crop"
    },

    {
        "nama": "Bakpao Ayam",
        "harga": "Rp 7.000",
        "deskripsi": "Isi ayam gurih dengan bumbu spesial yang nikmat dan mengenyangkan.",
        "gambar": "https://images.unsplash.com/photo-1496116218417-1a781b1c416c?q=80&w=1200&auto=format&fit=crop"
    },

    {
        "nama": "Bakpao Strawberry",
        "harga": "Rp 6.000",
        "deskripsi": "Perpaduan roti lembut dengan selai strawberry manis segar.",
        "gambar": "https://images.unsplash.com/photo-1509440159596-0249088772ff?q=80&w=1200&auto=format&fit=crop"
    }
]

# =========================
# CSS
# =========================
st.markdown("""
<style>

.stApp {
    background-image: url("https://images.unsplash.com/photo-1496116218417-1a781b1c416c?q=80&w=1600&auto=format&fit=crop");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.main-box {
    background: rgba(0,0,0,0.45);
    padding: 35px;
    border-radius: 30px;
    backdrop-filter: blur(8px);
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
    background: rgba(255,255,255,0.12);
    backdrop-filter: blur(18px);
    border-radius: 28px;
    overflow: hidden;
    margin-bottom: 35px;
    border: 1px solid rgba(255,255,255,0.2);
    box-shadow: 0 10px 35px rgba(0,0,0,0.35);
    transition: 0.3s;
}

.card:hover {
    transform: translateY(-8px);
}

.card img {
    width: 100%;
    height: 260px;
    object-fit: cover;
}

.card-body {
    padding: 28px;
}

.nama-produk {
    font-size: 32px;
    font-weight: bold;
    color: white;
    margin-bottom: 12px;
}

.harga {
    font-size: 28px;
    color: #FFD54F;
    font-weight: bold;
    margin-bottom: 15px;
}

.deskripsi {
    color: #F1F1F1;
    font-size: 18px;
    line-height: 1.7;
    margin-bottom: 22px;
}

.badge {
    display: inline-block;
    background: rgba(255,255,255,0.15);
    padding: 10px 18px;
    border-radius: 14px;
    color: white;
    font-weight: bold;
}

.contact-title {
    color: white;
    font-size: 50px;
    font-weight: bold;
    margin-top: 50px;
    margin-bottom: 25px;
}

.contact-box {
    background: rgba(255,255,255,0.12);
    backdrop-filter: blur(18px);
    border-radius: 30px;
    padding: 50px 35px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.25);
    box-shadow: 0 10px 35px rgba(0,0,0,0.35);
}

.contact-name {
    color: white;
    font-size: 52px;
    font-weight: bold;
    margin-bottom: 20px;
}

.contact-text {
    color: #f1f1f1;
    font-size: 28px;
    margin-bottom: 15px;
}

.contact-desc {
    color: #eeeeee;
    font-size: 20px;
    margin-top: 20px;
    line-height: 1.8;
}

div.stLinkButton {
    margin-top: 35px;
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
}

</style>
""", unsafe_allow_html=True)

# =========================
# WRAPPER
# =========================
st.markdown('<div class="main-box">', unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown("""
<div class="title">
🥟 Katalog Bakpao Ceu Mumun
</div>

<div class="subtitle">
Bakpao homemade lembut, halal, dan cocok untuk reseller maupun acara keluarga
</div>
""", unsafe_allow_html=True)

# =========================
# PRODUK
# =========================
col1, col2 = st.columns(2)

for i, item in enumerate(produk):

    html_card = f"""
    <div class="card">

        <img src="{item['gambar']}">

        <div class="card-body">

            <div class="nama-produk">
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
    """

    if i % 2 == 0:
        with col1:
            st.markdown(html_card, unsafe_allow_html=True)

    else:
        with col2:
            st.markdown(html_card, unsafe_allow_html=True)

# =========================
# CONTACT
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
        📱 WhatsApp: 0895701152656
    </div>

    <div class="contact-text">
        📍 Bandung, Jawa Barat
    </div>

    <div class="contact-desc">
        Melayani reseller, acara keluarga, snack box,
        dan pesanan harian.
    </div>

</div>
""", unsafe_allow_html=True)

# =========================
# TOMBOL WA
# =========================
wa_link = "https://wa.me/62895701152656"

st.link_button(
    "📲 Pesan Sekarang via WhatsApp",
    wa_link,
    use_container_width=True
)

st.markdown("</div>", unsafe_allow_html=True)
