
def create_vehicle(id, brand):
    animal = {
        'id': id,
        'brand': brand
        }
    return animal

def create_car(id, brand):
    car = create_vehicle(id, brand)
    return car

def create_truck(name, brand, number_of_wheels):
    truck = create_vehicle(id, brand)
    truck['number_of_wheels'] = number_of_wheels
    return truck

def create_air_plane(id, brand, number_of_motors):
    air_plane = create_vehicle(id, brand)
    air_plane['number_of_motors'] = number_of_motors
    return air_plane
