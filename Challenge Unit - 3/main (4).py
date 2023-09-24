def linearSearchProduct(productList, targetProduct):
  indices = [] 

  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)

  return indices


products = ["pencil", "book", "pencil", "dress", "sandal", "pencil"]
target = "pencil"
result = linearSearchProduct(products,target)
print(result)