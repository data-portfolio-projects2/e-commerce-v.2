set.seed(123)  
demographics <- data.frame(
  Age = sample(18:65, 10, replace = TRUE),
  Location = sample(c("Urban", "Suburban", "Rural"), 10, replace = TRUE),
  Gender = sample(c("Male", "Female"), 10, replace = TRUE),
  Income_Level = sample(20000:100000, 10, replace = TRUE)
)

library(cluster)
library(factoextra)

clustering_data <- demographics[, c("Age", "Income_Level")]
scaled_data <- scale(clustering_data)
set.seed(123)
kmeans_result <- kmeans(scaled_data, centers = 3, nstart = 25)
demographics$Cluster <- as.factor(kmeans_result$cluster)

fviz_cluster(kmeans_result, data = scaled_data,
             geom = "point", 
             ellipse.type = "norm",
             ggtheme = theme_minimal(),
             main = "Customer Segmentation by Age and Income Level")

cluster_profiles <- aggregate(demographics[, c("Age", "Income_Level")], 
                               by = list(Cluster = demographics$Cluster), 
                               FUN = mean)
print(cluster_profiles)
