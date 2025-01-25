```r
head(campaign_data)
  Group Budget      Channel Impressions Conversions       CTR Conversion_Rate
1     A   9104        Email       42555         178 0.4182822       0.4182822
2     A  13908       Search        7175         447 6.2299652       6.2299652
3     A   7403        Email       33744         486 1.4402560       1.4402560
4     B  17801 Social Media       30789         437 1.4193381       1.4193381
5     A  17716 Social Media       47338         918 1.9392454       1.9392454
6     B  12168        Email       29451         736 2.4990662       2.4990662
```

```r
Call:
lm(formula = Conversion_Rate ~ Budget + Channel + Group, data = campaign_data)

Residuals:
   Min     1Q Median     3Q    Max 
-4.972 -3.044 -2.086 -0.132 75.046 

Coefficients:
                      Estimate Std. Error t value Pr(>|t|)    
(Intercept)          3.152e+00  8.242e-01   3.824 0.000139 ***
Budget               7.080e-05  5.421e-05   1.306 0.191862    
ChannelSearch       -5.258e-03  5.588e-01  -0.009 0.992494    
ChannelSocial Media  5.362e-01  5.794e-01   0.925 0.354947    
GroupB               2.612e-01  4.648e-01   0.562 0.574313    
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 7.339 on 995 degrees of freedom
Multiple R-squared:  0.003101,	Adjusted R-squared:  -0.0009064 
F-statistic: 0.7738 on 4 and 995 DF,  p-value: 0.5423
```
