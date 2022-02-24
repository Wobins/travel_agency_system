import csv

from prettytable import PrettyTable
import carModule
import passengerModule

print("What do you want to do?")
print("\t1-Add a bus to the fleet")
print("\t2-Enroll a passenger")
print("\t3-Add a passenger to a bus")
print("\t4-View number of seats")
#print("\t4-List all the passengers of a specific bus")

option = int(input("Enter your option:\t\t"))

def choose(option):
    match option:
        case 1:
            carModule.create_fleet()
        case 2:
            passengerModule.add_passenger()
        case 3:
            # list_passengers = passengerModule.add_to_bus()
            # with open('fleet.csv') as f:
            #     csvReader = csv.reader(f, delimiter=',')
            #     for row in csvReader:
            #         list_bus.append(row[0])
            print("hello")
        case 4:
            carModule.print_seats()
        case _:
            print("hello")

choose(option)
#carModule.print_seats()
