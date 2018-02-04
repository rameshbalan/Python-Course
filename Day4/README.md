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

