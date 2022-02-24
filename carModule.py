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
    print(cars_fleet)

    response = input("Do you want to add a car to the fleet?\n\t Yes/No? ")

    while response.lower() == "yes":
        car = add_car()
        cars_fleet.append(car)
        response = input("Do you want to proceed your shopping?\n\t Yes/No? ")

    f = open("fleet.csv", "w")
    f.write("\t\t\t\tListe des bus de notre flotte!!\n")
    f.write("vin,seats\n")
    f.close()

    for bus in cars_fleet:
        f = open('fleet.csv', 'a')
        writer = csv.writer(f)
        writer.writerow([bus["car_vin"], bus["car_seats"]])
    #f.close()

# for x in range(2):
#     car = add_car()
#     cars_fleet.append(car)
#
# t = PrettyTable(['Car VIN', 'Car seats'])
# for car in cars_fleet:
# 	t.add_row([car["car_vin"], car["car_seats"]])
# print(t)