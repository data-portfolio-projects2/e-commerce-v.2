load_required_packages <- function() {
  if (!require("tidyverse")) install.packages("tidyverse")
  if (!require("sentimentr")) install.packages("sentimentr")
  library(tidyverse)
  library(sentimentr)
}

prepare_feedback_data <- function() {
  data.frame(
    Customer = paste("Customer", 1:20),
    Feedback = c(
      "I love this product! It is amazing.",
      "The service was terrible, I won't buy again.",
      "It was okay, nothing special.",
      "The best experience I've ever had, will recommend to everyone!",
      "Horrible quality, I feel scammed.",
      "Great customer service, very helpful staff.",
      "Very disappointed, will never use again.",
      "Fantastic product! Worth every penny.",
      "The worst purchase I ever made.",
      "The product arrived late, but it works fine.",
      "Good value for the price, but could improve packaging.",
      "I had high expectations, but I was let down.",
      "Excellent quality, will buy again!",
      "Not worth the price, very dissatisfied.",
      "I'm very pleased with this product!",
      "I regret buying this item.",
      "Very fast delivery, but the product quality was poor.",
      "Okay product, but there are better alternatives.",
      "Amazing quality! Exceeded my expectations.",
      "Totally disappointing, won't be coming back."
    )
  )
}

calculate_sentiment <- function(feedback_data) {
  sentiment_results <- sentiment(feedback_data$Feedback)
  feedback_data$Sentiment <- sapply(1:nrow(feedback_data), function(i) {
    feedback_sentences <- sentiment_results[sentiment_results$element_id == i, ]
    mean(feedback_sentences$sentiment)
  })
  return(feedback_data)
}
