import streamlit as st
import math

st.title("Cálculo de Excentricidad de Discos")

# Entradas
velocidad = st.number_input("Ingrese la velocidad en RPM:", min_value=0.0, format="%.2f")
f1 = st.number_input("Ingrese la fuerza 1 en libras:", format="%.2f")
theta1 = st.number_input("Ingrese la dirección de la fuerza 1 en grados:", format="%.2f")
f4 = st.number_input("Ingrese la fuerza 4 en libras:", format="%.2f")
theta4 = st.number_input("Ingrese la dirección de la fuerza 4 en grados:", format="%.2f")
peso = st.number_input("Ingrese el peso de los discos en libras:", format="%.2f")

if st.button("Calcular"):
    pi = math.pi
    gravedad = 386.22047
    omega = (velocidad * 2 * pi / 60) ** 2

    f1x = f1 * math.cos(math.radians(theta1))
    f1y = f1 * math.sin(math.radians(theta1))
    f4x = f4 * math.cos(math.radians(theta4))
    f4y = f4 * math.sin(math.radians(theta4))

    m2 = peso / gravedad
    m3 = m2

    a1 = 1.75
    a3 = 6
    a4 = 8.25

    excentricidad = ((((f1x*a1 - f4x*a4)**2) + ((f1y*a1 - f4y*a4)**2))**0.5) / (a3 * m3 * omega)
    f3 = m3 * excentricidad * omega
    inversa3 = (f1x*a1 - f4x*a4) / (f3 * a3)
    theta3 = math.acos(inversa3)

    f3x = f3 * math.cos(theta3)
    f3y = f3 * math.sin(theta3)
    f2y = -f1y - f3y - f4y
    f2x = -f1x - f3x - f4x
    f2 = ((f2y ** 2) + (f2x ** 2)) ** 0.5
    theta2 = math.atan2(f2y, f2x)
    excentricidad2 = f2 / (m2 * omega)

    # Resultados
    st.subheader("Resultados")
    st.write(f"📌 Excentricidad del disco 3: **{excentricidad:.4f} inches**")
    st.write(f"📌 Ángulo del disco 3: **{math.degrees(theta3):.2f} grados**")
    st.write(f"📌 Excentricidad del disco 2: **{excentricidad2:.4f} inches**")
    st.write(f"📌 Ángulo del disco 2: **{math.degrees(theta2):.2f} grados**")
    st.write(f"📌 Sumatoria en x: **{f1x + f2x + f3x + f4x:.4f}**")
    st.write(f"📌 Sumatoria en y: **{f1y + f2y + f3y + f4y:.4f}**")
