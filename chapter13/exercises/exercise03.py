"""Binary search is significantly faster than the built-in 
search but requires that the list is sorted. As you know, the
 running time for the best sorting algorithm is on the order of 
 N log2 N, where N is the length of the list. If we search a lot 
 of times on the same list of data, it makes sense to sort it once 
 before doing the searching. Roughly how many times do we need to 
 search in order to make sorting and then searching faster than using 
 the built-in search?"""

 """
 Answer: Sorting depending on the length varies like this
 N log_2 N . K is the number of searches to make
 N log_2 N + k*log_2 N < k * N
 N log_2 N <k * N - k * log_2 N
 N log_2 N < k(N-log_2 N)
 N log_2 N / (N - log_2 N) < k
 """




