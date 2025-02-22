library(tidyverse)
library(ggplot2)
library(dplyr)
library(lubridate)

#Import data set
parking_tickets <- read_csv('/Users/tylerkatz/Documents/Datathon/Datathon-AW-TK-BL-JK-WC/Data/SYRParking Violations/Parking_Violations_-_2023_-_Present.csv')

#Convert issued_date column into POSIXct data type
parking_tickets <- parking_tickets %>%
  mutate(issued_date = ymd_hms(issued_date, tz = "UTC"))

#ChatGPT assisted code, creates issue_month, issue_day, and week_in_month columns
parking_tickets <- parking_tickets %>%
  mutate(issue_month = format(issued_date, "%B"),  
         issue_day = format(issued_date, "%A"),
         week_in_month = (day(issued_date) - 1) %/% 7 + 1
         )

#ChatGPT assisted
#Converts the issue_month, issue_day and week_in_month columns into factors so they appear in order on graph
#Categorizes the hours into different groups, and orders them to graph how many tickets are issued at different times of day
parking_tickets <- parking_tickets %>%
  mutate(issue_month = factor(issue_month, 
                              levels = month.name),
         week_in_month = ifelse(week_in_month %in% c("1", "2", "3", "4"), week_in_month, "4"),
         week_in_month =factor(week_in_month, levels = rev(levels(factor(week_in_month)))),
         issue_day = factor(issue_day, 
                            levels = c("Monday", "Tuesday", "Wednesday", 
                                       "Thursday", "Friday", "Saturday", "Sunday")),
         hour = hour(issued_date),  
         time_range = case_when(
           hour >= 6 & hour < 9  ~ "6 AM - 9 AM",
           hour >= 9 & hour < 12 ~ "9 AM - 12 PM",
           hour >= 12 & hour < 15 ~ "12 PM - 3 PM",
           hour >= 15 & hour < 18 ~ "3 PM - 6 PM",
           hour >= 18 & hour < 21 ~ "6 PM - 9 PM",
           hour >= 21 & hour < 24 ~ "9 PM - 12 AM",
           hour >= 0 & hour < 6  ~ "12 AM - 6 AM"  
         ),
         time_range = factor(time_range, levels = c(
           "6 AM - 9 AM", "9 AM - 12 PM", "12 PM - 3 PM",
           "3 PM - 6 PM", "6 PM - 9 PM", "9 PM - 12 AM", "12 AM - 6 AM"
         ))
         )

#Creates bar graph showing month of ticket issued by which week of the month the date falls into
issued_months <- ggplot(parking_tickets)+
                 aes(x = issue_month, fill = week_in_month)+
                 geom_bar(color = "#cc7a00", position = "stack")+
                 ggtitle("Months of Issued Parking Tickets by Week in Month")+
                 xlab("Months of Issued Tickets")+
                 ylab("Number of Tickets Issued")+
                 theme(axis.text.x = element_text(angle = 45, hjust = 1))+
                 scale_fill_manual(values = c("1" = "#ffe0b3", "2" = "#ffcc80", "3" = "#ffb84d", "4" = "#ff9900"),
                    name = "Week in Month")

#Creates bar graph showing days of the week of issued tickets
issue_day <- ggplot(parking_tickets)+
             aes(x = issue_day)+
             geom_bar(color = "#ffb84d", fill = "#ff9900")+
             ggtitle("Days of the Week of Issued Tickets")+
             xlab("Days of the Week")+
             ylab("Number of Issued Tickets")+
             theme(axis.text.x = element_text(angle = 45, hjust = 1))

#Creates bar graph showing the times of issued tickets
issue_time <- ggplot(parking_tickets)+
              aes(x = time_range)+
              geom_bar(color = "#ffb84d", fill = "#ff9900")+
              ggtitle("Time of Issued Tickets")+
              xlab("Time Ranges")+
              ylab("Number of Tickets")+
              theme(axis.text.x = element_text(angle = 45, hjust = 1))

#Outputs the graph
issued_months

issue_day

issue_time

