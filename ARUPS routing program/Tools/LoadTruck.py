from Classes.Truck import Truck
from datetime import time

class LoadTruck:
    def __init__(self, hash_table):
        self.low_priority_packages = []
        self.medium_priority_packages = []
        self.high_priority_packages = []

        for key in range(1, 41):
            package = hash_table.hash_search(key)
            if package:
                if '9:00' in package.delivery_deadline or 'Must be delivered with' in package.notes:
                    package.priority = 1
                    self.high_priority_packages.append(package)
                elif '10:30' in package.delivery_deadline or 'on truck 2' in package.notes:
                    package.priority = 2
                    self.medium_priority_packages.append(package)
                else:
                    package.priority = 3
                    self.low_priority_packages.append(package)

    def assign_packages_to_trucks(self):
        trucks = [
            Truck(1, time(8, 0)),
            Truck(2, time(9, 5)),
            Truck(3, time(10, 30))
        ]

        # Load Truck 1 with high priority packages
        while self.high_priority_packages and not trucks[0].is_full():
            trucks[0].load_package(self.high_priority_packages.pop(0))

        # Load Truck 2 with medium priority packages
        while self.medium_priority_packages and not trucks[1].is_full():
            trucks[1].load_package(self.medium_priority_packages.pop(0))

        # Load Truck 3 with low priority packages
        while self.low_priority_packages and not trucks[2].is_full():
            trucks[2].load_package(self.low_priority_packages.pop(0))

        # Fill Truck 1 and Truck 2 with remaining low priority packages if they have space
        for truck in trucks[:2]:  # Only Truck 1 and Truck 2
            while self.low_priority_packages and not truck.is_full():
                truck.load_package(self.low_priority_packages.pop(0))

        # Start deliveries for all trucks
        for truck in trucks:
            truck.start_delivery(truck.start_time)

        # for truck in trucks:
        #     print(f"Truck {truck.id} loaded with packages: {[package.id for package in truck.packages]}")

        return trucks