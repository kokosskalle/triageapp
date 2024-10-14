# sbar_generator.py

import utils

def generate_sbar_summary(data, care_type):
    if care_type == "Nytt sjukdomstillstånd":
        return generate_new_condition_summary(data)
    elif care_type == "Äldre sjukdomstillstånd":
        return generate_old_condition_summary(data)
    elif care_type == "Årskontroll":
        return generate_annual_checkup_summary(data)
    else:
        return "Ingen SBAR-sammanfattning tillgänglig för vald typ av vård."

def generate_new_condition_summary(data):
    # Ensure required inputs are present
    if not data["duration"]:
        return "Vänligen ange hur länge du haft dina symptom."

    # Situation
    situation = "Patienten söker för ett nytt sjukdomstillstånd."

    # Background
    background = f"Symptomens varaktighet är {data['duration']}."

    # Assessment
    current = ""
    symptom_categories = {}

    if data["general_condition"] == "Ja":
        symptom_categories["Allmänt"] = "Patienten känner sig allmänt mycket påverkad."

    if data["breathing"] == "Ja":
        breathing_desc = "Patienten har problem med andningen."
        if data["breathing_difficulty"] == "Ja":
            breathing_desc += " Andningssvårigheter även i vila."
        symptom_categories["Andning"] = breathing_desc

    if data["chest_pain"] == "Ja":
        chest_pain_desc = "Patienten har ont i bröstet."
        if data["chest_pain_type"] == "Ja":
            chest_pain_desc += " Smärtan är konstant eller tryckande."
        if data["chest_pain_exertion"] == "Ja":
            chest_pain_desc += " Smärtan förvärras vid promenad eller ansträngning."
        symptom_categories["Bröstsmärta"] = chest_pain_desc

    if data["abdominal_pain"] == "Ja":
        abdominal_desc = "Patienten har buksmärta."
        if data["abdominal_symptoms"]:
            symptoms = ", ".join(data["abdominal_symptoms"])
            abdominal_desc += f" Upplever följande symptom: {symptoms}."
        else:
            abdominal_desc += " Inga ytterligare symptom angivna."
        symptom_categories["Buksmärta"] = abdominal_desc

    if data["ear_problems"] == "Ja":
        ear_desc = "Patienten har öronbesvär."
        if data["ear_symptoms"]:
            symptoms = ", ".join(data["ear_symptoms"])
            ear_desc += f" Upplever följande symptom: {symptoms}."
        else:
            ear_desc += " Inga ytterligare symptom angivna."
        symptom_categories["Öronbesvär"] = ear_desc

    if data["skin_lesion"] == "Ja":
        skin_lesion_desc = "Patienten har en hudförändring. Har ombetts att ta ett foto och infoga i chatten."
        symptom_categories["Hudförändring"] = skin_lesion_desc

    if data["headache"] == "Ja":
        headache_desc = "Patienten har huvudvärk."
        if data["headache_symptoms"]:
            if "Inget av ovanstående" in data["headache_symptoms"]:
                headache_desc += " Inga varningssymptom."
            else:
                symptoms = ", ".join(data["headache_symptoms"])
                headache_desc += f" Upplever följande varningssymptom: {symptoms}."
        else:
            headache_desc += " Inga varningssymptom angivna."
        symptom_categories["Huvudvärk"] = headache_desc

    if data["fever"] == "Ja":
        fever_desc = f"Patienten har {data['fever_grade']}."
        if data["main_symptoms"]:
            main_symptoms_desc = f"Huvudsakliga besvär: {', '.join(data['main_symptoms'])}."
        else:
            main_symptoms_desc = "Inga huvudsakliga besvär angivna."
        symptom_categories["Feber"] = f"{fever_desc} {main_symptoms_desc}"
    else:
        if data["main_symptoms"]:
            main_symptoms_desc = f"Huvudsakliga besvär: {', '.join(data['main_symptoms'])}."
            symptom_categories["Symptom"] = main_symptoms_desc

    if data["mental_health"] == "Ja":
        mental_health_desc = "Patienten har problem med sin psykiska hälsa."
        if data["suicidal_thoughts"] == "Ja":
            mental_health_desc += " Har självmordstankar eller planer."
        if data["mental_symptoms"]:
            mental_symptoms_desc = f" Upplever följande psykiska symptom: {', '.join(data['mental_symptoms'])}."
            mental_health_desc += mental_symptoms_desc
        symptom_categories["Psykisk hälsa"] = mental_health_desc

    if data["svf_conditions"]:
        svf_desc = f"Patienten har följande specifika symptom: {', '.join(data['svf_conditions'])}."
        symptom_categories["Specifika symptom"] = svf_desc

    if data["other_symptoms"]:
        symptom_categories["Övrigt"] = data["other_symptoms"]

    # Build the 'current' text
    if symptom_categories:
        categories_order = [k for k in symptom_categories.keys() if k != "Övrigt"] + ["Övrigt"]
        for category in categories_order:
            if category in symptom_categories:
                current += f"<b>{category}:</b> {symptom_categories[category]}<br>"
    else:
        current = "Inga specifika symptom angivna."

    # Recommendation
    recommendations = []

    # ... [Add logic for recommendations as per your original R code]

    # Initialize recommendation variable
    recommendation = ""

    if recommendations:
        if len(recommendations) == 1:
            recommendation = recommendations[0]
        else:
            recommendation = f"Patienten verkar söka för flera olika besvär. {' '.join(recommendations)} Avgör vilket besvär som är mest brådskande."

    # Build SBAR summary
    sbar_text = f"""
    <b>Situation:</b> {situation}<br><br>
    <b>Bakgrund:</b> {background}<br><br>
    <b>Aktuellt:</b><br>{current}<br><br>
    """
    if recommendation:
        sbar_text += f"<b>Rekommendation:</b> {recommendation}"

    return sbar_text

