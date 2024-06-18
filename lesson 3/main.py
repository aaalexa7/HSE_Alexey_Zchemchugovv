"""
Homework #5
"""
import json
import csv
import re
from ics import Calendar
from datetime import datetime, timedelta
import zoneinfo

zone = zoneinfo.ZoneInfo("Europe/Moscow")
email_pattern = re.compile(r'\b[0-9a-zA-Z.-_]+@[0-9a-zA-Z.-_]+\.[a-zA-Z]+\b')
inn_org_pattern = re.compile(r'\b\d{10}\b')
inn_person_pattern = re.compile(r'\b\d{12}\b')


def parse_into_csv():
    with open("traders.txt", "r") as file:
        inn_data = [i.rstrip() for i in file.readlines()]
    with open("traders.json", "r") as file:
        trader_data_array = json.load(file)
    traders = []
    for trader in trader_data_array:
        if trader['inn'] in inn_data:
            traders.append(trader)
    with open('traders.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['INN', 'OGRN', 'ADDRESS'])
        for i in traders:
            writer.writerow([i['inn'], i['ogrn'], i['address']])


def find_email_addresses():
    with open("1000_efrsb_messages.json", "r") as file:
        bankrupt_data = json.load(file)
    results = {}
    for row in bankrupt_data:
        email_data_array = re.findall(email_pattern, row['msg_text'])
        for email in email_data_array:
            email = email.lower()
            found = results.get(row['publisher_inn'])
            if found and email not in found:
                results[row['publisher_inn']].append(email)
            elif not found:
                new_item = {row['publisher_inn']: [email]}
                results.update(new_item)

    with open('email_data_array.json', "w") as file:
        json.dump(results, file)


if __name__ == '__main__':
    parse_into_csv()
    find_email_addresses()

