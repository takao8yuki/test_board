#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[4]:


# インポート
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options # オプションを使うために必要
import matplotlib.pyplot as plt
import time
import datetime
import csv
import os

import gspread
from oauth2client.service_account import ServiceAccountCredentials


# In[5]:


scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

#キー認証
credentials = ServiceAccountCredentials.from_json_keyfile_name('tenderloin05-9b8ef6de1a21.json', scope)
gc = gspread.authorize(credentials)


# In[6]:


wks = gc.open('リサーチシート6').sheet1   # スプレッドシートを開く

# wks.update_acell('I1', 'Hello World!')   # 値を入力
# print(wks.acell('I1'))


# In[7]:


# 検索対象のURLを取得する
i = 2
urlGot = True # URLの取得有無

# ブラウザを開く
# 本pythonファイルと同じディレクトリにchromeriver.exeがある場合、
# 引数空でも良い
option = Options()                          # オプションを用意
option.add_argument('--incognito')          # シークレットモードの設定を付与
#option.add_argument('--headless')           # headlessモードを使用する
#option.add_argument('--disable-infobars')   # 右記メッセージを非表示「Chrome は自動テスト ソフトウェアによって制御されています。」
browser = webdriver.Chrome(options=option)  # Chromeを準備
browser.get('https://www.google.com/')

while(urlGot):
    cell1 = 'D' + str(i)
    i+=1
    cell2 = 'D' + str(i)
    url = wks.acell(cell1).value
    if(wks.acell(cell2).value == ""):
        urlGot = False
    print(url)
    
    browser = webdriver.Chrome(options=option)  # Chromeを準備
    browser.refresh(url) 
    
    time.sleep(1)


# In[ ]:





# In[ ]:




