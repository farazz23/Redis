import time
from connection_redis import connect_redis




r= connect_redis()

# r.set('Alice', 200)
# r.set('Damon', 100)


# with r.pipeline() as p:
#     p.multi()       #start transaction
#     p.decrby('Alice',50)
#     p.incrby('Damon', 50)
#     p.execute()

# print(f"Alice: {r.get('Alice')}")
# print(f"Damon: {r.get('Damon')}")


#TODO: executing the redis transaction and pipeline using watch command
r.set('Acc_Bal', 100)

with r.pipeline() as pipe:
    while True:
        try:
            pipe.watch('Acc_Bal')
            Balance = int(r.get('Acc_Bal'))
            print(Balance)
            if(Balance < 50):
                pipe.unwatch()
                print("Not enough balance...")
                break
            pipe.multi()
            pipe.decrby('Acc_Bal', 50)
            print("Transaction successful")
            print(f"Current bal: {r.get('Acc_Bal')}")       #! Balance has not been deducted yet
            pipe.execute()
            print(f"Current bal: {r.get('Acc_Bal')}")

            break
        except r.WatchError:
            print('Balance changed by someone else')
            time.sleep(0.2)

        
