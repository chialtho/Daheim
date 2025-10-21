setwd("P:/DWD_Daten")

library(readxl)
library(tidyverse)
library(ggplot2)

names_of_columns <- c("Jahr", "Monat", "precip", "H+_f", "Cl-_f", "NO3-N_f",
                      "SO4-S_f", "Na+_f",	"NH4-N_f",	"K+_f", "Mg2+_f",	"Ca2+_f",
                      "Atot_f", "NO3-", "SO4--", "NH4+", "NH4/SO4", "NH4/NO3",
                      "Na7Cl", "NA", "NA", "NA", "NA", "NA", "NA", "pH",
                      "H+_uf",	"Cl-_uf", "NO3-N_uf", "SO4-S_uf", "Na+_uf",
                      "NH4-N_uf",	"K+_uf", "Mg2+_uf",	"Ca2+_uf", "Atot_uf",
                      "NO3-_uf", "SO4--_uf", "NH4+_uf", "N", "flag", "NA",
                      "Kat", "An", "cond_bal", "Ion_bal")

mw <- read_excel("Aerosol_Gesamtfilter.xlsx", sheet = "Monatswerte",
                 range = "A5:AT316", col_names = names_of_columns)

monatswerte <- tibble(mw)
view(monatswerte)


gg <- ggplot(monatswerte, mapping = aes(x = Monat, y = pH)) +
  geom_line(color = "blue") +
  geom_smooth(method = "lm", color = "red", se = FALSE) +
  geom_point(color = "green", size = 1) + ylim(4.5, 6)
gg
ggsave("gg.pdf")



all_months <- c("JAN", "FEB", "MAR", "APR", "MAI", "JUN",
                "JUL", "AUG", "SEP", "OKT", "NOV", "DEZ")


monatswerte$precip[is.na(monatswerte$precip)] <- all_months

view(monatswerte)


names_colums_years <- c("Jahr", "H+_f",	"Cl-_f", "NO3-N_f",
                        "SO4-S_f", "Na+_f",	"NH4-N_f",
                        "K+_f", "Mg2+_f",	"Ca2+_f", "Atot_f",
                        "NO3-", "SO4--", "NH4+")

jw <- read_excel("Aerosol_Gesamtfilter.xlsx",
                 sheet = "Monatswerte",
                 range = "C337:P362",
                 col_names = names_colums_years)

jahreswerte <- tibble(jw)
view(jahreswerte)

gg_gesamt <- ggplot(jahreswerte, aes(x = Jahr, y = `Atot_f`)) +
  geom_bar(stat = "identity",
           color = "darkblue",
           fill = "darkblue",
           width = 0.5)

gg_gesamt


gg2 <- ggplot(jahreswerte, aes(x = `Atot_f`)) +
  geom_histogram(aes(y = ..density..),
                 fill = "white",
                 color = "darkblue",
                 bins = 20) +
  geom_density(color = "blue", fill = "lightblue", lwd = 1, alpha = 0.5)
gg2