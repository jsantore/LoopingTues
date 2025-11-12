def load_data():
    data = [{'name': 'Terraria', 'release': 2011, 'price': 9.99, 'total_sales': 180000000}, {'name': 'Stardew Valley', 'release': 2016, 'price': 14.99, 'total_sales': 150000000}, {'name': 'RimWorld', 'release': 2018, 'price': 34.99, 'total_sales': 95000000}, {'name': 'Factorio', 'release': 2020, 'price': 35.0, 'total_sales': 91000000}, {'name': "Don't Starve Together", 'release': 2016, 'price': 14.99, 'total_sales': 82000000}, {'name': 'Hollow Knight', 'release': 2017, 'price': 14.99, 'total_sales': 82000000}, {'name': 'é¬¼è°·å…«è’ Tale of Immortal', 'release': 2023, 'price': 19.99, 'total_sales': 69000000}, {'name': 'Project Zomboid', 'release': 2013, 'price': 19.99, 'total_sales': 69000000}, {'name': 'The Binding of Isaac:Rebirth', 'release': 2014, 'price': 14.99, 'total_sales': 66000000}, {'name': 'Bloons TD 6', 'release': 2018, 'price': 13.99, 'total_sales': 66000000}]
    return data

def print_menu():
    print("[1] Quit")
    print("[2] Print older game")
    print("[3] Print big money making game")
    print("[4] Print games selling many copies")

def main():
    game_data = load_data()
    while True:
        print_menu()
        choice = input("Please enter the number of your choice")
        if choice =='1':
            break
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        else:
            print("Please enter a valid choice")

    main()