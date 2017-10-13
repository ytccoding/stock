# -- coding: utf-8 --
import twstock
import os
import time
import _thread
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

stock_5_all = []#儲存接近五日線之上全部
stock_10_all = []
stock_20_all = []
stock_60_all = []
stock_5_allS = []
stock_10_allS = []
stock_20_allS = []
stock_60_allS = []
today = time.strftime("%y_%m_%d")

def saveuse(a,b): #存檔用
    with open(today + "/" + str(today) + "_"  + a,"w") as stock_save:
        print(b , file = stock_save)

if not os.path.exists(today):    #先確認資料夾是否存在
    os.makedirs(today)
    
if os.path.exists('stock0927' + '.txt'): #確認股票期貨名單是否存在
    with open('stock0927' + '.txt') as data:
        stockdata = data.readline()
        stocknumber = stockdata.strip().split(',')
    stocknumber.sort()
else:
    print("stock list lost")

try:
    for j in stocknumber: #名單內都查詢一遍
        stock = twstock.Stock(str(j))
        stock.fetch_from(2017, 5) #從2017/05開始收資料
        stock_60 = stock_20 = stock_10 = stock_5 = 0
        k = 60

        for i in stock.price[-60:]:
            stock_60 = stock_60 + i
            if k <= 20:
              stock_20 = stock_20 + i
            if k <= 10:
              stock_10 = stock_10 + i
            if k <= 5:
              stock_5 = stock_5 + i
            k = k - 1
                  
        stock_60 = stock_60 / 60 #季線
        stock_20 = stock_20 / 20 #月線
        stock_10 = stock_10 / 10 #十日線
        stock_5 = stock_5 / 5 #五日線
        
        #print(str(j) + "今日收盤" +str(stock.price[-1]))
        #print(str(j) + "五日線" + str(stock_5))
        #print(str(j) + "十日線" + str(stock_10))
        #print(str(j) + "月線" + str(stock_20))
        #print(str(j) + "季線" + str(stock_60))

        if stock.price[-1] / stock_5 < 1.1 and stock.price[-1]  >= stock_5 >= stock_10 >= stock_20 >= stock_60:
            #print("近五日線")
            stock_5_all.append(j)
        elif stock.price[-1] / stock_10 <= 1.1 and stock.price[-1]  >= stock_10 >= stock_20 >= stock_60:
            #print("近十日線")
            stock_10_all.append(j)
        elif stock.price[-1] / stock_20 <= 1.1 and stock.price[-1]  >= stock_20 >= stock_60:
            #print("近月線")
            stock_20_all.append(j)
        elif stock.price[-1] / stock_60 <= 1.1 and stock.price[-1]  >= stock_60:
            #print("近季線")
            stock_60_all.append(j)
        elif stock.price[-1] / stock_5 < 1.1 and stock.price[-1]  <= stock_5 <= stock_10 <= stock_20 <= stock_60:
            #print("五日線反")
            stock_5_allS.append(j)
        elif stock.price[-1] / stock_10 <= 1.1 and stock.price[-1]  <= stock_10 <= stock_20 <= stock_60:
            #print("近十日線反")
            stock_10_allS.append(j)
        elif stock.price[-1] / stock_20 <= 1.1 and stock.price[-1]  <= stock_20 <= stock_60:
            #print("近月線反")
            stock_20_allS.append(j)
        elif stock.price[-1] / stock_60 <= 1.1 and stock.price[-1]  <= stock_60:
            #print("近季線反")
            stock_60_allS.append(j)
        #else:
            #print("NA")
        print("Run")      
except:
    print("NG" + str(j))
finally:
    saveuse('stock_5多_data.txt',stock_5_all)#存檔專用
    saveuse('stock_10多_data.txt',stock_10_all)
    saveuse('stock_20多_data.txt',stock_20_all)
    saveuse('stock_60多_data.txt',stock_60_all)
    saveuse('stock_5空_data.txt',stock_5_allS)
    saveuse('stock_10空_data.txt',stock_10_allS)
    saveuse('stock_20空_data.txt',stock_20_allS)
    saveuse('stock_60空_data.txt',stock_60_allS)

here = os.getcwd()
callfile = ["60","20","10","5","60S","20S","10S","5S"]#檔案名稱
def webstart(i):#啟動法人買賣超截圖
    os.system(here + "/" + "stock3_0927_5_" + str(i) + ".py")
    
for i in callfile:
    _thread.start_new_thread(webstart,(i,))

callvolumefile = ["60","60S"]#檔案名稱
def webstartvolume(l):#啟動股票期貨成交量截圖
    os.system(here + "/" + "stock3_0927_5_" + str(l) + "_" + "volume" + ".py")

for l in callvolumefile:
    _thread.start_new_thread(webstartvolume,(l,))
