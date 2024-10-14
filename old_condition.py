# old_condition.py

import streamlit as st

def old_condition_module():
    st.header("Äldre sjukdomstillstånd")

    with st.form("old_condition_form"):
        old_condition = st.text_input("Ange vilket sjukdomstillstånd det gäller:")

        condition_change = st.radio("Hur har dina besvär förändrats?",
                                    options=["Besvären har förvärrats akut",
                                             "Besvären har förvärrats senaste tiden",
                                             "Besvären är oförändrade"])

        scheduled_visit = st.radio("Har du redan ett inbokat besök för något annat besvär den närmsta tiden?",
                                   options=["Ja", "Nej"])

        submitted = st.form_submit_button("Generera SBAR-sammanfattning")

        if submitted:
            data = {
                "old_condition": old_condition,
                "condition_change": condition_change,
                "scheduled_visit": scheduled_visit
            }
            return data
        else:
            return None
