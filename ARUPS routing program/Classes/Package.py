from datetime import time


class Package:
    def __init__(self, package_id, address, city, state, package_zip, delivery_deadline, weight, notes):
        # Initialize package attributes
        self.id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip = package_zip
        self.delivery_deadline = delivery_deadline
        self.weight = weight
        self.notes = notes
        self.status = 'At Hub'
        self.delivery_time = None  # Time when the package was delivered
        self.en_route_time = None  # Time when the package was en route
        self.priority = 0  # Priority based on delivery deadline
        self.truck_id = None

    # Method to set the package as delivered and record the delivery time
    def deliver(self, delivery_time):
        self.status = "Delivered"
        self.delivery_time = delivery_time

    # Method to update the status of the package
    def update_status(self, status, current_time=None):
        self.status = status  # Update the status
        if status == "Delivered":
            self.delivery_time = current_time  # Set delivery time if delivered
        elif status == "En Route":
            self.en_route_time = current_time  # Set en route time if en route

    # Method to get the status of the package at a specific query time
    def get_status(self, query_time):
        if self.delivery_time and query_time == self.delivery_time:
            return f"Delivered at {self.delivery_time.strftime('%H:%M:%S')}"
        elif self.status == "En Route" and query_time >= self.en_route_time:
            return f"En Route since {self.en_route_time.strftime('%H:%M:%S')}"
        return self.status  # Return the current status if not delivered or en route

    # Method to get the delivery time of the package
    def get_delivery_time(self):
        return self.delivery_time

    def set_address(self,new_address):
        self.address = new_address

    def set_package_zip(self, new_zip):
        self.zip = new_zip


    def __str__(self):
        return "%s, %s ,%s ,%s ,%s, %s ,%s ,%s, %s, %s, %s" % (
            self.id, self.address, self.city, self.state, self.zip,
            self.delivery_deadline, self.weight, self.notes,
            self.status, self.delivery_time, self.priority
        )
