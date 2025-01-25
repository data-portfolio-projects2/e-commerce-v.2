library(ggplot2)
library(caret)
library(CCA)
library(gridExtra)

scaled_data <- scale(demographics[, c("Age", "Income_Level")])
pca_result <- prcomp(scaled_data, center = TRUE, scale. = TRUE)
pca_summary <- summary(pca_result)

pca_scree_plot <- ggplot(data.frame(PC = 1:length(pca_result$sdev), Variance = pca_result$sdev^2),
                         aes(x = PC, y = Variance)) +
  geom_bar(stat = "identity", fill = "skyblue") +
  labs(title = "PCA - Scree Plot", x = "Principal Component", y = "Variance Explained") +
  theme_minimal()

X <- demographics[, c("Age", "Income_Level", "Gender")]
Y <- demographics[, c("Location")]
X$Gender <- as.numeric(factor(X$Gender))
Y$Location <- as.numeric(factor(Y$Location))

cca_result <- cancor(X, Y)
cca_summary <- cca_result$cor

grid.arrange(pca_scree_plot, ncol = 1)
print(pca_summary)
print("Canonical Correlations (CCA):")
print(cca_summary)
