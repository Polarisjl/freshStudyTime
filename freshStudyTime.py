#coding=utf-8
#!/usr/bin/python3

import requests
import configparser
import threading

config = configparser.ConfigParser()
config.read("config.txt")

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0",
    "Cookie": config.get('header', 'Cookie'),
    "Referer": config.get('header', 'Referer'),
    "videoTimeTotalLong": "0"
}
data = {
    "courseId": config.get('data', 'courseId'),
    "moduleIds": config.get('data', 'moduleIds'),
    "cellId": config.get('data', 'cellId'),
    "auvideoLength": "0"
}

url = "https://aq.fhmooc.com/api/design/LearnCourse/statStuProcessCellLogAndTimeLong"


def freshStudyTimeThread():
    for i in range(1, 300):
        res = requests.post(url, headers=header, data=data)
        if "\"code\":1" in res.text:
            print(threading.current_thread().name + " time:" + str(i) + " ok")
        else:
            print(threading.current_thread().name + " time:" + str(i) + " ERROR")


def main():
    # written by Polarisjl 2021.12.15
    t0 = threading.Thread(target=freshStudyTimeThread, name='Thread0')
    t1 = threading.Thread(target=freshStudyTimeThread, name='Thread1')
    t2 = threading.Thread(target=freshStudyTimeThread, name='Thread2')
    t0.start()
    t1.start()
    t2.start()

if __name__ == '__main__':
    main()