def generate_old_condition_summary(data):
    if not data["old_condition"]:
        return "Vänligen ange vilket sjukdomstillstånd det gäller."

    # Situation
    situation = f"Patienten söker för ett äldre sjukdomstillstånd: {data['old_condition']}"

    # Background
    background = data["condition_change"]

    # Assessment
    assessment = "Patienten har redan ett inbokat besök för något annat besvär den närmsta tiden." if data["scheduled_visit"] == "Ja" else "Patienten har inget inbokat besök för något annat besvär den närmsta tiden."

    # Recommendation
    recommendation = "Bedöm behovet av uppföljning eller justering av behandling för patientens tillstånd."

    # Build SBAR summary
    sbar_text = f"""
    <b>Situation:</b> {situation}<br><br>
    <b>Bakgrund:</b> {background}<br><br>
    <b>Aktuellt:</b> {assessment}<br><br>
    <b>Rekommendation:</b> {recommendation}
    """

    return sbar_text

def generate_annual_checkup_summary(data):
    if not data["common_diseases_annual"] and not data["other_diseases_annual"]:
        return "Vänligen ange vilken sjukdom du vill ha årskontroll för."

    # Situation
    situation = "Patienten söker för årskontroll."

    # Background
    diseases = data["common_diseases_annual"]
    if data["other_diseases_annual"]:
        diseases.append(data["other_diseases_annual"])
    diseases_list = ", ".join(diseases)
    background = f"Årskontroll för följande sjukdomar: {diseases_list}"

    # Assessment
    last_checkup_text = data["last_checkup_annual"]
    assessment = last_checkup_text
    if data["scheduled_visit_annual"] == "Ja":
        assessment += " Patienten har redan ett inbokat besök för något annat besvär den närmsta tiden."
    else:
        assessment += " Patienten har inget inbokat besök för något annat besvär den närmsta tiden."

    # Recommendation
    recommendation = "Planera för årskontroll och bedöm behovet av provtagning eller undersökningar."

    # Build SBAR summary
    sbar_text = f"""
    <b>Situation:</b> {situation}<br><br>
    <b>Bakgrund:</b> {background}<br><br>
    <b>Aktuellt:</b> {assessment}<br><br>
    <b>Rekommendation:</b> {recommendation}
    """

    return sbar_text
