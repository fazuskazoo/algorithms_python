
def maximumWealth(accounts: list[list[int]]) -> int:
    max_val = 0
    for i in range(0,len(accounts)):
        total = 0
        for j in range(0,len(accounts[i])):
            total += accounts[i][j]
        if total > max_val:
            max_val = total
    return max_val

i = [[2,8,7],[7,1,3],[1,9,5],[4,5,6]]
print(maximumWealth(i))
