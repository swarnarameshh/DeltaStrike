from pix_apidata import *

api = apidata_lib.ApiData()

def on_trade(msg):
    print("TRADE RECEIVED")
    print(msg)
    print("-" * 80)


def connection_started():
    print("✅ Connected to Accelpix")


def connection_stopped():
    print("❌ Connection Stopped")