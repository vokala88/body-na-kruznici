import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Body na kružnici", page_icon="⭕")

st.title("⭕ Generátor bodů na kružnici")

# --- Vstupy ---
st.sidebar.header("Parametry kružnice")
x_center = st.sidebar.number_input("Souřadnice středu X [m]", value=0.0)
y_center = st.sidebar.number_input("Souřadnice středu Y [m]", value=0.0)
radius = st.sidebar.slider("Poloměr kružnice [m]", 1.0, 20.0, 5.0)
points = st.sidebar.slider("Počet bodů", 1, 36, 8)

# Výběr barvy ze seznamu
barvy = {
    "Červená": "red",
    "Modrá": "blue",
    "Zelená": "green",
    "Fialová": "purple",
    "Černá": "black"
}
color = st.sidebar.selectbox("Barva bodů", list(barvy.keys()))

# Možnost vykreslit i obvod kružnice
zobraz_kruznici = st.sidebar.checkbox("Zobrazit kružnici", value=True)

# --- Výpočet bodů ---
angles = np.linspace(0, 2*np.pi, int(points), endpoint=False)
x_points = x_center + radius * np.cos(angles)
y_points = y_center + radius * np.sin(angles)

# --- Vykreslení ---
fig, ax = plt.subplots(figsize=(6,6))

# Body s čísly
for i, (xp, yp) in enumerate(zip(x_points, y_points), start=1):
    ax.plot(xp, yp, "o", color=barvy[color])
    ax.text(xp+0.2, yp+0.2, str(i), fontsize=9)

# Volitelně kružnice
if zobraz_kruznici:
    kruznice = plt.Circle((x_center, y_center), radius, fill=False, linestyle="--", color="gray")
    ax.add_artist(kruznice)

# Osy
ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.set_aspect("equal", adjustable="box")
ax.grid(True)

st.pyplot(fig)

# --- Info o aplikaci ---
st.divider()
st.subheader("ℹ️ O aplikaci")
st.markdown("""
Tato aplikace generuje zadaný počet bodů rovnoměrně rozmístěných na kružnici.  
**Použité technologie:** Python, Streamlit, Matplotlib  
**Autor:** Alexandr Vokál 
""")
