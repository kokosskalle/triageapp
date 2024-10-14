# annual_checkup.py

import streamlit as st

def annual_checkup_module():
    st.header("Årskontroll")

    with st.form("annual_checkup_form"):
        common_diseases_annual = st.multiselect("Välj vilken sjukdom du vill ha årskontroll för:",
                                                options=["Diabetes typ 2", "Hypertoni", "Astma/KOL",
                                                         "Hjärtsvikt", "Demens", "Depression",
                                                         "Annat"])

        other_diseases_annual = None
        if "Annat" in common_diseases_annual:
            other_diseases_annual = st.text_input("Ange annan sjukdom:")

        last_checkup_annual = st.radio("När hade du din senaste årskontroll?",
                                       options=["Senaste året", "För mer än 1 år sedan", "För mer än 2 år sedan"])

        scheduled_visit_annual = st.radio("Har du redan ett inbokat besök för något annat besvär den närmsta tiden?",
                                          options=["Ja", "Nej"])

        submitted = st.form_submit_button("Generera SBAR-sammanfattning")

        if submitted:
            data = {
                "common_diseases_annual": common_diseases_annual,
                "other_diseases_annual": other_diseases_annual,
                "last_checkup_annual": last_checkup_annual,
                "scheduled_visit_annual": scheduled_visit_annual
            }
            return data
        else:
            return None
