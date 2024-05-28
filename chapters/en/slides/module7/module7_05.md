---
type: slides
---

# Working with Other Files

Notes: <br>

---

<center>

<img src='/module7/m7_1.png'  width = "90%" alt="404 image" />

</center>

Notes: We are going to talk about what to do when you have a function in
one Jupyter notebook, but you want to use it in another jupyter
notebook.

Let’s take this `exponent_a_list` function we’ve seen previously that
creates a new list containing the exponent values of the input list.

We are using this function inside our notebook called `exponents.ipynb`.

Let’s remind ourselves how it works.

---

<center>

<img src='/module7/m7_2.png'  width = "90%" alt="404 image" />

</center>

Notes:

First, we run the cell to put the function into Python’s memory, and we
take some tests that we wrote earlier and run them to make sure our
function still works.

We then execute the cell that calls the function on a list containing
the values `2`, `3`, and `4` and get the output.

---

<center>

<img src='/module7/m7_3.png'  width = "90%" alt="404 image" />

</center>

Notes:

Let’s say we want to create a new jupyter notebook.

---

<center>

<img src='/module7/m7_4.png'  width = "90%" alt="404 image" />

</center>

Notes:

We then named it `more-exp-calc.ipynb`.

---

<center>

<img src='/module7/m7_5.png'  width = "90%" alt="404 image" />

</center>

Notes:

If we call the function `exponent_a list` with the values 1, 3, and 5
inside of this notebook, it will result in an error because exponent a
list doesn’t exist in this workspace.

What can we do to solve this problem?

One thing we could do is copy and paste the function into this notebook.

This would be annoying to do that every single time that we want to use
this function.

---

<center>

<img src='/module7/m7_6.png'  width = "90%" alt="404 image" />

</center>

Notes:

Instead, we can create a python script and put the function inside that.

Then for each notebook that needs this function, we can import it
similarly to how we imported packages like pandas or Altair.

---

<center>

<img src='/module7/m7_8.png'  width = "90%" alt="404 image" />

</center>

Notes:

Let’s create a text file and rename it `exponent_a_list,` and instead of
an ending of `.txt`, we’re going to end it with `.py`.

---

<center>

<img src='/module7/m7_9.png'  width = "90%" alt="404 image" />

</center>

Notes:

Inside of this python script `exponent_a_list.py`, we’re going to copy
the original function and save this file.

---

<center>

<img src='/module7//m7_10.png'  width = "90%" alt="404 image" />

</center>

Notes:

Next, we can go into our `more-exp-calc.ipynb` notebook, and in a new
cell at the top, we write a statement that will tell Python where the
`exponent_a_list` function is located and bring it into the notebook
environment.

We write

``` python
from exponent_a_list import exponent_a_list
```

You may wonder why we write exponent\_a\_list twice; well, the
`exponent_a_list` is referencing the name of this python script file
that we just created, so whatever we name this file is what we put after
the `from` statement.

The second `exponent_a_list` of our statement is telling us what
function would like to import from that file.

We only have one function in the file `exponent_a_list.py,` but you can
have multiple functions that could live in this file.

---

<center>

<img src='/module7/m7_11.png'  width = "90%" alt="404 image" />

</center>

Notes:

We can now run the cell containing the import statement followed by the
function `exponent_a list` for values 1, 3, and 5.

This time instead of an error, we get the expected results.

---

<center>

<img src='/module7/m7_14.png'  width = "90%" alt="404 image" />

</center>

Notes:

We can go back to our original notebook `exponent.ipynb` and replace the
function we had written with that import statement.

This now gives us the ability to run all of the cells in this notebook
the way we just did in the other notebook `more-exp-calc.ipynb`.

---

# Let’s apply what we learned\!

Notes: <br>
