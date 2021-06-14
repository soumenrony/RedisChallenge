#Pushing data into the redis oss cluster
import redis
redisclient = redis.StrictRedis(host= '34.122.87.78' , port= 6379 , db=0)
i = 1
while(i <= 100):
    redisclient.rpush('key', i)
    i += 1

#Print out the values from 1 - 100(optional)
print(redisclient.lrange('key', 0, -1))



# Read and Print out the values from 100 - 1 in reverse order
import redis
redisclient = redis.StrictRedis(host='35.238.133.28', port=19646, db=0, password='June@2021')
i = 100
while (i >= 0):
    print(redisclient.lindex('key', i))
    i -= 1
