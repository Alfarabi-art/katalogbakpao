import streamlit as st

st.set_page_config(
    page_title="Katalog Bakpao",
    page_icon="🥟",
    layout="wide"
)

# ================= CSS =================
st.markdown("""
<style>

.stApp{
    background-image: url("https://images.unsplash.com/photo-1495195134817-aeb325a55b65");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

.block-container{
    padding-top: 2rem;
}

.judul{
    text-align:center;
    color:white;
    font-size:60px;
    font-weight:800;
    margin-bottom:10px;
}

.subjudul{
    text-align:center;
    color:white;
    font-size:22px;
    margin-bottom:50px;
}

.card{
    background: rgba(255,255,255,0.12);
    backdrop-filter: blur(14px);
    border-radius:25px;
    overflow:hidden;
    margin-bottom:30px;
    border:1px solid rgba(255,255,255,0.2);
    box-shadow:0 8px 32px rgba(0,0,0,0.35);
}

.card img{
    width:100%;
    height:260px;
    object-fit:cover;
}

.card-body{
    padding:25px;
}

.nama{
    color:white;
    font-size:32px;
    font-weight:700;
    margin-bottom:10px;
}

.harga{
    color:#FFD54F;
    font-size:28px;
    font-weight:800;
    margin-bottom:15px;
}

.deskripsi{
    color:#F5F5F5;
    font-size:18px;
    line-height:1.7;
    margin-bottom:20px;
}

.badge{
    display:inline-block;
    background:rgba(255,255,255,0.15);
    color:white;
    padding:10px 16px;
    border-radius:14px;
    font-weight:600;
}

.contact-box{
    background: rgba(255,255,255,0.12);
    backdrop-filter: blur(14px);
    border-radius:30px;
    padding:40px;
    text-align:center;
    margin-top:50px;
    margin-bottom:40px;
    border:1px solid rgba(255,255,255,0.2);
}

.contact-title{
    color:white;
    font-size:48px;
    font-weight:800;
    margin-bottom:20px;
}

.contact-info{
    color:white;
    font-size:24px;
    margin-bottom:15px;
}

.contact-desc{
    color:#F5F5F5;
    font-size:18px;
    margin-top:20px;
    line-height:1.8;
}

.wa-btn{
    display:inline-block;
    margin-top:30px;
    background:#25D366;
    color:white !important;
    padding:16px 28px;
    border-radius:14px;
    text-decoration:none;
    font-size:22px;
    font-weight:700;
}

</style>
""", unsafe_allow_html=True)

# ================= HEADER =================
st.markdown("""
<div class="judul">
🥟 Bakpao Ceu Mumun
</div>

<div class="subjudul">
Bakpao Premium • Lembut • Fresh Setiap Hari
</div>
""", unsafe_allow_html=True)

# ================= DATA =================
produk = [
    {
        "nama":"Bakpao Coklat",
        "harga":"Rp 5.000",
        "deskripsi":"Bakpao lembut dengan isian coklat premium yang lumer di mulut.",
        "gambar":"https://images.unsplash.com/photo-1504674900247-0877df9cc836"
    },

    {
        "nama":"Bakpao Ayam",
        "harga":"Rp 7.000",
        "deskripsi":"Isi ayam gurih dengan bumbu spesial yang nikmat dan mengenyangkan.",
        "gambar":"https://images.unsplash.com/photo-1544025162-d76694265947"
    },

    {
        "nama":"Bakpao Keju",
        "harga":"Rp 6.000",
        "deskripsi":"Perpaduan roti lembut dan keju creamy premium.",
        "gambar":"https://images.unsplash.com/photo-1515003197210-e0cd71810b5f"
    },

    {
        "nama":"Bakpao Kacang Hijau",
        "harga":"Rp 5.000",
        "deskripsi":"Isian kacang hijau manis tradisional.",
        "gambar":"https://images.unsplash.com/photo-1482049016688-2d3e1b311543"
    }
]

# ================= PRODUK =================
col1, col2 = st.columns(2)

for i, item in enumerate(produk):

    html = f"""
    <div class="card">

        <img src="{item['gambar']}">

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
            st.markdown(html, unsafe_allow_html=True)
    else:
        with col2:
            st.markdown(html, unsafe_allow_html=True)

# ================= CONTACT =================
st.markdown("""
<div class="contact-box">

    <div class="contact-title">
        📞 Contact Person
    </div>

    <div class="contact-info">
        📱 WhatsApp: 0895701152656
    </div>

    <div class="contact-info">
        📍 Bandung, Jawa Barat
    </div>

    <div class="contact-desc">
        Melayani reseller, snack box, acara keluarga,
        arisan, dan pesanan harian.
    </div>

    <a class="wa-btn"
       href="https://wa.me/62895701152656"
       target="_blank">

       📲 Pesan Sekarang via WhatsApp

    </a>

</div>
""", unsafe_allow_html=True)
