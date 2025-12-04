class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buy_log, sell_log = [], []  # list of (price, size)
        for price, amount, orderType in orders:
            # process buy order
            if orderType == 0:
                # continue matching
                while amount and sell_log and sell_log[0][0] <= price:
                    batch_size = min(amount, sell_log[0][1])
                    amount -= batch_size
                    
                    if batch_size < sell_log[0][1]:
                        sell_log[0][1] -= batch_size
                    else:
                        # may need to continue processing w/ next sell order batch
                        heappop(sell_log)
                
                # add remaining orders to buy log
                if amount:
                    heappush(buy_log, [-price, amount])

            # process sell order
            elif orderType == 1:
                # continue matching
                while amount and buy_log and -buy_log[0][0] >= price:
                    batch_size = min(amount, buy_log[0][1])
                    amount -= batch_size
                    
                    if batch_size < buy_log[0][1]:
                        buy_log[0][1] -= batch_size
                    else:
                        # may need to continue processing w/ next buy order batch
                        heappop(buy_log)
                
                # add remaining orders to sell log
                if amount:
                    heappush(sell_log, [price, amount])

        print(buy_log)
        print(sell_log)

        res = 0
        for _, amount in buy_log:
            res += amount
        for _, amount in sell_log:
            res += amount

        return res % (10**9 + 7)


"""
problem notes:
- input is a list of orders to be executed
- create a backlog and add to it based on the rules
    - backlog for both buy and sell orders
- a buy order is matched w/ a sell order if
 sell order price <= buy order price
- a sell order is matched w/ a buy order if
  buy order price >= sell order price

initial thoughts (brute force solution):
- create backlogs
    - one entry for each order (no batches)
- for each order, process them one at a time O(n*k)
- processing steps:
    - find max or min of other type O(k)
    - check if match can be made
    - add/remove from backlogs accordingly
Time: O(n*k^2)
    - n is number of batch orders
    - k is order amount
    - possible that k >> n 

optimizations:
- create backlogs as heaps
    - max heap for buy orders
    - min heap for sell orders
    - one entry for each batch
- for each order, process them in batches O(n)
    - batch size will be min of current order
      and corresponding order in backlog
    - may require processing multiple batches for order
- processing steps:
    - find max or min of other type O(1)
    - check if match can be made
    - add/remove from backlogs accordingly
        - update batch size if backlog if necessary
Time: O(n)
"""