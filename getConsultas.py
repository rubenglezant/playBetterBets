IMEI_ANT =""
with open("/home/ruben/temp2/dataSorted.dat", "r") as f:
  for line in f:
      partes = line.split("|")
      IMEI = (partes[0])
      if (IMEI==IMEI_ANT):
          print ("Consultar - IMEI "+ IMEI + " - " +(partes[1])+ " - "+BTs_ANT + " - con diferencia de tiempo en minutos: " + str(int(partes[2])-TEMPO_ANT))
      IMEI_ANT = IMEI
      BTs_ANT = (partes[1])
      TEMPO_ANT = int(partes[2])


