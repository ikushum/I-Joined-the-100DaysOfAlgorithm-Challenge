#!/bin/python3

t = int(input().strip())
for a0 in range(t):
    N = int(input().strip())
    prices = list(map(int, input().strip().split(' ')))
    
    if N == 0 or N == 1:
        print(0)
    else:
        # find max value, set everything before it to -1
        max_pos = prices.index(max(prices))
        opt_sol = [-1]*max_pos
        opt_sol.append(max_pos)
        
        while (max_pos < len(prices)-1):
            #print(prices[max_pos+1:])
            #print(max(prices[max_pos+1:]))
            new_max_pos = prices[max_pos+1:].index(max(prices[max_pos+1:]))
            max_pos += new_max_pos + 1
            
            opt_sol = opt_sol + [-1]*new_max_pos
            opt_sol.append(new_max_pos)

    # calculate max_stock            
    max_stock = 0
    #print(opt_sol)
    for b in range(len(prices)):
        max_stock += prices[b] * opt_sol[b]
                
    print(max_stock)