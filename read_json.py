import json


def read_json():
    with open("app_information.json", "a+") as file:
        try:
            file.seek(0)
            take_from_file = json.load(file)
        except:
            return app_information
    return take_from_file


def save_on_close(program_data):
    with open('app_information.json', 'w') as data:
        json.dump(program_data, data, indent=2)


app_information = {
    "distributors": {},
    "products": {}
}