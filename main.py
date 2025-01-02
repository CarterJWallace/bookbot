def count_characters(text):
    out = {}
    for char in text.lower():
        if char in out:
            out[char] = out[char] + 1
        else:
            out[char] = 1
    return out

def number_words(text):
    words = text.split()
    return len(words)

def main():
    test_book = "books/frankenstein.txt"
    with open(test_book) as f:
        file_contents = f.read()
        print(f"--- Begin report of {test_book} ---")
        print(f"{number_words(file_contents)} words found in the document")
        char_dict = count_characters(file_contents)
        for char in dict(sorted(char_dict.items(), key=lambda item:item[1], reverse=True)):
            if char.isalpha():
                print(f"The '{char}' character was found {char_dict[char]} times")
        print("--- End report ---")

main()
