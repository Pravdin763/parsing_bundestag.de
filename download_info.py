import json
import csv



def json_file(d):
    with open('info_person.json', 'w', encoding='utf-8') as file:
        json.dump(d, file, indent=4, ensure_ascii=False)

def csv_file(d):
    with open('info_person1.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['name', 'post', 'images', 'url_card', 'social_media'])
        for key, value in d.items():
            writer.writerow([key]+[*value.values()])


