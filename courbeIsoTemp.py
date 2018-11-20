# state file generated using paraview version 5.4.1

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

#### import the simple module from the paraview
import sys
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1101, 802]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [1.999999999987267, 46.45, 0.0]
renderView1.StereoType = 0
renderView1.CameraPosition = [1.999999999987267, 46.45, 10000.0]
renderView1.CameraFocalPoint = [1.999999999987267, 46.45, 0.0]
renderView1.CameraParallelScale = 16.616332326949994
renderView1.Background = [0.32, 0.34, 0.43]

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'NetCDF Reader'
donnesmeteonc = NetCDFReader(FileName=[sys.argv[1]])
donnesmeteonc.Dimensions = '(latitude, longitude)'
donnesmeteonc.SphericalCoordinates = 0
donnesmeteonc.ReplaceFillValueWithNan = 1

# create a new 'Threshold'
threshold1 = Threshold(Input=donnesmeteonc)
threshold1.Scalars = ['POINTS', 'RH_2maboveground']
threshold1.ThresholdRange = [19.5445556640625, 101.0133056640625]

# create array of surfaces 

contour = [float(sys.argv[2])+273,15]
for i in (1,int(sys.argv[3])) : 
	contour.append(float(sys.argv[2])+273.15+i*float(sys.argv[4])) 

# create a new 'Contour'
contour1 = Contour(Input=threshold1)
contour1.ContourBy = ['POINTS', 'TMP_2maboveground']
contour1.ComputeScalars = 1
contour1.Isosurfaces = contour
contour1.PointMergeMethod = 'Uniform Binning'

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get color transfer function/color map for 'TMP_2maboveground'
tMP_2mabovegroundLUT = GetColorTransferFunction('TMP_2maboveground')
tMP_2mabovegroundLUT.RGBPoints = [258.8880615234375, 0.231373, 0.298039, 0.752941, 278.3148193359375, 0.865003, 0.865003, 0.865003, 297.7415771484375, 0.705882, 0.0156863, 0.14902]
tMP_2mabovegroundLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'TMP_2maboveground'
tMP_2mabovegroundPWF = GetOpacityTransferFunction('TMP_2maboveground')
tMP_2mabovegroundPWF.Points = [258.8880615234375, 0.0, 0.5, 0.0, 297.7415771484375, 1.0, 0.5, 0.0]
tMP_2mabovegroundPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from contour1
contour1Display = Show(contour1, renderView1)
# trace defaults for the display properties.
contour1Display.Representation = 'Surface'
contour1Display.ColorArrayName = ['POINTS', 'TMP_2maboveground']
contour1Display.LookupTable = tMP_2mabovegroundLUT
contour1Display.OSPRayScaleArray = 'TMP_2maboveground'
contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display.SelectOrientationVectors = 'None'
contour1Display.ScaleFactor = 2.4092324256896975
contour1Display.SelectScaleArray = 'TMP_2maboveground'
contour1Display.GlyphType = 'Arrow'
contour1Display.GlyphTableIndexArray = 'TMP_2maboveground'
contour1Display.DataAxesGrid = 'GridAxesRepresentation'
contour1Display.PolarAxes = 'PolarAxesRepresentation'

# show color legend
contour1Display.SetScalarBarVisibility(renderView1, True)

# setup the color legend parameters for each legend in this view

# get color legend/bar for tMP_2mabovegroundLUT in view renderView1
tMP_2mabovegroundLUTColorBar = GetScalarBar(tMP_2mabovegroundLUT, renderView1)
tMP_2mabovegroundLUTColorBar.Title = 'TMP_2maboveground'
tMP_2mabovegroundLUTColorBar.ComponentTitle = ''

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(contour1)
# ----------------------------------------------------------------

Interact()
