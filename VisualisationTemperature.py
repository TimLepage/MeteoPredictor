# state file generated using paraview version 5.6.0

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# trace generated using paraview version 5.6.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1063, 808]
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
aromeHD_SP1_DateRun_20181130T060000_DatePrev_20181130T160000grib2nc = NetCDFReader(FileName=['/home/terrier/Documents/RICM5/MeteoPredictor/METEO/METEO_VISUALISATION_SIMPLE/DATA/AromeHD_SP1_DateRun_2018-11-30T06:00:00_DatePrev_2018-11-30T16:00:00.grib2.nc'])
aromeHD_SP1_DateRun_20181130T060000_DatePrev_20181130T160000grib2nc.Dimensions = '(latitude, longitude)'
aromeHD_SP1_DateRun_20181130T060000_DatePrev_20181130T160000grib2nc.SphericalCoordinates = 0
aromeHD_SP1_DateRun_20181130T060000_DatePrev_20181130T160000grib2nc.ReplaceFillValueWithNan = 1

# create a new 'Threshold'
threshold1 = Threshold(Input=aromeHD_SP1_DateRun_20181130T060000_DatePrev_20181130T160000grib2nc)
threshold1.Scalars = ['POINTS', 'RH_2maboveground']
threshold1.ThresholdRange = [26.98919677734375, 100.98919677734375]

# create a new 'Calculator'
calculator1 = Calculator(Input=threshold1)
calculator1.ResultArrayName = 'Temp\xc3\xa9rature (en \xc2\xb0C)'
calculator1.Function = ''

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from calculator1
calculator1Display = Show(calculator1, renderView1)

# get color transfer function/color map for 'TMP_2maboveground'
tMP_2mabovegroundLUT = GetColorTransferFunction('TMP_2maboveground')
tMP_2mabovegroundLUT.EnableOpacityMapping = 1
tMP_2mabovegroundLUT.RGBPoints = [255.30003356933594, 0.0, 0.0, 0.5625, 259.7971010801849, 0.0, 0.0, 1.0, 270.07613277037814, 0.0, 1.0, 1.0, 275.2156384970627, 0.5, 1.0, 0.5, 280.35514422374723, 1.0, 1.0, 0.0, 290.63417591394045, 1.0, 0.0, 0.0, 295.773681640625, 0.5, 0.0, 0.0]
tMP_2mabovegroundLUT.ColorSpace = 'RGB'
tMP_2mabovegroundLUT.NumberOfTableValues = 10
tMP_2mabovegroundLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'TMP_2maboveground'
tMP_2mabovegroundPWF = GetOpacityTransferFunction('TMP_2maboveground')
tMP_2mabovegroundPWF.Points = [255.30003356933594, 0.0, 0.5, 0.0, 274.43968537740324, 0.45588234066963196, 0.5, 0.0, 295.773681640625, 1.0, 0.5, 0.0]
tMP_2mabovegroundPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
calculator1Display.Representation = 'Surface'
calculator1Display.ColorArrayName = ['POINTS', 'TMP_2maboveground']
calculator1Display.LookupTable = tMP_2mabovegroundLUT
calculator1Display.OSPRayScaleArray = 'RH_2maboveground'
calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1Display.SelectOrientationVectors = 'None'
calculator1Display.ScaleFactor = 2.8000000000000003
calculator1Display.SelectScaleArray = 'None'
calculator1Display.GlyphType = 'Arrow'
calculator1Display.GlyphTableIndexArray = 'None'
calculator1Display.GaussianRadius = 0.14
calculator1Display.SetScaleArray = ['POINTS', 'RH_2maboveground']
calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1Display.OpacityArray = ['POINTS', 'RH_2maboveground']
calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1Display.SelectionCellLabelFontFile = ''
calculator1Display.SelectionPointLabelFontFile = ''
calculator1Display.PolarAxes = 'PolarAxesRepresentation'
calculator1Display.ScalarOpacityFunction = tMP_2mabovegroundPWF
calculator1Display.ScalarOpacityUnitDistance = 0.20666834150287358

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
calculator1Display.OSPRayScaleFunction.Points = [258.8880615234375, 0.0, 0.5, 0.0, 277.2615661621094, 0.45588234066963196, 0.5, 0.0, 297.7415771484375, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator1Display.ScaleTransferFunction.Points = [258.8880615234375, 0.0, 0.5, 0.0, 277.2615661621094, 0.45588234066963196, 0.5, 0.0, 297.7415771484375, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator1Display.OpacityTransferFunction.Points = [258.8880615234375, 0.0, 0.5, 0.0, 277.2615661621094, 0.45588234066963196, 0.5, 0.0, 297.7415771484375, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
calculator1Display.DataAxesGrid.XTitleFontFile = ''
calculator1Display.DataAxesGrid.YTitleFontFile = ''
calculator1Display.DataAxesGrid.ZTitleFontFile = ''
calculator1Display.DataAxesGrid.XLabelFontFile = ''
calculator1Display.DataAxesGrid.YLabelFontFile = ''
calculator1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
calculator1Display.PolarAxes.PolarAxisTitleFontFile = ''
calculator1Display.PolarAxes.PolarAxisLabelFontFile = ''
calculator1Display.PolarAxes.LastRadialAxisTextFontFile = ''
calculator1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

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
calculator1Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(calculator1)
# ----------------------------------------------------------------