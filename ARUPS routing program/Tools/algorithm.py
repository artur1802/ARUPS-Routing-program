from datetime import timedelta, time, datetime
from Classes.Truck import Truck


class Algorithm:
    def __init__(self):
        self.all_packages = []  # List to store all delivered packages

    # Nearest Neighbor Algorithm to find the shortest path for the truck
    def nearest_neighbor_algorithm(self, truck, distance_matrix, start_index=-1):
        packages = truck.packages  # Get packages assigned to the truck
        num_locations = len(packages) + 1  # Number of locations (packages + start point)
        visited = [False] * num_locations  # Track visited locations
        path = [start_index]  # Initialize path with the starting index
        total_distance = 0  # Initialize total distance traveled
        visited[start_index] = True  # Mark the start location as visited

        current_index = start_index  # Start from the initial location
        current_time = truck.start_time  # Initialize current time with the truck's start time

        # Loop to visit all locations
        for _ in range(num_locations - 1):
            nearest_distance = float('inf')  # Initialize nearest distance to infinity
            nearest_index = -1  # Initialize nearest index

            # Find the nearest unvisited location
            for i in range(num_locations):
                if not visited[i] and 0 < distance_matrix[current_index][i] < nearest_distance:
                    nearest_distance = distance_matrix[current_index][i]
                    nearest_index = i

            # Update path, total distance, and current index
            path.append(nearest_index)
            visited[nearest_index] = True  # Mark the nearest location as visited
            total_distance += nearest_distance  # Add the distance to the total distance
            current_index = nearest_index  # Update current index to the nearest location

            # Calculate travel time to the nearest location
            travel_time = timedelta(hours=nearest_distance / 18)  # Assuming an average speed of 18 miles/hour
            new_time = (datetime.combine(datetime.today(), current_time) + travel_time).time()  # Calculate new time
            current_time = new_time  # Update current time

            # Deliver the package at the nearest location
            package = packages[nearest_index]
            truck.deliver_package(package, current_time)

            # Store the delivered package
            self.all_packages.append(package)

        # Return to the start point and update total distance
        total_distance += distance_matrix[current_index][start_index]
        path.append(start_index)  # Append start index to the path to complete the loop

        return path, total_distance  # Return the path and total distance

    # Function to get all delivered packages
    def get_all_packages(self):
        return self.all_packages