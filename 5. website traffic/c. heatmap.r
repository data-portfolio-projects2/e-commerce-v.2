required_packages <- c("markovchain", "ggplot2", "dplyr")

install_and_load_packages <- function(packages) {
  for (pkg in packages) {
    if (!require(pkg, character.only = TRUE)) {
      install.packages(pkg, dependencies = TRUE)
      library(pkg, character.only = TRUE)
    }
  }
}

generate_transition_matrix <- function(data) {
  transition_table <- table(data$Page, data$Next_Page)
  transition_matrix <- as.matrix(transition_table)
  transition_matrix <- apply(transition_matrix, 1, function(row) {
    if (sum(row) == 0) return(row) else return(row / sum(row))
  })
  transition_matrix <- t(transition_matrix)
  transition_matrix <- as.matrix(transition_matrix)
  return(transition_matrix)
}

create_markov_chain <- function(transition_matrix) {
  new(
    "markovchain",
    states = rownames(transition_matrix),
    transitionMatrix = transition_matrix,
    name = "Website Path Analysis"
  )
}

generate_click_data <- function(num_clicks) {
  data.frame(
    x = sample(1:10, num_clicks, replace = TRUE),
    y = sample(1:10, num_clicks, replace = TRUE)
  )
}

plot_click_heatmap <- function(click_data) {
  ggplot(click_data, aes(x = x, y = y)) +
    stat_density2d(aes(fill = after_stat(density)), geom = "tile", contour = FALSE) +
    scale_fill_viridis_c() +
    theme_minimal() +
    labs(title = "Simulated Webpage Click Heatmap",
         x = "X-Axis (Webpage Areas)",
         y = "Y-Axis (Webpage Areas)",
         fill = "Density") +
    theme(axis.text = element_text(size = 12), axis.title = element_text(size = 14))
}

data <- data.frame(
  Page = c("Home", "Home", "About", "Home", "Products", 
           "Products", "About", "Contact", "Contact", "Home"),
  Next_Page = c("About", "Products", "Products", "Products", 
                "About", "Contact", "Contact", "Home", "Home", "About"),
  stringsAsFactors = FALSE
)
