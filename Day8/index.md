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
m = re.search(r"GC[ATGC]GC", dna)
print(m.group())
```

`group(1)` `group(2)`

## Finding the position of the match
`start()` `stop()`


## Splitting a string using regular expression
`re.split()`

## Finding Multiple matches
`re.findall()`

`re.finditer()`
