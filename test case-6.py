#35.Text Compression Using Character Runs
text = input("Enter string: ")

result = ""
count = 1

for i in range(len(text)-1):
    if text[i] == text[i+1]:
        count += 1
    else:
        result += text[i] + str(count)
        count = 1

result += text[-1] + str(count)
print("Compressed:", result)
