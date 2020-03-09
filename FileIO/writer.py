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


### Update_Users Exercise ###
import csv

def update_users(old_first, old_last, new_first, new_last):
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        rows = list(csv_reader)

    count = 0

    with open("users.csv", "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in rows:
            if row[0] == old_first and row[1] == old_last:
                csv_writer.writerow([new_first, new_last])
                count += 1 
            else:
                csv_writer.writerow(row)

        return f"User updated: {count}."


### Delete Users Exercise ###

import csv

def delete_users(first, last):
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        rows = list(csv_reader)
        
    count = 0 
    
    with open("users.csv", "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in rows:
            if row[0] == first and row[1] == last:
                count += 1
            else:
                csv_writer.writerow(row)
            
        return "Users deleted: {}.".format(count)


