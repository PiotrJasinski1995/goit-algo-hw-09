import sys
from collections import Counter


COINS = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(money_given):
    money_sum = money_given
    coin_possible = True
    coin_dict = {}
    
    # for coin in COINS:
    #     coin_dict[coin] = 0

    while coin_possible:
        if money_sum == 0:
            break

        for coin in COINS:
            if money_sum >= coin:
                if coin_dict.get(coin) == None:
                    coin_dict[coin] = 1
                else:
                    coin_dict[coin] += 1

                money_sum -= coin
                break

    return coin_dict


def min_dict(list_of_dicts):
    min_dict_index = 0
    max_coin_amount = sys.maxsize

    for index in range(1, len(list_of_dicts)):
        actual_dict = list_of_dicts[index]
        min_dict = list_of_dicts[min_dict_index]
        actual_coin_amount = sum(actual_dict.values()) if actual_dict else max_coin_amount
        min_coin_amount= sum(min_dict.values()) if min_dict else max_coin_amount

        if actual_coin_amount <= min_coin_amount:
            min_dict_index = index
    
    return list_of_dicts[min_dict_index]
        


def find_min_coins(V):
     
    # table[i] will be storing the minimum 
    # number of coins required for i value. 
    # So table[V] will have result
    # table = [{} for _ in range(V + 1)]
    # [[0 for w in range(W + 1)] for i in range(n + 1)]
    coins = sorted(COINS)
    coins.insert(0, 0)
    table = [[{} for _ in range(len(coins))] for _ in range(V + 1)]
    min_table = [{} for _ in range(V + 1)]
 
    # # Base case (If given value V is 0)
    # table[0] = 0
 
    # # Initialize all table values as Infinite
    # for i in range(1, V + 1):
    #     table[i] = sys.maxsize
 
    # Compute minimum coins required 
    # for all values from 1 to V
    for i in range(1, V + 1):
        if i == V:
            ala = 'ma kota'
         
        # Go through all coins smaller than i
        for j in range(1, len(coins)):
            if (coins[j] <= i):
                table[i][j][coins[j]] = 0
                table[i][j][coins[j]] = table[i][j][coins[j]] + 1
                sub_res = min_table[i- coins[j]].copy()

                if (sub_res != {}):
                     table[i][j].update(Counter(table[i][j]) + Counter(sub_res))
        
        min_table[i] = min_dict(table[i])

        
     
    # if table[V] == sys.maxsize:
    #     return -1
       
    return dict(sorted(min_table[V].items()))


# def dpChangeMoney(total, units, stored, min_ix=0):
#     if total < 0:
#         return []

#     if total == 0:
#         return [{}]

#     if min_ix == len(units):
#         return []

#     key = (total, min_ix)
#     if key in stored:
#         return stored[key]

#     sol_list = []
#     u = units[min_ix]
#     for c in range(total // u + 1):
#         sols = dpChangeMoney(total - c*u, units, stored, min_ix + 1)
#         for sol in sols:
#             if c > 0:
#                 sol2 = sol.copy()
#                 sol2[u] = c
#             else:
#                 sol2 = sol
#             sol_list.append(sol2)

#     stored[key] = sol_list
#     return sol_list


print(find_coins_greedy(113))
print(find_coins_greedy(200))
print(find_min_coins(113))
print(find_min_coins(200))
