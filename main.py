import sys
if len(sys.argv)!=2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)
path_to_book = sys.argv[1]
from stats import words_count, count_char, sort_list

def get_book_text(filepath):
	with open(filepath) as f:
		return f.read()

def main():
	book_text = get_book_text(path_to_book)

	number_of_words = words_count(book_text)
	print(f"Found {number_of_words} total words")
	count = count_char(book_text)
	items = sort_list(count)

	for item in items:
		ch = item["char"]
		if ch.isalpha():
			print(f"{ch}: {item['num']}")

main()
