---
type: slides
---

# More plotting tricks using Altair

Notes:

<br>

---

``` python
chart0 = alt.Chart(cereal, width=500, height=300).mark_circle().encode(
    x='mfr', 
    y='calories'
).properties(title="Scatter plot of manufacturer calorie content")

chart0
```
<img src="/module2/chart0.png" alt="A caption" width="60%" />

Notes:

Let’s build on the Altair skills we learned in the previous module.

At this point, we are familiar with writing basic plotting code similar
to what is shown here.

However, it’s important that we start specifying what kind of variable
type we use for our `x` and `y` values with the `encode(..)` verb.

Before, Altair would guess what type of data it was plotting. Usually
it’s pretty smart and guesses correctly like we saw in our previous
plots, but unfortunately this is not always the case.

---

``` python
chart1 = alt.Chart(cereal_modified, width=500, height=300).mark_circle().encode(
                   x='mfr', 
                   y='calories'
         ).properties(title="Scatter plot of manufacturer calorie content")

chart1
```
<img src="/module2/chart1.png" alt="A caption" width="60%" />

Notes:

Let’s see an example where `Altair` fails to determine the correct data
type.

For this example, we have modified the `calories` column in the `cereal`
dataframe.

We will now generate a scatter plot of `mfr` and `calories` from this
modified cereal dataset.

Notice how 150 comes before 100 on the y-axis? It seems we have a
problem here, which is due to Altair failing to recognize that
`calories` is a numerical type.

Even Altair can’t always get it right every time, which is why it’s so
important we specify the data type when plotting.

---

``` python
chart2 = alt.Chart(cereal_modified, width=500, height=300).mark_circle().encode(
                   x='mfr:N', 
                   y='calories:Q'
                  ).properties(title="Scatter plot of manufacturer calorie content")

chart2
```
<img src="/module2/chart2.png" alt="A caption" width="60%" />

Notes:

We can help Altair by giving it clear instructions on what type of
columns our x and y values are.

In this case we are going to specify `N` for the *nominal* column `mfr`
and `Q` for the *quantitative* column `calories`.

That’s better!

---

| Data Type    | Shorthand Code | Description                    | Examples                               |
|--------------|----------------|--------------------------------|----------------------------------------|
| Ordinal      | `O`            | a discrete ordered quantity    | “dislike”, “neutral”, “like”           |
| Nominal      | `N`            | a discrete un-ordered quantity | eye color, postal code, university     |
| Quantitative | `Q`            | a continuous quantity          | 5, 5.0, 5.011                          |
| Temporal     | `T`            | a time or date value           | date (August 13 2020), time (12:00 pm) |

Notes:

Altair recognizes the following column types and it’s best practice that
we specify this when we plot going forward.

Ordinal values imply that there is some natural ordering to the values.

For example, the ratings of a a movie could be on an ordinal scale since
a five star rating is better than a single star rating.

In contrast, there is no such natural ordering for nominal values. An
example of this would be someone’s eye colour, their country location or
the university they attended.

Anything numeric is considered a `quantitative` variable and `time` or
`date` values are considered as `temporal`.

---

``` python
chart3 = alt.Chart(cereal, width=500, height=300).mark_circle().encode(
                   x='sugars:Q',  # set the sugars column as quantitative
                   y='rating:Q'   # set the rating column as quantitative
         ).properties(title="Scatter plot of cereal rating vs sugar content")

chart3
```
<img src="/module2/chart3.png" alt="A caption" width="60%" />

Notes:

Let’s practice this.

Maybe we are interested in plotting the rating of cereals vs the amount
of sugar they contain from `cereal` dataframe.

We do this using a scatter plot which uses `.mark_circle()`. We can
assign `sugars` as the the `x` variable and `ratings` as the `y`
variable from the `cereal` dataframe we have been using.

Here, `sugars` and `rating` are both quantitative columns so we specify
`Q` as variable types in our plot.

---

# Variable types

