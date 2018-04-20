Day 1 - [Here](https://rameshbalan.github.io/Python-Course/Day1) 
Day 2 - [Here](https://rameshbalan.github.io/Python-Course/Day2) 
Day 3 - [Here](https://rameshbalan.github.io/Python-Course/Day3)
Day 4 - [Here](https://rameshbalan.github.io/Python-Course/Day4)
Day 5 - [Here](https://rameshbalan.github.io/Python-Course/Day5)
Day 6 - [Here](https://rameshbalan.github.io/Python-Course/Day6)
Day 7 - [Here](https://rameshbalan.github.io/Python-Course/Day7)
Day 8 - [Here](https://rameshbalan.github.io/Python-Course/Day8)


# Basic Linux Commands

Last week we learnt **ls, pwd** and **cd**. Lets learn few more commands which will help in understanding more about linux.

```shell
$mkdir
$rmdir
$touch
$rm
$cp
$mv
```

## Linux directory structure

![](filesystem-structure.png)

## Linux Boot process

![](linux-boot-process.png)

## Absolute paths vs Relative paths

**What is a path?**  
A path is a unique location to a file or a folder in a file system of an OS. A path to a file is a combination of / and alpha-numeric characters.

**What is an absolute path?**  
An absolute path is defined as the specifying the location of a file or directory from the root directory(/). In other words we can say absolute path is a complete path from start of actual filesystem from / directory. For example

```shell
$cd /home/dinosaur/Desktop/my_file.txt
```

**What is the relative path?**  
Relative path is defined as path related to the present working directory(pwd). Suppose I am located in /home/dinosaur and I want to change directory to /home/dinosaur/Downloads. I can use relative path concept to change directory to kernel.

```shell
$pwd
/home/dinosaur
$cd ./Downloads/songs/rock/
$pwd 
/home/dinosaur/Downloads/songs/rock
```

## Shortcuts to remember:

Comes in handy with cd and cp commands.

|S.No.| Symbol | Description
|:----|:-------|:-------------------------------------------
|1.   | .      | This directory/ Present directory (Period)
|2.   | ..     | One directory up the hierarchy (Double Dot)
|3.   | -      | Previous location (Hyphen)
|4.   | ~      | Home (Tilde)

For example:  

```shell
$pwd 
/home/dinosaur/Downloads/songs/rock
$cd ../../../
$pwd
/home/dinosaur
```

# Python 

Online python [interpreter](http://www.compileonline.com/execute_python3_online.php)

## Data types

They are differrent data types in python.Last week we discussed three data types which are str(), int() and float(). This week we will learn about lists and dictionary which are frequently used.

### List

List is a datatype available in Python which can be written as a list of comma-separated values between square brackets. A major feature of a list is that items in a list need not be of the same datatype.

A list is declared as follows:

```python
list =[]
```

Here is an example of list:

```python
list = ["Biology", "Physics", "Chemistry", 4, 5, 6]
print list
"Biology", "Physics", "Chemistry", 4, 5, 6
```

Last week we used a function called input() using which user enters a particular information.

```python
name = input("What's your name?\n")
Dinosaur
print(name)
Dinosaur
```

Now, remember, all the strings and lists are indexed in python and the indexing starts from 0. It means

```python
name[0]
"D"
name[1]
"i"
list[0]
"Biology"
list[3]
4
```

### Dictionary

Dictionary is a useful datatype where the values are stored as `key:value` pairs. An example will help in understanding this data type better.

A dictionary is declared as follows:

```python
dictionary = {}
```

Example:

```python
GC_content = {45:"ATGATGCTAGCTAGCTAGCATGCAT", 0 :"ATATATATATTATTTTATATATATATATA", 49 : "CTAGTGCATGCTAGCTAGCTAGCTAGCTAGTCGTAGCTAGTCGATCGTACT", 64 : "GCAGCAGCAGCGCGTGCTAGCAGCAGCGCAGCTGCTAGTCGATCGTA", 50:"GCAGCAGCAGCGCGTGCTAGCAGCAGCGCAGCTGCTAGTCGATCGTA", 100: "GCGCGCGCGCGCGCGCCCCGGGGCGCGCGCGCGCGGGG"}
print(GC_content[45])
"ATGATGCTAGCTAGCTAGCATGCAT"
```

What's the difference between lists and dictionaries? 

A list is an ordered sequence of objects, whereas dictionaries are unordered sets. But the main difference is that items in `dictionaries are accessed via keys and not via their position/index`.

#### Challenge:

For the given a nucleotide sequence and four integers a, b, c and d. Extract regions from a through b and c through d.

```python
nucleotide = "ATGCTATATCGGCTACTACGTAGCTAGTCGATGCTAGTCGA"
a = 3
b = 9
c = 6
d = 15
```

**Optional:** Make it better by obtaining the sequence and numbers from the user.

#### Expected Result
```python
Desired Sequence from 3 to 9 is GCTATAT
Desired Sequence from 6 to 15 is ATATCGGCTA
```

*HINT: Think in terms of list and index/position*
