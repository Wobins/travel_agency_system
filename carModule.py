from prettytable import PrettyTable
import csv

import passengerModule


def set_fleet():
    cars_fleet = []

    car_init = {
        "car_vin": "",
        "car_seats": 0,
        "passage_dashboard": []
    }

    def set_car():
        car_vin = input("What is the Vehicle Identification Number(VIN) of the car?\n\tEnter the VIN: \t")
        car_seats = int(input("How many seats are in the car?\n\tEnter the number of seats: \t"))

        car = car_init.copy()
        car["car_vin"] = car_vin
        car["car_seats"] = car_seats
        return car

    car = set_car()
    cars_fleet.append(car)

    response = input("Do you want to add another car to the fleet?\n\t Yes/No? ")

    while response.lower() == "yes":
        car = set_car()
        cars_fleet.append(car)
        response = input("Do you want to add another car to the fleet?\n\t Yes/No? ")

    with open('fleet.csv', 'w', newline='') as f:
        for bus in cars_fleet:
            writer = csv.writer(f)
            writer.writerow([bus["car_vin"], bus["car_seats"]])

    return cars_fleet


def print_seats():
    tab = PrettyTable(['Bus VIN', 'Seats'])
    with open('fleet.csv') as f:
        csvReader = csv.reader(f, delimiter=',')
        print("Here below are each bus and its number of seats")
        for row in csvReader:
            tab.add_row([row[0], row[1]])
    print(tab)


def board_passengers_in_bus():
    list_ids = passengerModule.get_passengers_ids()
    list_buses = []
    with open('fleet.csv') as f:
        csvReader = csv.reader(f, delimiter=',')
        for row in csvReader:
            list_buses.append({"car_vin": row[0], "passengers": [{"passenger_id": "<empty>"}]})
    num = int(input("What is the index of the listed bus in which you want to board passengers?\n\tEnter the index: "))

    for nic_id in list_ids:
        list_buses[num]["passengers"][0]["passenger_id"] = nic_id
    print(list_buses)

    tab = PrettyTable(['Bus VIN', 'Passenger\'s IDs'])
    for vehicle in list_buses:
        tab.add_row([vehicle["car_vin"], vehicle["passengers"]])
    print(tab)
