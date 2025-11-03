from connection_redis import connect_redis

r = connect_redis()
race_key = "race:france"
r.delete(race_key)


#TODO: XADD adds a new entry to a stream.
res_1 = r.xadd(race_key, {
    "racer" : "Max Verstapen",
    "speed" : 289.4,
    "team" : "Red Bull",
    "position" : 1,
    "location_id" : 1
})

res_2 =r.xadd(race_key ,{
    "racer" : "Lewis Hamilton",
    "team" : "Ferari",
    "speed" : 230.5,
    "position": 3, 
    "location_id" : 1
})

res_3 =r.xadd(race_key ,{
    "racer" : "Lando Noris",
    "speed" : 270.2,
    "team" : "Maclaren",
    "position" : 2,
    "location_id" :1
})
print(res_1)
print(res_2)
print(res_3)


#TODO:  XLEN returns the length of a stream.
key_len= r.xlen(race_key)
print(f"Lenght of the Stream is :{key_len}")

# TODO : XRANGE returns a range of entries between two supplied entry IDs.
# Reads all the entries in the stream from the earliest ('-') to the latest ('+'). Useful to inspect everything stored.
r.xrange(race_key, min='-', max='+')



# TODO: XREAD reads one or more entries, starting at a given position and moving forward in time.
resp = r.xread({ race_key: "0-0" }, count=10, block=5000)
print("XREAD response:", resp)
if resp:
    for sname, messages in resp:
        for eid, fields in messages:
            print(f"  New via XREAD {eid} ->", {k.decode(): v.decode() for k, v in fields.items()})


#TODO:  XDEL removes entries from a stream.
print("Deleting entry:", res_2)
deleted = r.xdel(race_key, res_2)
print(f"XDEL returned: {deleted} (1 means deleted)")

# TODO : XTRIM trims a stream by removing older entries.
trimmed = r.xtrim(race_key, maxlen=2, approximate=False)
print(f"XTRIM result: {trimmed}")  # number of entries removed or something similar
