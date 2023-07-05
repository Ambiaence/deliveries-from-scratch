from package import Package
import csv
packages = list()
with open('resources/rawpackage.csv', newline='') as f:
    rows = csv.reader(f)
    for data in rows:
        print(data)
        packages.append(Package(fields=data))

for package in packages:
    print(package.id_code)
    print(package.address)
    print(package.city)
    print(package.state)
    print(package.deadline)
    print(package.note)
    if package.note == "hasfriends":
        print(package.friends)
    print("\n\n")
