#set operators
>>> lows = set([0, 1, 2, 3, 4])
>>> odds = set([1, 3, 5, 7, 9])
>>> lows - odds
{0, 2, 4}
>>> lows & odds
{1, 3}
>>> lows <= odds
False
>>> lows >=odds
False
>>> lows | odds
{0, 1, 2, 3, 4, 5, 7, 9}
>>> lows ^ odds
{0, 2, 4, 5, 7, 9}