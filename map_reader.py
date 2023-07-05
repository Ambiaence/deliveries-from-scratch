import csv
from location import LocationGraph 

graph = LocationGraph()

packages = list()
with open('resources/rawdistance.csv', newline='') as f:
    rows = csv.reader(f)
    locations = list()
    for row in rows:
        locations.append(row[0])
        graph.add_location(row[0])
        for index in range(1, len(row[1:])):
            if row[index] == "0.0":
                break
            horizantal_location = locations[index-1]
            vertical_location = row[0]  
            graph.set_travel_time(horizantal_location, vertical_location, row[index])
            
        #graph.add_location(rows[i][0])


for columns in graph.travel_times:
    row_values = ""
    for cell in columns:
        row_values = row_values + "["+str(cell)+"] "
    
    print(row_values)
