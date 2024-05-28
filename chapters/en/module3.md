---
title: 'Module 3: Tidy Data and Joining Dataframes'
description:
  'In this Module, you will learn about tidy data and how to transform your dataset into a tidy format. It will also focus on how to concatenate and join multiple dataframes.'
prev: /module2
next: /module4
type: chapter
id: 3
---

<exercise id="0" title="Module Learning Outcomes" type="slides,video">

<slides source="module3/module3_00" shot="7" start="0:001" end="0:24">
</slides>

</exercise> 

<exercise id="1" title="What is Tidy Data?" type="slides,video">

<slides source="module3/module3_01" shot="1" start="43:56" end="47:32">
</slides>

</exercise>

<exercise id="2" title="Tidy Data Questions">

**Question 1**         

The same data may be considered tidy for different shaped dataframes depending on the statistical questions .

<choice id="1" >
<opt text='True' correct="true">

Good job! 

</opt>

<opt text= 'False' >

Tidy data depends quite often depends on the statistical question. 

</opt>

</choice> 

**Question 2**    

Which of the following does **not** characterize a tidy dataset?

<choice id="2" >
<opt text="Each row is a single observation">

You may want to look over this before moving forward.

</opt>

<opt text="Each column is a single variable">

You may want to look over this before moving forward.

</opt>

<opt text="Each value is a single cell" >

You may want to look over this before moving forward.

</opt>

<opt text="There are no <code>NaN</code> values in the dataset" correct="true">

You are right.  It is possible to still have tidy data with missing values. 

</opt>

</choice> 

</exercise>

<exercise id="3" title="Is it Tidy I ?">


Given the 3 tidy data criteria, would this dataframe be defined as tidy?

<center> <img src='/module3/Q3.png'  alt="404 image"/></center>

<choice>

<opt text="Yes">

Not quite!  Take a specific look at the column named `special_attack_defense`. Is this meeting criterion #3?

</opt>

<opt text= "No" correct="true">

Good job!  Did you notice that `special_attack_defense` had two values per cell defying criterion #3?

</opt>

</choice> 

</exercise>

<exercise id="4" title="Is it Tidy II?">

Given the 3 tidy data criteria, would this dataframe be defined as tidy?

<center> <img src='/module3/Q4.png'  alt="404 image"/></center>

<choice>
<opt text="Yes">

Not quite!  Do you notice anything about the rows?  Are they meeting Criterion #1? 

</opt>

<opt text= "No" correct="true">

Good job!  You must have seen the duplicate rows of `Ivysaur`, `Charmeleon` and `Squirtle`.

</opt>

</choice> 

</exercise>

<exercise id="5" title="Statistical Questions and Tidy Data" type="slides,video">

<slides source="module3/module3_05" shot="1" start="47:348" end="49:49">

</slides>

</exercise>

<exercise id="6" title="Which is Tidy?">

Which of the following would be considered tidy data for the following statistical questions: 

***What factors are associated with fruit with seeds?***


**Dataframe A**
<center> <img src='/module3/Q5a.png'  alt="404 image" width="60%"/></center>


**Dataframe B**
<center> <img src='/module3/Q5b.png'  alt="404 image" width="60%"/></center>

<br>
<choice>
<opt text="Dataframe A">

Not quite! Maybe try re-reading over the content. 

</opt>

<opt text= "Dataframe B" correct="true">

Good job! 

</opt>

</choice> 

</exercise>


<exercise id="7" title="Tidy Data True or False">

Is the following statement true or false?      

_A long dataframe is always a tidy dataframe._


<choice>
<opt text="True">

Did you read this section? 

</opt>

<opt text= "False" correct="true">

Good job! Of course it depends on the statistical question!

</opt>

</choice> 

</exercise>


<exercise id="8" title="Reshaping with Pivot" type="slides,video">

<slides source="module3/module3_08" shot="1" start="49:50" end="55:47">

</slides>

</exercise>

<exercise id="9" title="Pivoting Questions">

**Question 1**          
We use `.pivot()` to convert a wider dataframe with multiple columns into a longer dataframe with fewer columns.


<choice id="1" >
<opt text="True" >

The reverse is true.  Please review this section before continuing.

</opt>

<opt text="False" correct="true">

Great work!

</opt>

</choice> 

       
**Question 2**          
Which of the following will reset your index?

