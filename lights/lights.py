from simplejson import load
from tuya_connector import TuyaOpenAPI , TUYA_LOGGER
import typer
from typing import Optional
from dotenv import load_dotenv
import os

load_dotenv()

ACCESS_ID = os.getenv("ACCESS_ID")
ACCESS_KEY = os.getenv("ACCESS_KEY")
API_ENDPOINT = os.getenv("API_ENDPOINT")
DEVICE_ID = os.getenv("DEVICE_ID")

app = typer.Typer()

light = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
# Enable debug log
#TUYA_LOGGER.setLevel(logging.DEBUG)

def main():
    light.connect()
    app()


@app.command()
def switch(mode:str):
    '''
    Turns Light ON or OFF
    '''
    if mode == 'on':
        commands = {'commands': [{'code': 'switch_led', 'value': True}]}
        res = light.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICE_ID), commands)
        #typer.echo(res['success'])
    elif mode == 'off':
        commands = {'commands':[{'code':'switch_led','value':False}]}
        light.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICE_ID), commands)

@app.command()
def mode(mode:str):
    """
    Set color mode to WHITE or COLOR
    """
    if mode == 'w' or mode == "white":
        commands = {'commands': [{'code': 'work_mode', 'value': 'white'}]}
        res = light.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICE_ID), commands)
    elif mode== 'c' or mode == "color":
        commands = {'commands': [{'code': 'work_mode', 'value': 'colour'}]}
        res = light.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICE_ID), commands)
        #typer.echo(res)

@app.command()
def color(h : int , s:int , v:int):
    """
    Set Colour Value (H,S,V)
    H : 0-360
    S : 0-1000
    V : 0-1000
    """
    commands = {'commands': [{'code': 'colour_data_v2', 'value': {'h':h,'s':s,'v':v}}]}
    res = light.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICE_ID), commands)



@app.command()
def white(bright:int,temp:int):
    """
    Set light to white mode with BRIGHTNESS and TEMPERATURE
    """
    commands = {'commands': [{'code': 'temp_value_v2', 'value': temp},{'code': 'bright_value_v2', 'value': bright}]}
    res = light.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICE_ID), commands)


if __name__ == "__main__":
    main()