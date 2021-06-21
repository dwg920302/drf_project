import pandas as pd
import json
from rest_framework.common.abstracts import PrinterBase, ReaderBase, ScraperBase
import googlemaps
from selenium import webdriver


class Printer(PrinterBase):
    @staticmethod
    def dframe(this):
        meter = 3
        print('*' * 100)
        print(f'(1) Target Type = {type(this)}')
        print(f'(2) Target Column = {this.columns}')
        print(f'(3) Target의 상위 {meter}개 행 = {this.head(meter)}')
        print(f'(4) Target의 null 갯수 = {this.isnull().sum()}')
        print('*' * 100)


class Reader(ReaderBase):

    def from_csv(self, file) -> object:
        return pd.DataFrame(pd.read_csv(f'{self.new_file(file)}.csv', encoding='UTF-8', thousands=','))

    def from_xls(self, file, header, usecols) -> object:
        return pd.read_excel(f'{self.new_file(file)}.xls', header=header, usecols=usecols).dropna()

    def from_json(self, file) -> object:
        return json.load(open(f'{self.new_file(file)}.json', encoding='UTF-8'))

    @staticmethod
    def new_file(file) -> str:
        return file.context + file.fname

    def gmaps(self) -> object:
        return googlemaps.Client('')


class Scraper(ScraperBase):
    def driver(self) -> object:
        return webdriver.Chrome('C://Program Files/Google/Chrome/chromedriver.exe')
        # driver.get(URL)로 사용

    def auto_login(self):
        pass

    def scrap_it(self):
        pass
