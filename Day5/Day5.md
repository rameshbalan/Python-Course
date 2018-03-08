# Python

## User Defined Functions

### Why do we want to write our own functions?

Take a look back at the very first exercise in this book – the one in Day 2 where we had to write a program to calculate the GC content of a DNA sequence. Let's remind ourselves of the code:

```python
my_dna = input("Enter the DNA Sequence")
length = len(my_dna)
g_count = my_dna.count('G')
c_count = my_dna.count('C')
gc_content = (g_count + c_count) / length
print("GC content is " + str(gc_content))
```

It would be much simpler if Python had a built-in function (let's call it get_gc_content) for calculating GC content. If that were the case, then we could just run get_gc_content in the same way we run print, or len, or open. Although, sadly, Python does not have such a built-in function, it does have the next best thing – a way for us to create our own functions.

Creating our own function to carry out a particular job has many benefits. It allows us to re-use the same code many times within a program without having to copy it out each time. Additionally, if we find that we have to make a change to the code, we only have to do it in one place. Splitting our code into functions also allows us to tackle larger problems, as we can work on different bits of the code independently. We can also re-use code across multiple programs.

### Defining a function

Let's go ahead and create our get_gc_content function. Before we start typing, we need to figure out what the inputs (the number and types of the function arguments) and outputs (the type of the return value) are going to be. For this function, that seems pretty obvious – the input is going to be a single DNA sequence, and the output is going to be a decimal number. To translate these into Python terms: the function will take a single argument of type string, and will return a value of type number1. Here's the code:

```python
def get_gc_content(my_dna):
    length = len(my_dna)
    g_count = my_dna.count('G')
    c_count = my_dna.count('C')
    gc_content = (g_count + c_count) / length
    return gc_content
```

The first line of the function definition contains a several different elements. We start with the word def, which is short for define (writing a function is called defining it). Following that we write the name of the function, followed by the names of the argument variables in parentheses. Just like we saw before with normal variables, the function name and the argument names are arbitrary – we can use whatever we like.
The first line ends with a colon, just like the loops/condition statements. And just like loops, this line is followed by a block of indented lines – the function body. The function body can have as many lines of code as we like, as long as they all have the same indentation. Within the function body, we can refer to the arguments by using the variable names from the first line. In this case, the variable my_dna refers to the sequence that was passed in as the argument to the function.
The last line of the function causes it to return the GC content that was calculated in the function body. To return from a function, we simply write return followed by the value that the function should output.
There are a couple of important things to be aware of when writing functions.  
- Firstly, we need to make a clear distinction between defining a function, and running it (we refer to running a function as calling it). The code we've written above will not cause anything to happen when we run it, because we've not actually asked Python to execute the get_gc_content function – we have simply defined what it is. The code in the function will not be executed until we call the function like this:

```python
get_gc_content("ATGACTGGACCA")
```
If we simply call the function like that, however, then the GC content will vanish once it's been calculated. In order to use the function to do something useful, we must either store the result in a variable:

```python
gc_content = get_gc_content("ATGACTGGACCA")
```
or print it directly as follows:

```python
print("GC content is " + str(get_gc_content("ATGACTGGACCA")))
```

- Secondly, it's important to understand that the argument variable my_dna does not hold any particular value when the function is defined. Instead, its job is to hold whatever value is given as the argument when the function is called. In this way it's analogous to the loop variables we saw earlier: loop variables hold a different value each time round the loop, and function argument variables hold a different value each time the function is called.

- Finally, be aware that the same scoping rules that applied to loops also apply to functions – any variables that we create as part of the function only exist inside the function, and cannot be accessed outside. If we try to use a variable that's created inside the function from outside **we'll get an error**.

## Challenges

1. Write a function that takes two arguments - two numbers and returns its sum.  
2. Write a function that takes two arguments – a protein sequence and an amino acid residue code – and returns the percentage of the protein that the amino acid makes up.  
