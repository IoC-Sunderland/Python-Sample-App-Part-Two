""" Vince's Vehicles:

This system allows the user to rent different types of vehicles

"""

import sys
from vehicles import Car, Boat, Plane
from inventory import VehicleInventory


class Menu:

    def print_main_menu(self):
        print("""
            1.Add a Vehicle
            2.Remove a Vehicle
            3.View all Vehicles
            4.Exit/Quit
            """)

    def handle_input(self):

        self.ans = input("What would you like to do? ")

        # Enter a Vehicle
        if self.ans == "1":
            choice = input("Enter vehicle type\n1: Car\n"
                           "2: Plane\n"
                           "3: Boat\n")

            # Car
            if choice == "1":

                car_colour = input("Car Colour: ")
                car_weight = int(input("Car Weight: "))
                car_brand = input("Brand: ")

                new_car = Car(car_colour,
                              car_weight,
                              car_brand)

                # str_new_car = str(new_car).replace('\n', " ")

                VehicleInventory.ALL_VEHICLES.append(new_car)

                main_menu()

            # Plane
            elif choice == "2":

                plane_colour = input("Plane Colour: ")
                plane_weight = int(input("Plane Weight: "))
                plane_brand = input("Brand: ")

                new_plane = Plane(plane_colour,
                                  plane_weight,
                                  plane_brand)

                # str_new_plane = str(new_plane).replace('\n', " ")

                VehicleInventory.ALL_VEHICLES.append(new_plane)

                main_menu()

            # Boat
            elif choice == "3":

                boat_colour = input("Boat Colour: ")
                boat_weight = int(input("Boat Weight: "))
                boat_brand = input("Boat Brand: ")
                boat_motor_type = input("Motor Type: ")

                new_boat = Boat(boat_colour,
                                boat_weight,
                                boat_brand,
                                boat_motor_type)

                # str_new_boat = str(new_boat).replace('\n', " ")

                VehicleInventory.ALL_VEHICLES.append(new_boat)

                main_menu()

        # Remove a Vehicle
        elif self.ans == "2":
            vehicle_to_remove = int(input('Vehicle number to be removed: '))
            index_of_vehicle_to_remove = vehicle_to_remove - 1
            del VehicleInventory.ALL_VEHICLES[index_of_vehicle_to_remove]
            main_menu()

        # Print all Vehicles
        elif self.ans == "3":
            print('\n')
            print("Printing all vehicles...\n")
            for (i, item) in enumerate(VehicleInventory.ALL_VEHICLES, start=1):
                print(i, item)
            main_menu()

        # Exit system
        elif self.ans == "4":
            sys.exit()

        # Handle other inputs
        elif self.ans != "":
            print("\n Not Valid Choice Try again")
            main_menu()


def main_menu():

    menu = Menu()
    menu.print_main_menu()
    menu.handle_input()


if __name__ == "__main__":
    main_menu()
