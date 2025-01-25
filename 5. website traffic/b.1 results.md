![image](https://github.com/user-attachments/assets/19c8df86-1bee-4b69-a9c8-768359d795a4)

```r
Sample Web Traffic Data:
> print(data)
       Page Next_Page
1      Home     About
2      Home  Products
3     About  Products
4      Home  Products
5  Products     About
6  Products   Contact
7     About   Contact
8   Contact      Home
9   Contact      Home
10     Home     About
```

```r
Normalized Transition Matrix:
> print(transition_matrix)
          
           About Contact Home Products
  About      0.0     0.5    0      0.5
  Contact    0.0     0.0    1      0.0
  Home       0.5     0.0    0      0.5
  Products   0.5     0.5    0      0.0
```

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
Simulated Visitor Navigation Path:
> print(simulated_path)
 [1] "About"    "Products" "About"    "Products" "Contact"  "Home"     "Products"
 [8] "Contact"  "Home"     "About"
```
