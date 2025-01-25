required_packages <- c("markovchain", "DiagrammeR")

for (pkg in required_packages) {
  if (!require(pkg, character.only = TRUE)) {
    install.packages(pkg, dependencies = TRUE)
    library(pkg, character.only = TRUE)
  }
}

data <- data.frame(
  Page = c("Home", "Home", "About", "Home", "Products", 
           "Products", "About", "Contact", "Contact", "Home"),
  Next_Page = c("About", "Products", "Products", "Products", 
                "About", "Contact", "Contact", "Home", "Home", "About"),
  stringsAsFactors = FALSE
)

cat("Sample Web Traffic Data:\n")
print(data)

transition_table <- table(data$Page, data$Next_Page)
transition_matrix <- as.matrix(transition_table)

transition_matrix <- apply(transition_matrix, 1, function(row) {
  if (sum(row) == 0) return(row) else return(row / sum(row))
})

transition_matrix <- t(transition_matrix)
transition_matrix <- as.matrix(transition_matrix)

cat("\nNormalized Transition Matrix:\n")
print(transition_matrix)

path_markov_chain <- new(
  "markovchain",
  states = rownames(transition_matrix),
  transitionMatrix = transition_matrix,
  name = "Website Path Analysis"
)

cat("\nMarkov Chain Details:\n")
print(path_markov_chain)

cat("\nVisualizing the Markov Chain:\n")
plot(path_markov_chain)

set.seed(123)
simulated_path <- rmarkovchain(n = 10, object = path_markov_chain, t0 = "Home")

cat("\nSimulated Visitor Navigation Path:\n")
print(simulated_path)
