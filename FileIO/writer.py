import csv


# with open("fighterMoves.csv", "w") as file:
#     csv_writer = writer(file)
#     csv_writer.writerow(["Character", "Ability", "Special"])
#     csv_writer.writerow(["Ryu", "Hadouken", "Metsu Hadouken"])
#     csv_writer.writerow(["Dudley", "Machine Gun Blow", "Corkscrew Cross"])
#     csv_writer.writerow(["Sagat", "Tiger Shot", "Tiger Destruction"])

# with open("dogs.csv", "w") as file:
#     headers = ["Name", "Breed", "Age"]
#     csv_writer = DictWriter(file, fieldnames=headers)
#     csv_writer.writeheader()
#     csv_writer.writerow({
#         "Name": "Snoopy",
#         "Breed": "Beagle",
#         "Age": 49
#     })


### print_users Exercise ###
def print_users():
    with open("users.csv") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader: 
            print("{} {}".format(row['First Name'], row['Last Name']))


### find_user Exercise ###
def find_user(first, last):
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        for (index, row) in enumerate(csv_reader):
            first_name_match = first == row[0]
            last_name_match = last == row[1]
            if first_name_match and last_name_match:
                return index
        return f"{first} {last} not found."