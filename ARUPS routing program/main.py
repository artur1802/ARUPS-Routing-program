import csv
from Tools.FileReader import FileReader
from Tools.algorithm import Algorithm
from Tools.load_distance_matrix import load_distance_matrix
from Tools.print_trucks_content import print_truck_contents
from Tools.LoadTruck import LoadTruck
from Classes.Truck import Truck
from Classes.Package import Package
from Classes.HashTable import HashTable
from datetime import time
from Tools.package_status import show_package_status, show_all_package_status
from Tools.show_mileage import show_total_mileage

# *** STUDENT INFORMATION ***
# *** ID: 011395683
# *** First Name: Arturo
# *** Last Name: Rincon

# Load package data from CSV file
file_reader = FileReader('CSV/WGUPSPackageFile.csv')
data = file_reader.load_package_data()

# Instantiate LoadTruck object with loaded package data
load_truck = LoadTruck(data)

# Assign packages to trucks based on priority and other constraints
trucks = load_truck.assign_packages_to_trucks()

# Print the contents of each truck for verification
print_truck_contents(trucks)

#Load distance matrix from CSV file, which includes locations and distances between them
locations, distance_matrix = load_distance_matrix('CSV/WGUPS Distance Table.csv')
total = 0 # Initialize total distance traveled by all trucks

# Create an instance of the Algorithm class to calculate routes
algorithm = Algorithm()

# Calculate paths and total distances for each truck using the nearest neighbor algorithm
for truck in trucks:
    path, total_distance = algorithm.nearest_neighbor_algorithm(truck, distance_matrix)
    print(f"Truck {truck.id} Total Distance:", total_distance)
    # Display the delivery time of the last package (path[-2] represents the last package delivered
    print(f"The last package of Truck {truck.id} was delivered at : {truck.packages[path[-2]].get_delivery_time()}")

    #total distance traveled by all trucks
    total += total_distance


all_packages = algorithm.get_all_packages()
all_packages.sort(key=lambda p: int(p.id))


# User interaction loop for the packages
while True:
    print("\n--- Package and Truck Management System ---")
    print("1. View Package Status at a Specific Time")
    print("2. View Total Mileage Traveled")
    print("3. View all Packages Status at a Specific Time")
    print("4. Exit")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        try:
            package_id = int(input("Enter Package ID to view status: "))
        except ValueError:
            print("Invalid Package ID. Please enter a numeric ID.")
            continue

        query_time_str = input("Enter the time (HH:MM): ")
        try:
            query_hour, query_minute = map(int, query_time_str.split(':'))
            show_package_status(all_packages,package_id, query_hour, query_minute)
        except ValueError:
            print("Invalid time format. Please enter time as HH:MM.")
    elif choice == '2':
        show_total_mileage(total)
    elif choice == '3':
        query_time_str = input("Enter the time (HH:MM): ")
        try:
            query_hour, query_minute = map(int, query_time_str.split(':'))
            show_all_package_status(all_packages, query_hour, query_minute)
        except ValueError:
            print("Invalid time format. Please enter time as HH:MM.")
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3 or 4.")