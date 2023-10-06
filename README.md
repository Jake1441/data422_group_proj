# data422_group_proj
Data422 Group Project

By Jacob Reid, Katie, Rick

# Topic
We wanted to build an app that grabs the Vehicle Kilometres Travelled from the government site and the average fuel price per vehicle class using randomised vehicle types.

# Project Notes

# 20/09/2023
First team meet up for dataset work and prep for prototyping
We covered
- Trello
- Github
- Datasets

How we wanted to communicate ie whatsapp

# 27/09/2023
Discussed getting fields from the CAS csv to minimise the amount of fields in the new flatfile dataframe
Discussed how to wrangle the data and deal with not manipulating the main CAS CSV
looked into dealing with potential conflicts of interest (there are none) with information is beautfil using the same CAS file.
There is none since we do not collaborate with any other groups in such a way that would cause this ethical constraint.
Set up Github and Onedrive

Github is for coding
and Onedrive is for the project files github and onedrive are not connected.

# 29/09/2023
Trello - Project Management software
If not Katie, Rick - Description - Monday 02/09/2023

Web Scraping in julia crash analysis system - Jacob
Read, wrangle. -- Talk about Plot etc after read and wrangling - Do by Monday 02/09/2023


# 02/10/2023
Group Meeting 11am to 11:45am,

We covered
- Data visualisation for CAS 
- Code to save data frames to RDA
	- save data frame from r
	- load data frame into julia
- Make sure team members have access to Trello
- Assigned tasks through Trello 
- No tasks for Tuesday
- Tasks for Wednesday

# 04/10/2023
Discussed in lab about our datasets
Found issues with CAS and lack of unclean data and confusion with values in fields and how they relate to the reader i.e
bridges had areas with no values and adding 0 might confuse the reader.

We changed to VKT (Vehicle Kilometres Travelled)
We looked at changing the model to scraping average car price based on vehicle class and a random vehicle then started narrowing down
to fuel prices to consider

# 06/10/2023

In progress
Discuss fuel prices and if it is what we want to use,
if so combine it with
VKT some new fields that might be useful are 
- Vehicle Class (Random 5 of each for initial testing from scraping)
- Fuel Tank Size Litres
- Max distance a full tank can travel
- Fuel Type car uses
- Fuel price per litre
- VKT has 2010/11 which is the total kilometers travelled yearly per class.
  - Using this field maybe we can do the following
  - Work out how much it costs to travel yearly or monthly or weekly by combining
      - Find out how many tank refuels are needed over this period (likely to be calculated from other fields)

Divide work out to each member using Trello and work through questions for Katies Monday DATA422 Lab time.
Set a time to meet on Tuesday 1pm with our jupyter dataframes sorted

What story does this tell us?
Well if a oil company or the government wants to survey areas and costs for vehicles (assuming each region accurately calculates fuel price by type) they can work through how much fuel could be imported 
They can work through what class might travel the most than making assumptions ie saying Trucks might be correct but automation tasks allow for changes, thinking if say a quake happens and trucks are not feasible the car type and distance travelled may not be so certain
