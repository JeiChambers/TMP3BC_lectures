from csv import reader
from csv import DictReader

##### Using Reader to deal with .csv files   #####
with open("fighters.csv") as file:
    csv_reader = reader(file)
    next(csv_reader) # Starts with second line of file to get rid of header.
    for fighter in csv_reader:
        # each row is a list!
        print(f"{fighter[0]} is from {fighter[1]}")

# Saving data into a list for later use. 
# with open("fighters.csv") as file:
#     csv_reader = reader(file)
#     data =  list(csv_reader)
#     print(data)



with open("fighters.csv") as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        # each row is an OrderedDict!
        print(row)


