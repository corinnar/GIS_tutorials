The UN-REDD Programme is the United Nations Collaborative initiative on
Reducing Emissions from Deforestation and forest Degradation (REDD) in
developing countries. The Programme was launched in September 2008 to
assist developing countries prepare and implement national REDD+
strategies, and builds on the convening power and expertise of the Food
and Agriculture Organization of the United Nations (FAO), the United
Nations Development Programme (UNDP) and the United Nations Environment
Programme (UNEP).

The United Nations Environment Programme World Conservation Monitoring
Centre (UNEP-WCMC) is the specialist biodiversity assessment centre of
the United Nations Environment Programme (UNEP), the world’s foremost
intergovernmental environmental organisation.  The Centre has been in
operation for over 30 years, combining scientific research with
practical policy advice.

**Prepared by Xavier de Lamo, Yara Shennan-Farpón and Corinna
Ravilious.**

**Copyright:** 2019 United Nations Environment Programme

**Copyright release:** This publication may be reproduced for
educational or non-profit purposes without special permission, provided
acknowledgement to the source is made. Re-use of any figures is subject
to permission from the original rights holders. No use of this
publication may be made for resale or any other commercial purpose
without permission in writing from UNEP. Applications for permission,
with a statement of purpose and extent of reproduction, should be sent
to the Director, UNEP-WCMC, 219 Huntingdon Road, Cambridge, CB3 0DL, UK.

**Disclaimer:** The contents of this report do not necessarily reflect
the views or policies of UNEP, contributory organisations or editors.
The designations employed and the presentations of material in this
report do not imply the expression of any opinion whatsoever on the part
of UNEP or contributory organisations, editors or publishers concerning
the legal status of any country, territory, city area or its
authorities, or concerning the delimitation of its frontiers or
boundaries or the designation of its name, frontiers or boundaries. The
mention of a commercial entity or product in this publication does not
imply endorsement by UNEP.

We welcome comments on any errors or issues. Should readers wish to
comment on this document, they are encouraged to get in touch via:
ccb@unep-wcmc.org.

**Citation:** de Lamo, X. Shennan-Farpón, Y. and Ravilious, C. (2019)
Step-by-step tutorial v1.0: Calculating the relative importance of
forest for wind erosion control - QGIS v2.18. Prepared on behalf of the
UN-REDD Programme. UN Environment World Conservation Monitoring Centre,
Cambridge, UK.

**Acknowledgements:** These training materials have been produced from
materials generated for working sessions held in various countries to
aid the production of multiple benefits maps to inform REDD+ planning
and safeguards policies using open source GIS software.

|image0|

|image1|

Introduction
============

REDD+ has the potential to deliver multiple benefits beyond carbon. For
example, it can promote biodiversity conservation and secure ecosystem
services from forests such as water regulation and non-timber forest
products. Some of the potential benefits from REDD+, such as
biodiversity conservation, can be enhanced through identifying areas
where REDD+ actions might have the greatest impact using spatial
analysis.