<choice id="2" >
<opt text="<code>.index_reset()</code>">

You may want to look over this before moving forward.

</opt>

<opt text="<code>.reset_index()</code>" correct="true">

Good job!

</opt>

</choice> 

</exercise>


<exercise id="10" title="Applying Pivot">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**


Let's take a look at the new dataset named `lego`.

<codeblock id="lego_untidy">
</codeblock>



Let's convert the dataframe `lego` into a wider dataframe using `.pivot()`.  

Tasks:

- Convert the untidy data into tidy data using `.pivot()`.
- Don't forget to reset your index.
- Name the new dataframe `tidied_lego`.
- Save the mean number of parts (`num_parts`) of the Lego sets in an object named `set_parts_mean`. (We've added a verb named `.round()` to round to the nearest whole number)
  
     

<codeblock id="03_10">

- Are you pivoting the correct column named `lego_info` with `values='value'`?     
- Are you resetting your index after you pivot?     

</codeblock>


</exercise>


<exercise id="11" title="Reshaping with Pivot Table" type="slides,video">

<slides source="module3/module3_11" shot="1" start="55:49" end="61:37">

</slides>

</exercise>


</exercise>

<exercise id="12" title="Pivot Table Questions">

**Question 1**          
Which of the following does ***NOT*** continue to execute when there are duplicate rows in the dataframe?

<choice id="1" >
<opt text="<code>.pivot_table()</code>">

You may want to look over this before moving forward.

</opt>

<opt text="<code>.pivot()</code>" correct="true">

Great studying!

</opt>

</choice> 


**Question 2**          
What must we do before we use pivot table? 

<choice id="2" >
<opt text="Check for duplicate values of the columns in the arguments <code>index</code> and <code>columns</code>" correct="true" >

This is extremely important so we don't get averaging values! Well done. 

</opt>

<opt text="Remove any <code>NaN</code>s from the dataframe">

This is extremely important so you will want to look over this before moving forward.

</opt>

</choice> 

</exercise>



<exercise id="13" title="Applying Pivot Table">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**


_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Let's convert the dataframe `lego` into wider data but this time preserve all the columns in the dataframe by using `.pivot_table()`.

Tasks:

- Convert the untidy data into tidy data using `.pivot_table()` making sure to keep all the columns. 
- Assign your new dataframe `set_num` as your index.
- Name the new dataframe `tidied_lego`.
- Find the mean number of parts for each production year and save it in an object name `year_parts_mean`. (We've added a verb named `.round()` to round to the nearest whole number)

<codeblock id="03_13">

- Are you using the correct arguments such as `index`, `columns`, and `values`?
- Are you pivoting the correct column named `lego_info` with `values='value'`?
- Are you resetting your index again after you pivot?

</codeblock>

Which year has the highest average number of parts?    
*Hint: use `.sort_values()`.*

<choice id="1" >
<opt text='2016'>

Are your sorting by `ascending=False`?

</opt>

<opt text='2006'>

Are your sorting by `ascending=False`?

</opt>

<opt text= '2017' correct="true">

Good job! 

</opt>

<opt text='2007'>

Are your sorting by `ascending=False`?

</opt>

</choice> 


</exercise>



<exercise id="14" title="Reshaping with Melt" type="slides,video">

<slides source="module3/module3_14" shot="1" start="61:39" end="63:50">

</slides>

</exercise>


<exercise id="15" title="Melting Questions">

**Question 1**          
We use `.melt()` to convert a wide dataframe with multiple columns into a longer dataframe with fewer columns.


<choice id="1" >
<opt text="True"  correct="true" >

Great work! 

</opt>

<opt text="False">

It may be a good idea to look over the last section again. 

</opt>

</choice> 


**Question 2**         
`.melt()` has the same arguments as `.pivot()`.

<choice id="2" >
<opt text='True'>

It may be a good idea to look over the last section again. 

</opt>

<opt text= 'False' correct="true">

Good job!

</opt>

</choice> 

**Question 3**     
`.melt()`  and `.pivot()` always transform the data into tidy data.

<choice id="3" >
<opt text='True'>

It may be a good idea to look over the last section again. 

</opt>

<opt text= 'False' correct="true">

Good job!  Just because the data is transformed doesn't mean that it's transformed for the better! 

</opt>

</choice> 

</exercise>


<exercise id="16" title="Applying Melt">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Let's take a look at some new untidy data that we have named `lego`. 

<codeblock id="lego_untidy2">
</codeblock>



Let's melt this so that the 2 new columns named `matte` and `transparent` become a single one.  These columns refer to the opacity of the blocks and the values refer to the number of pieces of each included in the set. Since our variable of interest in this scenario is `opacity`, we need to combine the two measurements into one column.

Tasks:

- `melt` the dataframe columns `matte` and `transparent` into a single column named `opacity` and name the values column `quantity`.
- Name the new dataframe `tidied_lego`.

<codeblock id="03_16">

- Are you melting the correct columns named `matte` and `transparent`?
- Are you making sure to use all the columns (except `matte` and  `transparent` in the argument `id_vars`?

</codeblock>

</choice> 

</exercise>


<exercise id="17" title="Concatenation" type="slides,video">

<slides source="module3/module3_17" shot="1" start="63:5310" end="70:32">

</slides>

</exercise>

<exercise id="18" title="Concat questions">

**Question 1**     
If we wanted to concatenate Dataframe A with Dataframe B horizontally, what do we need to make sure **before** proceeding?

<choice id="1" >
<opt text="There are no <code>NaN</code> values">

We can still concatenate with missing values.

</opt>

<opt text= "The order of the rows in each dataframe are the same"  correct="true">

Good job!

</opt>

<opt text= "The columns are not duplicated">

We can remove duplicated columns after concatenation. 

</opt>

</choice> 

**Question 2**         
Which of the following statements are correct?


<choice id="2" >
<opt text='Concatenating horizontally requires the argument <code>axis=1</code>', correct="true">

Good job!  Maybe more solutions are correct...


</opt>

<opt text='Concatenating vertically requires the argument <code>axis=0</code>'  correct="true">

Good job!  Did you get multiple correct answers? 

</opt>

<opt text='Concatenating vertically requires the argument <code>axis=1</code>'>

I think you got mixed up.  Try reading over the notes again. 

</opt>

<opt text='Concatenating horizontally requires the argument <code>axis=0</code>'>

I think you got mixed up.  Try reading over the notes again. 

</opt>

</choice> 

</exercise>


<exercise id="19" title="Concatenating Vertically">


**Instructions:** 
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes.     

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

Sometimes we accumulate additional data that we need to combine with our existing data.  In the following question, we need to combine our dataframes to have a complete collection of all the Lego sets that exist. 

Tasks:

- Combine the two dataframes <a href="https://github.com/UBC-MDS/MCL-DSCI-011-programming-in-python/blob/master/data/lego_top.csv" target="_blank">`lego_top`</a> and  <a href="https://github.com/UBC-MDS/MCL-DSCI-011-programming-in-python/blob/master/data/lego_bottom.csv" target="_blank">`lego_bottom`</a>  vertically to make one large complete dataframe.
- Name the new dataframe `full_set`.
- Save the new dimension of `full_set` in an object named `full_set_shape`.
- Display the new dataframe.


<codeblock id="03_19">

- Are you using `pd.concat()`?
- Are you concatenating in the correct order with `lego_top` first and `lego_bottom` second?
- Are you putting your dataframes within square brackets? 
- Are you using `axis=0`
- Are you using `.shape` to find the dimension of the new dataframe?

</codeblock>

</exercise>

<exercise id="20" title="Concatenating Horizontally">

**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_ 

Our goal is to obtain a dataframe with the `lego_set` names and the total amount of pieces in each set but we only have 2 Lego dataframes (with the same indexes).  One dataframe has the set names and the other contains information amount the number of matte and transparent pieces included in each set.  Complete this question by using `pd.concat()` and techniques we learned in the previous model.

Tasks:

- Combine the two dataframes horizontally to make 1 large complete dataframe and name the new dataframe `lego_full`.
- Drop any duplicated columns using `.loc[]` and `.duplicate()`and save this new dataframe as `washed_lego`.
- Make a new column named `total_pieces` by adding up columns `matte` and `transparent`.
- Sort the dataframe by `total_pieces` in descending order.
- Save this in an object named `lego_details`.
- Display the new dataframe.


<codeblock id="03_20">

- Are you using `pd.concat()`?
- Are you concatenating the dataframes `lego_base` with `lego_opacity`?
- Are you putting your dataframes within square brackets? 
- Are you removing any duplicated columns?
- Are you using `axis=1`?
- Are you using `.assign()` to make a new column named `total_pieces`?
- Are you using using `.sort_values()` with the argument `ascending=False`

</codeblock>

</exercise>

<exercise id="21" title="Joining Dataframes using Merge" type="slides,video">

<slides source="module3/module3_21" shot="1" start="70:3401" end="78:13">

</slides>

</exercise>


<exercise id="22" title="Merge Questions">

**Question 1**          
Which of the following are **not** ways in which you can join dataframes using `.merge()`?

<choice id="1" >
<opt text="Vertically"  correct="true" >

Great work!  We cannot join dataframes vertically with `.merge()`. 

</opt>

<opt text="Outer">

"Outer" joins are possible with the `how` argument in `merge()`.

</opt>

<opt text="Inner">

"Inner" joins are possible with the `how` argument in `merge()`.

</opt>

<opt text="Left">

"Left" joins are possible with the `how` argument in `merge()`.

</opt>

<opt text="Right">

"Right" joins are possible with the `how` argument in `merge()`.

</opt>

</choice> 

**Question 2**    
Which join is the default when using `.merge()`?

<choice id="2" >

<opt text='Outer'>

Are you confusing the default join for `.pd.concat()`?

</opt>

<opt text= 'Inner' correct="true">

Good job!  Unlike `.pd.concat()`, "inner" is the default join for `.merge()`.

</opt>

<opt text='Left'>

This is an option for the argument `how` but not the default. 

</opt>

<opt text='Vertical'>

Are you confusing `.merge()` with `.pd.concat()`?

</opt>

</choice> 

**Question 3**         
What is the similarity between all 4 types of joins? 

<choice id="3" >
<opt text="They all need at least 1 of the dataframe's identifying key column to be an index">

It may be a good idea to look over the last section again. 

</opt>

<opt text= 'They all will produce a dataframe with columns from both of the initial dataframes' correct="true">

Good job!  Just because the data is transformed doesn't mean that it's transformed for the better! 

</opt>

<opt text='They all produce rows with <code>NaN</code> values'>

What about inner joins that only result in the rows present in both dataframes?

</opt>


<opt text='They all must have the same dimensions'>

It's still possible to have dataframes that have completely different dimensions joined together. 

</opt>

</choice> 


</exercise>


<exercise id="23" title="Merging I">

      
**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**

_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_

In this exercise, you are going to join two dataframes `lego_inventory_parts.csv` and `lego-colors.csv` and answer a few multiple-choice questions.  The multiple-choice questions are being asked with the intention of using the code cell to write your own code in any way that helps to answer the question. 


Tasks:

- Combine the two dataframes to make 1 large complete dataframe by using an outer join.
- Make sure to set the argument `indicator` to `True`. 
- Name the new dataframe `lego_tower`.


<codeblock id="03_23">

- Are you naming your new dataframe `lego_tower`? 
- Are you using the arguments  `left_on='color_id'`, `right_on=id`,  `how='outer'` and `indicator=True`?

</codeblock>

**Question 1**  
Which of the following colours doesn't have any pieces in inventory?       
*Hint: You can filter using the `_merge` column.*

<choice id="1" >
<opt text='Chrome Blue'>

You may want to try filtering using the `_merge` column 

</opt>

<opt text= 'Rust'>

You may want to try filtering using the `_merge` column 

</opt>

<opt text='Reddish Lilac' correct="true">

Good job!  You must have used `lego_tower[lego_tower['_merge'] == "right_only"]`

</opt>

<opt text='Metallic Silver'>

You may want to try filtering using the `_merge` column 

</opt>

</choice> 

**Question 2**  
Which colour has the largest number of pieces in the inventory?            
*Hint: You can use `.groupby()`  and `.sum()` to find the total amount of pieces for each set. Also`.sort_values()` may come in handy.*

<choice id="2" >
<opt text='White'>

You can use `lego_tower.groupby('name').sum().sort_values('quantity', ascending=False)` to help answer this. 

</opt>

<opt text= 'Blue'>

You can use `lego_tower.groupby('name').sum().sort_values('quantity', ascending=False)` to help answer this. 

</opt>

<opt text='Black' correct="true">

Wonderful!  Did you use `lego_tower.groupby('name').sum().sort_values('quantity', ascending=False)`?

</opt>

<opt text='Metallic Silver'>

You can use `lego_tower.groupby('name').sum().sort_values('quantity', ascending=False)` to help answer this. 

</opt>

</choice> 

**Question 3**   
How many Lego pieces from the `lego_inventory` dataframe do not have any matching rows in the `lego_colors` dataframe?     
*Hint: Filtering on the `_merge` column and using `.shape` can be useful here.* 

<choice id="3" >
<opt text='0' correct="true">

You got it!  All the pieces have matching rows from the `lego_colors` dataframe.  This code `lego_tower[lego_tower['_merge'] == "left_only"].shape` explains that there are 0 rows. 

</opt>

<opt text= '1'>

Maybe explore the `_merge` column by filtering or grouping and see if there are any `left_only` values. 

</opt>

<opt text='2'>

Maybe explore the `_merge` column by filtering or grouping and see if there are any `left_only` values. 

</opt>

<opt text='3'>

Maybe explore the `_merge` column by filtering or grouping and see if there are any `left_only` values. 

</opt>

</choice> 

</exercise>

<exercise id="24" title="Merging II">

      
**Instructions:**    
Running a coding exercise for the first time could take a bit of time for everything to load.  Be patient, it could take a few minutes. 

**When you see `____` in a coding exercise, replace it with what you assume to be the correct code.  Run it and see if you obtain the desired output.  Submit your code to validate if you were correct.**


_**Make sure you remove the hash (`#`) symbol in the coding portions of this question.  We have commented them so that the line won't execute and you can test your code after each step.**_ 


This question may be a bit more challenging.  We are wondering about the inventory of a store.  We want to see which Lego sets are in stock and if so how many?  After all, the store needs to make sure there are enough sets in stock to meet demand. 

Tasks:
- Combine the two dataframes to make one large complete dataframe by using an inner join.
- Name the new dataframe `lego_stock`.
- Group the new dataframe by `set_num` and find how many groups there are using `.ngroups`

This question is in two parts and we are going to walk you through how to tackle it. 

<codeblock id="03_24a">

- Are you naming your new dataframe `lego_stock`? 
- Are you using the arguments  `left_on='set_num'`, `right_index=True` and `how='inner'`?
- Are you grouping my using `groupby('set_num`)? 

</codeblock>


Ah, it appears we have multiple rows for some of the same sets.   
     
Although it shows initially the we have 2846 different sets due to the number of rows in `lego_stock`, when we group them by `set_num` we actually only get 2306 different sets. This means that we have some rows with the same `set_num` but with different inventory quantities.       
       
How are we going to get the stock quantity of each set now?         
We are going to have to sum up the quantity of each set using `.groupby()` and`.agg()`. 

Tasks:
- Use `.groupby()` and `.agg()` to sum up the quantity of each set and save this as `store_inventory`. 
- Inner join `store_inventory` with `lego_sets` and use chaining to sort the dataframe in descending order based on in-stock quantity
- Save this new dataframe as  `store_inventory_details`.
- Display the new dataframe.


<codeblock id="03_24b">

- Are you naming your new dataframe `store_inventory`? 
- Are you aggregating using `.agg({'quantity':'sum'})`?
- Are you using the arguments `left_index=True, right_index=True, how='inner'`?
- Are you sorting in descending order of `quantity`?

</codeblock>


Now we can return to our initial problem of identifying how many Lego sets are in stock.

**Question 1**  
How many different Lego sets are in stock?

<choice id="1" >
<opt text='11673'>

Did you look at the wrong dataframe?

</opt>

<opt text='2846'>

Did you look at the wrong dataframe?

</opt>

<opt text='3654' >

Did you look at the wrong dataframe?

</opt>

<opt text='2306' correct="true">

You got it!

</opt>

</choice> 

**Question 2**  
What's the largest quantity of stock available by any particular Lego set? 

<choice id="2" >
<opt text='12'>

Did you look at the wrong dataframe?

</opt>

<opt text='1'>

Did you look at the wrong dataframe?

</opt>

<opt text='60' correct="true">

Great!  You saw the top quantity of `lego_stock`.

</opt>

<opt text='65'>

Did you look at the wrong dataframe?

</opt>

</choice> 

</exercise>


<exercise id="25" title="What Did We Just Learn?" type="slides,video">
<slides source="module3/module3_25" shot ="7" start="0:255" end="1:08">>
</slides>
</exercise>
