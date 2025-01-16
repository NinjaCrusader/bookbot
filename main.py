# Reading the file so we only have to do it once

with open("books/frankenstein.txt") as f:
    file_contents = f.read()

#func to print the book to console

def main(input):
    return input

#func to count how many words are in the book

def count(input):
    words = input.split()
    return len(words)

#func to handle counting the characters and how many times they show up in the book.

def char_count(input):
    char_counter = {}
    lower_words = input.lower()
    for w in lower_words:
        if w.isalpha():
            if w not in char_counter:
                char_counter[w] = 1
            else:
                char_counter[w] += 1
    return char_counter
    
    


#report formatting

main_result = main(file_contents)
count_result = count(file_contents)
char_count_result = char_count(file_contents)

#this bit will handle sorting

chars_list = []

for char, count_value in char_count_result.items():
    chars_list.append({"char": char, "num": count_value})

#func to sort chars_list

def sort_on(dict):
    return dict["num"]

chars_list.sort(reverse=True, key=sort_on)

print("--- Begin report of books/frankenstein.txt ---")
print(f"{count_result} words found in the document")
print()
for char_dict in chars_list:
    print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")
print(f"--- End report ---")

     

