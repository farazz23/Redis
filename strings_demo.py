import time
from connection_redis import connect_redis 

#TODO: Connecting to the redis server
r = connect_redis()





#! 1️⃣ SET & GET ->
r.set("Site Learning", "Harvard Redis Learning")
value = r.get("Site Learning")
print(f"Site Learning: {value}")





#! 2️⃣ INCR / DECR (Atomic Counters) ->
r.set("page_views",1)
r.incr("page_views")
r.incr("page_views")
r.incr("page_views")
r.decr("page_views")
print(f"Page View : {r.get("page_views")}")




#! 3️⃣ APPEND ->
r.append("Site Learning", " Please Subscribe to my Channel")
print(f"String after append : {r.get("Site Learning")}")







#! 4️⃣ Expiration (TTL : time-to-live) -> 
r.set("temprory_key", "This key will expire in 3 sec", ex=3)
print(f"Temprory key set , {r.ttl("temprory_key")} sec")
time.sleep(3)
print(f"Temprory key after 3 sec is: {r.get("temprory_key")}")






#! 5️⃣ SET with NX/XX (Conditional Set)
#TODO:  NX: only set if key does NOT exist
#TODO:  XX: only set if key already exists

was_set = r.set("unique_key", "First time", nx=True)
print("5️⃣ NX -> First set success?", bool(was_set))
was_set_again = r.set("unique_key", "Overwrite attempt", nx=True)
print("5️⃣ NX -> Second set success?", bool(was_set_again))
print("Current value ->", r.get("unique_key"))