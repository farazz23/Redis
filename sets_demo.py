from connection_redis import connect_redis


r = connect_redis()
online_users="online:user"


# #TODO : Add user inside the set
# r.sadd(online_users, "Alice" , "Bob", "Charlie")
# print(f"Online users: {r.smembers(online_users)}")

# TODO : Add duplicated :
# r.sadd(online_users, "Alice")
# print(f"After adding the duplicate member: {r.smembers(online_users)} ")
#NOTE: After adding th e duplicate element , redis set will ignored the duplicate one

# TODO: Check Members :
# print(f"Is Alice member of the online group: {r.sismember(online_users, "Alice")}")
# print(f"Is Faraz member of the online group: {r.sismember(online_users, "Faraz")}")

# #TODO:  Count members
# print("Total users:", r.scard(online_users))

# #TODO: Remove a user
# r.srem(online_users, "Charlie")
# r.sadd(online_users, "Faraaz", "Aiman", )
# print("After Charlie left:", r.smembers(online_users))

# TODO: Randomly remove the user
# print(f"Random user {r.srandmember(online_users)}")
# print(f"Remove the random user : {r.spop(online_users)}")
# print(f"ALl the user now : {r.smembers(online_users)}")


#TODO : Moving members between sets: 
group_A="group:A"
group_B="group:B"
r.sadd(group_A, "Faraaz" , "Ashraf", "Aiman", "Fatima")
r.sadd(group_B, "Hey","there","nice","to","meet","you")

r.smove(group_A,group_B, 'Aiman')
print(f"Group A user : {r.smembers(group_A)}")
print(f"Group B user : {r.smembers(group_B)}")



#NOTE:    Operation Type	        Commands	                                Description
#NOTE:    Add/Remove	            SADD, SREM, SMOVE	                        Manage members
#NOTE:    Inspect	                SMEMBERS, SISMEMBER, SCARD	                Query contents
#NOTE:    Random	                SPOP, SRANDMEMBER	                        Random access
#NOTE:    Mathematical	            SINTER, SUNION, SDIFF	                    Combine or compare sets
#NOTE:    Store Results	            SINTERSTORE, SUNIONSTORE, SDIFFSTORE	    Persist derived sets
#NOTE:    TTL	                    EXPIRE	                                    Expire key after time
#NOTE:    Existence control	        SADD + EXISTS                               check	Emulate NX/XX behavior
