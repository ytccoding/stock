# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
import time

file_data = "20空"
file_name = "_月線空"
stocktoday = time.strftime("%y_%m_%d")
today = time.strftime("%y_%m_%d_%H_%M_%S")

if not os.path.exists(stocktoday):    #先確認資料夾是否存在
    os.makedirs(stocktoday)

station = os.getcwd()
os.chdir(station + "/" + stocktoday)

if not os.path.exists(stocktoday + file_name):
    os.makedirs(stocktoday + file_name)

if os.path.exists(str(stocktoday) +"_stock_" + file_data + "_data.txt"): #確認當日名單是否生成
    driver = webdriver.Chrome()
    with open(str(stocktoday) +"_stock_" + file_data + "_data.txt") as data:
         for stockdata in data:
            stockdata = stockdata.strip().split(',')
    for a in stockdata:
        if a == stockdata[-1]:
            a = a[2:-2]
        else:
            a = a[2:-1]
        driver.get("http://www.wantgoo.com/stock/" + str(a))
        driver.execute_script("window.scrollTo(0,2352)")
        driver.save_screenshot(stocktoday + file_name + "/" + str(today) + "_" + str(a) + ".png")
        sleep(5)
    driver.close()
else:
    print("Wait for list")