``` python
chart4 = alt.Chart(cereal, width=500, height=300).mark_circle().encode(
                   x=alt.X('sugars:Q'), # use alt.X() to map the x-axis
                   y=alt.Y('rating:Q')  # use alt.Y() to map the y-axis
         ).properties(title="Scatter plot of cereal rating vs sugar content")

chart4
```
<img src="/module2/chart4.png" alt="A caption" width="60%" />

Notes:

So far when plotting with Altair, we have been mapping our `x` and `y`
in the `encode(x=..,y=..)` verb.

However, doing so gives us very little control over how exactly we would
like to map our x and y values.

In order to have more control, we can map our x and y values using
`x=alt.X(...)` and `y=alt.Y(...)` respectively.

This gives us a lot more control over the customization of our plot.

You’ll see this coming up.

---

## Histograms

``` python
chart5 = alt.Chart(cereal, width=500, height=300).mark_bar().encode(
                   x=alt.X('calories:Q', bin=True), # set x-axis as calories 
                   y=alt.Y('count():Q')             # set the y-axis as the occurrence count for each calorie value
         ).properties(title="Histogram plot of cereal calorie content")
chart5
```
<img src="/module2/chart5.png" alt="A caption" width="60%" />

Notes:

Another type of plot we can make using Altair is called a **histogram**.

A histogram would be an ideal plot if we were interested in seeing how
many cereals in our dataframe have calories within a certain range. A
histogram is a `bar` chart where the height of each bar shows the
frequency of something occurring. When applied to quantitative data, it
groups the values into **ranges**, and the height of each bar shows the
frequency of each range.

We can generate a histogram plot of the `calories` values in the cereal
dataframe, which is quantitative. This will enable us to see the various
values of calories and how many times they occur.

To make a histogram, we use `mark_bar()`.

In the `encode()` verb, we specify the x-axis as `calories` and use the
argument `bin=True`. We assign the y-axis as `count():Q` to get the
number of cereals that have values within each of the ranges.

This is the same `count()` argument we use in Module 1 when we made bar
charts.

---

## Bins

``` python
chart6 = alt.Chart(cereal, width=500, height=300).mark_bar().encode(
                   x=alt.X('calories:Q', bin=alt.Bin(maxbins=20)), # set max number of bins to 20
                   y=alt.Y('count():Q')
         ).properties(title="Histogram of cereal calorie content with bins = 20")
chart6
```
<img src="/module2/chart6.png" alt="A caption" width="60%" />

Notes:

We have the ability to change the number of bars (bins) in our histogram
by using the `bin` argument and the `alt.Bin()` verb.

Within `alt.Bin()`, we can specify `maxbins` which is the maximum
allowed number of bins in our plot.

This may be useful when viewing a dataset with lots of different values.

Having control over the number of bins in a histogram can help to make
visualization easier to extract insights from.

Here, we set the number of max bins in the plot to `20` by setting
`bin=alt.Bin(maxbins=20)` inside `alt.X()`.

---

<img src="/module2/chart6.png" alt="A caption" width="70%" />

Notes:

When plotting with Altair, the `x` and `y` axis are labelled with the
default column names.

This may not always be ideal since column names may not always be
informative. In this plot, the x axis label `calories (binned)` is a
little messy.

Luckily Altair allows us to customize our axis labels.

---

``` python
chart7 = alt.Chart(cereal, width=500, height=300).mark_bar().encode(
                   x=alt.X('calories:Q', bin=alt.Bin(maxbins=20), title="Calorie Content"), # use alt.X() to label the x-axis
                   y=alt.Y('count():Q', title="Number of Cereals")                          # use alt.Y() to label the y-axis
        ).properties(title="Histogram plot of cereal calorie content")
chart7
```
<img src="/module2/chart7.png" alt="A caption" width="60%" />

Notes:

We can change these axis labels using the `title=""` argument within the
respective `alt.X()` and `alt.Y()` verbs that we talked about earlier.

This is a big help for the clarity of our analysis.

---

``` python
mfr_mean = cereal.groupby(by='mfr').mean()
mfr_mean
```

