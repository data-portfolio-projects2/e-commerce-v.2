plot1 <- ggplot(demographics, aes(x = Age)) +
  geom_histogram(binwidth = 5, fill = "skyblue", color = "black") +
  labs(title = "Age Distribution", x = "Age", y = "Frequency") +
  theme_minimal()

plot2 <- ggplot(demographics, aes(x = Gender, fill = Gender)) +
  geom_bar() +
  labs(title = "Gender Distribution", x = "Gender", y = "Count") +
  scale_fill_manual(values = c("Male" = "blue", "Female" = "pink")) +
  theme_minimal()

plot3 <- ggplot(demographics, aes(x = Location, fill = Location)) +
  geom_bar() +
  labs(title = "Location Distribution", x = "Location", y = "Count") +
  scale_fill_brewer(palette = "Set3") +
  theme_minimal()

plot4 <- ggplot(gender_counts, aes(x = "", y = n, fill = Gender)) +
  geom_col(width = 1) +
  coord_polar(theta = "y") +
  labs(title = "Gender Proportion") +
  theme_void() +
  scale_fill_manual(values = c("Male" = "blue", "Female" = "pink"))

plot5 <- ggplot(location_counts, aes(x = 2, y = n, fill = Location)) +
  geom_col() +
  coord_polar(theta = "y") +
  labs(title = "Location Proportion") +
  xlim(1.5, 2.5) +
  theme_void() +
  scale_fill_brewer(palette = "Set3")

grid.arrange(plot1, plot2, plot3, plot4, plot5, ncol = 2)
