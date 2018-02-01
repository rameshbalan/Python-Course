# Linux

## List of linux commands and its function

### So far...
| S.No. | Command | Function  
|:------|:--------|:---------  
|1.     |mkdir    |  
|2.     |rmdir    |  
|3.     |touch    |  
|4.     |rm       |  
|5.     |cp       |  
|6.     |mv       |  
|7.     |ls       |  
|8.     |pwd      |  
|9.     |cd       |  

### Shortcuts with cd

|S.No.| Symbol | Description
|:----|:-------|:-------------------------------------------
|1.   | .      | This directory/ Present directory (Period)
|2.   | ..     | One directory up the hierarchy (Double Dot)
|3.   | -      | Previous location (Hyphen)
|4.   | ~      | Home (Tilde)

### This week  

| S.No. | Command | Function  
|:------|:--------|:--------- 
|10.    |ssh      |  
|11.    |echo     |  
|12.    |head     |  
|13.    |tail     |  
|14.    |cat      |  
|15.    |scp      |  

### Linux Challenge

1. Rename a file without affecting the contents of the file using the command(s) learnt so far.
2. Copy the renamed file from your system to the server using *scp* command.
3. Print the first 10 lines of the renamed file opening it from the server.
4. Rename this file as *results.txt* and copy it from server to your local system.

# Python

Last week we discussed lists and dictionaries in python. We also learnt about position and indexing in lists and strings.

*Remember*:  

* Strings are immutable in python whereas lists are mutable.

**What does this mean?**

Lets try the following example.

```python
subjects = ["Biology", "Physics", "Chemistry", 4, 5, 6]
name = "Dinosaur"
```

What is the data type of *subjects* and *name* ?  
Try the following commands and explain what you see.

```python
subjects[3] = "Statistics"
name[3] = "a"
```

## Condition statements

Condition statements are if and else statements. To test multiple conditions, if, elif and else are used. Depending on the number of conditions the number of elif statements can be increased in the program.

**Observe the Syntax for if and else statements**

```python
a = 5
b = 7
if a < b:
  print(a,"is greater than",b)
else:
  print(a,"is smaller than",b)
```

**For if, elif and else**

```python
a = 5
b = 7
if a < b:
  print(a,"is greater than",b)
elif a == b:
  print(a,"is equal to", b)
else:
  print (a,"is smaller than",b)
```

## Comparision operators

| S.No. | Operator | Function  
|:------|:---------|:--------- 
|1.    |  >       |  Greater than
|2.    |  >=      |  Greater than or equal to
|3.    |  <       |  Lesser than
|4.    |  <=      |  Lesser than or equal to
|5.    |  ==      |  Equal to
|6.    |  !=      |  Not Equal to

## Membership operators

| S.No. | Operator | Function  
|:------|:---------|:--------- 
|1.     |   in     | True if it Hinds a variable in the speciHied sequence and false otherwise.
|2.     |   not in | True if it does not Hinds a variable in the speciHied sequence and false otherwise.

For example:

```python
dna=input('Enter DNA sequence:')
if 'n' in dna :
   nbases=dna.count('n')
   print("dna sequence has %d undefined bases " % nbases)
else:
   print("dna sequence has no undefined bases")
```

##Logical Operators

| S.No. | Operator | Function  
|:------|:---------|:--------- 
|1.     |   and    | True if both conditions are true
|2.     |   or     | True if at least one condition is true
|3.     |   not    | True if condition is false

```python
dna=input('Enter DNA sequence:')
if 'n' in dna :
   print("dna sequence has undefined bases ")
elif ‘N’ in dna :
   print("dna sequence has undefined bases ")
else:
   print("dna sequence has no undefined bases")
```

Now using logical operator

```python
dna=input('Enter DNA sequence:')
if 'n' in dna or ‘N’ in dna:
   nbases=dna.count('n')+dna.count(‘N’)
   print("dna sequence has %d undefined bases " % nbases)
else:
   print("dna sequence has no undefined bases")
```


### Challenge

1. Find the GC content of a given nucleotide sequence. If GC content is between 40% - 60% display "Suitable candidate for primer".

2. Create a BMI calculator. Obtain the user's height and weight. Calculate the BMI and inform the user of his BMI category.