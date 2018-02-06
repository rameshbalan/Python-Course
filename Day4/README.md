# Linux  
## List of linux commands  
### So far...

| S.No. | Command | Function  
|:------|:--------|:--------------------------------------------------------------------------  
|1.     |  mkdir  |  make a new directory  
|2.     |  rmdir  |  remove an empty directory  
|3.     |  touch  |  create a new file  
|4.     |  rm     |  remove a file  
|5.     |  cp     |  copy a file  
|6.     |  mv     |  move/rename a file  
|7.     |  ls     |  list the contents of a directory  
|8.     |  pwd    |  present working directory  
|9.     |  cd     |  change directory  
|10.    |ssh      | Secure Shell - helps gain access to a remote server via secure channel  
|11.    |echo     | Equivalent of print() function in python  
|12.    |head     | Displays the first 10 lines of a file  
|13.    |tail     | Displays the last 10 lines of a file  
|14.    |cat      | Displays the entire contents of a file 
|15.    |scp      | Secure Copy - helps to copy/transfer files between host and server  
|16.    |>        | Redirection Operator  
|17.    |chmod    | Change Mode - used to change file permissions  

#### Shortcuts with cd

|S.No.| Symbol | Description
|:----|:-------|:-------------------------------------------
|1.   | .      | This directory/ Present directory (Period)
|2.   | ..     | One directory up the hierarchy (Double Dot)
|3.   | -      | Previous location (Hyphen)
|4.   | ~      | Home (Tilde)

### This week

| S.No. | Command | Function  
|:------|:--------|:--------------------------------------------------------------------------------- 
|18.    |grep     |Matches pattern and returns the matching lines/number of lines/non matching lines.
|19.    |awk      |Pattern searching and processing language. Powerful as a complete language.
|20.    |sed      |Basic text transformation on a input line or file.

General usage of *grep, awk* and *sed*:

```
grep "pattern" filename
awk '{function}' filename
sed 's/word.to.replace/replacing.word/' filename
```

#### Some options with grep

|S.No.| Option | Description
|:----|:-------|:-----------------------------------------------
|1.   |n       | line number
|2.   |v       | All others except search pattern (Negation)
|3.   |c       | Count the number of lines with matching pattern
|4.   |l       | File name of the matching files
|5.   |i       | Case insensitive
|6.   |x       | Exact matches only
|7.   |E       | Used to search for regular Expressions

#### Some options with awk

|S.No.| Option | Description
|:----|:-------|:-----------------------------
|1.   |F       | (Input) Field separator
|2.   |OFS     | Output Field Separator
|3.   |$0      | All columns

```
awk '{print $1,$2,$3}' file.txt
ls -l| awk 'BEGIN {sum=0} {sum=sum+$5} END {print sum}'
```

#### Some options with sed

|S.No.| Option | Description
|:----|:-------|:--------------------
|1.   |e       | match pattern
|2.   |n       | line number
|3.   |i       | Case insensitive

Frequently Used flag in sed is **g** in the expression

```
sed -ei 's/U/X/g' protein-sequence.txt
```

# Python

So far we have seen Data types (int, str, float), Data Structures (list and dictionary) and Condition statements (if, elif and else). Today we will see tuples which is another data structure and looping (for and while loops) in python.

## Tuples

Tuples are similar to lists. They can hold different data types and structures. All the elements in the tuples are indexed like list. But a crucial difference between a tuple and a list is that the tuples are **immutable**. This feature makes tuple an asset when dealing with nucleotide and protein sequences.  

General Usage:

Assigning a tuple to a variable  
```python
tuple = ()
```

Example of a tuple  

```python
tuple = ("ATGCATGCAGCATC", "RHGLYHGRYLYCHRGL", ["DNA","RNA",4], 576)
```

### Challenge:

Extract "RNA" from the tuple.

## Loops
Loops are of immense help when it comes to doing a repetitive work for an entire file/ sometimes directory. We can iterate using two loops. They are *for* loop and *while* loop.

## while loop

The while loop repeats a block of commands/instructions as long as a given condition is True. Each repetition is called an iteration of the loop.

```python
n = 1

while n < 4:
	print(n)
	n = n + 1
```
```python
num = 1

while num <= 10:
    print(num)
    num += 1
```

General Syntax:

```python
loop_condition = True

while loop_condition:
    print("Loop Condition keeps: %s" %(loop_condition))
    loop_condition = False
```


## for loop

The for loop is another way to iterate over a list or a file or over a range of values. A for loop automatically assigns a variable to the current element being iterated on.

```python
for i in range(1, 11):
  print(i)
```

In the code above, the variable **i** is a placeholder for the element currently being iterated on.

## with open as 

open() - Opens the file
The function open takes two argument. One is the name or the path to the file. The second argument is the mode in which the file should be opened.

There are three modes.

r - read
w - write
a - append

So the general syntax is 

```python
with open ("DNA.sequence.file.fasta", 'r') as infile:
  for line in infile:
    print line
```
