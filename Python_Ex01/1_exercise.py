txt = input("Please Enter Text: ")
char_count = {}
for char in txt:
    if char != " ":
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1

      
print("+------+-----------+")
print("| Name | Frequency |")
print("+======+===========+")
for char, count in char_count.items():
    print("|{:<5} |          {:<1}|".format(char, count))
    print("+------+-----------+")