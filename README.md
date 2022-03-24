# UofU datathon4justice

This repo contains all of the curated data for the UofU datathon4justice:
- datathon_lights
- datathon_crashes
- Utah_Census_Tracts_2020
- census_data_2020.csv
- Streets_with_Address_Ranges
- LA_Census_Tracts_2020
- census_data_2020_LA.csv
- LA_Street_lights.zip

The core Salt Lake City data is contained in the zipped directory "datathon_sample_data.zip". A google colab notebook with instructions on how to get started with analyzing the SLC data is [available here](https://colab.research.google.com/drive/1wFibIh6pVIZf6V9_GnBkarmLEQE_z9OX?usp=sharing).

The lights and crash data sets were provided by Dr. Daniel Mendoza of the U. All other data was accessed from publicly available sources.

For more information on light pollution and environmental justice, see the [primer prepared for participants](https://docs.google.com/document/d/1DLcSbR4It1JvCrbmp8cm4UPjToZVGou2HbNDtOtDAzs/edit?usp=sharing).

**To download this data**, one can either
1. fork the repo,
2. download everything by clicking the green "Code" button to the top-right of the file explorer, and then "download zip", or
3. follow [these instructions](https://www.wikihow.com/Download-a-File-from-GitHub) to download individual files. Essentially: navigate to a file, view the raw data, and then right-click and save the page with your desired filename.

## datathon_lights and datathon_crashes

As mentioned, **the lights and crash data were provided by Dr. Daniel Mendoza**.

lights contains 20,091 light fixture data objects for SLC, including information about wattage, location, and whether the fixture is public or private. Moreover, the data has been processed to include which census tract the fixture is in.

crashes contains 67,686 data entries of incidents involving motor vehicles, possibly including pedestrians, motorcyclists, or bicyclists, as well is the occurence date and time, location, and severity of the incident. Like lights, crashes has been processed to include which census tract each occurrence was in.

More information about the variables in each of lights and crashes can be found in "Light_Crashes_Metadata.xlsx".

## Utah_Census_Tracts_2020

All census tracts for the state of Utah are provided, though census data is only provided for Salt Lake County. The .csv file "SLC_census_tracts.csv" has census tract codes for those tracts within Salt Lake City proper. A map showing census tracts for Salt Lake County can be [found here](https://www2.census.gov/geo/maps/DC2020/PL20/st49_ut/censustract_maps/c49035_salt_lake/DC20CT_C49035.pdf). For more information about census tracts, see the [official Census Glossary](https://www.census.gov/programs-surveys/geography/about/glossary.html#par_textimage_13).

**Census tract shapefiles were pulled from the [Utah state GIS open data website](https://opendata.gis.utah.gov/datasets/utah-census-tracts-2020/explore)**. In Utah there are 716 census tracts.

### census_data_2020.csv

The census data provided is the American Community Survey 5-year estimates data, available from the US Census Bureau. For more information about the ACS 5-year survey, see [their wiki page](https://en.wikipedia.org/wiki/American_Community_Survey). For more information about the US Census Bureau, and in particular data stewarship, see [their wiki page](https://en.wikipedia.org/wiki/American_Community_Survey).

Almost all available estimated census variables, for each tract in Salt Lake County, were accessed. For information about these variables, see the [census website](https://api.census.gov/data/2020/acs/acs5/profile/variables.html). **A short script ("read_census_data_share.py") used to access this data is also provided in this repo**. Note that to use this script yourself you need an API key from the US Census Bureau; getting a key is easy, and the process is detailed in the [official API User Guide](https://www.census.gov/data/developers/guidance/api-user-guide.html).

For Salt Lake County, there are 251 census tracts with 522 census variables each.

## Streets_with_Address_Ranges

**Shapefiles for streets with addresses for SLC were pulled from the [SLC GIS Hub Site](https://gis-slcgov.opendata.arcgis.com)**, under the "Base Map" tag.

## LA_Census_Tracts_2020

All census tracts for Los Angeles county, CA, are provided. **Census tract shapefiles were pulled from the [city of LA geohub website](https://geohub.lacity.org/datasets/lacounty::census-tracts-2020/about)**. See the above section on the Utah census tracts for more information on census tracts.

LA county has 2,498 census tracts.

### census_data_2020_LA.csv

Almost all available estimated census variables, for each tract in LA County, were accessed. For information about these variables, see the [census website](https://api.census.gov/data/2020/acs/acs5/profile/variables.html). **A short script ("read_census_data_share.py") used to access this data is also provided in this repo**.

For LA county there are 2,498 census tracts with 522 census variables each.

## LA_Street_lights.zip

Data of light fixtures in the city of LA are provided. **This data was accessed from the [city of LA geohub website](https://geohub.lacity.org/datasets/5e7c617cd8c141308c79024baa2ffcae)**. The dataset consists of 218,624 data objects, including information about lamp type and wattage, and location in the city of LA. Moreover, the data has been processed so that
1. Lamp type and wattage have been moved to separate rows for ease of access, and
2. Each data object keeps track of the census tract the fixture is located in.

The code to match fixtures to tracts was non-optimal, took approximately 5 hours to run, and can be found in "LA_streetlight_data_clean_up.py"; this script also includes the code that split the lamp data into separate columns (for ease of access).
