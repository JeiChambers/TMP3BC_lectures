from csv import reader, writer

# with open('fighters.csv') as file:
#     csv_reader = reader(file)
#     fighters = [[s.upper() for s in row] for row in csv_reader]
    

# with open('screaming_fighters.csv', "w") as file:
#     csv_writer = writer(file)
#     for fighter in csv_reader:
#         csv_writer.writerow(fighter)



# Refined Solution #
with open('fighters.csv') as file:
    csv_reader = reader(file)
    with open('screaming_fighters.csv', "w") as file:
        csv_writer = writer(file)
        for fighter in csv_reader:
            csv_writer.writerow([s.upper() for s in fighter])



