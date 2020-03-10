numberlist=[56,78,34,21,56,34,125,45,89,75,12,56]
print(sum(numberlist))
#this put the numbers in acending order
numberlist.sort()
print(numberlist)
#this is th=to remove number that appear more than once in the list
numberlist= list(dict.fromkeys(numberlist))
print(numberlist)

