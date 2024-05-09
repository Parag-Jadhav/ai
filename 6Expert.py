class MedicalDiagnosis:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.symptoms = {}

    def accept_details(self):
        self.name = input("What is the name of patient ? ==>  ")
        self.age = int(input(f"What is Age of {self.name} ? ==> "))

    def symptom(self, patient, symp):
        choice = input(f"Does {patient} have a {symp} (y/n) ?  ")
        self.symptoms[symp] = choice.lower() == 'y'

    def is_infected(self, symp):
        return self.symptoms.get(symp, False)

    def proposition(self, disease):
        if disease == "measles":
            return (self.is_infected("fever") and
                    self.is_infected("cough") and
                    self.is_infected("conjuctivities") and
                    self.is_infected("runny_nose") and
                    self.is_infected("rash"))
        elif disease == "german_measles":
            return (self.is_infected("fever") and
                    self.is_infected("headache") and
                    self.is_infected("runny_nose") and
                    self.is_infected("rash"))
        elif disease == "flu":
            return (self.is_infected("fever") and
                    self.is_infected("headache") and
                    self.is_infected("body_ahce") and
                    self.is_infected("conjuctivities") and
                    self.is_infected("chills") and
                    self.is_infected("soar_throat") and
                    self.is_infected("cough") and
                    self.is_infected("runny_nose"))
        elif disease == "common_cold":
            return (self.is_infected("headache") and
                    self.is_infected("sneezing") and
                    self.is_infected("soar_throat") and
                    self.is_infected("chills") and
                    self.is_infected("runny_nose"))
        elif disease == "mumps":
            return (self.is_infected("fever") and
                    self.is_infected("swollen_glands"))
        elif disease == "chicken_pox":
            return (self.is_infected("fever") and
                    self.is_infected("rash") and
                    self.is_infected("body_ahce") and
                    self.is_infected("chills"))
        elif disease == "whooping_cough":
            return (self.is_infected("cough") and
                    self.is_infected("sneezing") and
                    self.is_infected("runny_nose"))
        return False

    def conclude(self, name, disease):
        print(f"\n{name} probably has {disease}")

def main():
    print("\n\n\n")

    obj = MedicalDiagnosis()
    obj.accept_details()

    symptoms = ["fever", "rash", "headache", "runny_nose", "conjuctivities",
                "cough", "body_ahce", "chills", "soar_throat", "sneezing", "swollen_glands"]

    for symptom in symptoms:
        obj.symptom(obj.name, symptom)

    nothing_detected = True

    diseases = ["measles", "german_measles", "flu", "common_cold", "mumps", "chicken_pox", "whooping_cough"]
    for disease in diseases:
        if obj.proposition(disease):
            obj.conclude(obj.name, disease)
            nothing_detected = False

    if nothing_detected:
        print("\nI am sorry I am unable to identify the disease ...")

    print("\n\n")
    input("PRESS ANY KEY TO EXIT")

if __name__ == "__main__":
    main()