```out
      protein       fat      sodium     fiber      carbo    sugars      potass   vitamins     shelf    weight      cups     rating
mfr                                                                                                                               
A    4.000000  1.000000    0.000000  0.000000  16.000000  3.000000   95.000000  25.000000  2.000000  1.000000  1.000000  54.850917
G    2.318182  1.363636  200.454545  1.272727  14.727273  7.954545   85.227273  35.227273  2.136364  1.049091  0.875000  34.485852
K    2.652174  0.608696  174.782609  2.739130  15.130435  7.565217  103.043478  34.782609  2.347826  1.077826  0.796087  44.038462
N    2.833333  0.166667   37.500000  4.000000  16.000000  1.833333  121.000000   8.333333  1.666667  0.971667  0.778333  67.968567
P    2.444444  0.888889  146.111111  2.777778  13.222222  8.777778  113.888889  25.000000  2.444444  1.064444  0.714444  41.705744
Q    2.625000  1.750000   92.500000  1.337500  10.250000  5.500000   74.375000  12.500000  2.375000  0.875000  0.823750  42.915990
R    2.500000  1.250000  198.125000  1.875000  17.625000  6.125000   89.500000  25.000000  2.000000  1.000000  0.871250  41.542997
```

Notes:

In the previous slide deck, we asked the following question regarding
our cereal data:

***Which manufacturer has the highest mean sugar content?***

A nice way of answering this would be to plot the results using a bar
chart!

Before doing this, we need a few more tricks.

We can start using the mean statistics we calculated from the
`groupby(by='mfr')` object from the last section.

Here, we seem to have lost our index column of numbers that we usually
have. It also appears that `mfr` has now moved to the left of the
dataframe with its label `mfr` lower than the other column labels.

This is because when you apply `groupby()` to a column, the grouping
column becomes the new dataframe index.

Although this is a useful feature in many cases, Altair cannot access
the index column.

---

``` python
mfr_mean
```

```out
      protein       fat      sodium     fiber      carbo    sugars      potass   vitamins     shelf    weight      cups     rating
mfr                                                                                                                               
A    4.000000  1.000000    0.000000  0.000000  16.000000  3.000000   95.000000  25.000000  2.000000  1.000000  1.000000  54.850917
G    2.318182  1.363636  200.454545  1.272727  14.727273  7.954545   85.227273  35.227273  2.136364  1.049091  0.875000  34.485852
K    2.652174  0.608696  174.782609  2.739130  15.130435  7.565217  103.043478  34.782609  2.347826  1.077826  0.796087  44.038462
N    2.833333  0.166667   37.500000  4.000000  16.000000  1.833333  121.000000   8.333333  1.666667  0.971667  0.778333  67.968567
P    2.444444  0.888889  146.111111  2.777778  13.222222  8.777778  113.888889  25.000000  2.444444  1.064444  0.714444  41.705744
Q    2.625000  1.750000   92.500000  1.337500  10.250000  5.500000   74.375000  12.500000  2.375000  0.875000  0.823750  42.915990
R    2.500000  1.250000  198.125000  1.875000  17.625000  6.125000   89.500000  25.000000  2.000000  1.000000  0.871250  41.542997
```

``` python
mfr_mean = mfr_mean.reset_index()
mfr_mean
```

```out
  mfr   protein       fat      sodium     fiber      carbo    sugars      potass   vitamins     shelf    weight      cups     rating
0   A  4.000000  1.000000    0.000000  0.000000  16.000000  3.000000   95.000000  25.000000  2.000000  1.000000  1.000000  54.850917
1   G  2.318182  1.363636  200.454545  1.272727  14.727273  7.954545   85.227273  35.227273  2.136364  1.049091  0.875000  34.485852
2   K  2.652174  0.608696  174.782609  2.739130  15.130435  7.565217  103.043478  34.782609  2.347826  1.077826  0.796087  44.038462
3   N  2.833333  0.166667   37.500000  4.000000  16.000000  1.833333  121.000000   8.333333  1.666667  0.971667  0.778333  67.968567
4   P  2.444444  0.888889  146.111111  2.777778  13.222222  8.777778  113.888889  25.000000  2.444444  1.064444  0.714444  41.705744
5   Q  2.625000  1.750000   92.500000  1.337500  10.250000  5.500000   74.375000  12.500000  2.375000  0.875000  0.823750  42.915990
6   R  2.500000  1.250000  198.125000  1.875000  17.625000  6.125000   89.500000  25.000000  2.000000  1.000000  0.871250  41.542997
```

