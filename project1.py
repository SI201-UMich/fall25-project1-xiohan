# Name: Amanda Xiaohan Huang
# UID: 20979264
# Email: xiohan@umich.edu


# Planned Calculations - What is the average body mass of all female Adélie penguins in Dream island?
#                        What is the average bill length of male penguins above the body mass of 4,200g?

import csv

def filedic(filename):
    data = []
    with open(filename) as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def avg_mass_Fadelie_Dream(data): # columns: species, island, gender, mass
    masses = []
    for line in data:
        if line['species'] == 'Adelie' and line['island'] == 'Dream' and line['sex'] == 'female':
            masses.append(float(line['body_mass_g']))

    if len:
        avg = sum(masses) / len(masses)
        return f"{avg:.2f} grams"
    else:
        return None



def avg_bill_Mmass4k(data, min = 4200):
    bill_lengths = []
    for line in data:
        if line['sex'] == 'male':
            if float(line['body_mass_g']) > min:
                bill_lengths.append(float(line['bill_length_mm']))
    if bill_lengths:
        avg = sum(bill_lengths) / len(bill_lengths)
        return f"{avg:.2f} millimeters"
    else:
        return None
    
data = filedic('penguins.csv')
print(avg_mass_Fadelie_Dream(data))
print(avg_bill_Mmass4k(data))
