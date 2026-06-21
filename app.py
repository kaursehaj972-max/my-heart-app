import streamlit as st
import pandas as pd

# 1. Page Title & Styling
st.set_page_config(page_title="AI Advanced CardioPredict Engine", page_icon="🫀")
st.title("🫀 AI Advanced CardioPredict Engine")
st.write("Class 11 Biology Project: Integrating Predictive AI with Human Hemodynamics.")

# 2. Sidebar Inputs (Advanced Metrics)
st.sidebar.header("📋 Patient Clinical Metrics")
age = st.sidebar.slider("1. Patient Age", 18, 90, 17)
bp = st.sidebar.slider("2. Systolic Blood Pressure (mmHg)", 90, 180, 120)
cholesterol = st.sidebar.slider("3. Total Cholesterol (mg/dL)", 120, 300, 180)
heart_rate = st.sidebar.slider("4. Resting Heart Rate (BPM)", 50, 120, 72)
smoking = st.sidebar.selectbox("5. Smoking Status", ["Never Smoked", "Active Smoker"])

# 3. Scientific Calculations (Class 11 Biology Curriculum)
stroke_volume = 70 # Average mL per beat
cardiac_output_mL = heart_rate * stroke_volume
cardiac_output_L = round(cardiac_output_mL / 1000, 2)

# AI Weighted Risk Logic
age_risk = 15 if age > 50 else 0
bp_risk = 30 if bp >= 130 else 0
chol_risk = 20 if cholesterol >= 200 else 0
hr_risk = 15 if (heart_rate > 90 or heart_rate < 60) else 0
smoke_risk = 20 if smoking == "Active Smoker" else 0

total_risk = min(max(5 + age_risk + bp_risk + chol_risk + hr_risk + smoke_risk, 5), 95)

# 4. Display Live Results Dashboard
st.subheader("📊 Live AI Hemodynamic Analysis")

col1, col2 = st.columns(2)
with col1:
    st.metric(label="Calculated Cardiovascular Risk Score", value=f"{total_risk}%")
with col2:
    st.metric(label="Calculated Cardiac Output (L/min)", value=f"{cardiac_output_L} L", delta="Normal: 5.0L" if 4.5 <= cardiac_output_L <= 5.5 else "Abnormal Flow")

# 5. Visual Interactive Chart
st.write("### 📉 Multi-Factor Risk Vector Analysis")
risk_data = {
    "Risk Factor": ["Age Impact", "Blood Pressure", "Cholesterol", "Heart Rate Strain", "Toxin Exposure"],
    "Severity Score": [age_risk, bp_risk, chol_risk, hr_risk, smoke_risk]
}
df = pd.DataFrame(risk_data)
st.bar_chart(data=df, x="Risk Factor", y="Severity Score", color="#ff4b4b")

# 6. Class 11 Curriculum Corner
st.write("---")
with st.expander("🔬 Class 11 NCERT Biology Insights (Click to Expand)"):
    st.markdown("""
    * **Cardiac Output:** Calculated live above ($CO = HR \\times SV$). Normal resting output is roughly 5 Liters per minute.
    * **Hypertension:** Sustained blood pressure above 140/90 mmHg leads to hypertension, causing vital organ damage and forcing the cardiac muscles to work harder.
    * **Atherosclerosis:** High cholesterol values ($>200$ mg/dL) simulate the deposition of lipids/plaque inside the lumen of arteries, narrowing the passage and spiking blood velocity.
    """)
