---
type: slides
---

# Tidy data

Notes: <br>

---

### What is the concept of tidy data?

Tidy data satisfies the following three criteria:

  - Each row is a single observation,
  - Each variable is a single column, and
  - Each value is a single cell (i.e., its row, column position in the
    dataframe is not shared with another value)

<center>

<img src="https://d33wubrfki0l68.cloudfront.net/6f1ddb544fc5c69a2478e444ab8112fb0eea23f8/91adc/images/tidy-1.png" width="550" />

</center>

*Image Source: [R for Data Science](https://r4ds.had.co.nz/) by Garrett
Grolemund & Hadley Wickham*

What a variable and an observation is may depend on your immediate goal.

Notes: When we first hear “tidy data”, you likely think of clean,
organized, and orderly data. The same applies here, however, the concept
of ***tidy data*** stems from
<a href="https://vita.had.co.nz/papers/tidy-data.pdf" target="_blank">a
paper </a> written by renowned data scientist Hadley Wickham in 2014.

We tidy our data in such a way so that we can create a standard across
multiple analysis tools. It changes the focus from figuring out the
logistics of how the data is structured, to answering the actual
analysis question being asked.

This approach allows us to standardize input arguments of certain
analysis verbs like `.describe()` and other predictive methods.

---

***Are protein and calories content associated with different cereal
manufacturers?***

<center>

<img src="/module3/tidy-table.png" width="550" />

</center>

Notes: Let’s explore some different versions of our cereal dataset and
determine if they fit the *tidy* criteria given the statistical question
below:

***Are protein and calories content associated with different cereal
manufacturers?***

Here are a few rows from our unaltered cereal dataset.

Does it fit all three criteria?

---

## Criterion \#1: Each row is a single observation

<center>

<img src="/module3/tidy-crit1.png" width="550" />

</center>

Notes: From the dataframe we can see that each cereal has its own row.
Criterion \#1 is met\!

---

## Criterion \#2: Each variable is a single column

<center>

<img src="/module3/tidy-crit2.png" width="550" />

</center>

Notes: From the dataframe we can see that each of the variables `name`,
`mfr`, `calories` and `protein` have their own column. We can validate
that criterion \#2 is also met.

---

## Criterion \#3: Each value is a single cell

<center>

<img src="/module3/tidy-crit3.png" width="550" />

</center>

Notes: The variable value for each cereal has it’s own cell, confirming
that criterion \#3 is met\!

---

<center>

<img src="/module3/tidy2-table.png" width="500" />

<center>

Notes: As expected, the cereal data we have been working with is *tidy
data* for our statistical question.  
Let’s look at a longer dataframe with the same information where this is
not the case.

---

## Criterion \#1 Each row is a single observation

<center>

<img src="/module3/tidy2-crit1.png" width="400" />

</center>

Notes: From the dataframe we can see that each observation has its own
row. There are 2 rows per cereal but each row is unique.  
We can confirm that criterion 1 is met.

---

## Criterion \#2: Each variable is a single column

<center>

<img src="/module3/tidy2-crit2.png" width="400" />

</center>

Notes: It looks like we have a problem here. In this dataframe, two of
our variables we are measuring for our statistical question are
contained in a single column. This is making the data untidy and
potentially a problem to work with.  
For example, what if I wanted to know the average calorie content of the
cereals?

---

``` python
cereal2
```

```out
           name mfr nutrition  value
0   Apple Jacks   K   protein      2
1   Bran Flakes   P   protein      3
2      Cheerios   G   protein      6
3    Honey-comb   P   protein      1
..          ...  ..       ...    ...
10   Honey-comb   P  calories    110
11  Raisin Bran   K  calories    120
12    Special K   K  calories    110
13     Wheaties   G  calories    100

[14 rows x 4 columns]
```

``` python
cereal2[cereal2['nutrition'] == 'calories']['value'].mean()
```

```out
107.14285714285714
```

If we had tidy data we could have simply done:

``` python
cereal['calories'].mean()
```

```out
107.14285714285714
```

Notes: The dataframe `cereal2` shows our untidy data from the previous
slide. We could either groupby nutrition value or filter on `calories`
first before getting our results to calculate the mean, but if we had
tidy data, we could have calculated the mean directly from the
`calories` column.

---

# Let’s practice what we know about tidy data first\!

Notes: <br>
