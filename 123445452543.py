with open("aaaa.jpg", "rb") as file:
	content = file.read()
res = b''
res += content
print(len(res))

with open("123331.jpg", "wb") as file:
	file.write(res)