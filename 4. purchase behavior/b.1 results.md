![image](https://github.com/user-attachments/assets/50b526c0-fbab-4c61-9bc4-fdf21edb56b3)

```r
customer_id total_purchases most_recent_purchase recency_days total_spent cluster
        <int>           <int> <date>                      <int>       <int>   <int>
1           1               2 2024-10-10                     99         350       3
2           2               3 2024-11-28                     50         772       3
3           3               5 2024-01-17                    366        1126       1
4           4               3 2023-03-02                    687        1100       1
5           5               7 2024-02-06                    346        1759       1
6           6               5 2024-10-25                     84        1627       1
# ℹ 1 more variable: segment <chr>
> 
> # Summary statistics
> summary(rfm_data)
  customer_id    total_purchases most_recent_purchase  recency_days  
 Min.   : 1.00   Min.   : 2.0    Min.   :2023-03-02   Min.   :  0.0  
 1st Qu.: 3.25   1st Qu.: 3.0    1st Qu.:2024-03-31   1st Qu.: 41.0  
 Median : 5.50   Median : 5.0    Median :2024-10-17   Median : 91.5  
 Mean   : 5.50   Mean   : 5.0    Mean   :2024-07-20   Mean   :180.4  
 3rd Qu.: 7.75   3rd Qu.: 6.5    3rd Qu.:2024-12-07   3rd Qu.:292.0  
 Max.   :10.00   Max.   :11.0    Max.   :2025-01-17   Max.   :687.0  
  total_spent      cluster       segment         
 Min.   : 217   Min.   :1.00   Length:10         
 1st Qu.: 854   1st Qu.:1.00   Class :character  
 Median :1376   Median :1.00   Mode  :character  
 Mean   :1345   Mean   :1.70                     
 3rd Qu.:1745   3rd Qu.:2.75
```                
 Max.   :3029   Max.   :3.00               
