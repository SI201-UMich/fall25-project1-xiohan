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
        return f"The Average Mass of All Female Adelie Penguins in Dream Island is: {avg:.2f}g"
    else:
        return None


data = filedic('penguins.csv')
avg = avg_mass_Fadelie_Dream(data)
print(avg)




# def avg_bill_Mmass4k(data, min = 4200):