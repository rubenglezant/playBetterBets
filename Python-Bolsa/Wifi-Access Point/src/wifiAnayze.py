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

for mac in MACs.keys():
    print ("----------- MAC: " + mac)
    estado = 0
    with open(nombreFich) as f:
        for line in f:
            data = line.split("\t")
            seg = int(data[0].split(".")[0])
            src = data[1]
            totalSeg = 0
            if (src == mac):
                if (estado == 0):
                    print ("Inicio: " + str(seg))
                    inicioSeg = seg
                    estado = 1
                if (estado == 1):
                    segAnt = MACs[src]
                    if not ((segAnt + 30)>=seg):
                        print ("Fin: " + str(seg))
                        finSeg = seg
                        totalSeg += (finSeg - inicioSeg)
                        estado = 0
                MACs[src] = seg
        if (estado == 1):
            print ("- Fin: " + str(MACs[mac]))
            finSeg = MACs[mac]
            estado = 0

        totalSeg += (finSeg - inicioSeg)
        print ("- Total Seg: " + str(totalSeg))
        print ("- % Tiempo: " + str(float(totalSeg*100/2348)))
        MACs[mac] = totalSeg

print (MACs.keys())
print (MACs.values())

