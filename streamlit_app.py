import streamlit as st

st.set_page_config(
    page_title="Katalog Bakpao Ceu Mumun",
    page_icon="🥟",
    layout="wide"
)

# =========================
# CSS
# =========================
st.markdown("""
<style>

html, body, [class*="css"]{
    font-family: 'Poppins', sans-serif;
}

.stApp{
    background-image: url("https://images.unsplash.com/photo-1495195134817-aeb325a55b65");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* overlay gelap */
.main::before{
    content:"";
    position:fixed;
    top:0;
    left:0;
    width:100%;
    height:100%;
    background: rgba(0,0,0,0.45);
    z-index:-1;
}

/* judul */
.judul{
    text-align:center;
    color:white;
    font-size:60px;
    font-weight:800;
    margin-top:20px;
    margin-bottom:10px;
    text-shadow: 2px 2px 15px rgba(0,0,0,0.5);
}

.subjudul{
    text-align:center;
    color:white;
    font-size:22px;
    margin-bottom:50px;
}

/* card produk */
.card{
    background: rgba(255,255,255,0.12);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);

    border:1px solid rgba(255,255,255,0.2);

    border-radius:28px;

    overflow:hidden;

    margin-bottom:35px;

    box-shadow: 0 8px 32px rgba(0,0,0,0.3);

    transition:0.3s;
}

.card:hover{
    transform: translateY(-8px);
    box-shadow: 0 10px 35px rgba(0,0,0,0.45);
}

.card img{
    width:100%;
    height:270px;
    object-fit:cover;
}

.card-body{
    padding:28px;
}

/* nama produk */
.nama-produk{
    color:white;
    font-size:36px;
    font-weight:700;
    margin-bottom:10px;
}

/* harga */
.harga{
    color:#FFD54F;
    font-size:30px;
    font-weight:800;
    margin-bottom:18px;
}

/* deskripsi */
.deskripsi{
    color:#F5F5F5;
    font-size:19px;
    line-height:1.8;
    margin-bottom:20px;
}

/* badge */
.badge{
    display:inline-block;
    background: rgba(255,255,255,0.15);
    border:1px solid rgba(255,255,255,0.2);
    padding:10px 18px;
    border-radius:16px;
    color:white;
    font-weight:600;
    font-size:16px;
}

/* section contact */
.contact-title{
    color:white;
    font-size:48px;
    font-weight:800;
    margin-top:40px;
    margin-bottom:25px;
}

/* contact box */
.contact-box{
    background: rgba(255,255,255,0.12);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);

    border:1px solid rgba(255,255,255,0.2);

    border-radius:30px;

    padding:45px;

    text-align:center;

    box-shadow:0 8px 32px rgba(0,0,0,0.35);

    margin-bottom:30px;
}

/* nama toko */
.contact-nama{
    color:white;
    font-size:54px;
    font-weight:800;
    margin-bottom:20px;
}

/* info */
.contact-info{
    color:white;
    font-size:28px;
    margin-bottom:15px;
}

.contact-desc{
    color:#EEEEEE;
    font-size:22px;
    margin-top:25px;
    line-height:1.8;
}

/* tombol whatsapp */
.wa-button{
    display:flex;
    justify-content:center;
    align-items:center;

    margin-top:35px;

    background:#25D366;

    color:white !important;

    text-decoration:none;

    padding:18px 28px;

    border-radius:18px;

    font-size:24px;

    font-weight:700;

    transition:0.3s;
}

.wa-button:hover{
    background:#1ebe5d;
    transform:scale(1.03);
}

/* responsive */
@media(max-width:768px){

    .judul{
        font-size:42px;
    }

    .subjudul{
        font-size:18px;
    }

    .nama-produk{
        font-size:28px;
    }

    .harga{
        font-size:24px;
    }

    .deskripsi{
        font-size:16px;
    }

    .contact-title{
        font-size:36px;
    }

    .contact-nama{
        font-size:38px;
    }

    .contact-info{
        font-size:20px;
    }

    .contact-desc{
        font-size:18px;
    }

    .wa-button{
        font-size:20px;
        padding:15px 20px;
    }
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown("""
<div class="judul">
🥟 Bakpao Ceu Mumun
</div>

<div class="subjudul">
Bakpao Premium Lembut • Enak • Fresh Setiap Hari
</div>
""", unsafe_allow_html=True)

# =========================
# DATA PRODUK
# =========================
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
        "deskripsi": "Perpaduan roti lembut dan keju creamy premium.",
        "gambar": "images/kacang.jpg"
    },
    {
        "nama": "Bakpao Kentang",
        "harga": "Rp 5.000",
        "deskripsi": "Isian kacang hijau manis tradisional dengan rasa autentik.",
        "gambar": "images/kentang.jpg"
    },
    {
        "nama": "Bakpao Unti Kelapa",
        "harga": "Rp 5.000",
        "deskripsi": "Isian kacang hijau manis tradisional dengan rasa autentik.",
        "gambar": "images/kelapa.jpg"
    }
]

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

    <div class="contact-nama">
        🥟 Bakpao Ceu Mumun
    </div>

    <div class="contact-info">
        📱 WhatsApp: 0895701152656
    </div>

    <div class="contact-info">
        📍 Bandung, Jawa Barat
    </div>

    <div class="contact-desc">
        Melayani reseller, acara keluarga, snack box,
        arisan, dan pesanan harian.
    </div>

    <a class="wa-button"
       href="https://wa.me/62895701152656"
       target="_blank">

       📲 Pesan Sekarang via WhatsApp

    </a>

</div>
""", unsafe_allow_html=True)
