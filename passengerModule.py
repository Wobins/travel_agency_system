import csv


# function to register many passengers in the agency
def register_passenger():
    list_passengers = []  # list of all my passengers

    # passenger template
    passenger_init = {
        "passenger_id": "",
        "passenger_name": "",
        "passenger_weight": 0.0
    }

    # function to set a single passenger
    def set_passenger():
        passenger_name = input("What is the name of the passenger?\n\tEnter his name: \t")
        passenger_id = input("What is the passenger's national Id?\n\tEnter his id: \t")
        passenger_weight = float(input("How heavy are his luggage??\n\tEnter his luggage's weight: \t"))

        passenger = passenger_init.copy()
        passenger["passenger_id"] = passenger_id
        passenger["passenger_name"] = passenger_name
        passenger["passenger_weight"] = passenger_weight
        return passenger

    passenger = set_passenger()
    list_passengers.append(passenger)

    response = input("Do you want to set another passenger?\n\t Yes/No? ")

    while response.lower() == "yes":
        passenger = set_passenger()
        list_passengers.append(passenger)
        response = input("Do you want to set another passenger?\n\t Yes/No? ")

    with open('all-passengers.csv', 'w', newline='') as f:
        for person in list_passengers:
            writer = csv.writer(f)
            writer.writerow([person["passenger_id"], person["passenger_name"], person["passenger_weight"]])

    return list_passengers


# function to get back all the passenger's ids
def get_passengers_ids():
    list_ids = []
    with open('all-passengers.csv') as f:
        csvReader = csv.reader(f, delimiter=',')
        for row in csvReader:
            list_ids.append(row[0])

    return list_ids
