import streamlit as st
from PIL import Image

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

st.title('Team')


col1, col2, col3, col4, col5 = st.columns(5)

with col1:
   st.subheader("Nurul")
   st.image("nurul.jpg")
   st.markdown("**Nurul Lubna Gajalba**")
   st.markdown("**NIM: 2103101**")
   st.markdown("**Universitas Pendidikan Indonesia**")
   st.markdown("**Data Engineer**")

with col2:
   st.subheader("Aeni")
   st.image("aeni.jpeg")
   st.markdown("**Nur Aeni**")
   st.markdown("**NIM: 2020150124**")
   st.markdown("**Universitas Sains Al-Qur'an**")
   st.markdown("**Frontend Engineer**")
   
with col3:
   st.subheader("Irgi")
   st.image("irgi.jpg")
   st.markdown("**Irgi Ahmad Fauzi**")
   st.markdown("**NIM: 2006771**")
   st.markdown("**Universitas Pendidikan Indonesia**")
   st.markdown("**ML Engineer**")

with col4:
   st.subheader("Saskia")
   st.image("saskia.jpg")
   st.markdown("**Saskia Elnabilla**")
   st.markdown("**NIM: 2020150140**")
   st.markdown("**Universitas Sains Al-Qur'an**")
   st.markdown("**Backend Engineer**")

with col5:
   st.subheader("Wa Ode")
   st.image("wa_ode.jpg")
   st.markdown("**Wa Ode Lely Amaria**")
   st.markdown("**NIM: 2005156**")
   st.markdown("**Universitas Pendidikan Indonesia**")
   st.markdown("**UI/UX Designer & Technical Writter**")