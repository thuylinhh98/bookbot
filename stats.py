def words_count(s):
	return len(s.split())

def count_char(text: str):
	text = text.lower()
	counts = {}
	for ch in text:
		counts[ch] = counts.get(ch,0) + 1
	return counts

def sort_list(dictionary):
	result = []
	for k, v in dictionary.items():
		result.append({"char":k, "num":v})
	result.sort(reverse = True, key=lambda item:item["num"])
	return result

