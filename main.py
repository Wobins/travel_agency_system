import carModule
import passengerModule

print("What do you want to do?")
print("\t1-Set up a fleet")
print("\t2-Register a passenger")
print("\t3-Add a passenger to a bus")
print("\t4-View number of seats")

option = int(input("Enter your option:\t\t"))


def choose(opt):
    match opt:
        case 1:
            carModule.set_fleet()
        case 2:
            passengerModule.register_passenger()
        case 3:
            carModule.board_passengers_in_bus()
        case 4:
            carModule.print_seats()
        case _:
            print("hello")


choose(option)
