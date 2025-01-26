questions = [
    ('Are you wheezing?', 'wheezing'),                          
    ('Are you short of breath?', 'breathlessness'),             
    ('Do you have chest tightness?', 'chest_tightness'),       
    ('Do you have a high temperature?', 'high_temp'),          
    ('Do you have chest pain?', 'chest_pain'),                 
    ('Are you coughing?', 'cough'),                             
    ('Do you have joint pain?', 'joint_pain'),                 
    ('Do you have stiffness?', 'stiffness'),                   
    ('Do you have swelling?', 'swelling'),                     
    ('Do you have diarrhea?', 'diarrhea'),                      
    ('Are you vomiting?', 'vomiting'),                          
    ('Do you have nausea?', 'nausea'),                          
    ('Do you have numbness or weakness?', 'numbness_weakness'), 
    ('Are you confused?', 'confusion'),                         
    ('Do you have trouble speaking?', 'trouble_speaking'),     
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

