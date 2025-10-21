setwd("C:/Users/Chiara/Programmierung/Daheim/DWD_Daten/Zeitreihen_Animation/")
library(tidyverse)
library(ggplot2)
library(gridExtra)
library(gganimate)
library(readxl)


time_series_data <- read_excel("Monatsmittel_T_Abweichungen.xlsx",
                               sheet = "TempMittel_korr",
                               range = "B5:Q242",
                               col_names = FALSE)
time_series_data <- as_tibble(time_series_data)

time_series_data <- time_series_data %>% select("...1", "...16")
time_series_data <- rename(time_series_data,
                           Jahr = "...1",
                           Mitteltemperatur = "...16")


p <- ggplot(
  time_series_data,
  aes(x = Jahr, y =  Mitteltemperatur)
) +
  geom_line(color = "#c302d6", size = 1.1) +
  geom_point(color = "#130555") +
  labs(x = "Year", y = "Temperature", title = "Time course")

p <- p + transition_reveal(Jahr)

animate(p, height = 500, width = 800, fps = 20, duration = 60.5)

anim_save("first_anim.gif")
