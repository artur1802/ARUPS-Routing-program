def print_truck_contents(trucks):
    for truck in trucks:
        print(f"Truck {truck.id} contains the following packages:")
        for package in truck.packages:
            print(f" ID: {package.id}, Address: {package.address}, City: {package.city}, "
                  f"State: {package.state}, Zip: {package.zip}, Deadline: {package.delivery_deadline}, "
                  f"Weight: {package.weight}, Notes: {package.notes}")
        print("\n")