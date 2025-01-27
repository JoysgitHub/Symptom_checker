questions = [
    ('1. Have you experienced a sudden increase in body temperature?', 'high_temp'),
    ('2. Are you having difficulty breathing?', 'breathlessness'),
    ('3. Do you feel a tightness in your chest?', 'chest_discomfort'),
    ('4. Are you experiencing sharp or persistent pain in your chest?', 'chest_pain'),
    ('5. Is your cough dry or persistent?', 'cough'),
    ('6. Have you noticed a wheezing sound when you breathe?', 'wheezing'),
    ('7. Do you feel unusually cold or have episodes of shivering?', 'chills'),
    ('8. Are you feeling more fatigued than usual?', 'fatigue'),
    ('9. Have you experienced sudden numbness in your face, arms, or legs?', 'numbness'),
    ('10. Are you having trouble concentrating or feeling disoriented?', 'confusion'),
    ('12. Have you had frequent episodes of loose or watery stools?', 'diarrhea'),
    ('13. Are you experiencing persistent nausea?', 'nausea'),
    ('14. Have you been vomiting recently?', 'vomiting'),
    ('15. Have you had any recent stomach pain?', 'abdominal_pain'),
    ('16. Are you feeling excessively thirsty?', 'excessive_thirst'),
    ('17. Have you noticed any blurriness in your vision?', 'blurred_vision'),
    ('18. Are you experiencing pain in your joints?', 'joint_pain'),
    ('19. Do you feel stiffness in your joints?', 'stiffness'),
    ('20. Have you been sneezing frequently?', 'sneezing'),
    ('21. Is your nose often congested?', 'runny_nose'),
    ('22. Are you feeling persistently sad?', 'persistent_sadness'),
    ('23. Have you lost interest or pleasure in activities you once enjoyed?', 'loss_of_interest'),
    ('24. Do you experience a rapid heartbeat?', 'rapid_heartbeat'),
    ('25. Are you experiencing frequent headaches?', 'headache'),
    ('26. Do you feel chest discomfort or shortness of breath?', 'shortness_of_breath'),
    ('27. Are you experiencing flank pain?', 'flank_pain'),
    ('28. Do you feel a burning sensation when urinating?', 'burning_sensation'),
    ('29. Have you noticed any blisters on your skin?', 'blisters'),
    ('30. Have you noticed any itchy rashes on your skin?', 'itchy_rash'),
    ('31. Are you experiencing a throbbing headache?', 'throbbing_headache'),
    ('32. Do you find yourself needing to urinate more often than usual?', 'frequent_urination'),
    ('33. Are you experiencing increased sensitivity to light?', 'sensitivity_to_light'),
    ('34. Do you feel dizzy or lightheaded?', 'dizziness')
    ]


def rule_asthma(symptoms):
    return 'wheezing' in symptoms or 'breathlessness' in symptoms

def rule_pneumonia(symptoms):
    return 'chest_pain' in symptoms or 'cough' in symptoms

def rule_arthritis(symptoms):
    return 'joint_pain' in symptoms or 'stiffness' in symptoms

def rule_gastroenteritis(symptoms):
    return 'diarrhea' in symptoms or 'vomiting' in symptoms

def rule_stroke(symptoms):
    return 'numbness' in symptoms or 'confusion' in symptoms

def rule_flu(symptoms):
    return 'high_temp' in symptoms or 'fatigue' in symptoms or 'chills' in symptoms


def rule_allergies(symptoms):
    return 'runny_nose' in symptoms or 'sneezing' in symptoms

def rule_diabetes(symptoms):
    return 'excessive_thirst' in symptoms or 'fatigue' in symptoms

def rule_heart_disease(symptoms):
    return 'chest_discomfort' in symptoms or 'shortness_of_breath' in symptoms

def rule_kidney_infection(symptoms):
    return 'flank_pain' in symptoms or 'frequent_urination' in symptoms

def rule_urinary_tract_infection(symptoms):
    return 'burning_sensation' in symptoms or 'frequent_urination' in symptoms

def rule_migraine(symptoms):
    return 'throbbing_headache' in symptoms or 'sensitivity_to_light' in symptoms

def rule_depression(symptoms):
    return 'persistent_sadness' in symptoms or 'loss_of_interest' in symptoms

def rule_hypertension(symptoms):
    return 'headache' in symptoms or 'blurred_vision' in symptoms

def rule_anemia(symptoms):
    return 'fatigue' in symptoms or 'shortness_of_breath' in symptoms

def rule_appendicitis(symptoms):
    return 'abdominal_pain' in symptoms or 'nausea' in symptoms

def rule_chickenpox(symptoms):
    return 'itchy_rash' in symptoms or 'blisters' in symptoms

def rule_panic_attack(symptoms):
    return 'rapid_heartbeat' in symptoms or 'dizziness' in symptoms

