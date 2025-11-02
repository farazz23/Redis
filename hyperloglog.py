from connection_redis import connect_redis




r = connect_redis()

"""
! A HyperLogLog (HLL) is a probabilistic data structure for cardinality estimation, meaning it estimates how many unique items have been added to a dataset.
?It doesn’t store the items themselves — it only tracks a probabilistic fingerprint.
?This makes it memory efficient and extremely fast, with only ~0.81% standard error.
"""

#TODO : Create a HyperLogLog for unique webiste visitor
key = 'unique_visitor:2025-10-31'
r.delete(key)

r.pfadd(key, "user_1", "user_2","user_3","user_2")
print(f"All the unique user : {r.pfcount(key)}")



# TODO : 5️⃣ Merging Multiple HyperLogLogs
#? If your system runs in multiple regions (e.g., “us-east” and “us-west”), you can merge their counts efficiently.

r.pfadd("visitors:us-east", "Alice", "Bob", "Charlie")
r.pfadd("visitors:us-west", "David", "Eva", "Carol")

print(f"Merger all Member : {r.pfmerge("visitors:global" , "visitors:us-east" , "visitors:us-west")}")
print(f"All User Globally : {r.pfcount("visitors:global")}")



#TODO : Counting Unique Visitors per Day
#? Let’s simulate visitors across multiple days: 

days=['2025-10-01', '2025-10-02', '2025-10-03', '2025-10-04']

for day in days:
    new_key = f"visitors:user:{day}"

    for i in range(1000):
        r.pfadd(new_key, f"user:{i}")

for day in days :
    print(f"{day} -> {r.pfcount(f"visitors:user:{day}")}")


"""
Use Case	                Description
Web Analytics	            Estimate unique visitors to a site or API.
IoT Systems	                Estimate unique devices reporting in a time window.
Search Logs	                Count unique search queries.
Advertising Analytics	    Count unique ad impressions or clickers.
Monitoring Systems	        Count unique errors, IPs, or metrics efficiently.
"""