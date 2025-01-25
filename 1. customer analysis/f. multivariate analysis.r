load_required_packages <- function() {
  library(ggplot2)
  library(caret)
  library(CCA)
  library(gridExtra)
}

perform_pca <- function(data) {
  scaled_data <- scale(data[, c("Age", "Income_Level")])
  prcomp(scaled_data, center = TRUE, scale. = TRUE)
}

create_pca_scree_plot <- function(pca_result) {
  ggplot(data.frame(PC = 1:length(pca_result$sdev), Variance = pca_result$sdev^2),
         aes(x = PC, y = Variance)) +
    geom_bar(stat = "identity", fill = "skyblue") +
    labs(title = "PCA - Scree Plot", x = "Principal Component", y = "Variance Explained") +
    theme_minimal()
}

perform_cca <- function(X, Y) {
  X$Gender <- as.numeric(factor(X$Gender))
  Y$Location <- as.numeric(factor(Y$Location))
  cancor(X, Y)
}

display_results <- function(pca_summary, cca_summary) {
  print(pca_summary)
  print("Canonical Correlations (CCA):")
  print(cca_summary)
}

arrange_and_display_plots <- function(pca_scree_plot) {
  grid.arrange(pca_scree_plot, ncol = 1)
}
