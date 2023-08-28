import pandas as pd
import time
import requests
import io
from selenium import webdriver
from selenium.webdriver.common.by import By
from flask import Flask
from sqlalchemy import Boolean, Column, Date, DateTime, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from datetime import datetime

# 創建引擎和會話 ",encoding=utf-8
# engine = create_engine("mysql+pymysql://amy:test@file.fans98.com:3306/cex",encoding=utf8)
engine = create_engine("mysql+pymysql://amy:test@file.fans98.com:3306/cex?charset=utf-8")
Session = sessionmaker(bind=engine)
session = Session()

# 創建基礎模型
Base = declarative_base()

class TwHolidayRecords(Base):
    __tablename__ = "tw_holiday_records"

    id = Column(INTEGER(unsigned=True), primary_key=True)
    _subject = Column("subject", String(200), default="一般假日")
    _date = Column("date", Date, nullable=False)
    is_all_day = Column(Boolean, default=1)
    is_active = Column(Boolean, default=1)

    created_time = Column(DateTime, default=datetime.now)
    updated_time = Column(DateTime, onupdate=datetime.now, default=datetime.now)

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        try:
            decoded_value = value.encode("utf-8").decode("unicode_escape")
            self._subject = decoded_value
        except ValueError:
            raise ValueError("Error decoding and setting subject")

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date_str):
        try:
            date_obj = datetime.strptime(date_str, "%Y%m%d")
            self._date = date_obj.date()
        except ValueError:
            raise ValueError("Invalid date input")

app = Flask(__name__)

@app.route('/')
def scrape_website():
    driver = webdriver.Chrome()
    driver.maximize_window()

    url = "https://data.gov.tw/dataset/14718"
    driver.get(url)
    time.sleep(5)

    xpath = '//*[@id="app"]/main/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[11]/div[1]/a'
    link_element = driver.find_element(By.XPATH, xpath)
    download_link = link_element.get_attribute("href")

    driver.quit()

    response = requests.get(download_link, verify=False)
    if response.status_code == 200:
        file_content = response.text
        download_data = pd.read_csv(io.StringIO(file_content))
        print("success")

        for item in download_data.to_dict(orient="records"):
            if pd.notna(item["備註"]):
                new_record = TwHolidayRecords()
                new_record.subject = item["備註"]
                new_record.date = str(item["西元日期"]) 
                new_record.is_all_day = 1
                new_record.is_active = 1

                session.add(new_record)

        session.commit()
        print("Data inserted into database")
    else:
        print("failure")

    return "Done!"

if __name__ == '__main__':
    app.run(debug=True)








#source myenv/bin/activate
