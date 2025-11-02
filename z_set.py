from connection_redis import connect_redis

r= connect_redis()

leaderboard= "game_score"
r.delete(leaderboard)

# Add members with scores
r.zadd(leaderboard, {
    'alice': 10,
    'bob': 50,
    'charlie': 30,
    'damon': 60,
    'elijah': 80,
    'klaus' : 100
})
print(f"All members with score : {r.zrange(leaderboard, 0, -1 , withscores=True)}")

# Get Top N Players:
print(f"Top 3 players is : {r.zrange(leaderboard, 0,2 , withscores=False)}")

# Incrementing the score dynamically
r.zincrby(leaderboard, 10, "alice")  # Alice +10 points
print("Alice new score:", r.zscore(leaderboard, "alice"))

# Queue by scoring range :
players_50_80 = r.zrangebyscore(leaderboard, 50, 80, withscores=True)
print("Players with score between 50 and 80:", players_50_80)

# Ranking Position
print("Bob rank (0-based, ascending):", r.zrank(leaderboard, "bob"))
print("Bob rank (descending):", r.zrevrank(leaderboard, "bob"))


# Remove by Score or Member
r.zremrangebyscore(leaderboard, 0, 55)
print("After removing low scores:", r.zrange(leaderboard, 0, -1, withscores=True))
