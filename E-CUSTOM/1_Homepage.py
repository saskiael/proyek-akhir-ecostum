import streamlit as st 

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image : url(https://i.pinimg.com/564x/bf/20/62/bf2062653ee6816525b7711b8b1cdff5.jpg);
background-size: cover;
}

[data-testid="stHeader"]{
background-color: rgba(0, 0, 0, 0);
}

[data-testid="stToolbar"]{
right: 2rem;
}

[data-testid="stSidebar"]{
background-color: color-mix(in oklab, blue 30%, white 70%);
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
st.title ("E-CUSTOM")
st.markdown("**E-Custom merupakan modelmachine learning yang dapat mengukur banyaknya pelanggan tetap dan churn (keluar toko) disertai cara mempertahankan pelanggan**." "**Aplikasi ini berjalan dengan awal mula membaca dataset yang adakemudian diproses model datasetnya menggunkan algoritma E-CUSTOM untukmenentukan apakah customer tersebut akan churn atau tidak dengan waktu yang singkat dan tepat, jika cutomer churn maka pihak e-commerce atau disini lebih tepatnya dibagian marketing akan memberikan promo-promo yang menarik agarcustomer tersebut tidak churn, jika customer itu tidak churn maka akan diberireward/loyalty pack agar tetap setia**")


