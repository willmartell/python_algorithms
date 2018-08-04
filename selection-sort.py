import random

""" given an array and two indexes, swap the elements in place and return array """
def swap(arr1,idx1,idx2):
	arr1[idx1],arr1[idx2]=arr1[idx2],arr1[idx1]
	return 0

""" given an array and the length of the array sort the array in place """
def sel_sort(arr,n):
	for i in range(0,n):
		for j in range(0,n):
			if arr[i]<arr[j]:
				swap(arr,i,j)
	return arr


#testing
for i in xrange(random.randint(1,20)): #test up to 20 times
	b = random.sample(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],random.randint(2,26)) #create array of at least 2 up to 26 chars
	sort = sorted(b)
	my_sort = sel_sort(b,len(b))
	assert(sort==my_sort),str(sort)+"!="+str(my_sort)
