import streamlit as st
from app.chat_with_data import query_data

st.set_page_config(page_title="Churn Analysis Assistant", layout="wide")

st.title("📉 Customer Churn Dashboard")

tab1, tab2, tab3 = st.tabs(["📊 Churn Overview", "💬 Ask the Assistant", "🧠 Feature Insights"])

with tab1:
    st.subheader("Churn Overview")
    st.markdown("Upload your dataset or visualise from EDA.")
    st.warning("🚧 Under construction — coming soon!")

with tab2:
    st.subheader("Ask the Data Assistant")
    user_query = st.text_input("Enter your question:")
    if user_query:
        response = query_data(user_query)
        st.markdown("### Response")
        st.code(response, language='python')

with tab3:
    st.subheader("Feature Importance")
    st.markdown("Top predictive features driving churn.")
    st.warning("🚧 To be added next.")