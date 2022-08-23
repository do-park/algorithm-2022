N = int(input())
rewards = []
for _ in range(N):
    dices = list(map(int, input().split()))
    reward = 0
    for dice in dices:
        if dices.count(dice) == 3:
            reward = 10000 + 1000*dice
            break
        elif dices.count(dice) == 2:
            reward = 1000 + 100*dice
            break
        else:
            reward = reward if reward > 100*dice else 100*dice
    rewards.append(reward)
print(max(rewards))