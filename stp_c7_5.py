nums_1 = [8, 19, 148, 4]
nums_2 = [9, 1, 33, 83]

product = []

for nums1 in nums_1:
	for nums2 in nums_2:
		product.append(nums1 * nums2)
		
print(product)
