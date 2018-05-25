from collections import Counter

mylist = ['Tom', 'Barbara', 'Tom', 'Jerry', 'Jerry', 'Tom', 'Mher']
c = Counter(mylist)
print(c.most_common(1))
