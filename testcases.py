from project1 import *

# filedic()

test1 = filedic("penguins.csv")
# List of dict

# only one row of data
test2 = filedic("one_penguin.csv")
print(test2)
# list of one dict

# (only headers)
test3 = filedic("empty.csv")
print(test3)
# empty list []

# nonexistent file
try:
    test4 = filedic("no_file.csv")
except FileNotFoundError:
    print("Passed FileNotFoundError test")

# avg()
print(avg([1, 2, 3]))   # should be 2.0
print(avg([10, 20, 30]))  # should be 20.0
print(avg([100]))         # 100.0

try:
    print(avg([]))        # ZeroDivisionError
except ZeroDivisionError:
    print("Passed ZeroDivisionError")

# avg_mass_Fadelie_Dream()

# same island and species 
data1 = [{"species": "Adelie", "island": "Dream", "sex": "female", "body_mass_g": "3000"},{"species": "Adelie", "island": "Dream", "sex": "female", "body_mass_g": "3100"}]
print(avg_mass_Fadelie_Dream(data1))
# 3050.00

# island and species check
data2 = [{"species": "Adelie", "island": "Dream", "sex": "female", "body_mass_g": "3200"},{"species": "Gentoo", "island": "Dream", "sex": "female", "body_mass_g": "3000"}]
print(avg_mass_Fadelie_Dream(data2))
#  3200.00 grams

# wrong penguin
data3 = [{"species": "Chinstrap", "island": "Torgersen", "sex": "male", "body_mass_g": "3500"}]
print(avg_mass_Fadelie_Dream(data3))
# None

# nonesistent mass
data4 = [{"species": "Adelie", "island": "Dream", "sex": "female", "body_mass_g": "NA"}]
print(avg_mass_Fadelie_Dream(data4))
# None


# avg_bill_maxflip_2007()

#matching data
data1 = [{"bill_length_mm": "40.5", "flipper_length_mm": "200", "year": "2007"},{"bill_length_mm": "42.0", "flipper_length_mm": "210", "year": "2007"}]
print(avg_bill_maxflip_2007(data1))
# avg 41.25, max 210

# NA value
data2 = [{"bill_length_mm": "NA", "flipper_length_mm": "220", "year": "2007"},{"bill_length_mm": "44.5", "flipper_length_mm": "230", "year": "2007"}]
print(avg_bill_maxflip_2007(data2))
# avg 44.50, max 230 


# all NA
data3 = [{"bill_length_mm": "NA", "flipper_length_mm": "NA", "year": "2007"}]
print(avg_bill_maxflip_2007(data3))
# None

# Empty list
data4 = []
print(avg_bill_maxflip_2007(data4))
# None


# report()

# normal
report("test_output.txt", "avg1 test", "avg2 test")
# formatted text
report("test_report.txt", "The average mass is 3050.00 grams", "The average bill length is 41.25 millimeters, and the max flipper length is 210 millimeters.")
#empty
report("empty_report.txt", None, None)
# None