import sys
from collections import Counter
from timeit import default_timer as timer


COINS = [50, 25, 10, 5, 2, 1]

# defining decorator for time measuring
def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = timer()
        result = func(*args, **kwargs)
        end_time = timer()
        execution_time = end_time - start_time
        print(f"Function {func.__name__} took {execution_time:.4f} seconds to execute")
        return result
    return wrapper


@measure_execution_time
def find_coins_greedy(money_given):
    money_sum = money_given
    coin_possible = True
    coin_dict = {}

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
        

@measure_execution_time
def find_min_coins(V):
    coins = sorted(COINS)
    coins.insert(0, 0)
    table = [[{} for _ in range(len(coins))] for _ in range(V + 1)]
    min_table = [{} for _ in range(V + 1)]

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
    return dict(sorted(min_table[V].items()))


print(find_coins_greedy(113))
print(find_coins_greedy(200))
print(find_coins_greedy(345321))
print(find_min_coins(113))
print(find_min_coins(200))
print(find_min_coins(345321))
