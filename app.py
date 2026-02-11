import streamlit as st
import uuid

st.set_page_config(page_title="AI Health Record", layout="centered")

st.title("🩺 AI Health Record System")
st.write("A simple digital health record prototype for patients and doctors")

st.divider()

# Role selection
role = st.selectbox("Select your role", ["Patient", "Doctor"])

# Generate unique ID
user_id = str(uuid.uuid4())[:8]
st.info(f"Your Unique ID: {user_id}")

st.divider()

# Patient dashboard
if role == "Patient":
    st.subheader("👤 Patient Dashboard")
    st.write("• View your medical reports")
    st.write("• Understand reports in simple language")
    st.write("• Book appointments")

    st.markdown("### 📝 Add Medical Report")
    report_text = st.text_area(
        "Paste your medical report text below",
        placeholder="Example: Blood sugar level is 180 mg/dL..."
    )

    if st.button("Save Report"):
        if report_text.strip() == "":
            st.warning("Please enter report text")
        else:
            st.success("Report saved successfully (temporary)")

# Doctor dashboard
if role == "Doctor":
    st.subheader("👨‍⚕️ Doctor Dashboard")
    st.write("• View patient history")
    st.write("• Review reports")
    st.write("• Help patient with treatment")

    st.markdown("### 🔍 View Patient Record")
    patient_id = st.text_input("Enter Patient Unique ID")

    if st.button("View Patient Data"):
        if patient_id.strip() == "":
            st.warning("Please enter a patient ID")
        else:
            st.info("Patient data will be shown here (next step)")

st.divider()

st.caption("⚠️ This is a prototype. AI assistance will be added next.")

