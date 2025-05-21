import streamlit as st

st.title("tanntopup")
st.write(
    "Top up murah dan terpercaya hanya di TanTopUp."
)
st.image("IMG_20250520_165409.jpg", width=200) 

st. title(“topup termurah") 
st. header("aplikasi untuk topup semua game😈😈") 
angka = st.number_inputrf("tuliskan sebuah angka:", value=0, step=1) 

if (angka % 2) == 0:
    st.write(f"{angka} gacor kang🤬🤬") 
else:
    st.write(f"{angka} habisin duitnya disni😡") 

st. title("Top Up Murah")
st. header("Aplikasi untuk TopUp Semua Game")
angka = st.number_input("Tulislah sebuah angka:", value=0, step=1)

if (angka % 2) == 0:
    st.write(f"{angka} gacor kang 🤬")
else:
    st.write(f"{angka} habisin duitnya sini")
