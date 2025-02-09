def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)

    # print(f"{num_words} words found in the document")

    num_chars = get_num_chars(text)
    # print(num_chars)

    print_report(book_path, num_words, num_chars)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_chars(text):
    chars_to_counter = {}
    for char in text:
        char = char.lower()
        if char not in chars_to_counter:
            chars_to_counter[char] = 0
        chars_to_counter[char] += 1

    return chars_to_counter


def print_report(path, num_words, num_chars):
    chars_list = []
    for key in num_chars:
        if key.isalpha():
            chars_list.append({"char": key, "count": num_chars[key]})

    chars_list.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document\n")
    for row in chars_list:
        print(f"The '{row['char']}' character was found {row['count']} times")


def sort_on(dict):
    return dict["count"]


main()
