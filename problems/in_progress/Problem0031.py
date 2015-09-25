count = 0

for two_pounds in range(200, -1, -200):
	for one_pound in range(two_pounds, -1, -100):
		for fifty_pence in range(one_pound, -1, -50):
			for twenty_pence in range(fifty_pence, -1, -20):
				for ten_pence in range(twenty_pence, -1, -10):
					for five_pence in range(ten_pence, -1, -5):
						for two_pence in range(five_pence, -1, -2):
							count += 1

print count
