#coding=utf-8
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("baidu.com")
driver.maximize_window()
