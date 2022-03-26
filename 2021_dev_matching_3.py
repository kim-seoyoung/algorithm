def solution(enroll, referral, seller, amount):
    res = dict()
    tree = dict()
    
    for i, en in enumerate(enroll):
        res[en] = 0
        tree[en] = referral[i]

    for i in range(len(seller)):
        giver = seller[i]
        money = amount[i] * 100
        move = int(money * 0.1)
        while True:   
            res[giver] += money - move
            if move == 0:
                break
            money = move
            move = int(money * 0.1)
            giver = tree[giver]
            if giver == "-":
                break
    
    answer = []  
    for en in enroll:
        answer.append(res[en])
    
    return answer
