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

def avg_mass_Fadelie_Dream(data): # columns: species, island, gender, mass - 4
    masses = []
    for line in data:
        if line['species'] == 'Adelie' and line['island'] == 'Dream' and line['sex'] == 'female':
            masses.append(float(line['body_mass_g']))

    if len:
        avg = sum(masses) / len(masses)
        return f"{avg:.2f} grams"
    else:
        return None



def avg_bill_Mmass4k(data, min = 4200): # columns: gender, mass, bill length - 3
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
    
def report(filename, avg1, avg2):
    with open(filename, "w") as file:
        file.write("Data Analysis Calculations of the Penguin CSV File\n\n")

        file.write("What is the average body mass of all female Adelie penguins in Dream island?\n")
        file.write(avg1 + "\n\n")
        
        file.write("What is the average bill length of male penguins above 4200g?\n")
        file.write(avg2)


def main():
    data = filedic('penguins.csv')

    x = avg_mass_Fadelie_Dream(data)
    y = avg_bill_Mmass4k(data)

    report("penguin_report.txt", x, y)

main()