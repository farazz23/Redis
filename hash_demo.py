from connection_redis import connect_redis
import time 
import redis
from typing import Dict , Any

#TODO: Connecting to the redis 
redis_client = connect_redis()



#TODO : Create a user hah -> 
user_key = "user:1001"
redis_client.hset(user_key, mapping={
    'name' : 'Faraaz Ashraf',
    'profession' : 'Software Engineer',
    'domain' : 'Backend Devlopment',
    'salary' : 150000
})
print(f"User Creared Successfully")


#TODO: Retrieve a single field ->
print(f"Name of the user is : {redis_client.hget(user_key , "name")}")
print(f"Profession of the user is : {redis_client.hget(user_key , "name")}")
print(f"In which domain does {redis_client.hget(user_key , "name")} works : {redis_client.hget(user_key , "domain")}")
print(f"Total salary of his : {redis_client.hget(user_key , "name")}")



# TODO : Retrieve all fields -> 
print("All user data: ")
user_data = redis_client.hgetall(user_key)
for key , value in user_data.items():
    print(f"{key} : {value}")


# TODO: Increment a int value ->
print("Increment a value by 20000")
redis_client.hincrby(user_key, "salary", 20000)
print(f"After incrementation the salary is -> {redis_client.hget(user_key, "salary")}  ")


# TODO : Delete a field -> 
print("Deleting some unsed value :")
del_field = redis_client.hdel(user_key , 'domain')
print(f"Deleted 'domain 'fielsd ")
print(f"New User hashset is : {redis_client.hgetall(user_key)}")


# TODO : existence check -> 
print(f"Does email exist -> {redis_client.hexists(user_key , "email")} ")
print(f"Does age exist -> {redis_client.hexists(user_key , "age")} ")
print(f"Does Profession exist -> {redis_client.hexists(user_key , "profession")} ")
print(f"Does salary exist -> {redis_client.hexists(user_key , "salary")} ")

# TODO : Field count ->
print(f"How many total field present inside the hash set :{redis_client.hlen(user_key)} ")


# TODO : Returns all values only ->
print(f"All Keys : {redis_client.hkeys(user_key)}")
print(f"All value : {redis_client.hvals(user_key)}")


# TODO : Adding some extra vlaue inside the existing hashset : 
def h_nx(r : redis.Redis ,key : str , mapping : Dict[str , Any]) -> bool:
    if not r.exists(key):
        print("Updating the {key}")
        r.hset(key , mapping=mapping)
        return True
    else :
        return False
    
def h_xx(r: redis.Redis, key : str , mapping : Dict[str , Any]) -> bool :
    if r.exists(key):
        r.hset(key, mapping=mapping)
        return True 
    else:
        return False
    
new_data = {
    "age" : 24,
    "email" : "farazashraf1523@gmail.com",
}
was_set = h_xx(redis_client , user_key ,new_data )
if was_set :
    all_new_data = redis_client.hgetall(user_key)
    for key , value in all_new_data.items():
        print(f"{key} : {value}")
else :
    user_data = redis_client.hgetall(user_key)
    for key , value in user_data.items():
        print(f"{key} : {value}")


        














"""
? A Redis Hash is a map of fields and values stored under a single Redis key — conceptually similar to a Python dictionary (dict),
! The Redis key = the name of the hash (like a table name).
! Each field = an attribute or property name.
! Each value = the corresponding value for that field.
"""

"""
Command	Description	Example
# STUB  HSET Set one or more fields	HSET user:1 name "Alice" age "23"
# STUB  HGET	Get one field’s value	HGET user:1 name
# STUB  HGETALL	Get all fields and values	HGETALL user:1
# STUB  HMSET	Set multiple fields (deprecated; use HSET with mapping instead)	
# STUB  SET user:1 field1 val1 field2 val2
# STUB  HDEL	Delete specific fields	HDEL user:1 age
# STUB  HEXISTS	Check if a field exists	HEXISTS user:1 name
# STUB  HINCRBY	Increment numeric fields	HINCRBY user:1 login_count 1
# STUB  HLEN	Get number of fields	HLEN user:1
"""



