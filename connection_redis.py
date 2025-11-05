import redis



def connect_redis():

    r= redis.Redis(
        host='localhost',
        port='6379',
        db=0,
        decode_responses=True
    )

    return r

if __name__ == "__main__":
    redis_client = connect_redis()

    try:
        if redis_client.ping() :
            print("Connected to the Redis Successfully...", redis_client)
    except : 
        print("Failed to connect to Redis") 



    redis_client.set("Welcome", "Hey, Redis from Python!")
    greeting = redis_client.get("Welcome")
    redis_client.set("Name" , "Faraaz")
    name = redis_client.get("Name" )
    print(f"Greeting : {greeting}")
    print(f"My name is Faraaz: {name}")
