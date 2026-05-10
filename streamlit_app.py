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

.title {
    text-align: center;
    font-size: 55px;
    font-weight: bold;
    color: white;
}

.subtitle {
    text-align: center;
    font-size: 20px;
    color: #eeeeee;
    margin-bottom: 40px;
}

.card {
    background: rgba(255,255,255,0.12);
    backdrop-filter: blur(18px);
    border-radius: 25px;
    overflow: hidden;
    margin-bottom: 30px;
    border: 1px solid rgba(255,255,255,0.2);
    box-shadow: 0 8px 30px rgba(0,0,0,0.35);
}

.card-img {
    width: 100%;
    height: 260px;
    object-fit: cover;
}

.card-body {
    padding: 25px;
}

.nama {
    color: white;
    font-size: 30px;
    font-weight: bold;
    margin-bottom: 10px;
}

.harga {
    color: #FFD54F;
    font-size: 28px;
    font-weight: bold;
    margin-bottom: 15px;
}

.deskripsi {
    color: #f1f1f1;
    font-size: 18px;
    line-height: 1.7;
}

.badge {
    margin-top: 20px;
    display: inline-block;
    background: rgba(255,255,255,0.15);
    color: white;
    padding: 10px 18px;
    border-radius: 12px;
    font-weight: bold;
}

.contact-box {
    margin-top: 50px;
    background: rgba(255,255,255,0.12);
    backdrop-filter: blur(18px);
    border-radius: 30px;
    padding: 40px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.2);
}

.contact-title {
    color: white;
    font-size: 45px;
    font-weight: bold;
    margin-bottom: 20px;
}

.contact-text {
    color: white;
    font-size: 24px;
    margin-bottom: 10px;
}

.contact-desc {
    color: #eeeeee;
    font-size: 18px;
    margin-top: 20px;
    line-height: 1.7;
}

div.stLinkButton {
    margin-top: 30px;
}

div.stLinkButton > a {
    background: linear-gradient(135deg,#25D366,#128C7E);
    color: white !important;
    border-radius: 15px;
    font-size: 22px;
    font-weight: bold;
    padding: 16px 24px;
    border: none;
}

</style>
""", unsafe_allow_html=True)

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

    card_html = f"""
    <div class="card">

        <img class="card-img" src="{item['gambar']}">

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
    """

    if i % 2 == 0:
        with col1:
            st.markdown(card_html, unsafe_allow_html=True)

    else:
        with col2:
            st.markdown(card_html, unsafe_allow_html=True)

# =========================
# CONTACT
# =========================
st.markdown("""
<div class="contact-box">

    <div class="contact-title">
        📞 Contact Person
    </div>

    <div class="contact-text">
        📱 WhatsApp: 0895701152656
    </div>

    <div class="contact-text">
        📍 Bandung, Jawa Barat
    </div>

    <div class="contact-desc">
        Melayani reseller, snack box, acara keluarga,
        dan pesanan harian.
    </div>

</div>
""", unsafe_allow_html=True)

# =========================
# BUTTON WA
# =========================
st.link_button(
    "📲 Pesan Sekarang via WhatsApp",
    "https://wa.me/62895701152656",
    use_container_width=True
)
