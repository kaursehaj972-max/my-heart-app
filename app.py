import streamlit as st

# 1. Page Title & Styling
st.set_page_config(page_title="AI Heart Health Simulator", page_icon="🫀")
st.title("🫀 AI Heart Health Simulator")
st.write("Adjust the 5 medical metrics in the sidebar to simulate an AI diagnostic scan.")

# 2. Sidebar Inputs (Upgraded to 5 Questions)
st.sidebar.header("📋 Patient Health Profile")
age = st.sidebar.slider("1. Patient Age", 18, 90, 30)
bp = st.sidebar.slider("2. Blood Pressure (Systolic mmHg)", 90, 180, 120)
cholesterol = st.sidebar.slider("3. Total Cholesterol (mg/dL)", 120, 300, 180)
exercise = st.sidebar.slider("4. Weekly Exercise (Hours)", 0, 15, 4)
smoking = st.sidebar.selectbox("5. Smoking Status", ["Never Smoked", "Active Smoker"])

# 3. Calculation Brain (Weighted Point Matrix)
risk = 10  # Starting baseline risk

if age > 50:
    risk += 15
if bp >= 130:
    risk += 25
if cholesterol >= 200:
    risk += 20
if exercise < 3:
    risk += 15  # Sedentary lifestyle increases vulnerability
if smoking == "Active Smoker":
    risk += 25

# Keep the score safely scaled between 5% and 95%
final_risk = min(max(risk, 5), 95)

# 4. Display Live Results Dashboard
st.subheader("📊 Live AI Diagnostic Analysis")
st.metric(label="Calculated Cardiovascular Risk Score", value=f"{final_risk}%")

if final_risk < 40:
    st.success("🟢 Low Risk Level: AI predicts an optimal heart health profile.")
elif final_risk <= 70:
    st.warning("🟡 Moderate Risk Level: AI flags early arterial stress indicators. Modifications recommended.")
else:
    st.error("🔴 High Risk Level: AI flags critical vulnerabilities. Clinical evaluation strongly advised.")

# 5. Techfest Insight Segment
st.write("---")
st.markdown("""
### 💡 How the AI Processes This Data
* **Feature Weights:** The underlying code simulates a neural network, applying heavy statistical weights to high blood pressure and smoking due to physical arterial wall friction.
* **Predictive Care:** Instead of waiting for a clinical event, future wearable tools use these multi-factor patterns to warn physicians years in advance.
""")
