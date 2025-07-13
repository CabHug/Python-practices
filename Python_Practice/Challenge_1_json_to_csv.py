import csv
import json

# Define new .json file
def csv_to_json():
    json_file = 'flowers.json'
    with open('flowers.csv', mode='r') as file:
        flowers = csv.DictReader(file)

        f_list = []
        for flower in flowers:
            print(flower)
            f_list.append(flower)

        with open(json_file, mode='w') as newFile:
            json.dump(f_list, newFile, indent=4)

def json_to_csv():
    csv_file = 'new_csv_file.csv'
    with open('flowers.json', mode='r') as file:
        flowers = json.load(file)

        print(flowers[0].keys())
        fieldnames = flowers[0].keys()
        with open(csv_file, mode='w', newline='') as file:
            csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
            csv_writer.writeheader()

            for row in flowers:
                print(str(list(row.values())))
                csv_writer.writerow(row)



    

#csv_to_json()
json_to_csv()