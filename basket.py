def CalcTotalPrice(allItems):
	totalPrice = 0.0

	for item in allItems:
		totalPrice += item["itemTtlPrice"]

	return totalPrice
