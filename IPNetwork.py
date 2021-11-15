# IPNetwork.py

import PySimpleGUI as sg
import ipaddress
import netaddr

layout = [
        [sg.Text('Rete IP(/CIDR):'), sg.Input(key='-IN-')],
		[sg.Text('IP:'), sg.Input(key='-IN2-')],
        [sg.Text('network:', size=(30,1), key='-OUT-')],
        [sg.Text('broadcast:', size=(30,1), key='-OUT2-')],
        [sg.Text('size:', size=(30,1), key='-OUT3-')],
		[sg.Text('Inside:', size=(30,1), key='-OUT4-')],
        [sg.Button('OK'), sg.Button('Exit')]
]   

window = sg.Window('IPNetwork', layout)

while True:
    event, values = window.read()
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break
    inside=""
    if (values['-IN2-']!=""):	
        inside = ipaddress.ip_address(values['-IN2-']) in ipaddress.ip_network(values['-IN-'])
    #    window['-OUT-'].update("INSIDE!")
    #else:
    #    window['-OUT-'].update("OUTSIDE!")
    ip=netaddr.IPNetwork(values['-IN-'])
    window['-OUT-'].update(ip.network)
    window['-OUT2-'].update(ip.broadcast)
    window['-OUT3-'].update('size:'+str(ip.size))
    window['-OUT4-'].update('Inside:'+str(inside))

#window.close()
