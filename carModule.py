from prettytable import PrettyTable

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

for x in range(2):
    car = add_car()
    cars_fleet.append(car)

t = PrettyTable(['Car VIN', 'Car seats'])
for car in cars_fleet:
	t.add_row([car["car_vin"], car["car_seats"]])
print(t)