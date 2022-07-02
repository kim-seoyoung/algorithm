import heapq

def solution(food_times, k):
    food_dict = dict()
    for food in food_times:
        food_dict[food] = []
    len_ = len(food_times)
    for i in range(len_):
        food_dict[food_times[i]].append(i)
        
    food_hq = []
    for key in food_dict.keys():
        heapq.heappush(food_hq, (key, food_dict[key]))
            
    food_exist = [True for _ in range(len_)]
    remain_time = k
    num_food = len_
    min_num, food_list = heapq.heappop(food_hq)
    remain_num = min_num
    rotation = remain_time // num_food
    while rotation >= remain_num and len(food_hq) > 0:
        remain_time -= num_food * remain_num
        for food in food_list:
            food_exist[food] = False
        num_food -= len(food_dict[min_num])
        new_min_num, food_list = heapq.heappop(food_hq)
        remain_num = new_min_num - min_num
        rotation = remain_time // num_food
        min_num = new_min_num

    if rotation >= remain_num:
        return -1
    remain_time -= rotation * num_food
    
    idx = -1
    answer = 0
    while answer <= remain_time:
        idx += 1
        if food_exist[idx]:
            answer += 1

    return idx+1
