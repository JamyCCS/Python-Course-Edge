input_text = input("Paste your text here >>>   ")
input_text = input_text.lower()
input_text = input_text.replace(",", " ")
input_text = input_text.replace(".", " ")
input_text = input_text.replace("?", "")
input_text = input_text.replace("'", "")
word_list = input_text.split()

print(f"Total words: {len(word_list)}\n")

count_dict = {}
for word in word_list:
    if word in count_dict:
        count_dict[word] += 1
    else:
        count_dict[word] = 1

        
print(f"There are {len(count_dict.keys())} unique words available in the text\n")


max_word = ''
max_count = 0
for i in count_dict:
    if count_dict[i]>max_count:
      max_count=count_dict[i]
      max_word=i
if max_count == 1:
    print("All words appeared only once\n")
else:
    print(f"Most frequent word is '{max_word}' and it appeared {max_count} times\n")