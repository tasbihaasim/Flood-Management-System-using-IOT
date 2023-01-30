'''For the temperature of city of Qambar'''
# client_put.py
import asyncio
import random
import requests

# import pandas as pd
import gateway
from aiocoap import *
import datetime

# url = 'http://www.wapda.gov.pk/index.php/river-flow-data'
# link = "http://www.wapda.gov.pk/index.php/river-flow-data"
# dfs = pd.read_html(link, header=None, skiprows=4, index_col=None)

async def main():
    context = await Context.create_client_context()
    today = datetime.datetime.now()
    month = today.strftime("%b")
    temp = 0
    if month == 'Nov' or month == 'Dec' or month == 'Jan' or month == 'Feb':
        temp = random.randint(21, 97)
    if month == 'March' or month == 'April' or month == 'May':
        temp = random.randint(31, 99)
    if month == 'June' or month == 'July' or month == 'August':
        temp = random.randint(49, 100)
    if month == 'Sep' or month == 'Oct' or month == 'Nov':
        temp = random.randint(29, 97)

    for i in range(24):
        rn = random.randint(1,4)
        c = random.choice(["increment", "decrement"])
        if c=="increment":
            temp = temp + rn
        else:
            temp = temp - rn
        data = "{}".format(temp)
        request = Message(code=POST, payload=data.encode("ascii"),
                          uri='coap://localhost:5683/Jehlum_humidity_sensor1')
        try:
            response = await context.request(request).response
            # print(response)
        except Exception as e:
            print('Failed to send data:')
            print(e)
        else:
            print('Sent data:', data)
            print('Received ACK:', response.payload.decode("ascii"))
        #await asyncio.sleep(2)

asyncio.get_event_loop().run_until_complete(main())
