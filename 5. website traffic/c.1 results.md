![image](https://github.com/user-attachments/assets/2fd66ce7-1d86-40b5-afac-abd7804ea595)

```r
Markov Chain Details:
> print(path_markov_chain)
          
           About Contact Home Products
  About      0.0     0.5    0      0.5
  Contact    0.0     0.0    1      0.0
  Home       0.5     0.0    0      0.5
  Products   0.5     0.5    0      0.0
```

```r
Simulated Clickstream Data (first few entries):
> print(head(click_data))
   x y
1  3 6
2  3 2
3 10 1
4  2 5
5  6 9
6  5 4
```
