 
def getMaxLength(arr, n): 

	# intitialize count 
	count = 0
	
	# initialize max 
	result = 0

	for i in range(0, n): 
	
		# Reset count if 0 is found 
		if (arr[i] == 0): 
			count = 0

		# If 1 is found, increment count and update result 
		else: 
			
			# increase count 
			count+= 1
			result = max(result, count) 
		
	return result 

# Driver code 
arr = [1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1] 
n = len(arr) 

print(getMaxLength(arr, n)) 


