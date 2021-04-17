
library(rmarkdown)

# to change
setwd("/home/max/dl_pictures/")

render("markdown_dl.Rmd", output_file = Sys.Date(), clean = T, output_dir = "reports")


# firefox -kiosk --private-window http://167.71.158.245:3838/weather_clock/
