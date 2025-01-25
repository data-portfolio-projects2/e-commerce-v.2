set.seed(123)

create_demographics_data <- function() {
  data.frame(
    Age = sample(18:65, 10, replace = TRUE),
    Location = sample(c("Urban", "Suburban", "Rural"), 10, replace = TRUE),
    Gender = sample(c("Male", "Female"), 10, replace = TRUE),
    Income_Level = sample(20000:100000, 10, replace = TRUE)
  )
}

perform_kmeans_clustering <- function(data, centers = 3) {
  clustering_data <- data[, c("Age", "Income_Level")]
  scaled_data <- scale(clustering_data)
  kmeans_result <- kmeans(scaled_data, centers = centers, nstart = 25)
  return(kmeans_result)
}

add_cluster_column <- function(data, kmeans_result) {
  data$Cluster <- as.factor(kmeans_result$cluster)
  return(data)
}

visualize_clusters <- function(kmeans_result, scaled_data) {
  fviz_cluster(kmeans_result, data = scaled_data,
               geom = "point", 
               ellipse.type = "norm",
               ggtheme = theme_minimal(),
               main = "Customer Segmentation by Age and Income Level")
}

calculate_cluster_profiles <- function(data) {
  cluster_profiles <- aggregate(data[, c("Age", "Income_Level")], 
                                by = list(Cluster = data$Cluster), 
                                FUN = mean)
  return(cluster_profiles)
}

run_eda_pipeline <- function() {
  demographics <- create_demographics_data()
  kmeans_result <- perform_kmeans_clustering(demographics)
  demographics <- add_cluster_column(demographics, kmeans_result)
  scaled_data <- scale(demographics[, c("Age", "Income_Level")])
  visualize_clusters(kmeans_result, scaled_data)
  cluster_profiles <- calculate_cluster_profiles(demographics)
  print(cluster_profiles)
}

run_eda_pipeline()
