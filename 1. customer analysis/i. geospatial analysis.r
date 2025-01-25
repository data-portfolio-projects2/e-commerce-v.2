generate_random_coordinates <- function(data) {
  data$Longitude <- runif(10, min = -180, max = 180)
  data$Latitude <- runif(10, min = -90, max = 90)
  return(data)
}

fetch_base_map <- function() {
  get_stamenmap(bbox = c(left = -180, bottom = -90, right = 180, top = 90), zoom = 2)
}

create_geospatial_plot <- function(base_map, data) {
  ggmap(base_map) +
    geom_point(aes(x = Longitude, y = Latitude, color = Location), data = data, size = 3) +
    labs(title = "Geospatial Distribution of Customers", x = "Longitude", y = "Latitude") +
    theme_minimal()
}
