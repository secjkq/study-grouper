import pandas as pd
from geopy.distance import geodesic
import googlemaps
from itertools import combinations

# Load the data from the Excel sheet
data = pd.read_excel('Class-group-coding.xlsx')

# Filter students with "Digital Native" IT experience
native_students = data[data['IT Experience'] == 'Digital Native']

# Initialize Google Maps API client
gmaps = googlemaps.Client(key='AI************BAE') #INSERT YOUR API KEY HERE

# Function to calculate distance between two locations
def calculate_distance(location1, location2):
    coords1 = gmaps.geocode(location1)[0]['geometry']['location']
    coords2 = gmaps.geocode(location2)[0]['geometry']['location']
    return geodesic(coords1, coords2).kilometers

# Create mini-groups
mini_groups = []
remaining_students = native_students.copy()

while len(remaining_students) > 0:
    group = []
    # Select a random student from the remaining students
    student = remaining_students.sample(1).iloc[0]
    group.append(student)
    remaining_students = remaining_students.drop(student.index)

    # Find students within 12 km of the first student
    for _, row in remaining_students.iterrows():
        if calculate_distance(student['Location'], row['Location']) <= 12:
            group.append(row)

    # Ensure there are at least two "Digital Native" students in the group
    if len([s for s in group if s['IT Experience'] == 'Digital Native']) >= 2:
        mini_groups.append(group)

# Write the results to a text file
with open('mini_groups.txt', 'w') as f:
    for i, group in enumerate(mini_groups):
        f.write(f"Mini-Group {i + 1}:\n")
        for student in group:
            f.write(f"{student['Surname']}, {student['Location']}, {student['IT Experience']}\n")
        f.write("\n")
