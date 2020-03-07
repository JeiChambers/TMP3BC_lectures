with open("haiku.txt", "w") as file:
    file.write("Yuki ga huru\n")
    file.write("Yukkuri no Namida\n")
    file.write("Nakanaide")

with open("haiku.txt", "a") as file:
    file.write("\n")
    file.write("Look, I realize this isn't a great Haiku\n")
    file.write("...but it doesn't break any rules\n")
    file.write("...so there you go! \n")

with open("haiku.txt", "a") as file:
    file.seek(0) # Goes to the first available line at the end of the file. 
    file.write("}:-(")



### Copy Story Coding Challenge ###
def copy(s1, s2):
    with open(s1) as file:
        story = file.read()
        
    with open(s2, "w") as s2:
        s2.write(story)

### Copy and Reverse Coding Challenge ###
def copy_and_reverse(s, sr):
    with open(s) as file:
        story = file.read()
        
    with open(sr, "w") as sr:
        sr.write(story[::-1])

### Story Statistics ###
def statistics(story):
    with open(story) as file:
        lines = file.readlines()
        
        return {"lines": len(lines),
                "words":  sum(len(line.split(" "))for line in lines),
                "characters": sum(len(line) for line in lines) 
                }

### Find and Replace ###

def find_and_replace(story, old, new):
    with open(story, "r+") as file:
        text = file.read()
        new_text = text.replace(old, new)
        file.seek(0)
        file.write(new_text)
    
### Add_user Exercise ###
import csv

def add_user(first, last):
    with open("users.csv", "a") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([first, last])
