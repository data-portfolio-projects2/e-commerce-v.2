![image](https://github.com/user-attachments/assets/73366bd7-9b53-4d7e-9e1b-d7fc63018a27)

```r
Normal Fit for Age:> print(fit_age)
Fitting of the distribution ' norm ' by maximum likelihood 
Parameters:
     estimate Std. Error
mean 42.00000   4.024922
sd   12.72792   2.846050
> cat("\nNormal Fit for Income:")

Normal Fit for Income:> print(fit_income)
Fitting of the distribution ' norm ' by maximum likelihood 
Parameters:
     estimate Std. Error
mean 44856.80   5671.734
sd   17174.48   4010.522
> cat("\nPoisson Fit for Age:")

Poisson Fit for Age:> print(fit_poisson_age)
Fitting of the distribution ' pois ' by maximum likelihood 
Parameters:
       estimate Std. Error
lambda       42    2.04939
```
