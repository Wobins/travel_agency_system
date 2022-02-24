import csv

def create_fleet():
    cars_fleet = []

    car_init = {
        "car_vin": "",
        "car_seats": 0,
        "passage_dashboard": []
    }

    def add_car():
        car_vin = input("What is the Vehicle Identification Number(VIN) of the car?\n\tEnter the VIN: \t")
        car_seats = int(input("How many seats are in the car?\n\tEnter the number of seats: \t"))

        car = car_init.copy()
        car["car_vin"] = car_vin
        car["car_seats"] = car_seats
        return car

    car = add_car()
    cars_fleet.append(car)

    response = input("Do you want to add a car to the fleet?\n\t Yes/No? ")

    while response.lower() == "yes":
        car = add_car()
        cars_fleet.append(car)
        response = input("Do you want to proceed your shopping?\n\t Yes/No? ")

    with open('fleet.csv', 'w', newline='') as f:
        for bus in cars_fleet:
            writer = csv.writer(f)
            writer.writerow([bus["car_vin"], bus["car_seats"]])

    return cars_fleet

def print_seats():
    with open('fleet.csv') as f:
        csvReader = csv.reader(f, delimiter=',')
        print("Here below are each bus and its number of seats")
        for row in csvReader:
            print("\tBus VIN: {}\t\tSeats: {}".format(row[0], row[1]))

