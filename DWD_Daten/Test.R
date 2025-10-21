
setwd("P:/DWD_Daten")

install.packages("readxl")
library(readxl)
library(tidyverse)
library(ggplot2)



names_of_columns <- c("Start_Datum", "End_Datum", "H+_f",	"Cl-_f", "NO3-N_f", "SO4-S_f","Na+_f",	"NH4-N_f",	"K+_f", "Mg2+_f",	"Ca2+_f","Atot_f",
                      "H+_log",	"Cl-_log", "NO3-N_log", "SO4-S_log","Na+_log",	"NH4-N_log",	"K+_log", "Mg2+_log",	"Ca2+_log","Atot_log",
                      "H+_uf",	"Cl-_uf", "NO3-N_uf", "SO4-S_uf","Na+_uf",	"NH4-N_uf",	"K+_uf", "Mg2+_uf",	"Ca2+_uf",
                      "H+_eq",	"Cl-_eq", "NO3-N_eq", "SO4-S_eq","Na+_eq",	"NH4-N_eq",	"K+_f", "Mg2+_eq",	"Ca2+_eq", "OH-_eq", "HCO3-_eq",
                      "Kat", "An", "sond_bal", "Ion_bal", "flux", "elu", "days", "cond", "pH", 
                      "H+_co",	"Cl-_co", "NO3-N_co", "SO4-S_co","Na+_co",	"NH4-N_co",	"K+_co", "Mg2+_co",	"Ca2+_co")

pb_21 <- read_excel("Aerosol_Gesamtfilter.xlsx", sheet = "Jb2021", range = "A7:BH371", col_names = names_of_columns)
total <- tibble(pb_21)
view(total)


gg <- ggplot(total,mapping = aes(x = Start_Datum, y =  `H+_f`)) + 
  geom_line(color = "blue") +  geom_smooth(method = "lm", color = "red")

gg

library(RCy3)

