required_packages <- c("markovchain", "DiagrammeR")

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

simulate_visitor_navigation <- function(markov_chain, start_state, n_steps) {
  set.seed(123)
  simulated_path <- rmarkovchain(n = n_steps, object = markov_chain, t0 = start_state)
  return(simulated_path)
}

data <- data.frame(
  Page = c("Home", "Home", "About", "Home", "Products", 
           "Products", "About", "Contact", "Contact", "Home"),
  Next_Page = c("About", "Products", "Products", "Products", 
                "About", "Contact", "Contact", "Home", "Home", "About"),
  stringsAsFactors = FALSE
)

