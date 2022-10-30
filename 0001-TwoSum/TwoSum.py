def twoSumHash(nums, target):
	hashTable = dict()
	pair = []
	i = 0
	foundPair = False

	while i < len(nums):
		hashTable[nums[i]] = i
		i += 1

	i = 0

	while i < len(nums) and not foundPair:
		compliment = target - nums[i]
		if compliment in hashTable:
			if i != hashTable[compliment]:
				pair.append(i)
				pair.append(hashTable[complement])