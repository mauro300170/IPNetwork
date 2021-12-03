# IPNetwork.py

import PySimpleGUI as sg
import ipaddress
import netaddr

first_column = [
        [sg.Text('Network:', size=(20,1), key='-OUT-')],
        [sg.Text('Broadcast:', size=(20,1), key='-OUT2-')],
        [sg.Text('Size:', size=(20,1), key='-OUT3-')],
		[sg.Text('Inside:', size=(20,1), key='-OUT4-')],
        [sg.Button('OK'), sg.Button('Exit')]
]
second_column = [
        [sg.Text('/32 : 255 : 1\n/31 : 254 : 2\n/30 : 252 : 4\n/29 : 248 : 8\n/28 : 240 : 16\n/27 : 224 : 32\n/26 : 192 : 64\n/25 : 128 : 128\n/24 : 256 : 255', size=(20,9), key='-OUT1-')]
]

layout = [
        [sg.Text('Rete IP(/CIDR):'), sg.Input(key='-IN-')],
		[sg.Text('IP:'), sg.Input(key='-IN2-')],
		[
			sg.Column(first_column),
		    sg.VSeparator(),
            sg.Column(second_column),
		]
]   

window = sg.Window('IPNetwork', layout)

while True:
    event, values = window.read()
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break
    inside=""
    ip=netaddr.IPNetwork(values['-IN-'])
    if (values['-IN2-']!=""):
        res=values['-IN-'].find('/')
        rete=values['-IN-'][:res]
        #inside=rete
        if rete==str(ip.network):
            inside = ipaddress.ip_address(values['-IN2-']) in ipaddress.ip_network(values['-IN-'])
        else:
            inside = "WRONG Network!"		
    window['-OUT-'].update(ip.network)
    window['-OUT2-'].update(ip.broadcast)
    window['-OUT3-'].update('size:'+str(ip.size))
    window['-OUT4-'].update('Inside:'+str(inside))
