load_required_libraries <- function() {
  library(tm)
  library(wordcloud)
  library(tidyverse)
}

clean_feedback_data <- function(feedback_data) {
  feedback_data_cleaned <- feedback_data %>%
    mutate(
      Feedback_Cleaned = Feedback %>%
        tolower() %>%
        removePunctuation() %>%
        removeNumbers() %>%
        removeWords(stopwords("en"))
    )
  return(feedback_data_cleaned)
}

generate_wordcloud <- function(feedback_data_cleaned) {
  feedback_words <- unlist(str_split(feedback_data_cleaned$Feedback_Cleaned, " "))
  word_freq <- table(feedback_words)
  word_freq <- word_freq[word_freq > 0]

  wordcloud(names(word_freq), freq = word_freq, min.freq = 1, scale = c(3, 0.5), 
            colors = brewer.pal(8, "Dark2"))
  
  word_freq_sorted <- sort(word_freq, decreasing = TRUE)
  cat("Most frequent words:\n")
  print(head(word_freq_sorted, 10))
}
