#17.Student Performance Trend Analysis
test1 = int(input("Test 1 marks: "))
test2 = int(input("Test 2 marks: "))

if test2 > test1:
    print("Improved by", test2 - test1)
elif test2 < test1:
    print("Declined by", test1 - test2)
else:
    print("No change")
