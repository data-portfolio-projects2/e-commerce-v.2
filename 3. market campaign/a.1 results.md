```r
Group Budget      Channel Impressions Conversions       CTR Conversion_Rate
1     A   9104        Email       42555         178 0.4182822       0.4182822
2     A  13908       Search        7175         447 6.2299652       6.2299652
3     A   7403        Email       33744         486 1.4402560       1.4402560
4     B  17801 Social Media       30789         437 1.4193381       1.4193381
5     A  17716 Social Media       47338         918 1.9392454       1.9392454
6     B  12168        Email       29451         736 2.4990662       2.4990662
```

```r
T-test Results for Conversion Rates between Groups A and B:

Welch Two Sample t-test

data:  Conversion_Rate by Group
t = -0.48087, df = 918.3, p-value = 0.6307
alternative hypothesis: true difference in means between group A and group B is not equal to 0
95 percent confidence interval:
 -1.1378247  0.6899747
sample estimates:
mean in group A mean in group B 
       4.216993        4.440918
```
