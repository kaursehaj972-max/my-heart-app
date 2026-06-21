import streamlit as st

# 1. Page Title
st.set_page_config(page_title="AI Heart Health Simulator", page_icon="🫀")
st.title("🫀 AI Heart Health Simulator")
st.write("Adjust the metrics in the sidebar to see the simulated AI risk prediction live.")

# 2. Sidebar Inputs
st.sidebar.header("Patient Data")
age = st.sidebar.slider("Age", 18, 90, 30)
bp = st.sidebar.slider("Blood Pressure (Systolic)", 90, 180, 120)
smoking = st.sidebar.selectbox("Smoking Status", ["Never Smoked", "Active Smoker"])

# 3. Calculation Brain (The Logic)
risk = 10  # Starting base risk

if age > 50:
    risk += 20
if bp >= 130:
    risk += 30
if smoking == "Active Smoker":
    risk += 35

# Keep the score between 5% and 95%
final_risk = min(max(risk, 5), 95)

# 4. Display Results
st.subheader("📊 Live AI Analysis")
st.metric(label="Cardiovascular Risk Score", value=f"{final_risk}%")

if final_risk < 40:
    st.success("🟢 Low Risk: The heart profile looks healthy.")
elif final_risk <= 70:
    st.warning("🟡 Moderate Risk: Early lifestyle modifications recommended.")
else:
    st.error("🔴 High Risk: Warning signs detected. Clinical review advised.")
