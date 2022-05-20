# improvements for this file:
# decide on list of attrib to print based on class?

import json
import csv

json_file_name = input("Name of json file to open: ")
aci_class = input("ACI parent class in json file: ")

csv_file_name = json_file_name[0:-5] + '.csv'
attributes = attributes.split(",")

with open(json_file_name) as src_file:
    json_data = json.load(src_file)

with open(csv_file_name, "w") as file:
    csv_file = csv.writer(file,lineterminator='\n')
    csv_file.writerow(["name", "descr", "dn"])
    for item in json_data["imdata"]:
        csv_file.writerow([
            item[aci_class]['attributes']['name'],
            item[aci_class]['attributes']['descr'],
            item[aci_class]['attributes']['dn'],
        ])