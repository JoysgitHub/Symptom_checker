questions = [
    ('Have you noticed a rise in your body temperature or felt feverish?', 'high_temp'),
    ('Do you feel short of breath or have difficulty breathing?', 'breathlessness'),
    ('Do you feel any tightness or discomfort in your chest?', 'chest_tightness'),
    ('Are you experiencing any pain or pressure in your chest?', 'chest_pain'),
    ('Is your cough persistent or have you been coughing more than usual?', 'cough'),
    ('Have you been experiencing any wheezing or a whistling sound when breathing?', 'wheezing'),
    ('Have you been feeling unusually cold or shivering frequently?', 'chills'),
    ('Do you often feel exhausted, weak, or unusually tired?', 'fatigue'),
    ('Are you experiencing any numbness, weakness, or loss of sensation in any part of your body?', 'numbness_weakness'),
    ('Are you feeling confused, disoriented, or having trouble remembering things?', 'confusion'),
    ('Do you find it hard to speak clearly or understand speech?', 'trouble_speaking'),
    ('Have you been having loose or watery stools frequently?', 'diarrhea'),
    ('Have you been vomiting or feeling nauseous recently?', 'vomiting'),
    ('Do you often feel nauseous or queasy without a clear cause?', 'nausea'),
    ('Have you had any stomach pain or discomfort recently?', 'abdominal_pain'),
    ('Is your throat sore, scratchy, or painful when swallowing?', 'sore_throat'),
    ('Have you noticed any rash, spots, or unusual marks on your skin?', 'rash'),
    ('Do you feel excessively thirsty or have a dry mouth?', 'thirst'),
    ('Have you noticed any swelling in your arms, legs, or ankles?', 'swelling'),
    ('Are you experiencing pain, swelling, or discomfort in your joints?', 'joint_pain'),
    ('Have you had difficulty moving or felt stiffness in your joints?', 'stiffness'),
    ('Are you experiencing intense joint pain, swelling, or redness in your joints?', 'gout'),
    ('Have you been sneezing more than usual or having frequent sneezing bouts?', 'sneezing'),
    ('Is your nose frequently runny or congested?', 'runny_nose'),
    ('Do your eyes feel itchy, watery, or irritated?', 'itchy_eyes'),
    ('Are you experiencing soreness or aches in your muscles?', 'muscle_aches'),
    ('Do you experience dizziness or lightheadedness, especially when standing up?', 'dizziness'),
    ('Have you been dealing with any pain in your lower back or spine?', 'back_pain'),
    ('Have you noticed any changes in your menstrual cycle, such as irregular periods or mood swings?', 'menstrual_disorders'),
    ('Are you feeling unusually sad, disinterested in activities, or experiencing changes in appetite?', 'persistent_sadness'),
    ('Do you feel a rapid heartbeat, dizziness, or a sense of impending doom?', 'panic_attack'),
    ('Are you experiencing frequent headaches, nosebleeds, or blurred vision?', 'hypertension'),
    ('Do you feel chest discomfort, shortness of breath, or fatigue?', 'heart_disease'),
    ('Are you experiencing flank pain, frequent urination, or nausea?', 'kidney_infection'),
    ('Do you feel a burning sensation when urinating, or have you been experiencing pelvic pain?', 'urinary_tract_infection'),
    ('Have you noticed any itchy rash, fatigue, or blisters on your skin?', 'chickenpox'),
    ('Do you have a throbbing headache, nausea, or sensitivity to light?', 'migraine'),
]




def rule_asthma(symptoms):
    return 'wheezing' in symptoms or 'breathlessness' in symptoms or 'chest_tightness' in symptoms

def rule_pneumonia(symptoms):
    return 'high_temp' in symptoms or 'chest_pain' in symptoms or 'cough' in symptoms

def rule_arthritis(symptoms):
    return 'joint_pain' in symptoms or 'stiffness' in symptoms or 'swelling' in symptoms

def rule_gastroenteritis(symptoms):
    return 'diarrhea' in symptoms or 'vomiting' in symptoms or 'nausea' in symptoms

def rule_stroke(symptoms):
    return 'numbness_weakness' in symptoms or 'confusion' in symptoms or 'trouble_speaking' in symptoms

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

