import urllib
from lxml import html
import datetime

dgtURL = "http://infocar.dgt.es/etraffic/"


def getAttribute(_url, _attribute):
    atts = _url.split("&")
    for s in atts:
        if _attribute in s:
            return s.split("=")[1]


def getAforadores(provincia, poblacion):
    theUrl = dgtURL + "Buscador?accion_buscar=buscar&SensoresTrafico=true&provincia=" + provincia + "&poblacion=" + poblacion + "&carretera=&version=texto&pagina=buscador&caracter=acontecimiento"
    page = html.fromstring(urllib.urlopen(theUrl).read())
    aforadores = []
    for link in page.xpath("//a"):
        url = link.get("href")

        if url is not None and "SensorTrafico" in url:
            nombre = getAttribute(url, "nombre")
            elemGenCod = getAttribute(url, "elemGenCod")
            aforadores.append([nombre, elemGenCod])
    return aforadores


def getSensorData(_nombre, _elemGenCod):
    theUrl = dgtURL + "DetallesElementos?accion=detallesElemento&tipo=SensorTrafico&nombre=" + _nombre + "&elemGenCod=" + _elemGenCod
    page = html.fromstring(urllib.urlopen(theUrl).read())
    lis = page.xpath("//li")
    if len(lis) > 2:
        intensidad = lis[1].text_content().split(" ")[2]
        velocidad = lis[2].text_content().split(" ")[3]
        ocupacion = lis[3].text_content().split(" ")[3].encode("ascii")
        ligeros = lis[4].text_content().split(" ")[2]
        return [intensidad, velocidad, ocupacion, ligeros]
    return [0]

# Fecha - hora
ahora = datetime.datetime.now()
hora = ahora.hour
minuto = ahora.minute
dia = ahora.day
mes = ahora.month

# EJEMPLO DE USO
afs = getAforadores("28", "Madrid")

for element in afs:
    data = getSensorData(element[0], element[1])
    if (len(data)>2):
        print str(mes) + "," + str(dia) + "," + str(hora) + "," + str(minuto) + "," + element[0] + "," + element[1]+ "," + data[0]+ "," + data[1]+ "," + data[2]+ "," + data[3]
