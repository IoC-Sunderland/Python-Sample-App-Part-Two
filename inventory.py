class VehicleInventory:  # pylint: disable=too-few-public-methods

    ALL_VEHICLES = []

    def __init__(self, new_vehicle):

        VehicleInventory.ALL_VEHICLES.append(new_vehicle)
