# 20:55:31:db:62:cd
MACs = dict()

def isMAC(mac):
    if (mac.count(':') == 5):
        return True;
    else:
        return False;


nombreFich = 'wifi_20160802_1753.txt'
with open(nombreFich) as f:
    for line in f:
        data = line.split("\t")
        seg = int(data[0].split(".")[0])
        src = data[1]
        dst = data[2]
        if (isMAC(src)):
            if (not(MACs.has_key(src))):
                MACs[src] = seg

#MACs['50:55:27:ab:61:a1'] = 10

for mac in MACs.keys():
    print ("----------- MAC: " + mac)
    estado = 0
    totalApariciones = 0
    cadenaInicioFin = []
    with open(nombreFich) as f:
        for line in f:
            data = line.split("\t")
            seg = int(data[0].split(".")[0])
            src = data[1]
            totalSeg = 0
            if (src == mac):
                if (estado == 0):
                    print ("Inicio: " + str(seg))
                    cadenaInicioFin.append(seg)
                    inicioSeg = seg
                    estado = 1
                if (estado == 1):
                    segAnt = MACs[src]
                    if not ((segAnt + 30)>=seg):
                        print ("Fin: " + str(seg))
                        cadenaInicioFin.append(seg)
                        finSeg = seg
                        totalSeg += (finSeg - inicioSeg)
                        estado = 0
                MACs[src] = seg
                totalApariciones += 1
        if (estado == 1):
            print ("- Fin: " + str(MACs[mac]))
            cadenaInicioFin.append(MACs[mac])
            finSeg = MACs[mac]
            estado = 0

        totalSeg += (finSeg - inicioSeg)
        print ("- Total Seg: " + str(totalSeg))
        print ("- % Tiempo: " + str(float(totalSeg*100/2348)))
        MACs[mac] = str(totalSeg)+","+str(totalApariciones)+","+str(cadenaInicioFin[0])+","+str(cadenaInicioFin[-1])

f = open('resultsMAC.txt','w')
for mac in MACs.keys():
    print (mac + "," + MACs[mac])
    f.write(mac + "," + MACs[mac]+'\n')
f.close()

