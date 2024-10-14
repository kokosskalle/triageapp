# new_condition.py

import streamlit as st
import utils

def new_condition_module():
    st.header("Nytt sjukdomstillstånd")

    with st.form("new_condition_form"):
        duration = st.radio("Hur länge har du haft dina symptom?",
                            options=[
                                "Mindre än 24 timmar",
                                "1-3 dagar",
                                "3-7 dagar",
                                "7-14 dagar",
                                "14-30 dagar",
                                "Över 30 dagar"
                            ])
        
        st.subheader("Aktuellt")

        general_condition = st.radio("Känner du dig allmänt mycket påverkad?",
                                     options=["Ja", "Nej"])

        breathing = st.radio("Har du några problem med andningen?",
                             options=["Ja", "Nej"])
        breathing_difficulty = None
        if breathing == "Ja":
            breathing_difficulty = st.radio("Är det svårt att andas hela tiden, även i vila?",
                                            options=["Ja", "Nej"])

        chest_pain = st.radio("Har du ont i bröstet?",
                              options=["Ja", "Nej"])
        chest_pain_type = chest_pain_exertion = None
        if chest_pain == "Ja":
            chest_pain_type = st.radio("Är smärtan konstant eller tryckande?",
                                       options=["Ja", "Nej"])
            chest_pain_exertion = st.radio("Förvärras smärtan när du promenerar eller anstränger dig?",
                                           options=["Ja", "Nej"])

        abdominal_pain = st.radio("Har du buksmärta?",
                                  options=["Ja", "Nej"])
        abdominal_symptoms = None
        if abdominal_pain == "Ja":
            abdominal_symptoms = st.multiselect("Upplever du något av följande?",
                                                options=list(utils.abdominal_symptom_labels.keys()))

        ear_problems = st.radio("Har du öronbesvär?",
                                options=["Ja", "Nej"])
        ear_symptoms = None
        if ear_problems == "Ja":
            ear_symptoms = st.multiselect("Upplever du något av följande?",
                                          options=list(utils.ear_symptom_labels.keys()))

        skin_lesion = st.radio("Gäller ditt besvär en hudförändring?",
                               options=["Ja", "Nej"])
        if skin_lesion == "Ja":
            st.warning("Var god ta ett kort på hudförändringen och infoga i chatten.")

        headache = st.radio("Har du huvudvärk?",
                            options=["Ja", "Nej"])
        headache_symptoms = None
        if headache == "Ja":
            headache_symptoms = st.multiselect("Upplever du något av följande?",
                                               options=list(utils.headache_symptom_labels.keys()))
            # Ensure mutual exclusivity with "Inget av ovanstående"
            if "Inget av ovanstående" in headache_symptoms and len(headache_symptoms) > 1:
                headache_symptoms = ["Inget av ovanstående"]
                st.warning("Du kan endast välja 'Inget av ovanstående' eller andra alternativ, inte båda.")

        fever = st.radio("Har du haft feber?",
                         options=["Ja", "Nej"])
        fever_grade = main_symptoms = None
        if fever == "Ja":
            fever_grade = st.radio("Hur hög är febern?",
                                   options=["Låg (< 38°C)", "Måttlig (38-39°C)", "Hög (> 39°C)"])
            main_symptoms = st.multiselect("Vilka är dina huvudsakliga besvär?",
                                           options=["Hosta", "Ont i halsen", "Snuva", "Urinvägsbesvär",
                                                    "Hudutslag eller hudrodnad", "Ledvärk eller muskelvärk",
                                                    "Ögonbesvär"])

        mental_health = st.radio("Har du problem med din psykiska hälsa?",
                                 options=["Ja", "Nej"])
        suicidal_thoughts = mental_symptoms = None
        if mental_health == "Ja":
            suicidal_thoughts = st.radio("Har du haft självmordstankar eller självmordsplaner?",
                                         options=["Ja", "Nej"])
            mental_symptoms = st.multiselect("Vilka av följande symptom upplever du?",
                                             options=["Nedstämdhet", "Ångest", "Oro", "Stress",
                                                      "Sömnstörningar", "Koncentrationssvårigheter",
                                                      "Irritabilitet", "Anhedoni"])

        st.subheader("Specifika symptom")
        svf_conditions = st.multiselect("Välj om något av följande gäller dig:",
                                        options=["Knöl i bröstet", "Knöl i testikeln",
                                                 "Blodiga upphostningar", "Blod i urinen",
                                                 "Blod i avföringen"])

        st.subheader("Övriga besvär")
        other_symptoms = st.text_area("Om dina besvär inte passar in på ovanstående val, var god beskriv dem här:")

        submitted = st.form_submit_button("Generera SBAR-sammanfattning")

        if submitted:
            data = {
                "duration": duration,
                "general_condition": general_condition,
                "breathing": breathing,
                "breathing_difficulty": breathing_difficulty,
                "chest_pain": chest_pain,
                "chest_pain_type": chest_pain_type,
                "chest_pain_exertion": chest_pain_exertion,
                "abdominal_pain": abdominal_pain,
                "abdominal_symptoms": abdominal_symptoms,
                "ear_problems": ear_problems,
                "ear_symptoms": ear_symptoms,
                "skin_lesion": skin_lesion,
                "headache": headache,
                "headache_symptoms": headache_symptoms,
                "fever": fever,
                "fever_grade": fever_grade,
                "main_symptoms": main_symptoms,
                "mental_health": mental_health,
                "suicidal_thoughts": suicidal_thoughts,
                "mental_symptoms": mental_symptoms,
                "svf_conditions": svf_conditions,
                "other_symptoms": other_symptoms
            }
            return data
        else:
            return None
