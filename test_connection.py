import redis

#SECTION  : Create a Redis client connection
#! Redis stores data as bytes, not strings.
#! If you don’t set decode_responses=True, every value you get back from Redis will look like this:
#! Setting decode_responses=True tells redis-py to automatically decode all responses using UTF-8.
#! This gives you clean, human-readable Python strings

r= redis.Redis(host='localhost', port=6379, decode_responses=True)


try:
    response = r.ping()
    print("Connected to Redis Server Successfully..." , response)
except:
    print("Failed to connect to Redis")


