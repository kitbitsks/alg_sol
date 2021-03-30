# Space : O(n), Time : O(2^n)
def getNthFib(n):
	if n == 1:
		return 0
	if n == 2:
		return 1
	return (getNthFib(n-1) + getNthFib(n-2))

# Space: O(n), Time : O(n)
def getNthFib(n, cache = {1:0,2:1}):
    if n in cache:
		return cache[n]
	else:
		cache[n] = getNthFib(n-1,cache) + getNthFib(n-2,cache)
		return cache[n]

# Space: O(1), Time: O(n)
def getNthFib(n):
	updatedValue = 0
	first = 0
	second = 1
	counter = 0
	if n == 1:
		return first
	if n == 2:
		return second
	while counter != n-2:
		updatedValue = first + second
		first = second		
		second = updatedValue
		counter += 1
	return updatedValue
