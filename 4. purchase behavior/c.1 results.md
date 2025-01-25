![image](https://github.com/user-attachments/assets/4f187583-1a1d-4fcd-99e9-ad9b63bce224)

```r
transactions as itemMatrix in sparse format with
 10 rows (elements/itemsets/transactions) and
 5 columns (items) and a density of 0.6 

most frequent items:
Product D Product E Product A Product C Product B   (Other) 
        8         8         5         5         4         0 

element (itemset/transaction) length distribution:
sizes
1 2 3 4 5 
1 2 4 2 1 

   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
   1.00    2.25    3.00    3.00    3.75    5.00 

includes extended item information - examples:
     labels
1 Product A
2 Product B
3 Product C

includes extended transaction information - examples:
  transactionID
1             1
2             2
3             3
> 
> # Apply the Apriori algorithm to find association rules
> rules <- apriori(transactions, parameter = list(support = 0.2, confidence = 0.6, target = "rules"))
Apriori

Parameter specification:
 confidence minval smax arem  aval originalSupport maxtime support minlen maxlen
        0.6    0.1    1 none FALSE            TRUE       5     0.2      1     10
 target  ext
  rules TRUE

Algorithmic control:
 filter tree heap memopt load sort verbose
    0.1 TRUE TRUE  FALSE TRUE    2    TRUE

Absolute minimum support count: 2 

set item appearances ...[0 item(s)] done [0.00s].
set transactions ...[5 item(s), 10 transaction(s)] done [0.00s].
sorting and recoding items ... [5 item(s)] done [0.00s].
creating transaction tree ... done [0.00s].
checking subsets of size 1 2 3 4 done [0.00s].
writing ... [47 rule(s)] done [0.00s].
creating S4 object  ... done [0.00s].
> 
> # View the generated rules
> inspect(rules)
     lhs                                  rhs         support confidence coverage
[1]  {}                                => {Product D} 0.8     0.8000000  1.0     
[2]  {}                                => {Product E} 0.8     0.8000000  1.0     
[3]  {Product B}                       => {Product A} 0.3     0.7500000  0.4     
[4]  {Product A}                       => {Product B} 0.3     0.6000000  0.5     
[5]  {Product B}                       => {Product C} 0.3     0.7500000  0.4     
[6]  {Product C}                       => {Product B} 0.3     0.6000000  0.5     
[7]  {Product B}                       => {Product D} 0.3     0.7500000  0.4     
[8]  {Product B}                       => {Product E} 0.3     0.7500000  0.4     
[9]  {Product A}                       => {Product C} 0.3     0.6000000  0.5     
[10] {Product C}                       => {Product A} 0.3     0.6000000  0.5     
[11] {Product A}                       => {Product D} 0.3     0.6000000  0.5     
[12] {Product A}                       => {Product E} 0.4     0.8000000  0.5     
[13] {Product C}                       => {Product D} 0.3     0.6000000  0.5     
[14] {Product C}                       => {Product E} 0.5     1.0000000  0.5     
[15] {Product E}                       => {Product C} 0.5     0.6250000  0.8     
[16] {Product D}                       => {Product E} 0.6     0.7500000  0.8     
[17] {Product E}                       => {Product D} 0.6     0.7500000  0.8     
[18] {Product A, Product B}            => {Product C} 0.2     0.6666667  0.3     
[19] {Product B, Product C}            => {Product A} 0.2     0.6666667  0.3     
[20] {Product A, Product C}            => {Product B} 0.2     0.6666667  0.3     
[21] {Product A, Product B}            => {Product D} 0.2     0.6666667  0.3     
[22] {Product B, Product D}            => {Product A} 0.2     0.6666667  0.3     
[23] {Product A, Product D}            => {Product B} 0.2     0.6666667  0.3     
[24] {Product A, Product B}            => {Product E} 0.2     0.6666667  0.3     
[25] {Product B, Product E}            => {Product A} 0.2     0.6666667  0.3     
[26] {Product B, Product C}            => {Product D} 0.2     0.6666667  0.3     
[27] {Product B, Product D}            => {Product C} 0.2     0.6666667  0.3     
[28] {Product C, Product D}            => {Product B} 0.2     0.6666667  0.3     
[29] {Product B, Product C}            => {Product E} 0.3     1.0000000  0.3     
[30] {Product B, Product E}            => {Product C} 0.3     1.0000000  0.3     
[31] {Product C, Product E}            => {Product B} 0.3     0.6000000  0.5     
[32] {Product B, Product D}            => {Product E} 0.2     0.6666667  0.3     
[33] {Product B, Product E}            => {Product D} 0.2     0.6666667  0.3     
[34] {Product A, Product C}            => {Product E} 0.3     1.0000000  0.3     
[35] {Product A, Product E}            => {Product C} 0.3     0.7500000  0.4     
[36] {Product C, Product E}            => {Product A} 0.3     0.6000000  0.5     
[37] {Product A, Product D}            => {Product E} 0.2     0.6666667  0.3     
[38] {Product C, Product D}            => {Product E} 0.3     1.0000000  0.3     
[39] {Product C, Product E}            => {Product D} 0.3     0.6000000  0.5     
[40] {Product A, Product B, Product C} => {Product E} 0.2     1.0000000  0.2     
[41] {Product A, Product B, Product E} => {Product C} 0.2     1.0000000  0.2     
[42] {Product B, Product C, Product E} => {Product A} 0.2     0.6666667  0.3     
[43] {Product A, Product C, Product E} => {Product B} 0.2     0.6666667  0.3     
[44] {Product B, Product C, Product D} => {Product E} 0.2     1.0000000  0.2     
[45] {Product B, Product C, Product E} => {Product D} 0.2     0.6666667  0.3     
[46] {Product B, Product D, Product E} => {Product C} 0.2     1.0000000  0.2     
[47] {Product C, Product D, Product E} => {Product B} 0.2     0.6666667  0.3     
     lift      count
[1]  1.0000000 8    
[2]  1.0000000 8    
[3]  1.5000000 3    
[4]  1.5000000 3    
[5]  1.5000000 3    
[6]  1.5000000 3    
[7]  0.9375000 3    
[8]  0.9375000 3    
[9]  1.2000000 3    
[10] 1.2000000 3    
[11] 0.7500000 3    
[12] 1.0000000 4    
[13] 0.7500000 3    
[14] 1.2500000 5    
[15] 1.2500000 5    
[16] 0.9375000 6    
[17] 0.9375000 6    
[18] 1.3333333 2    
[19] 1.3333333 2    
[20] 1.6666667 2    
[21] 0.8333333 2    
[22] 1.3333333 2    
[23] 1.6666667 2    
[24] 0.8333333 2    
[25] 1.3333333 2    
[26] 0.8333333 2    
[27] 1.3333333 2    
[28] 1.6666667 2    
[29] 1.2500000 3    
[30] 2.0000000 3    
[31] 1.5000000 3    
[32] 0.8333333 2    
[33] 0.8333333 2    
[34] 1.2500000 3    
[35] 1.5000000 3    
[36] 1.2000000 3    
[37] 0.8333333 2    
[38] 1.2500000 3    
[39] 0.7500000 3    
[40] 1.2500000 2    
[41] 2.0000000 2    
[42] 1.3333333 2    
[43] 1.6666667 2    
[44] 1.2500000 2    
[45] 0.8333333 2    
[46] 2.0000000 2    
[47] 1.6666667 2    
> 
> # Get the lift ratio to evaluate the strength of the associations
> lift_rules <- subset(rules, lift > 1)  # Filter rules with lift greater than 1
> inspect(lift_rules)
     lhs                                  rhs         support confidence coverage
[1]  {Product B}                       => {Product A} 0.3     0.7500000  0.4     
[2]  {Product A}                       => {Product B} 0.3     0.6000000  0.5     
[3]  {Product B}                       => {Product C} 0.3     0.7500000  0.4     
[4]  {Product C}                       => {Product B} 0.3     0.6000000  0.5     
[5]  {Product A}                       => {Product C} 0.3     0.6000000  0.5     
[6]  {Product C}                       => {Product A} 0.3     0.6000000  0.5     
[7]  {Product C}                       => {Product E} 0.5     1.0000000  0.5     
[8]  {Product E}                       => {Product C} 0.5     0.6250000  0.8     
[9]  {Product A, Product B}            => {Product C} 0.2     0.6666667  0.3     
[10] {Product B, Product C}            => {Product A} 0.2     0.6666667  0.3     
[11] {Product A, Product C}            => {Product B} 0.2     0.6666667  0.3     
[12] {Product B, Product D}            => {Product A} 0.2     0.6666667  0.3     
[13] {Product A, Product D}            => {Product B} 0.2     0.6666667  0.3     
[14] {Product B, Product E}            => {Product A} 0.2     0.6666667  0.3     
[15] {Product B, Product D}            => {Product C} 0.2     0.6666667  0.3     
[16] {Product C, Product D}            => {Product B} 0.2     0.6666667  0.3     
[17] {Product B, Product C}            => {Product E} 0.3     1.0000000  0.3     
[18] {Product B, Product E}            => {Product C} 0.3     1.0000000  0.3     
[19] {Product C, Product E}            => {Product B} 0.3     0.6000000  0.5     
[20] {Product A, Product C}            => {Product E} 0.3     1.0000000  0.3     
[21] {Product A, Product E}            => {Product C} 0.3     0.7500000  0.4     
[22] {Product C, Product E}            => {Product A} 0.3     0.6000000  0.5     
[23] {Product C, Product D}            => {Product E} 0.3     1.0000000  0.3     
[24] {Product A, Product B, Product C} => {Product E} 0.2     1.0000000  0.2     
[25] {Product A, Product B, Product E} => {Product C} 0.2     1.0000000  0.2     
[26] {Product B, Product C, Product E} => {Product A} 0.2     0.6666667  0.3     
[27] {Product A, Product C, Product E} => {Product B} 0.2     0.6666667  0.3     
[28] {Product B, Product C, Product D} => {Product E} 0.2     1.0000000  0.2     
[29] {Product B, Product D, Product E} => {Product C} 0.2     1.0000000  0.2     
[30] {Product C, Product D, Product E} => {Product B} 0.2     0.6666667  0.3     
     lift     count
[1]  1.500000 3    
[2]  1.500000 3    
[3]  1.500000 3    
[4]  1.500000 3    
[5]  1.200000 3    
[6]  1.200000 3    
[7]  1.250000 5    
[8]  1.250000 5    
[9]  1.333333 2    
[10] 1.333333 2    
[11] 1.666667 2    
[12] 1.333333 2    
[13] 1.666667 2    
[14] 1.333333 2    
[15] 1.333333 2    
[16] 1.666667 2    
[17] 1.250000 3    
[18] 2.000000 3    
[19] 1.500000 3    
[20] 1.250000 3    
[21] 1.500000 3    
[22] 1.200000 3    
[23] 1.250000 3    
[24] 1.250000 2    
[25] 2.000000 2    
[26] 1.333333 2    
[27] 1.666667 2    
[28] 1.250000 2    
[29] 2.000000 2    
[30] 1.666667 2    
> 
> # Visualize the top association rules
> library(arulesViz)
> plot(rules, method = "graph", main = "Market Basket Analysis - Association Rules")
Warning: Unknown control parameters: main
Available control parameters (with default values):
layout	 =  stress
circular	 =  FALSE
ggraphdots	 =  NULL
edges	 =  <environment>
nodes	 =  <environment>
nodetext	 =  <environment>
colors	 =  c("#EE0000FF", "#EEEEEEFF")
engine	 =  ggplot2
max	 =  100
verbose	 =  FALSE
> 
> # Display the top rules based on lift
> top_rules <- sort(rules, by = "lift", decreasing = TRUE)
> inspect(head(top_rules, 10))  # Display top 10 rules
     lhs                                  rhs         support confidence coverage
[1]  {Product B, Product E}            => {Product C} 0.3     1.0000000  0.3     
[2]  {Product A, Product B, Product E} => {Product C} 0.2     1.0000000  0.2     
[3]  {Product B, Product D, Product E} => {Product C} 0.2     1.0000000  0.2     
[4]  {Product A, Product C}            => {Product B} 0.2     0.6666667  0.3     
[5]  {Product A, Product D}            => {Product B} 0.2     0.6666667  0.3     
[6]  {Product C, Product D}            => {Product B} 0.2     0.6666667  0.3     
[7]  {Product A, Product C, Product E} => {Product B} 0.2     0.6666667  0.3     
[8]  {Product C, Product D, Product E} => {Product B} 0.2     0.6666667  0.3     
[9]  {Product B}                       => {Product A} 0.3     0.7500000  0.4     
[10] {Product A}                       => {Product B} 0.3     0.6000000  0.5     
     lift     count
[1]  2.000000 3    
[2]  2.000000 2    
[3]  2.000000 2    
[4]  1.666667 2    
[5]  1.666667 2    
[6]  1.666667 2    
[7]  1.666667 2    
[8]  1.666667 2    
[9]  1.500000 3    
[10] 1.500000 3    
```
