#-------------------------------------------------------------------------------
#
# arcpy tool demo
#
#-------------------------------------------------------------------------------


# Importing arcpy
import arcpy

# We now setup our workspace, as well as out "out" workspace
arcpy.env.workspace = r"C:\Users"

toFileWorkspace=r"C:\Users"

arcpy.env.overwriteOutput = True

# We list feature classes using our dot function
ListedFC= arcpy.ListFeatureClasses()


# We now print out the values of the workspaces
print "\n The Current Workspace is: " + "\n\t" + arcpy.env.workspace

print "\n The Output will be put in" + "\n\t" + toFileWorkspace

# This function now lists the feature classes that will be in the workspace.
print "\n The feature classes in the workspace are:"

titleList=['_1','_2','_3','_4','_5','_6']
i=0
clusterTolerance = 10

clipfc = "study_quads.shp"

for FC in ListedFC:
    print "\t" + FC
    arcpy.Clip_analysis(FC,clipfc,toFileWorkspace+titleList[i],clusterTolerance)
    i=i+1



# Now we list the clip tools. We use the "*" to tell our script that we
# want all the avalable tools not just a specific name.
clipTools = arcpy.ListTools("cli*")

print "\n The Available clip tools are:"

clusterTolerance = 10


#printing tools and tool usage
for tool in clipTools:
    print "\t" + tool


for tool in clipTools:
    print "\t" + arcpy.Usage(tool)
