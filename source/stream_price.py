import pyEX
from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import sse

# You can generate a Token from the "Tokens Tab" in the UI
token = "KJItntKJX15CxF39y5n6_XMElGPBAAqm0JHiCK21LYtaraDxeBEOgt4bmWWg5I9hiICHcoin2AKLBFF21f-6Jw=="

org = "wfclark5@gmail.com"

bucket = "wfclark5's Bucket"

client = InfluxDBClient(url="https://eastus-1.azure.cloud2.influxdata.com", token=token)

tickers = ['GOOG']

c = sse.lastSSE(symbols='SPY', token="sk_0f24b5efbcb743dfa2681f1fabfd763a", on_data=print)

print(c)