Open Source GIS software can be used to undertake spatial analysis of
datasets of relevance to multiple benefits and environmental safeguards
for REDD+. Open-source software is released under a license that allow
software to be freely used, modified, and shared
(http://opensource.org/licenses). Therefore, using open source software
has great potential in building sustainable capacity and critical mass
of experts with limited financial resources.

The capacity of forest to control soil erosion is also regarded as a key
potential REDD+ benefit. Wind erosion, in particular, constitutes a key
component in soil degradation processes in arid areas; as it can cause
degradation of sedimentation crusts on the surface of stripped soils, as
well as reducing the capacity of soils to store nutrients and water (FAO
1996). Even though the importance of the contributing factors are
locally dependent, it is widely recognized that the amount of soil loss
by wind erosion at a regional scale is mainly dependent on four key
factors: climate, soil, topography and vegetation cover (Shao & Leslie
1997).

This tutorial provides a methodology to conduct a preliminary spatial
assessment of the relative importance of forest in protecting against
wind erosion by mapping these key factors, using Paraguay as a study
area. The analysis is undertaken by using an overlay approach, where
data on wind speed, precipitation, evapotranspiration, soil
characteristics and topographical complexity are generated and combined
with forest data. The method described here is partly based on the
USDA’s Universal Wind Erosion Equation (Wooddruf & Siddoway, 1965), as
well as on Mezosi *et al.* (2015), Tsogtbaarar & Khudulmur (2014), and
FAO (1979).

This method is not designed to predict exact locations of wind erosion
occurrence or making quantitative estimates of potential soil erosion –
it serves to assess the role of forests to wind erosion control based on
the general sensitivity of the land to wind erosion, taking into account
the dominant/general climate, soil and topographical conditions of the
area. The resulting map may be suitable for regional land use management
and identify wind erosion-prone areas, where more detailed quantitative
risk mapping may be needed.

The analysis runs entirely from QGIS version 2.18, R Software and R
Studio, which needs to be installed in order to execute this analysis.


Methodology
===========

The first step will be to prepare, download and process all the
necessary layers in order to have the required variables to estimate the
relative importance of forest for wind erosion control. Using the
formula from Woodruff and Siddoway (1965) as a starting point, we have
designed and adapted a formula which uses an overlay approach to
calculate the importance of forest for wind erosion control at a
regional scale as a function of 4 thematic layers’ parameters:

**Climate:** Wind speed and humidity are the main climatic controlling
factors. It is generally assumed that wind speed at values above 6 – 9
m/s wind erosion occurs (Mezosi *et al.* 2015)\ **.** Similarly, the
sensitivity to wind erosion increase with aridity, as humid soil
particles are more resistant to be displaced by wind (Shao & Leslie
1997).

**Soil characteristics:** Texture and gran size distribution are assumed
to determine soil erosion sensitivity. Coarse-textured soils, such as
sandy soils, are known to be more prone to wind erosion than
fine-textured ones, such as clay soils (Fryrear *et al.* 1998).

**Topography:** The more “rough” the surface is, the lower is the wind
speed, and hence the wind erodibility will decrease (Shao 2008).

**Vegetation cover:** Vegetation acts as a protection layer that
prevents the wind to displace soil particles. The density of the
vegetation determines the level of protection.

The method described in this document goes through the steps required to
develop the spatial layers for the first three factors listed above. A
final map showing the relative importance of forest for wind erosion
control, is produced by combining all the layers developed. This method
assumes that the user has a forest cover layer available for analysis,
which is utilized in this tutorial as a substitute of the vegetation
cover.

Below an image showing the workflow including the steps required to
carry out this analysis.

|image2|

1. .. rubric:: Prepare the climate, soil characteristics and topography
      layers.
      :name: prepare-the-climate-soil-characteristics-and-topography-layers.

2. .. rubric:: Create the Climate factor (C’) layer
      :name: create-the-climate-factor-c-layer

Climate erosivity is assessed in this method using the formula suggested
by FAO (1979) for the Universal Wind Erosion Equation (Wooddruf &
Sidoway, 1965):

.. math:: C = \frac{1}{100}\  \times \ \sum_{i = 1}^{12}{u^{3}\left( \frac{PETi - Pi}{\text{PETi}} \right)}d

Where:

*u* = monthly average wind speed (m/s)

*PETi* = monthly potential evaporation (mm)

*Pi* = monthly average precipitation (mm)

*d* = the number of days in a month.

Spatial layers will be developed for each parameter included in the
equation above, and will then be used as input layers in Raster
Calculator to produce a climate erosivity map.

3.1.1. Compute the monthly average wind speed layer (u)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Twelve layers, representing monthly average wind speed values for the
area of interest, will be developed for the *“u”* component of the
formula. If no spatial modelled surface for wind velocity are available
for your study area, you can develop one using daily wind speed station
data from `NOAA's National Climatic Data Center
website <https://www.climate.gov/data/maps-and-data>`__. This data will
be used in this tutorial to create average wind speed maps for each
month of the year in the study area, by using geostatistical methods in
QGIS and statistical analyses in RStudio.

Steps to download the daily wind speed data 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Go to: https://www.climate.gov/maps-data, and then click on to
   ***Dataset Gallery*** on the top of the page\ ***.***

2. On the left side of the page, under ***Refine by Coverage***, click
   on ***Global*** and then search for ***Daily Weather Statistics
   (Graph or Data table).***

|image3|

1. *Go to **Data Access ***\ and click on the link under ***Daily
   Observational Data*** in the ***Subsetting Service Row. ***

|image4|

1. A pop up window will open, click on **All Maps** and then on **Daily
   Observational Data.** A map viewer will automatically open.

2. Once the map viewer is open, **Search** for a location, Paraguay in
   this case, and tick the box next to **Global Summary of the Day** on
   the left side of the map.

|image5|

1. Click on the **tools** **icon** next to **Global Summary of the Day**
   and then to **Polygon** to select the area of interest. This will
   allow you to draw a polygon and select the weather stations for your
   area of interest. For a more accurate execution of the interpolation
   that will be carried out later on, it is advised to also select
   weather station in the surrounding area of our area of interest. In
   this example, we will draw a polygon around Paraguay.

   |image6|

2. On the left side of the map the list of the stations included in the
   polygon will appear. Select just the stations with at least *five
   years of data* and then click on **Access Data** at the bottom.

|image7|

In the following window, click on ***“Agree”***.

1. In the next window, you will be asked to select the date range of the
   weather records of the station selected. Select 01/01/1949 and leave
   the date in the “To” row as it is. Select ***“comma delimited”***
   under ***“Select output format”.*** Mark the box under “I am not a
   robot” and then click continue.

|image8|

1. The dataset of the records selected will then available for download
   as a csv. Click on the link to the text file and select ***“Save link
   as”*** and save it in your working file (“data\_downloaded.txt”).

|image9|

Steps to compute historical monthly wind speed averages from the daily wind speed data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now that we have downloaded all the required data, we need to compute
historical monthly wind speed averages from it. We will use R Software
and R Studio (an R user interface) to do this.

1. Open **R Studio** and set your working directory by going to
   **Session > Set Working Directory > Choose Directory.** Select the
   folder in which you have saved the weather data.

|image10|

1. Now we are going to import the weather dataset file,
   “data\_downloaded.txt”. Under the ‘Environment’ tab in R studio
   window, click on ***“Import Dataset”*** and select **“From Text
   (base)”**

|image11|

1. Select the dataset and ensure that the “\ ***Separator***\ ” is set
   as *“Comma”,* “\ ***Decimal***\ ” is set as *“Period”* and
   ***“na.strings”*** to *“999.9”*, which is the value to which our
   dataset assigns the missing values. Then click ***“Import”*.** You
   can change the name of the dataset to something easier to work with
   (for example, WS).

|image12|

    You are now able to see the dataset in the viewer window. We are now
    going to select from the dataset our parameters of interest: the
    Station Code Number (“STN…”), the date of the observations
    (“YEARMODA”) and the mean wind speed value (“WDSP”).

1. Change the name of the station name column (STN…) to something
   simpler to work with (fnamWSor example: STN). To do that, write the
   following formula in the console window:

   |image13|

|image14|

1. Now, we are going to create a new data frame (WS1) containing only
   the three variables of interest (STN, YEARMODA and WDSP). To do that,
   write the following command in the console.

|image15|

You should now see the following datasets (WS and WS1) in the Global
Environment tab:

|image16|

1. For computational purposes, the variable for the date of the
   observation (*YEARMODA*) must be split into three: year, month and
   day of observation. To do this, write the following formula into the
   Console window:

|image17|

|image18|

    Right click on the **WS1** data frame in **RStudio’s data window**
    to see the changes made in the data frame.

|image19|

The WS1 dataset now shows the new variables created, YEAR, MONTH and
DAY:

|image20|

1. The WS dataset contains some no data values (recorded as 999.9). We
   need to remove these values from the dataset before any other
   calculation is made. A new data frame will be created (WS2),
   containing only valid observations. To do that, write the following
   command in the console:

|image21|

    Note that you can now see WS2 in the Data window. The number of
    observations (obs.) included in WS2 has been reduced compared to
    WS1.

|image22|

1. In the ‘metadata’ txt file downloaded in Step 8 of the section “Steps
   to download the daily wind speed data”, you will see that wind speed
   values are in tenths of a knot (0.1 knots). The formula requires
   these values to be converted to meters per second (m/s). To convert
   these values to m/s and store them in a new column called ‘WDSP\_MS’,
   write the following command in the console:

|image23|

    In the WS2 data tab you can now see a new column ‘WDSP\_MS’ with new
    values for wind speed in m/s:

|image24|

    We can now compute mean monthly wind speed values for each of the
    stations of the dataset.

Steps to compute mean monthly wind speed values
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. We will carry out this operation using a **dplyr** package, which is
   not included in the core R software. To install and load the
   **dplyr** package, write the following formula in the Console tab:

   |image25|

    The download process will start automatically. Once the process is
    finished, you should see the text below in the Console window:

package ‘assertthat’ successfully unpacked and MD5 sums checked

package ‘R6’ successfully unpacked and MD5 sums checked

package ‘Rcpp’ successfully unpacked and MD5 sums checked

package ‘magrittr’ successfully unpacked and MD5 sums checked

package ‘lazyeval’ successfully unpacked and MD5 sums checked

package ‘DBI’ successfully unpacked and MD5 sums checked

package ‘BH’ successfully unpacked and MD5 sums checked

package ‘dplyr’ successfully unpacked and MD5 sums checked

The downloaded binary packages are in

C:\\Users\\yaras\\AppData\\Local\\Temp\\RtmpQV1ak4\\downloaded\_packages

This will also show you the directory of the downloaded package on your
computer.

|image26|

1. Once the package is loaded, write the following command in the
   console:

|image27|

    This will calculate monthly average wind speed for each of the
    weather stations in the data frame and store the values in a new
    data frame called WS3. The new data frame will then look like this.
    In order to see the WS3 data frame, click on WS3 in the Global
    Environments window:

|image28|

Add the geographical coordinates of the weather stations into the dataset
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We now have the average wind speed values we were looking for, but
before exporting the dataset we need to add further information in order
to be able to perform the interpolation in QGIS. First, we need to add
the geographical coordinates of each station. To do that, follow these
steps:

1. Download the coordinate system data from this link:
   http://www1.ncdc.noaa.gov/pub/data/noaa/

    This website will provide access to many datasets and folders
    grouped into different years. Select the file called
    ‘isd\_history.csv’ (or click here to download the data directly:
    http://www1.ncdc.noaa.gov/pub/data/noaa/isd-history.csv). The data
    is downloaded as a .csv file, comma delimited, which can be opened
    and viewed in R or Excel.

1. Open the csv data set, and save it as a text file, e.g.
   ‘isd.history-merge.txt’.

2. In R, use the Import button to import the txt file. Use the
   parameters as shown in the image below:

|image29|

You should now see the data in the data viewing window (top left), like
this:

|image30|

1. The station coordinate file (‘isd.history-merge.txt’) containing
   information of each station (its name, the country where is located
   and the geographic coordinates LAT and LONG) has now to be merged
   with the data frame containing information on mean\_wdsp. R will use
   the station code, STN, as the union element from the ‘WS3’ data frame
   and the station code USAF from the ‘isd.history-merge.txt’ data
   frame. In order to perform this step write in the console window the
   command shown below:

> WS4<-merge(WS3,isd.history\_merge,by.x=”STN”,by.y=“USAF”,all=FALSE)

    This will create a new data frame, WS4, using the Station Code as a
    common key variable. The new dataset will look something similar to
    this:

|image31|

1. To facilitate the steps of the analysis performed with QGIS, we now
   need to split the dataset into one file for each month. To do that,
   write the following commands in the console:

|image32|

|image33|

Finally, export the datasets created through the following commands:

|image34|

    This will create a separate csv file for each of the months, which
    will also be saved in the workspace directory folder.

|image35|

Develop continuous mean monthly wind speed surfaces for the study area 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To develop a final climate layer covering the whole area of interest, is
now necessary to estimate the average wind speed for the zones where
weather stations are missing. To perform this analyses, we need to
interpolate wind speed values for all the study area using
geostatistical techniques. The preliminary step requires to import all
the datasets exported in the previous step and convert them into point
shapefiles using QGIS.

**Follow the steps below, repeating them for every file of monthly wind
speeds. At the end of the process you will have 12 separate files:**

1. Select **‘Layer’ > ‘Add Layer’ > ‘Add delimited text layer’**, as
   shown below:

|image36|

    Select the parameters, using the CSV format (change the input layer
    name for each monthly dataset, e.g. “Mean\_WS\_Jan”,
    “Mean\_WS\_Feb”, etc.) as shown in the image below, and then click
    OK:

|image37|

1. A Coordinate Reference System Selector will appear asking you to
   select a coordinate reference system. Since the wind speed
   coordinates are in latitudes and longitudes, you should select WGS
   84. Click OK.

You should now have the point data loaded in QGIS, as in the image
below:

|image38|

1. The layers need now to be projected into a projected coordinate
   system. Right click on each layer and select “Save As…” a window will
   automatically appear. Select the folder to which you want to save the
   file, give it a name and select an appropriate projected coordinate
   system for your study area, in this case we will select WGS 84 UTM
   Zone 21S. Repeat for all twelve layers.

|image39|

|image40|

1. We are now going to apply the Universal Kriging technique to
   interpolate the monthly mean wind speed values. This particular
   technique has been chosen since is considered one of the most
   accurate techniques to spatially interpolate this kind of variable
   (Luo *et al.* 2007). To perform this analysis go to the processing
   toolbox and search for SAGA’s Universal Kriging tool. Right click and
   select “Execute as batch process”.

|image41|

1. This action will open a new window, insert each one of the projected
   point shapefiles produced in the prior step. In **Attribute**, select
   the name of the column that contain the monthly mean wind speed
   values. In the **Resampling** column, choose “Inverse Distance
   Interpolation”. In **Search Range**, choose “global”. In **Number of
   Points,** select “All points within search distance”. In **Cell
   Size**, select 1000. Finally, in the **Prediction and Quality
   Measures** columns specify the folder in which you want to save the
   output files and give each file a name. Leave the other parameters as
   they are. (**TIP**: you can automatically fill the columns with the
   value of the first row by double clicking the head of the column).
   Then click **Run**.

   |image42|

2. The layer you are interested in is the Prediction one, the second
   layer generated (Quality measures) just provides you with statistics
   on how well the prediction has been made. Interpolation does not give
   accurate results outside the collection area, so let’s clip the
   resulting surfaces with the study area boundary. To do that, we need
   to load a shapefile of the area of interest. Click on **‘Layer’ >
   ‘Add Layer’ > ‘Add Vector Layer’.**

   |image43|

3. Go to \ **Processing -> Toolbox** and search for **Clip raster by
   mask layer.** Rick click and select **“Execute as a batch process”.**
   In the **Input layer** column, select each of the recently created
   wind speed raster layers, in consecutive order. In the **Mask layer**
   column, select the shapefile of your study area. Then, select the
   folder and name of the 12 clipped layers in the **Clipped (mask)**
   column. Select “\ **Yes”** under **“Crop the extent of the target
   dataset to the extent of the cutline”** and leave the other
   parameters as they are. Once done, click **Run**. The interpolated
   data will now be cut to the region of interest:

   |image44|

3.1.2 Extract Potential Evapotranspiration (*PETi*) data 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    To be able to make the calculation as per the initial formula for
    climate erosivity (see Page 2), we need monthly potential
    evaporation data *PETi* (mm).

1. PET data can be downloaded from the `CGIAR-CSI Global PET
   Database. <https://figshare.com/articles/Global_Aridity_Index_and_Potential_Evapotranspiration_ET0_Climate_Database_v2/7504448/3>`__

|image45|

1. Select the “global\_et0\_monthly.tif.zip” to download and save in
   your working folder. Unzip the files.

2. Open the 12 raster files in QGIS. Select the 12 tif files (the number
   corresponds to the month).

|image46|

1. Once all PET files are open, we need to clip them to the study area
   border. Open a shapefile of the study area and ensure that it is in
   the same projection as the PET layers (EPGS 4326). To do that go to
   **Processing -> Toolbox** and search for **Clip raster by mask
   layer**. Right click on it and select **Execute as batch process.**

|image47|

1. In the **Input layer** column, select each of the PET raster layers,
   in consecutive order. In the **mask layer** column, select the
   shapefile of your study area. Then, select the folder and name of the
   12 clipped layers in the **Clipped (mask)** column. Leave the rest as
   it is. Once done, click **Run**.

|image48|

1. QGIS will automatically clip the twelve PET layers to the shape of
   your study area and save the resulting files in the folder that you
   specified. The result will be something similar to this:

|image49|

3.1.3 Extract monthly average precipitation (*Pi*) for your study area
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    The climate erosivity formula also requires monthly average
    precipitation (*Pi*) values. If a gridded precipitation layer is not
    available for your study area, it is possible to extract this data
    from a global dataset, called WorldClim, following the steps
    described below:

1. Go to WorldClim (`www.worldclim.org <http://www.worldclim.org>`__),
   click **Version 2.0. **
|image50|

1. This will take you to the download page for climate data at different
   resolutions. Click on the relative link to download raster data for
   precipitation at the required resolution, in this example, we will
   select the 30 sec resolution.

|image51|

    The download of a zip file including precipitation layers for each
    month of the year, numbered 1 to 12, will start.

1. Unzip these files, upload them in QGIS and clip them to the shape of
   your study area following the same steps described in the previous
   section.
3.1.4 Use Raster Calculator to compute the climatic ‘C’ factor layer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Now that we have all the required variables, we can calculate the C
    factor as per the initial formula using Raster Calculator in QGIS:

.. math:: C = \frac{1}{100}\  \times \ \sum_{i = 1}^{12}{u^{3}\left( \frac{PETi - Pi}{\text{PETi}} \right)}d

    The 3 sets of monthly layers (windspeed, precipitation and
    EvapoTranspiration) prepared in the previous steps will be used as
    input layers in Raster Calculator.

    To perform the analysis follow the instructions below:
    
    1. Open the 3 set of layers in QGIS. Ensure that they all have the same
   extent, resolution and are in the same projection.

2. Open the Raster Calculator tool in QGIS, clicking on ‘Raster’ ‘Raster
   Calculator’.

3. Write the formula in the raster calculator expression, following the
   example below. Call the output layer “C\_factor” and saved it in your
   working folder.

((("ws\_1@1"^3) \* (( "pet\_1@1" - "prec\_1@1") / "pet\_1@1")\*31) +
(("ws\_2@1"^3) \* (( "pet\_2@1" - "prec\_2@1") / "pet\_2@1")\*28) +
(("ws\_3@1"^3) \* (( "pet\_3@1" - "prec\_3@1") / "pet\_3@1")\*31) +
(("ws\_4@1"^3) \* (( "pet\_4@1" - "prec\_4@1") / "pet\_4@1")\*30) +
(("ws\_5@1"^3) \* (( "pet\_5@1" - "prec\_5@1") / "pet\_5@1")\*31) +
(("ws\_6@1"^3) \* (( "pet\_6@1" - "prec\_6@1") / "pet\_6@1")\*30) +
(("ws\_7@1"^3) \* (( "pet\_7@1" - "prec\_7@1") / "pet\_7@1")\*31) +
(("ws\_8@1"^3) \* (( "pet\_8@1" - "prec\_8@1") / "pet\_8@1")\*31) +
(("ws\_9@1"^3) \* (( "pet\_9@1" - "prec\_9@1") / "pet\_9@1")\*30) +
(("ws\_10@1"^3) \* (( "pet\_10@1" - "prec\_10@1") / "pet\_10@1")\*31) +
(("ws\_11@1"^3) \* (( "pet\_11@1" - "prec\_11@1") / "pet\_11@1")\*30) +
(("ws\_12@1"^3) \* (( "pet\_12@1" - "prec\_12@1") / "pet\_12@1")\*31)) /
100


1. |image52|\ The resulting map will look similar to the one shown on
   the side. The higher the value is (in dark orange), the higher is
   expected to be the climatic tendency to produce conditions conducive
   to wind erosion.

3.1.5 Re-classify the ‘C’ factor layer into classes for analysis 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Finally, we need to reclassify the C factor layer into classes, so
    as to be able to perform the final function which will produce a
    layer with different classes of wind erosion sensitivity.

First, we will compute the interval classes that will be utilised to
reclassify the C factor layer:

1. In the processing toolbox, open the **r.quantile** tool. This tool
   computes quantiles (intervals that contains equal number of features)
   in a dataset. In **Input raster layer** select the recently created
   C\_factor layer. In **Number of quantiles**, enter “7”. Thick on
   Generate recode values based on quantile-defined intervals. Finally
   in **Quantiles (raw output)** specify the path where to save the
   output file.

   |image53|
