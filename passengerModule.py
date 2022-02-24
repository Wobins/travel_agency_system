list_passengers = []

passenger_init = {
    "passenger_id": "",
    "passenger_name": "",
    "passenger_weight": 0.0
}

def add_passenger():
    passenger_name = input("What is the name of the passenger?\n\tEnter his name: \t")
    passenger_id = input("What is the passenger's national Id?\n\tEnter his id: \t")
    passenger_weight = float(input("How heavy are his luggage??\n\tEnter his luggage's weight: \t"))

    passenger = passenger_init.copy()
    passenger["passenger_id"] = passenger_id
    passenger["passenger_name"] = passenger_name
    passenger["luggage_weight"] = passenger_weight
    return passenger

print(add_passenger())





