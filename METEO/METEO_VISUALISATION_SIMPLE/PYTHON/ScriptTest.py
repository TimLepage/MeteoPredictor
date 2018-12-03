# state file generated using paraview version 5.6.0

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# trace generated using paraview version 5.6.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`
import sys
#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
Monechelle = 0.5
renderView1.ViewSize = [(int)(2801*Monechelle),(int) (1791*Monechelle)]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [1.999999999987267, 46.45, 0.0]
renderView1.StereoType = 0
renderView1.CameraPosition = [1.999999999987267, 46.45, 10000.0]
renderView1.CameraFocalPoint = [1.999999999987267, 46.45, 0.0]
renderView1.CameraParallelScale = 16.616332326949994
renderView1.Background = [0.32, 0.34, 0.43]
renderView1.OSPRayMaterialLibrary = materialLibrary1

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView1.AxesGrid.XTitleFontFile = ''
renderView1.AxesGrid.YTitleFontFile = ''
renderView1.AxesGrid.ZTitleFontFile = ''
renderView1.AxesGrid.XLabelFontFile = ''
renderView1.AxesGrid.YLabelFontFile = ''
renderView1.AxesGrid.ZLabelFontFile = ''

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'NetCDF Reader'
aromeHD_SP1_DateRun_20181130T030000_DatePrev_20181130T220000grib2nc = NetCDFReader(FileName=[sys.argv[1]])
aromeHD_SP1_DateRun_20181130T030000_DatePrev_20181130T220000grib2nc.Dimensions = '(latitude, longitude)'
aromeHD_SP1_DateRun_20181130T030000_DatePrev_20181130T220000grib2nc.SphericalCoordinates = 0
aromeHD_SP1_DateRun_20181130T030000_DatePrev_20181130T220000grib2nc.ReplaceFillValueWithNan = 1

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from aromeHD_SP1_DateRun_20181130T030000_DatePrev_20181130T220000grib2nc
aromeHD_SP1_DateRun_20181130T030000_DatePrev_20181130T220000grib2ncDisplay = Show(aromeHD_SP1_DateRun_20181130T030000_DatePrev_20181130T220000grib2nc, renderView1)