replies = {
    'Asthma': 'You may have asthma. Consult your doctor for inhalers and management.',
    'Pneumonia': 'You may have pneumonia. See a doctor for tests and antibiotics.',
    'Arthritis': 'You may have arthritis. Consult a rheumatologist for treatment options.',
    'Gastroenteritis': 'You may have gastroenteritis. Stay hydrated and see a doctor if symptoms worsen.',
    'Stroke': 'A stroke is a medical emergency. Seek immediate medical attention.',
    'Flu': 'You may have the flu. Rest, hydrate, and consult your doctor if symptoms worsen.',
    'Allergies': 'You may have an allergy. Antihistamines may help; consult a doctor for evaluation.',
    'Diabetes': 'You may have diabetes. Consult an endocrinologist for diagnosis and treatment.',
    'Heart Disease': 'Heart disease is serious. Consult a cardiologist for further evaluation.',
    'Kidney Infection': 'A kidney infection requires medical attention. Seek a doctor immediately.',
    'Urinary Tract Infection': 'You may have a UTI. See a doctor for treatment and antibiotics.',
    'Migraine': 'You may have a migraine. Over-the-counter pain relief may help; consult a doctor if frequent.',
    'Depression': 'Depression is serious. Consult a mental health professional for support.',
    'Hypertension': 'Hypertension needs management. Consult a doctor for a treatment plan.',
    'Anemia': 'Anemia is treatable. Consult a doctor for diagnosis and treatment options.',
    'Appendicitis': 'Appendicitis is an emergency. Seek medical attention immediately.',
    'Chickenpox': 'Chickenpox is contagious. Rest and consult a doctor if necessary.',
    'Panic Attack': 'Panic attacks can be managed. Consult a mental health professional for guidance.'
}


replies = {
    'Asthma': 'You may have asthma. Consult your doctor for inhalers and management.',
    'Pneumonia': 'You may have pneumonia. See a doctor for tests and antibiotics.',
    'Arthritis': 'You may have arthritis. Consult a rheumatologist for treatment options.',
    'Gastroenteritis': 'You may have gastroenteritis. Stay hydrated and see a doctor if symptoms worsen.',
    'Stroke': 'A stroke is a medical emergency. Seek immediate medical attention.',
    'Flu': 'You may have the flu. Rest, hydrate, and consult your doctor if symptoms worsen.',
    'Allergies': 'You may have an allergy. Antihistamines may help; consult a doctor for evaluation.',
    'Diabetes': 'You may have diabetes. Consult an endocrinologist for diagnosis and treatment.',
    'Heart Disease': 'Heart disease is serious. Consult a cardiologist for further evaluation.',
    'Kidney Infection': 'A kidney infection requires medical attention. Seek a doctor immediately.',
    'Urinary Tract Infection': 'You may have a UTI. See a doctor for treatment and antibiotics.',
    'Migraine': 'You may have a migraine. Over-the-counter pain relief may help; consult a doctor if frequent.',
    'Depression': 'Depression is serious. Consult a mental health professional for support.',
    'Hypertension': 'Hypertension needs management. Consult a doctor for a treatment plan.',
    'Anemia': 'Anemia is treatable. Consult a doctor for diagnosis and treatment options.',
    'Appendicitis': 'Appendicitis is an emergency. Seek medical attention immediately.',
    'Chickenpox': 'Chickenpox is contagious. Rest and consult a doctor if necessary.',
    'Panic Attack': 'Panic attacks can be managed. Consult a mental health professional for guidance.'
}

def get_yes_no(question):
    while True:
        answer = input(question + " (y/n): ").strip().lower()
        if answer in ['y', 'yes']:
            return True
        elif answer in ['n', 'no']:
            return False
        else:
            print("Please answer with 'y' or 'n'.")

def collect_symptoms():
    symptoms = []
    for question, symptom in questions:
        if get_yes_no(question):
            symptoms.append(symptom)
    return symptoms

def welcome_message():
    print("=" * 60)
    print("      Welcome to the Medical Diagnosis System      ")
    print("=" * 60)
    print("  Your health is our priority. Let's get started!  ")
    print("=" * 60)

def diagnose(symptoms):
    possible_diagnoses = []
    print('\n')
    for illness, explanation, condition in rules:
        if condition(symptoms):
            possible_diagnoses.append((illness, explanation))

    if possible_diagnoses:
        print("=" * 60)
        print("Possible Diagnoses and Recommendations:\n")
        for illness, explanation in possible_diagnoses:
            print("=" * 60)
            print(f"Disease: {illness}")
            print(f"Reason: {explanation}")
            print(f"Recommendation: {replies[illness]}")
    else:
        print("=" * 60)
        print("No matching conditions found. Please consult a doctor for further examination.")


        print("=" * 60)

def main():
    welcome_message()
    symptoms = collect_symptoms()
    diagnose(symptoms)

if __name__ == "__main__":
    main()


