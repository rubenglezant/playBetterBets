import json
import glob, os
from pprint import pprint


def readFile(nombre):
	with open(nombre) as data_file:
		data = json.load(data_file)

	#print (data['resourceSets']['resources']['travelDistance'])
	dist = (data['resourceSets'][0]['resources'][0]['travelDistance'])
	durBase = (data['resourceSets'][0]['resources'][0]['travelDuration'])
	dur = (data['resourceSets'][0]['resources'][0]['travelDurationTraffic'])
	time = (nombre.split("=")[1].split('.')[0])
	timeH = time.split('-')[0]
	timeM = time.split('-')[1]
	day = (nombre.split("=")[0].split('-')[3])
	mes = (nombre.split("=")[0].split('-')[2])
	print (str(mes)+str(day)+str(timeH)+str(timeM)+";"+str(dist)+";"+str(durBase)+";"+str(dur))
	# pprint(data)
	return

print 'Fecha Hora;distancia;Valor Minimo;Valor Estimado'
os.chdir("/home/ruben/data-temp")
for file in glob.glob("*.txt"):
    try:
        readFile(file)
    except:
        continue
