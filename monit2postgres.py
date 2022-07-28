import xmltodict
import yaml
import schedule
from time import sleep
import requests
from icecream import ic
import psycopg2
import json

response = requests.get('http://192.168.1.21:2812/_status?format=xml')
monitDict = xmltodict.parse(response.text, dict_constructor=dict, attr_prefix="")
print (monitDict)

conn = psycopg2.connect("host=test-postgres dbname=testing user=postgres password=mysecretpassword")
cur = conn.cursor()
sql = """INSERT INTO test(id, data)
             VALUES(%s);"""
cur.execute(sql, (1,json.dumps(monitDict)))