Notes:

To deal with this, we use `reset_index()` which will convert `mfr` to a
regular column again.

We can see that `mfr` column has now moved right and our index column of
integers has returned on the left!

---

``` python
chart8 = alt.Chart(mfr_mean, width=500, height=300).mark_bar().encode(
                   x=alt.X('mfr:N', title="Manufacturer"),
                   y=alt.Y('sugars:Q', title="Mean sugar content")
         ).properties(title="Bar plot of manufacturers mean sugar content")
chart8
```
<img src="/module2/chart8.png" alt="A caption" width="60%" />

Notes:

Now that we have our `mfr_mean` in the correct format, we can proceed.

Using Altair we can plot the `mfr` column on the x axis which we’ve
identified to contain nominal values and `sugars` which we agreed was a
quantitative value on the y axis. (Also, let’s not forget our title!)

---

<br> <br>

1.  Groupby object and calculated the mean
2.  Reset index
3.  Plot using Altair

Notes:

Let’s go through the steps that were needed to make the plot in the
previous slide.

First, we created a groupby object and calculated the mean for each
column in the resulting dataframe.  
Second, since `.groupby()` made `mfr` the new index, we had to use
`reset_index()` to make `mfr` a regular column again. And finally, we
generated a bar plot using Altair.

---

## Sorting

``` python
chart9 = alt.Chart(mfr_mean, width=500, height=300).mark_bar().encode(
                   x=alt.X('mfr:N', sort="y", title="Manufacturer"),  # use sort="y" to sort in ascending order
                   y=alt.Y('sugars:Q', title="Mean sugar content")
        ).properties(title="Bar plot of manufacturers mean sugar content in ascending order")
chart9
```
<img src="/module2/chart9.png" alt="A caption" width="60%" />

Notes:

Sometimes sorting a dataframe by quantity helps us obtain insights more
easily.

For example, if we sorted the mean sugar content for the manufacturers
before generating the previous plot, it would be easier to identify
which manufacturer produces cereals with the highest mean sugar content.

Altair allows us to sort a column while plotting.

Sorting can be done on either the x or y axis using the `sort=` in the
`alt.X` or `alt.Y` verb.

The sort argument takes in either `x` or `y` to specify which axis to
sort by.

Here we are sorting in ascending order of which manufacturers have the
largest mean sugar content.

This plot shows us immediately that manufacturer `P` has the highest
mean cereal sugar content.

---

``` python
chart10 = alt.Chart(mfr_mean, width=500, height=300).mark_bar().encode(
    x=alt.X('mfr:N', sort="-y", title="Manufacturer"),  # use sort="-y" to sort in descending order
    y=alt.Y('sugars:Q', title="Mean sugar content")
).properties(title="Bar plot of manufacturers mean sugar content sorted in descending order")
chart10
```
<img src="/module2/chart10.png" alt="A caption" width="60%" />

Notes:

To generate a bar plot of mean calorie content sorted in `descending`
order, we recycle the code from the previous slide.

This time, we add `-y` in the `sort` argument to specify that we would
like to sort the y variable in descending order.

---

<br> <br> <br>
<center>
<font size="+3"> If you enjoyed this part of the module and you wish to
learn more advanced visualizations using Altair, take a look at our <br>
<a href="https://viz-learn.mds.ubc.ca/" target="_blank"><b>Data
Visualization</b></a> course </font>
<center>

Notes:

<br>

---

# Let’s apply what we learned!

Notes: <br>

