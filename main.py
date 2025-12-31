import streamlit as st

st.title("BMI Calculator")
st.write('## "BMI" stands for Body Mass Index')

height = st.slider("Enter your Height (in cms)", 100, 250, 175)
weight = st.slider("Enter your weight (in kgs)", 40, 200, 70)

# Convert height to meters
height_m = height / 100

# Correct BMI formula
bmi = weight / (height_m ** 2)

st.write(f"### Height = {height} cm")
st.write(f"### Weight = {weight} kg")
st.write(f"### BMI = {bmi:.2f}")

st.write("## BMI Category")

if bmi < 18.5:
    st.info("Underweight")
elif bmi < 25:
    st.success("Normal")
elif bmi < 30:
    st.warning("Overweight")
else:
    st.error("Obesity")