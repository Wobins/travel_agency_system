import csv

def add_passenger():
    list_passengers = []

    passenger_init = {
        "passenger_id": "",
        "passenger_name": "",
        "passenger_weight": 0.0
    }

    def enroll_passenger():
        passenger_name = input("What is the name of the passenger?\n\tEnter his name: \t")
        passenger_id = input("What is the passenger's national Id?\n\tEnter his id: \t")
        passenger_weight = float(input("How heavy are his luggage??\n\tEnter his luggage's weight: \t"))

        passenger = passenger_init.copy()
        passenger["passenger_id"] = passenger_id
        passenger["passenger_name"] = passenger_name
        passenger["passenger_weight"] = passenger_weight
        return passenger

    passenger = enroll_passenger()
    list_passengers.append(passenger)

    response = input("Do you want to pursue another enrollment?\n\t Yes/No? ")

    while response.lower() == "yes":
        passenger = enroll_passenger()
        list_passengers.append(passenger)
        response = input("Do you want to pursue another enrollment?\n\t Yes/No? ")

    with open('all-passengers.csv', 'w', newline='') as f:
        for person in list_passengers:
            writer = csv.writer(f)
            writer.writerow([person["passenger_id"], person["passenger_name"], person["passenger_weight"]])

    return list_passengers


def add_to_bus():
    list_bus = []
    with open('all-passengers.csv') as f:
        csvReader = csv.reader(f, delimiter=',')
        for row in csvReader:
            list_bus.append(row[0])

    return list_bus