<!-- We've added a title before, so there is nothing new there but adding x and y-axis labels is a little different. We can increase the label font sizes using the argument `fontsize`. In this case, we reference our initial plot and use the verb `.set_ylabel()` and `.set_xlabel()` with the desired axis label as an argument and `fontsize` to assign a desired label size.  -->
<!-- To avoid unnecessary information that will be returned otherwise, whatever our last verb being used with our plot (named `sugar_plot) has to be reassigned back to the object. If we did this any other way, we would not have the ability to do more transformations on our plot, or we would get additional information with the plot output.  -->
<!-- ```{python  out.width = '45%', fig.asp = .40} -->
<!-- sugar_plot = (df.groupby(by='mfr') -->
<!--                 .mean() -->
<!--                 .loc[:,'sugars'] -->
<!--                 .plot.bar(title='Mean sugar content among manufacturers') -->
<!--               ) -->
<!-- sugar_plot.set_ylabel('Sugar content (in grams)', fontsize=9) -->
<!-- sugar_plot = sugar_plot.set_xlabel('Manufacturer', fontsize=9) -->
<!-- sugar_plot -->
<!-- ``` -->
<!-- Notes: Script here -->
<!-- <html> -->
<!-- <audio controls > -->
<!--   <source src="/placeholder_audio.mp3" /> -->
<!-- </audio></html> -->
<!-- --- -->
<!-- In the last plot, we used `.loc[:,'sugars']` to select a single column to the plot, however, we can show multiple mean column values in a single plot by selecting more columns. The columns `fat`, `fiber` and `protein` seem like good choices.  -->
<!-- ```{python out.width = '60%', fig.asp = .58} -->
<!-- nutrition_plot = (df.groupby(by='mfr') -->
<!--                     .mean() -->
<!--                     .loc[:, ['fat', 'fiber', 'protein']] -->
<!--                     .plot.bar(title='Mean nutritrion value over different manufacturers') -->
<!--                  ) -->
<!-- nutrition_plot.set_ylabel('Content (in grams)', fontsize=9) -->
<!-- nutrition_plot = nutrition_plot.set_xlabel('Manufacturer', fontsize=9) -->
<!-- nutrition_plot -->
<!-- ``` -->
<!-- If you want high fibre and low fat, consider having N's cereals for breakfast (or lunch or dinner)! -->
<!-- Notes: Script here -->
<!-- <html> -->
<!-- <audio controls > -->
<!--   <source src="/placeholder_audio.mp3" /> -->
<!-- </audio></html> -->
<!-- --- -->
<!-- ## Multiple Grouping  -->
<!-- We can group by multiple columns as well.  -->
<!-- For example we can grouping by not only manufacturer but also by cereal type! All we do is put both both column labels in square brackets within `.groupby()`. -->
<!-- ```{python} -->
<!-- mfr_type_group = df.groupby(by=['mfr', 'type']) -->
<!-- mfr_type_group.groups -->
<!-- ``` -->
<!-- The attribute `ngroups` indicates how many groups there are.   -->
<!-- ```{python} -->
<!-- mfr_type_group.ngroups -->
<!-- ``` -->
<!-- Notes: Script here -->
<!-- <html> -->
<!-- <audio controls > -->
<!--   <source src="/placeholder_audio.mp3" /> -->
<!-- </audio></html> -->
<!-- --- -->
<!-- If we want to get the dataframe of a specific group now, we put the value of each column in parentheses.  -->
<!-- ```{python} -->
<!-- mfr_type_group.get_group(('K', 'Cold')) -->
<!-- ``` -->
<!-- Notes: Script here -->
<!-- <html> -->
<!-- <audio controls > -->
<!--   <source src="/placeholder_audio.mp3" /> -->
<!-- </audio></html> -->
<!-- --- -->
<!-- We can plot in the same way as before  -->
<!-- ```{python fig.width = 13, fig.height = 9,  out.width = '50%'} -->
<!-- type_plot = (df.groupby(by=['mfr', 'type']) -->
<!--                     .mean() -->
<!--                     .loc[:, ['sugars']] -->
<!--                     .plot.bar(title='Mean sugar value over different manufacturers and types')) -->
<!-- type_plot.set_ylabel('Sugar (in grams)', fontsize=16) -->
<!-- type_plot.set_xlabel('Manufacturer and cereal type', fontsize=16) -->
<!-- type_plot -->
<!-- ``` -->
<!-- Notes: Script here -->
<!-- <html> -->
<!-- <audio controls > -->
<!--   <source src="/placeholder_audio.mp3" /> -->
<!-- </audio></html> -->
<!-- --- -->
