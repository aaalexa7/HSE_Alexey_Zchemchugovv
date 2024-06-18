"""
Homework #13.1
"""
import json
import sys
from datetime import date

import requests
from bs4 import BeautifulSoup


class ParserCBRF:
    format_date = '%d.%m.%Y'
    today = date.today().strftime("%d.%m.%Y")
    link = f"https://www.cbr.ru/hd_base/KeyRate/?" \
           f"UniDbQuery.Posted=True&" \
           f"UniDbQuery.From=17.09.2013&" \
           f"UniDbQuery.To={today}"

    def __parse_html(self, response):
        try:
            soup = BeautifulSoup(response.text, 'html.parser')

            rate_dict = {}
            rows = soup.find('table', class_='data').find_all('tr')

            for row in rows:
                cells = row.find_all('td')

                if not cells:
                    continue

                key = cells[0].text
                value = float(cells[1].text.replace(',', '.')) if len(cells) > 1 else None

                if value is not None:
                    rate_dict[key] = value

            return rate_dict
        except AttributeError:
            sys.exit()

    def __get_response(self):
        response = requests.get(self.link)
        return self.__parse_html(response)

    def __save(self, data):
        filename = f"parsed data {self.today}"
        with open(filename, 'w') as json_file:
            json.dump(data, json_file)

    def start(self):
        data = self.__get_response()
        self.__save(data)


if __name__ == '__main__':
    ParserCBRF().start()
