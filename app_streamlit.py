import streamlit as st
from value_bets_toolkit import detectar_value_bets

st.title("Value Bets Detector")

odd_real = st.number_input("Odd Real", min_value=1.0)
odd_justa = st.number_input("Odd Justa", min_value=1.0)

if st.button("Detectar Value Bet"):
    resultado = detectar_value_bets(odd_real, odd_justa)
    if resultado:
        st.success("Value Bet Detectado!")
    else:
        st.warning("Sem Valor")
