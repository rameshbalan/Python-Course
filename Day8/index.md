## Regular Expression (Regex) - Part II

Last week, we had an introduction to regular expression. We imported re module, we searched for patterns using `re.search()` function. We also understood about alternators, character grouping and quantifiers which are used for pattern searching. Here is a table summarizing all the concepts discussed so far.

|S.No |Identifier|Purpose|
|:----:-------:-------|
|1.   |&#x7c; |Alternator|
|2.|?|Preceding character Zero or One times|
|3.|+|Preceding character One or More times|
|4.|*|Preceding character Zero or More times|
|5.|[...]|Group of characters out of which, one is matched|
|6.|{..}|Matching a specific number of times, preceding character occurs|
|7.|{..**,**..}|Matching a range of values in which preceding character occurs|

Moving on, this week we will learn two more identifiers.

|S.No |Identifier|Purpose|Example|
|:----:-------:-------:----|
|8.   |^ |Matches the pattern at starting positions only|`^TTT` matches **TTT**AAA but not AAA**TTT**AAA|
|9.|$|Matches the pattern at the end positions only|`TTT$` matches AAA**TTT** but not TTTAAAA**TTT**AAA|

Similar to `re.search()`, we have `re.match` which will match a pattern as a complete string, whereas `re.search` will match the pattern anywhere in the string.
