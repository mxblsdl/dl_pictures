
library(rmarkdown)

# to change
setwd("/home/max/Documents/raspberry/dl_pictures/")

render("markdown_dl.Rmd", output_file = Sys.Date(), clean = T, output_dir = "reports")
