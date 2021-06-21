import pandas as pd
import numpy as np
import folium
from selenium import webdriver
from rest_framework.common.services import Printer, Reader, Scraper
from rest_framework.common.entity import FileDTO
from glob import glob
import re

'''
문제 정의
셀프 주유소는 정말 저렴할까?
4-1 Selenium 사용하기
4-2 서울시 구별 주유소 가격 정보 얻어오기
4-5 구별 주유 가격에 대한 데이터 정리
4-6 서울시 주유 가격 상/하위 10개 주유소 지도에 표기하기
'''

'''
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   지역      537 non-null    object
 1   상호      537 non-null    object
 2   주소      537 non-null    object
 3   상표      537 non-null    object
 4   전화번호    537 non-null    object
 5   셀프여부    537 non-null    object
 6   고급휘발유   537 non-null    object
 7   휘발유     537 non-null    object
 8   경유      537 non-null    object
 9   실내등유    537 non-null    object
dtypes: object(10)
memory usage: 46.1+ KB
----------------------------------------------------------------------------------------------------
      지역      상호                     주소      상표  ... 고급휘발유   휘발유    경유 실내등유
0  서울특별시  오렌지주유소   서울 강동구 성안로 102 (성내동)   SK에너지  ...     -  1554  1354  997
1  서울특별시  구천면주유소  서울 강동구 구천면로 357 (암사동)  현대오일뱅크  ...     -  1556  1355    -

[2 rows x 10 columns]
       지역       상호                     주소     상표  ... 고급휘발유   휘발유    경유  실내등유
44  서울특별시    오천주유소  서울 강남구 봉은사로 503 (삼성동)  SK에너지  ...  2293  2107  1909  1232
45  서울특별시  뉴서울(강남)   서울 강남구 언주로 716 (논현동)  SK에너지  ...  2420  2120  1920  1330

[2 rows x 10 columns]

Process finished with exit code 0

'''


class GasService:
    def __init__(self):
        self.file = FileDTO()
        self.printer = Printer()
        self.reader = Reader()
        self.scraper = Scraper()

    def get_url(self):
        file = self.file
        reader = self.reader
        printer = self.printer
        scraper = self.scraper
        file.url = 'https://www.opinet.co.kr/searRgSelect.do'
        driver = scraper.driver()
        print(driver.get(file.url))
        '''
        gu_list_raw = driver.find_element_by_xpath("""//*[@id="SIGUNGU_NM0"]""")
        gu_list = gu_list_raw.find_elements_by_tag_name("option")
        gu_names = [option.getattribute("value") for option in gu_list]
        gu_names.remove('')
        print(gu_names)
        '''

    def gas_station_price_info(self):
        reader = self.reader
        # print(glob('./data/지역_위치별(주유소)*xls'))
        station_files = glob('./data/지역_위치별(주유소)*xls')
        tmp_raw = []
        for file in station_files:
            tmp_raw.append(pd.read_excel(file, header=2))
        station_raw = pd.concat(tmp_raw)
        '''
        print('-'*100)
        print(station_raw.head(2))
        print(station_raw.tail(2))
        '''
        station_raw.info()

        stations = pd.DataFrame({'Oil_store': station_raw['상호'],
                                 'Address': station_raw['주소'],
                                 'Price': station_raw['휘발유'],
                                 'Self': station_raw['셀프여부'],
                                 'Trademark': station_raw['상표']})
        # print(stations.head())
        stations['구'] = [i.split()[1] for i in stations['Address']]
        stations['구'].unique()

        stations = stations[stations['Price'] != '-']
        stations['Price'] = [float(i) for i in stations['Price']]
        stations.reset_index(inplace=True)
        del stations['index']
        print(stations.columns)
        print(f'{stations.head(2)}\n{stations.tail(2)}')


if __name__ == '__main__':
    s = GasService()
    s.get_url()
    s.gas_station_price_info()
