# data422_group_proj
Data422 Group Project

By Jacob Reid
DATA422 Group Project Lead

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

# 07/10/2023
JAR141 Started work on Fuel Prices
- Found 3 datasets to try
- Kaggle
- Data.world
- MBIE

The first two required log ins and Kaggle seemed to be a bit more complex to log into to find the dataset
Data.world offered a more reasonable login but R could not impute the username or password fields with a name as the form fields did not
have names. 

MBIE rejected scraping with 403 errors on campus 

Overall ended up choosing Overseas Trade Indexes (Prices and Volumes) from 
https://catalogue.data.govt.nz/dataset?q=fuel+price&sort=score+desc%2C+metadata_modified+desc

and finding a link from Stats NZ to download.
Tried a form of scraping the site using the web tools but the site uses xml_document may try t his under julia and get lab help hopefully
on Wendesday and Thursday to try and achieve something using julia to scrape the goverment site and provide the xlsx file for R to use.

for now, R just downloads the xslx link directly,

interestingly the data is ok when opened in excel but the same data and table is not interpreted the same by R leading to far more missing data values
it looks to be more that some of the data might be circular (imputed by a formula on loading excel) and or is just not able to be completely read by the R
excel function.

# 08/10/2023
Discuss Fuel prices excel file with Rick
We looked at scraping gaspy through R but had issues
Jacob established that RSelenium set up seemed to require more complexity than could be easily achieved based
on docs from installing chromium web driver, java and linux

Jacob will look at graphs using Julia so we can have visulisations ready once the dataset is ready.
A databased planning flowchart would be helpful


What story does this tell us?
Well if a oil company or the government wants to survey areas and costs for vehicles (assuming each region accurately calculates fuel price by type) they can work through how much fuel could be imported 
They can work through what class might travel the most than making assumptions ie saying Trucks might be correct but automation tasks allow for changes, thinking if say a quake happens and trucks are not feasible the car type and distance travelled may not be so certain

# 09/10/2023
Begin looking at different julia graphs https://juliagraphs.org/packages/

# 10/10/2023
Jacob
Created graphs to test ability to graph fuel prices using histograms, box plots, plots, scatter plots, density plot and
a linear regression model.

Katie
Found a stuff.co.nz car type article with light vehicles, has chosen to only use the light vehicle for the datasets as trucks and bus tank size is difficult to find.

discussion on how to deal with the 2010/11 field cost being high
a suggestion was we just impute it based on a fleet of 10 vehicles, the target of our project will want to project the cost for
a fleet of 10 vehicles.

This may rule out regions as finding specific fuel prices and scraping them for region has been difficult.

Saved figures to temp project directory (not on onedrive) so plots will eventually
be saved disk for viewing

Gather presentation templates to look at stylising presentation
# 11/10/2023
Discussed VKT dataset with tutors 
worked out with them long dataframe might be a better approach

Worked out the authority type for VKT would be 'National'
and the car type would be 'Light (Car, LCV)'
We realised this flattened out the VKT dataset with one row
containing every data and the KMS per year given were confusingly large.

We adapted the dataset to be a new VKT dataset based on
the years in the weekly fuel prices (2004-2023) We
decided on two vehicles per years and the following rules.

- vehicles per year (combine {make, model})
- a fleet of 10 vehicles:
  the calculation will be kms travelled 10*(2013 range * 26 refuels)
- 26 refuels is two weekly refuels a arbitrary number to work distance travelled
- get fuel cost per fleet of 10 vehicles based on tank size, fuel costs and refuels
	10 * ((55 * 26) * 2.38)

Divide the work out,
Katie: Get year, random  unique vehicle and fuel type
Rick: Get KMs travelled, Fuel costs, these will be calculated
Jacob: Finalise using Julia graphs and sort out presentation and project report

# 12/10/2023
Further work on presentation and finding some templates to use, 
prepare for report writing.

# 13/10/2023
Covered more work on presentation and commenced writing up draft project report

# 14/10/2023
No work done

# 15/10/2023
Created basic Entity Relationship Diagram using R

# 16/10/2023

Start work on graphing fuel types
cleaned up plots into a plot function (one field only)

Collect linear regression model code to start configuring for final graphing
created a text file called JuliaLinRegressionModel_Code to test linear regression

created a jupyter notebook to test the code before implementing it into the final julia graphing
created a lineaadapted linear regression model to fuel prices based on diesel and regular petrol.
premium petrol has too little fields at the moment .

FuelCost	Freq
String	Int64
1	Diesel	100
2	Regular_Petrol	180
3	Premium_Petrol_95R	20
