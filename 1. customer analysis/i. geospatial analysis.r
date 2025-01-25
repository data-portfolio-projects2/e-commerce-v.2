install.packages("ggmap")
library(ggplot2)
library(ggmap)

set.seed(123)
demographics$Longitude <- runif(10, min = -180, max = 180)
demographics$Latitude <- runif(10, min = -90, max = 90)

base_map <- get_stamenmap(bbox = c(left = -180, bottom = -90, right = 180, top = 90), zoom = 2)

geospatial_plot <- ggmap(base_map) +
  geom_point(aes(x = Longitude, y = Latitude, color = Location), data = demographics, size = 3) +
  labs(title = "Geospatial Distribution of Customers", x = "Longitude", y = "Latitude") +
  theme_minimal()

print(geospatial_plot)
