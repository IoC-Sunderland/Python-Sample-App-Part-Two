class Vehicle:
    """ A Vehicle Class """

    vehicle_count = 1

    VEHCILE_TYPES = []

    def __init__(self, colour, weight, brand):
        # Attributes that are common across all vehicles
        self.colour = colour
        self.weight = weight
        self.brand = brand
        self.vehicle_number = f'VV{str(Vehicle.vehicle_count)}'
        Vehicle.vehicle_count += 1

    def __str__(self):

        vehicle_description = f"\nVehicle Number: {self.vehicle_number}\n" \
                              f"Colour: {self.colour}\n" \
                              f"Weight: {self.weight}\n" \
                              f"Brand: {self.brand}\n"

        return vehicle_description

    def __repr__(self):

        repr_output = f'{self.__class__.__name__}(' \
                      f'colour="{self.colour}", ' \
                      f'weight="{self.weight}", ' \
                      f'brand="{self.brand}")'

        return repr_output


class Car(Vehicle):
    """ A Car Class """
    pass


class Boat(Vehicle):  # pylint: disable=too-few-public-methods
    """ A Boat Class """

    def __init__(self, colour, weight, brand, motor_type):

        self.motor_type = motor_type
        super().__init__(colour, weight, brand)

    def __str__(self):
        # Needs to include motor_type
        boat_description = f"{super().__str__()}" \
                           f"Motor Type: {self.motor_type}"

        return boat_description

    def __repr__(self):
        # Needs to include motor_type
        boat_repr = super().__repr__()

        return boat_repr

    def get_motor_type(self):
        return self.motor_type


class Plane(Vehicle):  # pylint: disable=too-few-public-methods
    """ A Plane Class """
    pass
