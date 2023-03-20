# Import system modules
import sys, string, os, arcgisscripting

# Create the Geoprocessor object
##gp = arcgisscripting.create()
import arcpy
from arcpy import env
from arcpy.sa import *

import itertools

arcpy.env.overwriteOutput = True

arcpy.AddMessage("Checking to see if it is an empty raster")
# You will need to set your license level to the appropriate level below
# by removing the ## for the appropriate line

# Gets the value from the Model Process

rst = arcpy.GetParameterAsText(0)
Input_File = arcpy.GetParameterAsText(1)
In_features = arcpy.GetParameterAsText(2)
cellsize = arcpy.GetParameterAsText(3)
value_field = arcpy.GetParameterAsText(4)
outras = arcpy.GetParameterAsText(5)
snapgrid = arcpy.GetParameterAsText(6)
extent = arcpy.GetParameterAsText(7)
out_coor_system = arcpy.GetParameterAsText(8)
outras2 = arcpy.GetParameterAsText(9)
cell_assignment = "MOST_FREQUENT"


##rst = r"C:\Honduras\Birdwarching_corinna\IUCN_boolean1_nd.gdb\S_62154828"
##Input_File = r"C:\Honduras\Birdwarching_corinna\empty_raster_recreated_birdwatching.txt"
##In_features = r"C:\Honduras\Birdwarching_corinna\SBA hnd_BirdList_POselection\SBA.gdb\S_62154828"
##cellsize = "1000"
##value_field = "unique"
##outras = r"C:\Honduras\Birdwarching_corinna\IUCN_boolean1_nd.gdb\S_62154828"
##snapgrid = r"C:\Honduras\Birdwarching_corinna\snapgrid_1km"
##XMIN = arcpy.GetRasterProperties_management(snapgrid,"LEFT")
##YMIN = arcpy.GetRasterProperties_management(snapgrid,"BOTTOM")
##XMAX = arcpy.GetRasterProperties_management(snapgrid,"RIGHT")
##YMAX = arcpy.GetRasterProperties_management(snapgrid,"TOP")
##extent = arcpy.Extent(XMIN,YMIN,XMAX,YMAX)
##out_coor_system = "PROJCS['Honduras_la_equal_area',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Azimuthal_Equal_Area'],PARAMETER['False_Easting',0.0],PARAMETER['False_Northing',0.0],PARAMETER['central_meridian',-86.5],PARAMETER['latitude_of_origin',14.8],UNIT['Meter',1.0]]"
##outras2 = r"C:\Honduras\Birdwarching_corinna\IUCN_boolean1_nd.gdb\S_62154828"
##cell_assignment = "MOST_FREQUENT"

property = arcpy.GetRasterProperties_management(rst, property_type="ALLNODATA", band_index="")
if str(property) == "1":
    outpnt = "in_memory/pnt"
    arcpy.env.overwriteOutput = True
    arcpy.Delete_management(rst)
    arcpy.FeatureToPoint_management(In_features, outpnt, "INSIDE")
    arcpy.env.snapRaster = snapgrid
    arcpy.env.outputCoordinateSystem = out_coor_system
    arcpy.env.extent = extent
    arcpy.PointToRaster_conversion(outpnt, value_field, outras, cell_assignment, value_field, cellsize)
    all_nd = arcpy.GetRasterProperties_management(outras, property_type="ALLNODATA", band_index="")
    if str(all_nd) == "1":
        arcpy.Delete_management(outras)
        arcpy.AddMessage("Raster is all NODATA, range does not fall within AOI")
        print "Raster is all NODATA, range does not fall within AOI"
        openfile = open (Input_File, "a")
        openfile.write (str(rst) + ": Raster is all NODATA, and range does not fall within AOI" + '\n')
        openfile.close()
    else:
        arcpy.AddMessage("Raster is all NODATA, Raster recreated from centroid")
        print "Raster is all NODATA, Raster recreated from centroid"
        openfile = open (Input_File, "a")
        openfile.write (str(rst) + ": Raster is all NODATA, Raster recreated from centroid" + '\n')
        openfile.close()
else:
    pass
    arcpy.AddMessage("Raster is not ALL NODATA so no additional processing needed")
    outras2 = "ID"+ rst

