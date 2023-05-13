# CSV Iterator

The CSV iterator is a small python application that generates an iterator over all possible combinations of elements from a provided CSV file.

# How to run

Simply run `py main.py`

## Files

The program requires an input file in the form of a csv. This should be stored in the data folder. Modify line 18 of the **main.py** file to match the input file you wish to use.

The program will output a csv to the same data folder.

## Function

`generate_combinations` is a static method of the `CombinationGenerator` class. You don't need an instance of `CombinationGenerator` to use this method; you can call it directly from the class like so: `CombinationGenerator.generate_combinations(data)`

The method itself uses the `itertools.product` function to generate a Cartesian product of input iterables, which in this case is the `data` list of lists. This will create all possible combinations by picking one element from each list.

The `*data` syntax is used to unpack the argument list. So `itertools.product(*data)` is equivalent to `itertools.product(data[0], data[1], ..., data[n])` for a `data` list of `n` elements.

The type hint `Iterator` indicates that the function returns an iterator, which is a type of object you can iterate over (like in a for loop). The `List[List[str]]` indicates that the function expects a list of lists of strings as input.

## Use Cases

### Solving Dice Combinations

The intended use was to solve every possible combination of a set of dice. There would be a row for each dice, and each value (face) would be seperated with a comma.

### Test Scenarios

It would also be useful for building test cases, you could use it to generate unique test cases for software and web development. For example, if you were testing a log in page:

    Correct Email, Incorrect Email
    Correct Password, Incorrect Password
    Firefox, Edge, Chrome, iOS, Android

Would return

    Correct Email,Correct Password, Firefox
    Correct Email,Correct Password, Edge
    Correct Email,Correct Password, Chrome
    Correct Email,Correct Password, iOS
    Correct Email,Correct Password, Android
    Correct Email, Incorrect Password, Firefox
    Correct Email, Incorrect Password, Edge
    Correct Email, Incorrect Password, Chrome
    Correct Email, Incorrect Password, iOS
    Correct Email, Incorrect Password, Android
    Incorrect Email,Correct Password, Firefox
    Incorrect Email,Correct Password, Edge
    Incorrect Email,Correct Password, Chrome
    Incorrect Email,Correct Password, iOS
    Incorrect Email,Correct Password, Android
    Incorrect Email, Incorrect Password, Firefox
    Incorrect Email, Incorrect Password, Edge
    Incorrect Email, Incorrect Password, Chrome
    Incorrect Email, Incorrect Password, iOS
    Incorrect Email, Incorrect Password, Android
