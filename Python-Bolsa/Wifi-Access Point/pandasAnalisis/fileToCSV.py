f = open('wifi_data1.csv', 'w')
f.write("Fecha|MAC|MACDst|Sennal\n")
with open("wifi_20160821_2351.txt", "r") as ins:
    for line in ins:
        data = line.split("\t")
        fecha = data[0]
        src = data[1]
        dst = data[2]
        sennal = data[4].split(",")[0]
        s = (fecha+"|"+src+"|"+dst+"|"+sennal)
        print (s)
        f.write(s+"\n")
f.close()
