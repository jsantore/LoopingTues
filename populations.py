population_file = open("CountryPops.txt")
population_lines = population_file.readlines()
country_pops = []
for line in population_lines:
    country_data = line.split(",")
    current_dictionary ={}
    current_dictionary["country"] = country_data[0]
    current_dictionary["population"] = int(country_data[1])
    current_dictionary["pop_change"] = int(country_data[2])
    country_pops.append(current_dictionary)

while True:
    print("[1] Press one to quit")
    print("[2] Press two to find biggest population gain")
    print("[3] press 3 to find the biggest population loss")
    choice = input("Please enter the number of your choice")
    if choice =='1':
        break
    elif choice == '2':
        biggest_gain = country_pops[0]
        for country_record in country_pops:
            if country_record["pop_change"] > biggest_gain["pop_change"]:
                biggest_gain = country_record
        print(f" The country with the biggest population gain was {biggest_gain['country']}")
    elif choice == '3':
        biggest_loss = country_pops[0]
        for country_record in country_pops:
            if country_record["pop_change"] < biggest_loss["pop_change"]:
                biggest_loss = country_record
        print(f" The country with the biggest population loss was {biggest_loss['country']}")
    else:
        print("Please enter a valid choice")