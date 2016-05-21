import numpy as np

f = open('data.csv', 'w')
print f

value = 'Fecha Hora;Valor Estimado;distancia;Valor Minimo'
s = str(value)+'\n'
f.write(s)

for j in range(10,30):
    for i in range(10,60):
        aleatorio = np.random.randint(50) + 90
        value = '2016-'+str(j)+'-01 00:'+str(i)+';'+str(aleatorio)+';13000;90'
        s = str(value)+'\n'
        f.write(s)
