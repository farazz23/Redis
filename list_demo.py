"""
#! Redis Lists are ordered sequences of strings — essentially, they behave like linked lists rather than arrays.
#! They are ideal for queue-like and stack-like operations such as:
? 1. Message queues
? 2. Background job buffers
? 3. Task pipelines
? 4. Stream-like logs
"""

from connection_redis import connect_redis

# TODO: Connecting to Redis:
r = connect_redis()
# list_key = "shipping:list:items"

# #TODO: Adding Element ->
# r.rpush(list_key , "Milk","Bread")
# r.rpush(list_key , "Cheese", "Butter")
# print(f"After a Right push : {r.lrange(list_key, 0, -1)}")

# r.lpush(list_key, "Apple" , "Orange", "Mango")
# print(f"After a Left push : {r.lrange(list_key, 0, -1)}")


# #TODO: LINSERT-> Insert element based on a pivot value ->
# r.linsert(list_key, 'BEFORE',"Mango","Litchi" )
# print(f"After LINSERT: {r.lrange(list_key, 0, -1)}")

# TODO: RPUSHX/LPUSHX -> Add only if the list exists
# r.lpushx(list_key, 'Egg')
# r.lpushx(list_key , '')

# #TODO: LLEN: Get the length of the list
# length = r.llen(list_key)
# print(f"LLEN: The list length is {length}")

# #TODO:  LRANGE: Get a range of elements (0 to -1 means all)
# full_list = r.lrange(list_key, 0, -1)
# print(f"LRANGE 0 -1 (Full List): {full_list}")

# #TODO:  LINDEX: Get element by index
# item_at_2 = r.lindex(list_key, 2)
# print(f"LINDEX 2 (3rd element): {item_at_2}")

# #TODO: LPOS: Find the index of an element
# pos_of_cheese = r.lpos(list_key, 'Cheese')
# print(f"LPOS 'Cheese': Index is {pos_of_cheese}")


# ==========================================================
## 3. Removing Elements (LPOP, RPOP, LREM, LTRIM)
# ==========================================================
# print(f"All the element {r.lrange(list_key, 0, -1)}")
# right_popped = r.rpop(list_key)
# left_popped = r.lpop(list_key)
# print(left_popped)
# print(right_popped)
# print(f"Elements after Popping : {r.lrange(list_key, 0, -1)}")

#TODO LSET: Replace an element by index
# r.lset(list_key, 0, "Organic Milk")
# print(f"LSET 0 'Organic Milk'. List: {r.lrange(list_key, 0, -1)}")

# ==========================================================
## 4. Moving and Blocking (RPOPLPUSH, LMOVE, BLPOP)
# ==========================================================

#NOTE : MOVING: 
# primary_list ="job:item"
# r.rpush(primary_list, 'working','drinking','singing','dancing','playing')
# print(f"Primary List: {r.lrange(primary_list,0,-1)}")

# #!LMOVE -> Pop from LEFT of primary_list and Push to RIGHT of secondary_list
# secondary_list = "processing:item"
# r.lmove(primary_list, secondary_list, 'LEFT','RIGHT')
# print(f"Secondary List: {r.lrange(secondary_list,0,-1)}")

#NOTE : MOVING: 

pending_queue="pending:job"
processing_queue = "processing:job"
# r.rpush(processing_queue,"job-1","job-2","job-3","job-4")
print(f"Processed Job : {r.lrange(processing_queue, 0, -1)}")
