import random

# Create random_lists below:

random_list_first_names = []
random_list_last_names = []


first_name_file = open("firstnames.txt", "r")
last_name_file = open("lastnames.txt", "r")
#print(first_name_file.read())
#print(last_name_file.read())

for line in first_name_file:
    random_list_first_names.append(line.strip("\n"))


for line in last_name_file:
    random_list_last_names.append(line.strip("\n"))


hot_girl_name = random.choice(random_list_first_names) + " " +random.choice(random_list_last_names)

print(hot_girl_name)
