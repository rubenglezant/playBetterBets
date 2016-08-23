import redis
from random import randint

r_server = redis.Redis("localhost")
for i in range (0,10000000):
    a = randint(1, 125000)
    b = r_server.get("BT"+str(a).zfill(12))
    print (b)

# Populate
r_server = redis.Redis("localhost")

for i in range (0,125000):
    r_server.set("BT"+str(i).zfill(12), str(i)+"|"+str(i))

