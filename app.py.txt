# app.py

import streamlit as st
from new_condition import new_condition_module
from old_condition import old_condition_module
from annual_checkup import annual_checkup_module
from sbar_generator import generate_sbar_summary
import utils

def main():
    st.set_page_config(page_title="Vårdtriage App", layout="wide")
    st.title("Vårdtriage App")

    st.sidebar.header("Vad söker du för?")
    care_type = st.sidebar.radio("Typ av vård:", 
                                 options=["Nytt sjukdomstillstånd", "Äldre sjukdomstillstånd", "Årskontroll", "Intyg", "Receptförnyelse"],
                                 index=0)
    
    if care_type == "Nytt sjukdomstillstånd":
        data = new_condition_module()
        if data:
            sbar_text = generate_sbar_summary(data, care_type)
            st.markdown(sbar_text, unsafe_allow_html=True)
    elif care_type == "Äldre sjukdomstillstånd":
        data = old_condition_module()
        if data:
            sbar_text = generate_sbar_summary(data, care_type)
            st.markdown(sbar_text, unsafe_allow_html=True)
    elif care_type == "Årskontroll":
        data = annual_checkup_module()
        if data:
            sbar_text = generate_sbar_summary(data, care_type)
            st.markdown(sbar_text, unsafe_allow_html=True)
    else:
        st.info("Ingen SBAR-sammanfattning tillgänglig för vald typ av vård.")

if __name__ == "__main__":
    main()
