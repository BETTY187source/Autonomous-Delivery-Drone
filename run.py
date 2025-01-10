from drone.controller import DroneController

if __name__ == '__main__':
    drone = DroneController(start_location=(0, 0), end_location=(3, 3))
    drone.navigate()
