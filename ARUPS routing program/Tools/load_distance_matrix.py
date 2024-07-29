import csv

def load_distance_matrix(fileName):
    with open(fileName, newline='') as distance_file:
        reader = csv.reader(distance_file)
        locations = next(reader)[1:]  # Skip the first cell and get location names
        distance_matrix = []
        for row in reader:
            distances = list(map(float, row[1:]))  # Skip the first cell and convert distances to float
            distance_matrix.append(distances)
    return locations, distance_matrix