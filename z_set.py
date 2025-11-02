from connection_redis import connect_redis

r= connect_redis()

leaderboard= "game_score"
r.delete(leaderboard)

r.zadd(leaderboard, {
    'alice': 1,
    'bob': 2,
    'charlie': 3,
    'damon': 4
})
print(f"All members with score : {r.zrange(leaderboard, 0, -1 , withscores=True)}")