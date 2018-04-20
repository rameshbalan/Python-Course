[Day-1](https://rameshbalan.github.io/Python-Course/Day1) 
[Day-2](https://rameshbalan.github.io/Python-Course/Day2) 
[Day-3](https://rameshbalan.github.io/Python-Course/Day3) 
[Day-4](https://rameshbalan.github.io/Python-Course/Day4) 
[Day-5](https://rameshbalan.github.io/Python-Course/Day5) 
[Day-6](https://rameshbalan.github.io/Python-Course/Day6) 
[Day-7](https://rameshbalan.github.io/Python-Course/Day7) 
[Day-8](https://rameshbalan.github.io/Python-Course/Day8) 

## Regular Expression (Regex) - Part II

Last week, we had an introduction to regular expression. We imported re module, we searched for patterns using `re.search()` function. We also understood about alternators, character grouping and quantifiers which are used for pattern searching. Here is a table summarizing all the concepts discussed so far.

|S.No |Identifier|Purpose|
|:----:-------:-------|
|1.   |&#x7c; |Alternator|
|2.|?|Preceding character Zero or One times|
|3.|+|Preceding character One or More times|
|4.|*|Preceding character Zero or More times|
|5.|[...]|Group of characters out of which, one is matched|
|6.|{...}|Matching a specific number of times, preceding character occurs|
|7.|{..**,**..}|Matching a range of values in which preceding character occurs|

Moving on, this week we will learn two more identifiers.

|S.No |Identifier|Purpose|Example|
|:----:-------:-------:----|
|8.   |^ |Matches the pattern at starting positions only|`^TTT` matches **TTT**AAA but not AAA**TTT**AAA|
|9.|$|Matches the pattern at the end positions only|`TTT$` matches AAA**TTT** but not TTTAAAA**TTT**AAA|

Similar to `re.search()`, we have `re.match()` which will match a pattern as a complete string, whereas `re.search()` will match the pattern anywhere in the string.

## Extracting part of the string that matched:

Now, let us focus on `re.search()`. `re.search()` function matches a particular pattern and returns an *match object*. Using this object, different functions can be used to identify features such as  
1. The location of the pattern in the string.
2. The number of times each pattern that occurs in the string.
3. Start and stop position of the pattern in the string and so on...

One such method is called the `group()` method. If we use this `group()` function on the  *match object*, we can identify the pattern that matched. For example, here is a code from last week

```python
import re
dna = "ACTGATCGTAGCTCGTGAATTCACACGAA"
if re.search(r"GC[ATGC]GC", dna):
  print("Restriction Enzyme Site found!!!")
```

The code snippet above matches one of the following, `GCAGC` or `GCTGC` or `GCGGC` or `GCCGC`. To find out the exact pattern,

```python
import re
dna = "ACTGATCGTAGCTCGTGAATTCACACGAA"
m = re.search(r"GA([ATGC]{3})AC", dna)
print("Entire Pattern" + m.group())
```
If the pattern has more than one unknown parts, we can extract them by using `group(1)`, `group(2)`and so on. For example,

```python
import re
dna = "ACTGATCGTAGCTCGTGAATTCACACGAA"
m = re.search(r"GA([ATGC]{3})([ATGC]{2})AC", dna)
print("Entire Pattern :" + m.group())
print("First Bit of pattern :" + m.group(1))
print("Second Bit of pattern :" + m.group(2))
```

Here, notice the use of parentheses. Identifying the unknown bits in pattern by use of parenthesis is called *capturing*.

## Finding the position of the match
The match object can be used to identify the position of the pattern in a long string. Position is identified using `start()` and `stop()` function.

```python
import re
dna = "ACTGATCGTAGCTCGTGAATTCACACGAA"
m = re.search(r"GA([ATGC]{3})([ATGC]{2})AC", dna)
print("Entire Pattern :" + m.group())
print("Pattern start position:" + str(m.start()))
print("Pattern end position:" + str(m.end()))
```

Identical to *capturing* in `group()` function, `start()` and `end()` functions also support the use of parenthesis.

```python
import re
dna = "ACTGATCGTAGCTCGTGAATTCACACGAA"
m = re.search(r"GA([ATGC]{3})([ATGC]{2})AC", dna)
print("Entire Pattern :" + m.group())
print("Pattern start position:" + str(m.start()))
print("Pattern end position:" + str(m.end()))
print("First Bit start position:" + str(m.start(1)))
print("First Bit end position:" + str(m.end(1)))
print("Second Bit start position:" + str(m.start(2)))
print("Second Bit end position:" + str(m.end(2)))
```

## Splitting a string using regular expression
A string can be split using a pattern. This is made possible with the use of `re.split()` function.

```python
import re
dna = "ACTNGCATRGCTACGTYACGATSCGAWTCG"
split_strings = re.split(r"[^ATGC]", dna)
print(split_strings)
```

## Finding Multiple matches

So far, all the functions that we learnt finds only the first occurrence of the pattern. However, if we have to *find all* the occurrence of the pattern, we can use `re.findall()` function.

```python
import re
dna = "ATATATGCGCGCGATGCATGCATCGTAGCTAGCTATATATTATATATTAGCTGCGCGCGCTAGCTAGATTACCTAGCTAGCATCGTATATATATATCGCTAGCTACTACT"
pattern = re.findall(r"[AT]{6,100}",dna)
print(pattern)
```
Since `re.findall()` function returns a list of string object, the exact start and stop position of the pattern can not be identified. To do something more complicated than just identifying the pattern, we can use `re.finditer()` function. This function returns a list of match object instead of string object. Hence, `start()`, `stop()` and other function can be applied.

```python
import re
dna = "ATATATGCGCGCGATGCATGCATCGTAGCTAGCTATATATTATATATTAGCTGCGCGCGCTAGCTAGATTACCTAGCTAGCATCGTATATATATATCGCTAGCTACTACT"
pattern = re.finditer(r"[AT]{6,100}",dna)
for match in pattern:
  match_start = match.start()
  match_end = match.end()
  print("AT rich region starts from" + str(match_start) +"to"+ str(match_end))
```

## Practice Space:

<iframe src="https://trinket.io/embed/python3/ef42646a7d" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

## Challenge:
### Accession names
Here's a list of made-up gene accession names:
xkn59438, yhdck2, eihd39d9, chdsye847, hedle3455, xjhd53e, 45da, de37dp.  
Write a program that will print only the accession names that satisfy the following criteria – treat each criterion separately:  
• contain the number 5  
• contain the letter d or e  
• contain the letters d and e in that order  
• contain the letters d and e in that order with a single letter between them  
• contain both the letters d and e in any order
• start with x or y  
• start with x or y and end with e  
• contain three or more numbers in a row  
• end with d followed by either a, r or p  

### Double digest
Use [dna.txt](dna_sequence.txt) which contains a made-up DNA sequence. Predict the fragment lengths that we will get if we digest the sequence with two made-up restriction enzymes – AbcI, whose recognition site is ANT\*AAT, and AbcII, whose recognition site is GCRW\*TG (asterisks indicate the position of the cut site).
