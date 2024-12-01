import csv
import json


def load_from_csv(csv_file_path):
    with open(csv_file_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        cars_list = [row for row in csv_reader]
    return cars_list


def save_to_json(json_file_path, cars_list):
    with open(json_file_path, mode='w') as json_file:
        json.dump(cars_list, json_file, indent=2)
    return json_file_path


def main():
    cars_list = load_from_csv('../tasks/utils/cars.csv')
    save_to_json('../tasks/utils/cars.json', cars_list)


if __name__ == '__main__':
    main()