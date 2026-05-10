import streamlit as st
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
