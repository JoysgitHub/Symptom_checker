questions = [
    ('1. Have you experienced a sudden increase in body temperature?', 'high_temp'),
    ('2. Are you having difficulty breathing?', 'breathlessness'),
    ('3. Do you feel a tightness in your chest?', 'chest_discomfort'),
    ('4. Are you experiencing sharp or persistent pain in your chest?', 'chest_pain'),
    ('5. Is your cough dry or productive?', 'cough'),
    ('6. Have you noticed a wheezing sound when you breathe?', 'wheezing'),
    ('7. Do you feel unusually cold or have episodes of shivering?', 'chills'),
    ('8. Are you feeling more fatigued than usual?', 'fatigue'),
    ('9. Have you experienced sudden numbness in your face, arms, or legs?', 'numbness'),
    ('10. Are you having trouble concentrating or feeling disoriented?', 'confusion'),
    ('11. Do you find it difficult to articulate your thoughts?', 'trouble_speaking'),
    ('12. Have you had frequent episodes of loose or watery stools?', 'diarrhea'),
    ('13. Are you experiencing persistent nausea?', 'nausea'),
    ('14. Have you been vomiting recently?', 'vomiting'),
    ('15. Have you had any recent stomach pain?', 'abdominal_pain'),
    ('16. Is your throat sore or painful when swallowing?', 'sore_throat'),
    ('17. Have you noticed any unusual rashes or spots on your skin?', 'rash'),
    ('18. Are you feeling excessively thirsty?', 'excessive_thirst'),
    ('19. Have you noticed swelling in your legs or ankles?', 'swelling'),
    ('20. Are you experiencing pain in your joints?', 'joint_pain'),
    ('21. Do you feel stiffness in your joints?', 'stiffness'),
    ('22. Have you been sneezing frequently?', 'sneezing'),
    ('23. Is your nose often congested?', 'runny_nose'),
    ('24. Are your eyes itchy or watery?', 'itchy_eyes'),
    ('25. Are you experiencing muscle soreness or aches?', 'muscle_aches'),
    ('26. Do you feel dizzy or lightheaded?', 'dizziness'),
    ('27. Have you been experiencing persistent pain in your lower back?', 'back_pain'),
    ('28. Have you noticed any changes in your menstrual cycle?', 'menstrual_disorders'),
    ('29. Are you feeling persistently sad?', 'persistent_sadness'),
    ('30. Have you lost interest or pleasure in activities you once enjoyed?','loss_of_interest'),
    ('31. Do you experience a rapid heartbeat?', 'rapid_heartbeat'),
    ('32. Are you experiencing frequent headaches?', 'headache'),
    ('33. Do you feel chest discomfort or shortness of breath?', 'shortness_of_breath'),
    ('34. Are you experiencing flank pain?', 'flank_pain'),
    ('36. Do you feel a burning sensation when urinating?', 'burning_sensation'),
    ('36. Have you noticed any blisters on your skin?', 'blisters'),
    ('37. Have you noticed any itchy rashes on your skin?', 'itchy_rash'),
    ('38. Are you experiencing a throbbing headache?', 'throbbing_headache'),
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
    return 'high_temp' in symptoms or 'fatigue' in symptoms

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



def get_yes_no(question):
    while True:
        answer = input(question + " (y/n): ").strip().lower()
        if answer in ['y', 'yes']:
            return True
        elif answer in ['n', 'no']:
            return False
        else:
            print("Please answer with 'y' or 'n'")


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


def main():
    welcome_message()
    print('\n')
    symptoms = collect_symptoms()
    diagnose(symptoms)

if __name__ == "__main__":
    main()

