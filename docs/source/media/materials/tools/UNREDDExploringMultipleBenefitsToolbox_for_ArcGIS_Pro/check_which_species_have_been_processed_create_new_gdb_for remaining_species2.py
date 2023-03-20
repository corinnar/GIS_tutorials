#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      corinnar
#
# Created:     09/06/2017
# Copyright:   (c) corinnar 2017
# Licence:     <your licence>
#------------------------------------------------------------------------

import sys, os
import os
import arcpy, arcinfo
from arcpy import env
from arcpy.sa import *

import time

beginTime = time.clock()
arcpy.env.overwriteOutput = True

##splits_workspace = arcpy.GetParameterAsText(0)
##folder_name = arcpy.GetParameterAsText(1)

check_boolean_1_nd_rsr = arcpy.GetParameterAsText(0)
boolean_1_nd = arcpy.GetParameterAsText(1)
new_boolean_1_nd_rem = arcpy.GetParameterAsText(2)


##check_boolean_1_nd_rsr = r"G:\p07698_GEF_Star\IUCN_170609\rlspecies_080617_processing\splits_raster\CHONDRICHTHYES_Mar_id_cat\IUCN_boolean1_0_RSR.gdb"
##boolean_1_nd = r"G:\p07698_GEF_Star\IUCN_170609\rlspecies_080617_processing\splits\CHONDRICHTHYES_Mar_id_cat.gdb"
##new_boolean_1_nd_rem = r"G:\p07698_GEF_Star\IUCN_170609\rlspecies_080617_processing\splits\CHONDRICHTHYES_Mar_id_cat_remaining.gdb"

RSlist = []
arcpy.env.workspace = check_boolean_1_nd_rsr
rsts = arcpy.ListRasters("*", "ALL")
RSlist.append(rsts)
char_list=['u','[',']']
ch = str(char_list)

RSList2 = str(RSlist)
RSList3 = RSList2.replace("u","").replace("[","").replace("]","")

arcpy.Copy_management(boolean_1_nd, new_boolean_1_nd_rem, data_type="Workspace")
arcpy.env.workspace = boolean_1_nd
origRSTs = arcpy.ListRasters("*", "ALL")
for rs in origRSTs:
    for rst in rsts:
        if rst == rs:
            in_data = new_boolean_1_nd_rem + "\\" + rst
            arcpy.Delete_management(in_data)
            print rst, "already created, deleted ", in_data
        else:
            pass

print ("Total elapsed time (seconds): " + str((time.clock() - beginTime)/60), " minutes")
print "Script finished"

