import datetime
import logging
logging.basicConfig(level=logging.WARNING)
logging.getLogger("coap-server").setLevel(logging.WARNING)
import asyncio
import aiocoap.resource as resource
import aiocoap
import csv

f = open('C:/Users/Tasbiha/Iot/rawdata.csv', 'w', newline='')
writer = csv.writer(f)


class Humidity(resource.Resource):

    def __init__(self, name):
        self.name = name

    async def render_post(self, request):
        payload = request.payload.decode("ascii")
        writer.writerow((self.name, payload))
        print("Received message: ", payload, "from", self.name)
        return  #aiocoap.Message(code=CHANGED, payload=b"ACK")

class Temperature(resource.Resource):
    def __init__(self, name):
        self.name = name

    async def render_post(self, request):
        payload = request.payload.decode("ascii")
        writer.writerow((self.name, payload))
        print("Received message: ", payload, "from", self.name)
        return #aiocoap.Message(code=CHANGED, payload=b"ACK")

# logging setup

logging.basicConfig(level=logging.INFO)
logging.getLogger("coap-server").setLevel(logging.DEBUG)

async def main():
    # Resource tree creation
    root = resource.Site()
    root.add_resource(('humidity_sensor1_indus',), Humidity('humidity_sensor1_indus'))
    root.add_resource(('humidity_sensor2_indus',), Humidity('humidity_sensor2_indus'))
    root.add_resource(('temperature_sensor1_indus',), Temperature('temperature_sensor1_indus'))
    root.add_resource(('temperature_sensor2_indus',), Temperature('temperature_sensor2_indus'))

    root.add_resource(('humidity_sensor1_jehlum',), Humidity('humidity_sensor1_jehlum'))
    root.add_resource(('humidity_sensor2_jehlum',), Humidity('humidity_sensor2_jehlum'))
    root.add_resource(('temperature_sensor2_jehlum',), Temperature('temperature_sensor2_jehlum'))
    root.add_resource(('temperature_sensor1_jehlum',), Temperature('temperature_sensor1_jehlum'))


    await aiocoap.Context.create_server_context(root, bind = ('localhost', 5683))

    # Run forever
    await asyncio.get_running_loop().create_future()
    # close the file
    f.close()



if __name__ == "__main__":
    asyncio.run(main())

