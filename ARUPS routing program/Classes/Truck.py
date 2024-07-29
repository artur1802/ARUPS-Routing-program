from datetime import time
from Classes.Package import Package


class Truck:
    def __init__(self, id, start_time, capacity=16):
        # Initialize truck attributes
        self.id = id
        self.capacity = capacity  # Maximum capacity of the truck
        self.packages = []  # List to store packages loaded on the truck
        self.start_time = start_time  # Start time of the truck's delivery route
        self.en_route_time = None  # Time when the truck started its delivery

    # Method to load a package onto the truck
    def load_package(self, package):
        if len(self.packages) < self.capacity: # Check if the truck has available capacity
            package.truck_id = self.id
            self.packages.append(package)  # Add package to the truck's load
            return True  # Indicate successful loading
        return False  # Indicate that the truck is full

    # Method to start delivery and update the status of all loaded packages
    def start_delivery(self, current_time):
        self.en_route_time = current_time  # Set the en route time for the truck
        for package in self.packages:
            package.en_route_time = current_time  # Set the en route time for each package
            package.update_status("En Route", current_time)

    # Method to deliver a package and update its delivery time
    def deliver_package(self, package, delivery_time):
        package.update_status("Delivered", delivery_time)  # Update the status of the package
        package.delivery_time = delivery_time  # Set the delivery time for the package

    # Method to check if the truck is full
    def is_full(self):
        return len(self.packages) >= self.capacity

    # String representation of the truck object
    def __str__(self):
        return f"Truck {self.id}: " + ', '.join(str(pkg.id) for pkg in self.packages)
