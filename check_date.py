import json

def compare_holidays(previous_data, current_data):
    added_holidays = [holiday for holiday in current_data if holiday not in previous_data]
    removed_holidays = [holiday for holiday in previous_data if holiday not in current_data]

    return added_holidays, removed_holidays

def load_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

previous_holidays = load_json('previous_holidays.json')
current_holidays = load_json('current_holidays.json')

added_holidays, removed_holidays = compare_holidays(previous_holidays, current_holidays)

print("Added holidays:", added_holidays)
print("Removed holidays:", removed_holidays)
