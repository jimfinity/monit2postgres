import xmltodict
import yaml
import schedule
from time import sleep
import requests
from icecream import ic

response = requests.get('http://192.168.1.21:2812/_status?format=xml')
monitDict = xmltodict.parse(response.text, dict_constructor=dict, attr_prefix="")
print (monitDict)