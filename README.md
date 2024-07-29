# ARUPS-Routing-program

Assumptions
•  Each truck can carry a maximum of 16 packages, and the ID number of each package is unique.

•  The trucks travel at an average speed of 18 miles per hour and have an infinite amount of gas with no need to stop.

•  There are no collisions.

•  Three trucks and two drivers are available for deliveries. Each driver stays with the same truck as long as that truck is in service.

•  Drivers leave the hub no earlier than 8:00 a.m., with the truck loaded, and can return to the hub for packages if needed.

•  The delivery and loading times are instantaneous (i.e., no time passes while at a delivery or when moving packages to a truck at the hub). This time is factored into the calculation of the average speed of the trucks.

•  There is up to one special note associated with a package.

•  The delivery address for package #9, Third District Juvenile Court, is wrong and will be corrected at 10:20 a.m. WGUPS is aware that the address is incorrect and will be updated at 10:20 a.m. However, WGUPS does not know the correct address (410 S. State St., Salt Lake City, UT 84111) until 10:20 a.m.

•  The distances provided in the “WGUPS Distance Table” are equal regardless of the direction traveled.

•  The day ends when all 40 packages have been delivered.

:Brief Description: Developed an algorithm and software solution to optimize delivery routes for local deliveries, ensuring all packages are delivered on time while keeping the total distance traveled under 140 miles.
Technologies Used: Python, Data Structures (Hash Tables), Algorithms (Nearest Neighbor Algorithm), datetime library.

•	Efficient Routing: Implemented the Nearest Neighbor Algorithm to calculate the shortest paths between delivery locations, optimizing the routes for three trucks.

•	Constraints Handling: Designed the system to handle specific delivery constraints and requirements, such as unique package criteria and time-sensitive address corrections.

•	Progress Tracking: Included features to monitor the progress of each truck and package delivery in real-time, providing detailed updates based on various package attributes.

•	Outcome: Successfully created a routing solution that ensures all 40 packages are delivered within the constraints, with a total travel distance under 140 miles.

