# Name: Amanda Xiaohan Huang
# UID: 20979264
# Email: xiohan@umich.edu


# Planned Calculations - What is the average body mass of all female Adélie penguins in Dream island?
#                        What is the average bill length of and max flipper length of penguins in 2007?

import csv

def filedic(filename):
    data = []
    with open(filename) as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def avg(values):
    return sum(values)/len(values)

def avg_mass_Fadelie_Dream(data): # columns: species, island, gender, mass - 4
    masses = []
    for line in data:
        if line['species'] == 'Adelie' and line['island'] == 'Dream' and line['sex'] == 'female':
            if line['body_mass_g'] != "NA":
                masses.append(float(line['body_mass_g']))

    if masses:
        return f"The average mass is {avg(masses):.2f} grams"
    else:
        return None


def avg_bill_maxflip_2007(data): # columns: bill length, flipper length, year
    bill = []
    flip = []
    for line in data:
        bill_val = line['bill_length_mm']
        flip_val = line['flipper_length_mm']

        if bill_val != "NA" and flip_val != "NA":
            bill.append(float(bill_val))
            flip.append(int(flip_val))
    if bill and flip:
        return f"The average bill length is {avg(bill):.2f} millimeters, and the max flipper length is {max(flip)} millimeters."
    else:
        return None
        

    
def report(filename, avg1, avg2):
    with open(filename, "w") as file:
        file.write("Data Analysis Calculations of the Penguin CSV File\n\n")

        file.write("What is the average body mass of all female Adelie penguins in Dream island?\n")
        if avg1 is not None:
            file.write(avg1 + "\n\n")
        
        file.write("What is the average bill length of and max flipper length of penguins in 2007?\n")
        if avg2 is not None:    
            file.write(avg2)


def main():
    data = filedic('penguins.csv')

    x = avg_mass_Fadelie_Dream(data)
    y = avg_bill_maxflip_2007(data)

    report("penguin_report.txt", x, y)

main()