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




print(filedic('penguins.csv'))



# def avg_mass_Fadelie_Dream(header):


    


# def avg_bill_Mmass4k():