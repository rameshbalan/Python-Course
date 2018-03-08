# Answers to Challenges on Day 4

## Python

- [x] Given two numbers a and b. Find the sum of all odd numbers between the two.

```python
a = input("Starting number: \n")
b = input("Last number: \n")
i = 0
while a <= b:
	if a % 2 == 1:
		i = i + a
		a += 1
	else:
		a += 1

print "The sum of all odd numbers between the given range is %d" % (i)
```

- [x] Given a file, print only the even numbered lines from the file. Assume 1-based numbering of lines.

```python
a=input("Drag and Drop the file and Press enter\n")
my_file = open(a,'r')
all_lines=my_file.read().splitlines()
i=1
e=len(all_lines)-1
while i<=e:
	print all_lines[i]
	i += 2
my_file.close()
```

- [x] Given a string, count the number of times each word appears.


```python
from collections import Counter

a=input("Drag and Drop the file and Press enter\n")
my_file = open(a,'r')
words = my_file.read().strip().split(' ')
for key,value in dict.items(Counter(words)):
	print key, value

my_file.close()

```
