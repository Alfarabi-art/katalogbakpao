import streamlit as st

# =========================
# PAGE CONFIG
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
        "gambar": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?q=80&w=1200&auto=format&fit=crop"
    },
    {
        "nama": "Bakpao Ayam",
        "harga": "Rp 7.000",
        "deskripsi": "Isi ayam gurih dengan bumbu spesial yang nikmat dan mengenyangkan.",
        "gambar": "https://images.unsplash.com/photo-1544025162-d76694265947?q=80&w=1200&auto=format&fit=crop"
    },
    {
        "nama": "Bakpao Strawberry",
        "harga": "Rp 6.000",
        "deskripsi": "Perpaduan roti lembut dengan selai strawberry manis segar.",
        "gambar": "https://images.unsplash.com/photo-1496116218417-1a781b1c416c?q=80&w=1200&auto=format&fit=crop"
    },
]

# =========================
# CSS
# =========================
st.markdown("""
<style>

html, body, [class*="css"]  {
    font-family: 'Poppins', sans-serif;
}

/* BACKGROUND */
.stApp {
    background-image: url("https://images.unsplash.com/photo-1496116218417-1a781b1c416c?q=80&w=1600&auto=format&fit=crop");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* OVERLAY */
.main {
    background: rgba(0,0,0,0.45);
    padding: 40px;
    border-radius: 30px;
}

/* TITLE */
.title {
    text-align: center;
    font-size: 64px;
    font-weight: 800;
    color: white;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    font-size: 24px;
    color: rgba(255,255,255,0.85);
    margin-bottom: 50px;
}

/* CARD */
.card {
    background: rgba(255,255,255,0.08);

    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);

    border: 1px solid rgba(255,255,255,0.15);

    border-radius: 28px;

    overflow: hidden;

    margin-bottom: 35px;

    box-shadow:
        0 8px 32px rgba(0,0,0,0.35),
        inset 0 1px 1px rgba(255,255,255,0.08);

    transition: all 0.35s ease;

    min-height: 680px;
}

.card:hover {
    transform: translateY(-8px) scale(1.01);

    box-shadow:
        0 15px 40px rgba(0,0,0,0.45),
        inset 0 1px 1px rgba(255,255,255,0.1);
}

/* IMAGE */
.card img {
    width: 100%;
    height: 320px;
    object-fit: cover;

    border-top-left-radius: 28px;
    border-top-right-radius: 28px;
}

/* BODY */
.card-body {
    padding: 28px;
}

/* PRODUCT NAME */
.nama-produk {
    font-size: 38px;
    font-weight: 800;
    color: white;
    margin-bottom: 10px;
}

/* PRICE */
.harga {
    font-size: 30px;
    font-weight: bold;
    color: #FFD54F;
    margin-bottom: 18px;
}

/* DESCRIPTION */
.deskripsi {
    color: rgba(255,255,255,0.88);
    font-size: 20px;
    line-height: 1.8;
    margin-bottom: 28px;
}

/* BADGE */
.badge {
    display: inline-block;

    background: rgba(255,255,255,0.12);

    border: 1px solid rgba(255,255,255,0.12);

    color: white;

    padding: 12px 20px;

    border-radius: 16px;

    font-size: 18px;
    font-weight: bold;

    backdrop-filter: blur(8px);
}

/* CONTACT TITLE */
.contact-title {
    color: white;
    font-size: 50px;
    font-weight: bold;
    margin-top: 70px;
    margin-bottom: 35px;
}

/* CONTACT BOX */
.contact-box {
    background: rgba(255,255,255,0.08);

    backdrop-filter: blur(15px);

    border-radius: 30px;

    padding: 55px 40px;

    text-align: center;

    border: 1px solid rgba(255,255,255,0.15);

    box-shadow: 0 10px 35px rgba(0,0,0,0.35);
}

/* CONTACT NAME */
.contact-name {
    color: white;
    font-size: 58px;
    font-weight: 800;
    margin-bottom: 25px;
}

/* CONTACT TEXT */
.contact-text {
    color: rgba(255,255,255,0.92);
    font-size: 28px;
    margin-bottom: 15px;
}

/* CONTACT DESC */
.contact-desc {
    color: rgba(255,255,255,0.85);
    font-size: 22px;
    margin-top: 25px;
    line-height: 1.8;
}

/* BUTTON */
div.stLinkButton > a {
    background: linear-gradient(135deg, #25D366, #128C7E);

    color: white !important;

    font-size: 22px;
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

</style>
""", unsafe_allow_html=True)

# =========================
# WRAPPER
# =========================
st.markdown('<div class="main">', unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown("""
<div class="title">
🥟 Katalog Bakpao Ceu Mumun
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
col1, col2 = st.columns(2)

for i, item in enumerate(produk):

    card = f"""
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
        col1.markdown(card, unsafe_allow_html=True)
    else:
        col2.markdown(card, unsafe_allow_html=True)

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
📱 WhatsApp: 0895701152656
</div>

<div class="contact-text">
📍 Bandung, Jawa Barat
</div>

<div class="contact-desc">
Melayani reseller, acara keluarga, snack box, dan pesanan harian.
</div>

</div>
""", unsafe_allow_html=True)

# =========================
# SPACING
# =========================
st.markdown(
    "<div style='margin-top:45px;'></div>",
    unsafe_allow_html=True
)

# =========================
# BUTTON WHATSAPP
# =========================
wa_link = "https://wa.me/62895701152656"

st.link_button(
    "📲 Pesan Sekarang via WhatsApp",
    wa_link,
    use_container_width=True
)

# =========================
# END WRAPPER
# =========================
st.markdown("</div>", unsafe_allow_html=True)
