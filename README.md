# Simple Calculator

Welcome to your first big project! The goal is to make a simple calculator using everything you've learned up to this point!

Your job is to implement the code under `calculator.py`; note that we've left only placeholders for the functions. Your job is to write the body of those functions.

### Step 1:

* Add
* Subtract
* Multiply

We've set up 3 functions here that you need to finish. These are fairly straight-forward and shouldn't give you too much trouble, think back to your lesson on operators!
##### To run tests, use these commands in the command line:

```bash
# For the add() function
$ py.test test_add.py

# For the subtract() function
$ py.test test_subtract.py

# For the mulitply() function
$ py.test test_multiply.py
```

### Step 2

* Divide

You'll notice here that divide is the only function that has two tests for it - that's because you'll need to program some exceptional behavior in case the user tries to divide by 0! 

If 0 is passed as a denominator when using this function, instead of an integer, return a string warning the user not to divide by 0. You can chose any message you want, for example `return "Invalid value for denominator, cant't divide by 0!"`

```bash
$ py.test test_divide.py
```

### Step 3

* Square
* Power
* Square Root

Rounding out the last three tests are functions dealing with powers. They can be kind of tricky (especially finding the square root!) but you shouldn't have any problem if you review your lesson on operators.

```bash
$ py.test test_square.py
$ py.test test_power.py
$ py.test test_sqrt.py
```
