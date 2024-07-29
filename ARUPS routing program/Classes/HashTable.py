class HashTable:
    def __init__(self, size=40):
        self.size = size  # Size of the hash table
        self.buckets = []  # List to hold the buckets
        for _ in range(self.size):
            self.buckets.append([])  # Initialize each bucket as an empty list

    # Hash function to determine the bucket index based on the remainder
    def hash_remainder(self, key):
        return int(key) % self.size

    # Function to insert an item into the hash table
    def hash_insert(self, id, item):
        if self.hash_search(id) is None:  # Check if the item already exists
            index = self.hash_remainder(id)  # Get the bucket index
            self.buckets[index].append(item)  # Insert the item into the appropriate bucket

    # Function to search for an item in the hash table
    def hash_search(self, key):
        index = self.hash_remainder(key)  # Get the bucket index
        bucket = self.buckets[index]  # Get the bucket
        for item in bucket:  # Iterate through the items in the bucket
            if item.id == str(key):  # Check if the item's id matches the key
                return item  # Return the item if found
        return None  # Return None if the item is not found

    # Function to remove an item from the hash table
    def hash_remove(self, item):
        index = self.hash_remainder(item.id)  # Get the bucket index
        bucket = self.buckets[index]  # Get the bucket

        for i, existing_item in enumerate(bucket):  # Iterate through the items in the bucket
            if existing_item.id == item.id:  # Check if the item's id matches the item's id to be removed
                bucket.pop(i)  # Remove the item from the bucket
                return

    # Function to print all items in the hash table
    def print_all(self):
        for bucket in self.buckets:  # Iterate through each bucket
            for item in bucket:  # Iterate through each item in the bucket
                print(item)  # Print the item

    # Function to lookup package information based on package ID
    def lookup_package_info(self, package_id):
        package = self.hash_search(package_id)
        if package:
            return {
                'delivery_address': package.address,
                'delivery_deadline': package.delivery_deadline,
                'delivery_city': package.city,
                'delivery_zip_code': package.zip,
                'package_weight': package.weight,
                'delivery_status': package.status,
                'delivery_time': package.delivery_time
            }  # Return package information
        else:
            return None  # Return None if the package is not found
