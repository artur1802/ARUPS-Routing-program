import csv
from Classes.Package import Package
from Classes.HashTable import HashTable


import csv
from Classes.Package import Package
from Classes.HashTable import HashTable

class FileReader:

    def __init__(self, file_name):
        self.file_name = file_name  # Initialize with the file name
        self.row_count = 0  # Initialize row count to zero

    def load_distance_matrix(self):
        # Function to load distance matrix from CSV file
        with open(self.file_name, newline='') as distance_file:
            reader = csv.reader(distance_file)
            locations = next(reader)[1:]  # Skip the first cell and get location names
            distance_matrix = []
            for row in reader:
                distances = list(map(float, row[1:]))  # Skip the first cell and convert distances to float
                distance_matrix.append(distances)
        return locations, distance_matrix  # Return locations and distance matrix

    def load_package_data(self):
        # Function to load package data from CSV into a hash table
        hash_table = HashTable(40)  # Create a hash table instance with size 40

        with open(self.file_name) as packages_data:
            data = csv.reader(packages_data, delimiter=',')  # Read CSV data

            for row in data:
                # Extract data from each row
                package_id = row[0]
                address = row[1]
                city = row[2]
                state = row[3]
                zip_code = row[4]
                delivery_time = row[5]
                weight = row[6]
                notes = row[7]

                # Create a Package object with extracted data
                package = Package(package_id, address, city, state, zip_code, delivery_time, weight, notes)

                # Insert package into the hash table using package_id as key
                hash_table.hash_insert(package_id, package)
                # Uncomment the line below for debugging or confirmation
                # print(f"Inserted package {package_id} into hash table.")

        # Print hash table contents for confirmation
        print("Hash table contents:")
        hash_table.print_all()

        return hash_table  # Return the populated hash table

    def get_row_count(self):
        # Function to count the number of rows in the file
        with open(self.file_name, 'r') as file:
            for line in file:
                self.row_count += 1
        return self.row_count  # Return the total row count
