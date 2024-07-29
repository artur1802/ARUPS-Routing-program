from datetime import time


# Function to show package status at a specific time
def show_package_status(all_packages, package_id, query_hour, query_minute):
    query_time = time(query_hour, query_minute)
    package9_updated = time(10,20)
    if(query_time <package9_updated):
        package9 = all_packages[8]
        package9.set_address("300 State St")
        package9.set_package_zip("84103")

    else:
        package9 = all_packages[8]
        package9.set_address("410 S. State St")
        package9.set_package_zip("84111")

    package_found = False
    for package in all_packages:
        if package.id == str(package_id):
            package_found = True
            if query_time < package.en_route_time:
                package.status = f'At Hub in Truck {package.truck_id}'
                print(f"ID: {package.id}, Address: {package.address}, City: {package.city}, "
                      f"State: {package.state}, Zip: {package.zip}, Deadline: {package.delivery_deadline}, "
                      f"Weight: {package.weight}, Notes: {package.notes}, Status: {package.status} ")

            elif query_time < package.delivery_time:
                package.status = f'On Route in Truck {package.truck_id}'
                print(f"ID: {package.id}, Address: {package.address}, City: {package.city}, "
                      f"State: {package.state}, Zip: {package.zip}, Deadline: {package.delivery_deadline}, "
                      f"Weight: {package.weight}, Notes: {package.notes}, Status: {package.status}, "
                      f"Expected Delivery Time: {package.delivery_time.strftime('%H:%M:%S')}")
            else:
                package.status = f'Delivered by Truck {package.truck_id}'
                print(f"ID: {package.id}, Address: {package.address}, City: {package.city}, "
                      f"State: {package.state}, Zip: {package.zip}, Deadline: {package.delivery_deadline}, "
                      f"Weight: {package.weight}, Notes: {package.notes}, Status: {package.status}, "
                      f"Delivery Time: {package.delivery_time.strftime('%H:%M:%S')}")

    if not package_found:
        print(f"Package with ID {package_id} not found.")


# Function to show all package status at a specific time
def show_all_package_status(all_packages, query_hour, query_minute):
    query_time = time(query_hour, query_minute)
    package9_updated = time(10,20)

    if(query_time <package9_updated):
        package9 = all_packages[8]
        package9.set_address("300 State St")
        package9.set_package_zip("84103")

    else:
        package9 = all_packages[8]
        package9.set_address("410 S. State St")
        package9.set_package_zip("84111")


    for package in all_packages:
        if query_time < package.en_route_time:
            package.status = f'At Hub in Truck {package.truck_id}'
            print(f"ID: {package.id}, Address: {package.address}, City: {package.city}, "
                  f"State: {package.state}, Zip: {package.zip}, Deadline: {package.delivery_deadline},"
                  f"Weight: {package.weight}, Notes: {package.notes}, Status: {package.status} ")

        elif query_time < package.delivery_time:
            package.status = f'On Route in Truck {package.truck_id}'
            print(f"ID: {package.id}, Address: {package.address}, City: {package.city}, "
                  f"State: {package.state}, Zip: {package.zip}, Deadline: {package.delivery_deadline}, "
                  f"Weight: {package.weight}, Notes: {package.notes}, Status: {package.status}, "
                  f"Expected Delivery Time: {package.delivery_time.strftime('%H:%M:%S')}")
        else:
            package.status = f'Delivered by Truck {package.truck_id}'
            print(f"ID: {package.id}, Address: {package.address}, City: {package.city}, "
                  f"State: {package.state}, Zip: {package.zip}, Deadline: {package.delivery_deadline}, "
                  f"Weight: {package.weight}, Notes: {package.notes}, Status: {package.status}, "
                  f"Delivery Time: {package.delivery_time.strftime('%H:%M:%S')}")