from connection_redis import connect_redis

r = connect_redis()

"""
#! A Redis Bitmap is not a separate data type — it’s a bit-level view on top of a simple string.
#? Each bit in the string (0 or 1) represents a binary flag — and because Redis strings can store up to 512 MB, you can represent over 4 billion bits per key.
"""

key = 'user_activity'
r.delete(key)

r.setbit(key, 1 , 1)   # user id 1 is active
r.setbit(key, 3,1)
r.setbit(key, 5,1)
r.setbit(key, 7,1)

print(f"is user 2 exist {r.getbit(key, 2)}")
print(f"is user 1 exist {r.getbit(key, 1)}")
print(f"is user 5 exist {r.getbit(key, 5)}")
print(f"is user 8 exist {r.getbit(key, 8)}")


#TODO : Count total user :
print(f"Get all users : {r.bitcount(key)}")


# TODO: Range and Position Queries : 
r.setbit(key, 10, 1)
r.setbit(key, 11, 1)

# Count only within a range of bytes
print("Active users (0–1 byte):", r.bitcount(key, 0, 1))

# Find position of the first 1-bit
print("First active user ID:", r.bitpos(key, 1))
