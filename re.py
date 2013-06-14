import re 
Find(pat,txt):
	match = re.search(pat,txt)
	if match:
		print(match.group())
	else:
		print("not found")
	