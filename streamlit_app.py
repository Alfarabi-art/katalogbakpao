import streamlit as st

# ============================================
# CONFIG
# ============================================
st.set_page_config(
    page_title="Katalog Bakpao",
    page_icon="🥟",
    layout="wide"
)

# ============================================
# CSS
# ============================================
st.markdown("""
<style>

/* ============================= */
/* BACKGROUND */
/* ============================= */
.stApp{
    background-image: url("https://images.unsplash.com/photo-1495195134817-aeb325a55b65");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* overlay */
.stApp::before{
    content:"";
    position:fixed;
    top:0;
    left:0;
    width:100%;
    height:100%;
    background:rgba(0,0,0,0.45);
    z-index:-1;
}

/* ============================= */
/* HIDE STREAMLIT */
/* ============================= */
#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

header{
    visibility:hidden;
}

/* ============================= */
/* TITLE */
/* ============================= */
.title{
    text-align:center;
    color:white;
    font-size:64px;
    font-weight:800;
    margin-top:30px;
    margin-bottom:10px;
}

.subtitle{
    text-align:center;
    color:white;
    font-size:22px;
    margin-bottom:50px;
}

/* ============================= */
/* CARD */
/* ============================= */
.card{
    background: rgba(255,255,255,0.10);

    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);

    border:1px solid rgba(255,255,255,0.20);

    border-radius:28px;

    overflow:hidden;

    margin-bottom:35px;

    box-shadow:0 8px 32px rgba(0,0,0,0.35);

    transition:0.3s;
}

.card:hover{
    transform: translateY(-8px);
}

/* gambar */
.card img{
    width:100%;
    height:270px;
    object-fit:cover;
}

/* body */
.card-body{
    padding:28px;
}

/* nama produk */
.nama-produk{
    color:white;
    font-size:34px;
    font-weight:700;
    margin-bottom:12px;
}

/* harga */
.harga{
    color:#FFD54F;
    font-size:28px;
    font-weight:800;
    margin-bottom:18px;
}

/* deskripsi */
.deskripsi{
    color:#F5F5F5;
    font-size:18px;
    line-height:1.8;
    margin-bottom:20px;
}

/* badge */
.badge{
    display:inline-block;

    padding:10px 18px;

    border-radius:16px;

    background: rgba(255,255,255,0.15);

    border:1px solid rgba(255,255,255,0.20);

    color:white;

    font-weight:600;
}

/* ============================= */
/* CONTACT */
/* ============================= */
.contact-title{
    color:white;
    font-size:48px;
    font-weight:800;
    margin-top:40px;
    margin-bottom:25px;
}

.contact-box{
    background: rgba(255,255,255,0.10);

    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);

    border:1px solid rgba(255,255,255,0.20);

    border-radius:30px;

    padding:45px;

    text-align:center;

    box-shadow:0 8px 32px rgba(0,0,0,0.35);

    margin-bottom:50px;
}

.contact-nama{
    color:white;
    font-size:52px;
    font-weight:800;
    margin-bottom:20px;
}

.contact-info{
    color:white;
    font-size:26px;
    margin-bottom:15px;
}

.contact-desc{
    color:#EEEEEE;
    font-size:20px;
    line-height:1.8;
    margin-top:20px;
}

/* tombol wa */
.wa-btn{
    display:inline-block;

    margin-top:35px;

    padding:18px 30px;

    border-radius:18px;

    background:#25D366;

    color:white !important;

    font-size:22px;

    font-weight:700;

    text-decoration:none;

    transition:0.3s;
}

.wa-btn:hover{
    background:#1ebe5d;
    transform:scale(1.03);
}

/* responsive */
@media(max-width:768px){

    .title{
        font-size:42px;
    }

    .subtitle{
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
        font-size:34px;
    }

    .contact-nama{
        font-size:36px;
    }

    .contact-info{
        font-size:20px;
    }

    .wa-btn{
        font-size:18px;
        padding:15px 22px;
    }
}

</style>
""", unsafe_allow_html=True)

# ============================================
# HEADER
# ============================================
st.markdown("""
<div class="title">
🥟 Bakpao Ceu Mumun
</div>

<div class="subtitle">
Bakpao Premium • Lembut • Fresh Setiap Hari
</div>
""", unsafe_allow_html=True)

# ============================================
# DATA PRODUK
# ============================================
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
        "deskripsi":"Isian kacang hijau manis tradisional dengan rasa autentik.",
        "gambar":"https://images.unsplash.com/photo-1482049016688-2d3e1b311543"
    }

]

# ============================================
# PRODUK
# ============================================
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
        with col1:
            st.markdown(card, unsafe_allow_html=True)

    else:
        with col2:
            st.markdown(card, unsafe_allow_html=True)

# ============================================
# CONTACT
# ============================================
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
