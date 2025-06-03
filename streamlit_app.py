import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("🎈Cálculo del Valor Presente Neto (VPN)🎈")
with st.sidebar:
    st.header("Datos de entrada")
    inversion_inicial = st.number_input("Inversión inicial:", value=-10000.0)
    tasa_descuento = st.slider("Tasa de descuento (%)", min_value=0.0, max_value=20.0, value=10.0) / 100
    años = st.number_input("Número de años:", min_value=1, max_value=10, value=5)
flujos = []
    for i in range(int(años)):
        flujo = st.number_input(f"Flujo de caja para el año {i+1}:", value=2000.0)
        flujos.append(flujo)
        vpn = inversion_inicial + sum([flujos[i] / (1 + tasa_descuento)**(i + 1) for i in range(len(flujos))])
st.write(f"**Valor Presente Neto (VPN):** ${vpn:,.2f}")

st.subheader("Visualización de Flujos de Caja")
fig, ax = plt.subplots()
ax.bar(range(1, int(años) + 1), flujos, color="blue")
ax.set_xlabel("Años")
ax.set_ylabel("Flujo de Caja")
st.pyplot(fig)
