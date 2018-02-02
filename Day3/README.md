# Linux

## List of linux commands and its function

### So far...

| S.No. | Command | Function  
|:------|:--------|:---------  
|1.     |  mkdir  |  make a new directory
|2.     |  rmdir  |  remove an empty directory
|3.     |  touch  |  create a new file
|4.     |  rm     |  remove a file
|5.     |  cp     |  copy a file
|6.     |  mv     |  move/rename a file
|7.     |  ls     |  list the contents of a directory
|8.     |  pwd    |  present working directory
|9.     |  cd     |  change directory

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
|10.    |ssh      | Secure Shell - helps gain access to a remote server via secure channel
|11.    |echo     | Equivalent of print() function in python
|12.    |head     | Displays the first 10 lines of a file 
|13.    |tail     | Displays the last 10 lines of a file 
|14.    |cat      | Displays the entire contents of a file 
|15.    |scp      | Secure Copy - help to copy/transfer files between host and server
|16.    |>        | Redirection Operator
|17.    |chmod    | Change Mode - used to change file permissions 

General format for chmod:  
chmod u+x *name_of_the_python_file*

General format for scp: from host to remote server  
scp *name_of_the_file* *username@servername:path/to/the/file*

**Example:**    
The following command copies dna.fasta file from present working directory to DNA directory under Documents in the server.    
`scp dna.fasta manager@pine64.uta.edu:~/Documents/DNA/`

General format for scp: from remote server to the host.    
scp *username@servername:path/to/the/file* *path/to/where/you/want/to/copy/*  

**Example:**   
The following command copies dna.fasta from server to present working directory.    
`scp manager@pine64.uta.edu:~/Documents/DNA/dna.fasta ./`


Here is a sample [file](https://rameshbalan.github.io/Python-Course/Day3/dna.example.fasta "Sample File") for your challenge.

### Linux Challenge

1. Rename a file without affecting the contents of the file using the command(s) learnt so far.
2. Copy the renamed file from your system to the server using *scp* command.
3. Print the first 16 lines of the renamed file opening it from the server.
4. Write these 16 lines to *results.txt*. 
5. Copy it from server to your local system.

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
  print(a,"is smaller than",b)
else:
  print(a,"is greater than",b)
```

**For if, elif and else**

```python
a = 5
b = 7
if a < b:
  print(a,"is smaller than",b)
elif a == b:
  print(a,"is equal to", b)
else:
  print (a,"is greater than",b)
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
if "n" in dna :
   nbases=dna.count("n")
   print("dna sequence has %d undefined bases " % nbases)
else:
   print("dna sequence has no undefined bases")
```

## Logical Operators

| S.No. | Operator | Function  
|:------|:---------|:--------- 
|1.     |   and    | True if both conditions are true
|2.     |   or     | True if at least one condition is true
|3.     |   not    | True if condition is false

```python
dna=input('Enter DNA sequence:')
if "n" in dna :
   print("dna sequence has undefined bases ")
elif "N" in dna :
   print("dna sequence has undefined bases ")
else:
   print("dna sequence has no undefined bases")
```

Now using logical operator

```python
dna=input('Enter DNA sequence:')
if "n" in dna or "N" in dna:
   nbases=dna.count("n")+dna.count("N")
   print("dna sequence has %d undefined bases " % nbases)
else:
   print("dna sequence has no undefined bases")
```


### Challenge

1. Find the GC content of a given nucleotide sequence. If GC content is between 40% - 60% display "Suitable candidate for primer".

2. Create a BMI calculator. Obtain the user's height and weight. Calculate the BMI and inform the user of his BMI category.
