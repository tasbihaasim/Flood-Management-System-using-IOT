import sys
    # caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, 'C:/Users/Tasbiha/Iot/publisher_client')

from threading import Thread
import os

Thread(target = exec(open('C:/Users/Tasbiha/Iot/publisher_client/Indus/water_inflow_sensor1_indus.py').read())).start()
Thread(target = exec(open('C:/Users/Tasbiha/Iot/publisher_client/Indus/humidity_sensor1_indus.py').read())).start()
Thread(target = exec(open('C:/Users/Tasbiha/Iot/publisher_client/Indus/humidity_sensor2_indus.py').read())).start()
Thread(target = exec(open('C:/Users/Tasbiha/Iot/publisher_client/Indus/temperature_sensor1_indus.py').read())).start()
Thread(target = exec(open('C:/Users/Tasbiha/Iot/publisher_client/Indus/temperature_sensor2_indus.py').read())).start()
Thread(target = exec(open('C:/Users/Tasbiha/Iot/publisher_client/Indus/water_outflow_sensor2_indus.py').read())).start()

Thread(target = exec(open('C:/Users/Tasbiha/Iot/publisher_client/Jehlum/water_inflow_sensor1_jehlum.py').read())).start()
Thread(target = exec(open('C:/Users/Tasbiha/Iot/publisher_client/Jehlum/water_outflow_sensor2_jehlum.py').read())).start()
Thread(target = exec(open('C:/Users/Tasbiha/Iot/publisher_client/Indus/humidity_sensor1_jehlum.py').read())).start()
Thread(target = exec(open('C:/Users/Tasbiha/Iot/publisher_client/Indus/humidity_sensor2_jehlum.py').read())).start()
Thread(target = exec(open('C:/Users/Tasbiha/Iot/publisher_client/Indus/temperature_sensor1_jehlum.py').read())).start()
Thread(target = exec(open('C:/Users/Tasbiha/Iot/publisher_client/Indus/temperature_sensor2_jehlum.py').read())).start()