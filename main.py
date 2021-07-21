import csv


# create function to put each col into list
def list_importer(lst, csv_file, col_name):
    with open(csv_file) as insurance_file:
        insurance_data = csv.DictReader(insurance_file)
        for row in insurance_data:
            lst.append(row[col_name])
        return lst


# In my Python file I create empty lists for the various attributes in insurance.csv
ages = []
sexes = []
bmis = []
num_children = []
smoker_statuses = []
regions = []
insurance_charges = []

list_importer(ages, 'insurance.csv', 'age')
list_importer(sexes, 'insurance.csv', 'sex')
list_importer(bmis, 'insurance.csv', 'bmi')
list_importer(num_children, 'insurance.csv', 'children')
list_importer(smoker_statuses, 'insurance.csv', 'smoker')
list_importer(regions, 'insurance.csv', 'region')
list_importer(insurance_charges, 'insurance.csv', 'charges')

# average age of the patients = analyse_ages
# number of men vs. women counted in the dataset = analyse_sex_ratio
# geographical regions of patients within the dataset = analyse_location
# average yearly medical charges of the patients = analyse_charges
# creating a dictionary that contains all patient information = create_dictionary


# Create class Patient info with methods to perform above tasks
class PatientsInfo:
    def __init__(self, patients_ages, patients_sexes, patients_bmis, patients_num_children,
                 patients_smoker_statuses, patients_regions, patients_charges):
        self.patients_ages = patients_ages
        self.patients_sexes = patients_sexes
        self.patients_bmis = patients_bmis
        self.patients_num_children = patients_num_children
        self.patients_smoker_statuses = patients_smoker_statuses
        self.patients_regions = patients_regions
        self.patients_charges = patients_charges

    def analyse_ages(self):
        total_age = 0
        for age in self.patients_ages:
            total_age += int(age)
        return "Average Patient Age: " + str(round(total_age / len(self.patients_ages), 2)) + " years"

    def analyse_sex_ratio(self):
        total_men = 0
        total_women = 0
        for sex in self.patients_sexes:
            if sex == 'male':
                total_men += 1
            elif sex == 'female':
                total_women += 1
        print("Number of females: ", total_women)
        print("Number of males: ", total_men)

    def analyse_location(self):
        locations = []
        for location in self.patients_regions:
            if location not in locations:
                locations.append(location)
        return locations

    def analyse_charges(self):
        total_charges = 0
        for charge in self.patients_charges:
            total_charges += float(charge)
        return ("Average Yearly Medical Insurance Charges: " +
                str(round(total_charges / len(self.patients_charges), 2)) + " dollars.")

    def create_dictionary(self):
        self.patient_dictionary = {}
        self.patient_dictionary["age"] = [int(age) for age in self.patients_ages]
        self.patient_dictionary["sex"] = [self.patients_ages]
        self.patient_dictionary["bmi"] = [self.patients_bmis]
        self.patient_dictionary["children"] = [self.patients_num_children]
        self.patient_dictionary["smoker"] = [self.patients_smoker_statuses]
        self.patient_dictionary["regions"] = [self.patients_regions]
        self.patient_dictionary["charges"] = [self.patients_charges]
        return self.patient_dictionary


# create instance of PatientInfo class and run methods
patient_info = PatientsInfo(ages, sexes, bmis, num_children, smoker_statuses, regions, insurance_charges)
print(patient_info.analyse_ages())
patient_info.analyse_sex_ratio()
print(patient_info.analyse_location())
print(patient_info.analyse_charges())
print(patient_info.create_dictionary())
