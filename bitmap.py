from connection_redis import connect_redis

r = connect_redis()

"""
#! A Redis Bitmap is not a separate data type — it’s a bit-level view on top of a simple string.
#? Each bit in the string (0 or 1) represents a binary flag — and because Redis strings can store up to 512 MB, you can represent over 4 billion bits per key.
"""

key = 'user_activity'
r.delete(key)

r.setbit(key, 91 , 1)   # user id 91 is active
r.setbit(key, 3,1)      # user id 3 is active 
r.setbit(key, 5,1)      # user id 5 s active
r.setbit(key, 7,1)      # user id 7 is active 

print(f"is user 2 exist {r.getbit(key, 2)}")
print(f"is user 1 exist {r.getbit(key, 1)}")
print(f"is user 5 exist {r.getbit(key, 5)}")
print(f"is user 8 exist {r.getbit(key, 8)}")


#TODO : Count total user :
print(f"Get all users : {r.bitcount(key)}")


# TODO: Range and Position Queries : 
r.setbit(key, 10, 1)
r.setbit(key, 11, 1)

#? Count only within a range of bytes
print("Active users (0–1 byte):", r.bitcount(key, 0, 1))

#? Find position of the first 1-bit
print("First active user ID:", r.bitpos(key, 1))


# TODO : Bitwise Operations (BITOP)
# ? ou can combine multiple bitmaps logically — perfect for tracking users across days.
r.setbit("day1", 1, 1)
r.setbit("day2", 1, 1)
r.setbit("day2", 2, 1)


#? Combine using OR (users active on any day)
r.bitop("OR" , "Anyday" , "day1" , "day2")
print(f"User Active anyday {r.bitcount("Anyday")}")

#? Combine using AND (users active both days)
r.bitop("AND", "Bothdays", "day1", "day2")
print("Users active both days:", r.bitcount("Bothdays")) 


# TODO : 7️⃣ Advanced Bitfield Operations
#? BITFIELD lets you treat bitmaps like arrays of integers (signed or unsigned).

r.delete("bitfield_example")

# Increment a 5-bit unsigned integer starting at offset 0
r.bitfield("bitfield_example", "INCRBY", "u5", 0, 1)
r.bitfield("bitfield_example", "INCRBY", "u5", 0, 1)

# Retrieve the same 5-bit integer
value = r.bitfield("bitfield_example", "GET", "u5", 0)
print("Counter value:", value)



"""
! Key Takeaways

? Bitmaps are highly memory-efficient — ideal for boolean data on a massive scale.
? Used extensively in analytics systems, gaming platforms, ad-tech, and feature rollouts.
? They shine in temporal tracking, user behavior analysis, and binary data compression use cases.
"""