# get color transfer function/color map for 'TMP_2maboveground'
tMP_2mabovegroundLUT = GetColorTransferFunction('TMP_2maboveground')
tMP_2mabovegroundLUT.EnableOpacityMapping = 1
tMP_2mabovegroundLUT.RGBPoints = [251.60775756835938, 0.231373, 0.298039, 0.752941, 272.9134216308594, 0.865003, 0.865003, 0.865003, 294.2190856933594, 0.705882, 0.0156863, 0.14902]
tMP_2mabovegroundLUT.NumberOfTableValues = 10
tMP_2mabovegroundLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'TMP_2maboveground'
tMP_2mabovegroundPWF = GetOpacityTransferFunction('TMP_2maboveground')
tMP_2mabovegroundPWF.Points = [251.60775756835938, 0.0, 0.5, 0.0, 271.75830050818263, 0.45588234066963196, 0.5, 0.0, 294.2190856933594, 1.0, 0.5, 0.0]
tMP_2mabovegroundPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
aromeHD_SP1_DateRun_20181130T030000_DatePrev_20181130T220000grib2ncDisplay.Representation = 'Slice'
aromeHD_SP1_DateRun_20181130T030000_DatePrev_20181130T220000grib2ncDisplay.ColorArrayName = ['POINTS', 'TMP_2maboveground']
aromeHD_SP1_DateRun_20181130T030000_DatePrev_20181130T220000grib2ncDisplay.LookupTable = tMP_2mabovegroundLUT
aromeHD_SP1_DateRun_20181130T030000_DatePrev_20181130T220000grib2ncDisplay.OSPRayScaleArray = 'RH_2maboveground'
aromeHD_SP1_DateRun_20181130T030000_DatePrev_20181130T220000grib2ncDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
aromeHD_SP1_DateRun_20181130T030000_DatePrev_20181130T220000grib2ncDisplay.SelectOrientationVectors = 'None'
aromeHD_SP1_DateRun_20181130T030000_DatePrev_20181130T220000grib2ncDisplay.ScaleFactor = 2.7999999999974534
aromeHD_SP1_DateRun_20181130T030000_DatePrev_20181130T220000grib2ncDisplay.SelectScaleArray = 'None'
aromeHD_SP1_DateRun_20181130T030000_DatePrev_20181130T220000grib2ncDisplay.GlyphType = 'Arrow'
aromeHD_SP1_DateRun_20181130T030000_DatePrev_20181130T220000grib2ncDisplay.GlyphTableIndexArray = 'None'
aromeHD_SP1_DateRun_20181130T030000_DatePrev_20181130T220000grib2ncDisplay.GaussianRadius = 0.13999999999987267
aromeHD_SP1_DateRun_20181130T030000_DatePrev_20181130T220000grib2ncDisplay.SetScaleArray = ['POINTS', 'RH_2maboveground']
aromeHD_SP1_DateRun_20181130T030000_DatePrev_20181130T220000grib2ncDisplay.ScaleTransferFunction = 'PiecewiseFunction'
aromeHD_SP1_DateRun_20181130T030000_DatePrev_20181130T220000grib2ncDisplay.OpacityArray = ['POINTS', 'RH_2maboveground']
aromeHD_SP1_DateRun_20181130T030000_DatePrev_20181130T220000grib2ncDisplay.OpacityTransferFunction = 'PiecewiseFunction'
aromeHD_SP1_DateRun_20181130T030000_DatePrev_20181130T220000grib2ncDisplay.DataAxesGrid = 'GridAxesRepresentation'
aromeHD_SP1_DateRun_20181130T030000_DatePrev_20181130T220000grib2ncDisplay.SelectionCellLabelFontFile = ''
aromeHD_SP1_DateRun_20181130T030000_DatePrev_20181130T220000grib2ncDisplay.SelectionPointLabelFontFile = ''
aromeHD_SP1_DateRun_20181130T030000_DatePrev_20181130T220000grib2ncDisplay.PolarAxes = 'PolarAxesRepresentation'
aromeHD_SP1_DateRun_20181130T030000_DatePrev_20181130T220000grib2ncDisplay.ScalarOpacityUnitDistance = 0.1941905735298652
aromeHD_SP1_DateRun_20181130T030000_DatePrev_20181130T220000grib2ncDisplay.ScalarOpacityFunction = tMP_2mabovegroundPWF

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
aromeHD_SP1_DateRun_20181130T030000_DatePrev_20181130T220000grib2ncDisplay.OSPRayScaleFunction.Points = [258.8880615234375, 0.0, 0.5, 0.0, 277.2615661621094, 0.45588234066963196, 0.5, 0.0, 297.7415771484375, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
aromeHD_SP1_DateRun_20181130T030000_DatePrev_20181130T220000grib2ncDisplay.ScaleTransferFunction.Points = [258.8880615234375, 0.0, 0.5, 0.0, 277.2615661621094, 0.45588234066963196, 0.5, 0.0, 297.7415771484375, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
aromeHD_SP1_DateRun_20181130T030000_DatePrev_20181130T220000grib2ncDisplay.OpacityTransferFunction.Points = [258.8880615234375, 0.0, 0.5, 0.0, 277.2615661621094, 0.45588234066963196, 0.5, 0.0, 297.7415771484375, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
aromeHD_SP1_DateRun_20181130T030000_DatePrev_20181130T220000grib2ncDisplay.DataAxesGrid.XTitleFontFile = ''
aromeHD_SP1_DateRun_20181130T030000_DatePrev_20181130T220000grib2ncDisplay.DataAxesGrid.YTitleFontFile = ''
aromeHD_SP1_DateRun_20181130T030000_DatePrev_20181130T220000grib2ncDisplay.DataAxesGrid.ZTitleFontFile = ''
aromeHD_SP1_DateRun_20181130T030000_DatePrev_20181130T220000grib2ncDisplay.DataAxesGrid.XLabelFontFile = ''
aromeHD_SP1_DateRun_20181130T030000_DatePrev_20181130T220000grib2ncDisplay.DataAxesGrid.YLabelFontFile = ''
aromeHD_SP1_DateRun_20181130T030000_DatePrev_20181130T220000grib2ncDisplay.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
aromeHD_SP1_DateRun_20181130T030000_DatePrev_20181130T220000grib2ncDisplay.PolarAxes.PolarAxisTitleFontFile = ''
aromeHD_SP1_DateRun_20181130T030000_DatePrev_20181130T220000grib2ncDisplay.PolarAxes.PolarAxisLabelFontFile = ''
aromeHD_SP1_DateRun_20181130T030000_DatePrev_20181130T220000grib2ncDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
aromeHD_SP1_DateRun_20181130T030000_DatePrev_20181130T220000grib2ncDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# setup the color legend parameters for each legend in this view

# get color legend/bar for tMP_2mabovegroundLUT in view renderView1
tMP_2mabovegroundLUTColorBar = GetScalarBar(tMP_2mabovegroundLUT, renderView1)
tMP_2mabovegroundLUTColorBar.Title = 'TMP_2maboveground'
tMP_2mabovegroundLUTColorBar.ComponentTitle = ''
tMP_2mabovegroundLUTColorBar.TitleFontFile = ''
tMP_2mabovegroundLUTColorBar.LabelFontFile = ''

# set color bar visibility
tMP_2mabovegroundLUTColorBar.Visibility = 1

# show color legend
aromeHD_SP1_DateRun_20181130T030000_DatePrev_20181130T220000grib2ncDisplay.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(aromeHD_SP1_DateRun_20181130T030000_DatePrev_20181130T220000grib2nc)
# ----------------------------------------------------------------

SaveScreenshot(sys.argv[1]+".png",viewOrLayout=renderView1,TransparentBackground=1)
