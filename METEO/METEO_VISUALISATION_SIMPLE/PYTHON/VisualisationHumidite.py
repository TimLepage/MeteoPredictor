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
MonEchelle = 0.5
renderView1.ViewSize = [(int) (2801*MonEchelle),(int) (1791*MonEchelle)]
renderView1.InteractionMode = '2D'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [2., 46.45, 0.0]
renderView1.CameraPosition = [2., 46.45, 60.]
renderView1.CameraFocalPoint = [2., 46.45, 0.0]
renderView1.CameraParallelScale = 9.
renderView1.CameraParallelProjection = 1
renderView1.Background = [1.0, 1.0, 1.0]
renderView1.UseGradientBackground = 1

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'NetCDF Reader'
aromeHD_SP1_DateRun_20181130T060000_DatePrev_20181130T160000grib2nc = NetCDFReader(FileName=[sys.argv[1]])
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
calculator1.Function = 'TMP_2maboveground-273.15'

# create a new 'Extract Subset'
extractSubset1 = ExtractSubset(Input=aromeHD_SP1_DateRun_20181130T060000_DatePrev_20181130T160000grib2nc)
extractSubset1.VOI = [0, 2800, 0, 1790, 0, 0]
extractSubset1.SampleRateI = 100
extractSubset1.SampleRateJ = 100
extractSubset1.SampleRateK = 100

# create a new 'Threshold'
threshold2 = Threshold(Input=extractSubset1)
threshold2.Scalars = ['POINTS', 'RH_2maboveground']
threshold2.ThresholdRange = [43.77044677734375, 100.11419677734375]

# create a new 'Calculator'
calculator2 = Calculator(Input=threshold2)
calculator2.ResultArrayName = 'Vitesse du vent'
calculator2.Function = 'UGRD_10maboveground*iHat+VGRD_10maboveground*jHat'

# create a new 'Glyph'
glyph1 = Glyph(Input=calculator2,
    GlyphType='2D Glyph')
glyph1.OrientationArray = ['POINTS', 'Vitesse du vent']
glyph1.ScaleArray = ['POINTS', 'No scale array']
glyph1.ScaleFactor = 0.7020000000000001
glyph1.GlyphTransform = 'Transform2'

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(Input=calculator2,
    SeedType='High Resolution Line Source')
streamTracer1.Vectors = ['POINTS', 'Vitesse du vent']
streamTracer1.InterpolatorType = 'Interpolator with Cell Locator'
streamTracer1.MaximumSteps = 100
streamTracer1.MaximumStreamlineLength = 26.0

# init the 'High Resolution Line Source' selected for 'SeedType'
streamTracer1.SeedType.Point1 = [-11.0, 38.5, 0.0]
streamTracer1.SeedType.Point2 = [15.0, 54.5, 0.0]
streamTracer1.SeedType.Resolution = 50

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from aromeHD_SP1_DateRun_20181130T060000_DatePrev_20181130T160000grib2nc
aromeHD_SP1_DateRun_20181130T060000_DatePrev_20181130T160000grib2ncDisplay = Show(aromeHD_SP1_DateRun_20181130T060000_DatePrev_20181130T160000grib2nc, renderView1)

# get color transfer function/color map for 'RH_2maboveground'
rH_2mabovegroundLUT = GetColorTransferFunction('RH_2maboveground')
rH_2mabovegroundLUT.EnableOpacityMapping = 1
rH_2mabovegroundLUT.RGBPoints = [26.98919677734375, 0.23137254902, 0.298039215686, 0.752941176471, 63.98919677734375, 0.865, 0.865, 0.865, 100.98919677734375, 0.705882352941, 0.0156862745098, 0.149019607843]
rH_2mabovegroundLUT.NumberOfTableValues = 10
rH_2mabovegroundLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'RH_2maboveground'
rH_2mabovegroundPWF = GetOpacityTransferFunction('RH_2maboveground')
rH_2mabovegroundPWF.Points = [26.98919677734375, 0.0, 0.5, 0.0, 61.98318178463275, 0.45588234066963196, 0.5, 0.0, 100.98919677734375, 1.0, 0.5, 0.0]
rH_2mabovegroundPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
aromeHD_SP1_DateRun_20181130T060000_DatePrev_20181130T160000grib2ncDisplay.Representation = 'Slice'
aromeHD_SP1_DateRun_20181130T060000_DatePrev_20181130T160000grib2ncDisplay.ColorArrayName = ['POINTS', 'RH_2maboveground']
aromeHD_SP1_DateRun_20181130T060000_DatePrev_20181130T160000grib2ncDisplay.LookupTable = rH_2mabovegroundLUT
aromeHD_SP1_DateRun_20181130T060000_DatePrev_20181130T160000grib2ncDisplay.OSPRayScaleArray = 'RH_2maboveground'
aromeHD_SP1_DateRun_20181130T060000_DatePrev_20181130T160000grib2ncDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
aromeHD_SP1_DateRun_20181130T060000_DatePrev_20181130T160000grib2ncDisplay.SelectOrientationVectors = 'None'
aromeHD_SP1_DateRun_20181130T060000_DatePrev_20181130T160000grib2ncDisplay.ScaleFactor = 2.7999999999974534
aromeHD_SP1_DateRun_20181130T060000_DatePrev_20181130T160000grib2ncDisplay.SelectScaleArray = 'None'
aromeHD_SP1_DateRun_20181130T060000_DatePrev_20181130T160000grib2ncDisplay.GlyphType = 'Arrow'
aromeHD_SP1_DateRun_20181130T060000_DatePrev_20181130T160000grib2ncDisplay.GlyphTableIndexArray = 'None'
aromeHD_SP1_DateRun_20181130T060000_DatePrev_20181130T160000grib2ncDisplay.GaussianRadius = 0.13999999999987267
aromeHD_SP1_DateRun_20181130T060000_DatePrev_20181130T160000grib2ncDisplay.SetScaleArray = ['POINTS', 'RH_2maboveground']
aromeHD_SP1_DateRun_20181130T060000_DatePrev_20181130T160000grib2ncDisplay.ScaleTransferFunction = 'PiecewiseFunction'
aromeHD_SP1_DateRun_20181130T060000_DatePrev_20181130T160000grib2ncDisplay.OpacityArray = ['POINTS', 'RH_2maboveground']
aromeHD_SP1_DateRun_20181130T060000_DatePrev_20181130T160000grib2ncDisplay.OpacityTransferFunction = 'PiecewiseFunction'
aromeHD_SP1_DateRun_20181130T060000_DatePrev_20181130T160000grib2ncDisplay.DataAxesGrid = 'GridAxesRepresentation'
aromeHD_SP1_DateRun_20181130T060000_DatePrev_20181130T160000grib2ncDisplay.SelectionCellLabelFontFile = ''
aromeHD_SP1_DateRun_20181130T060000_DatePrev_20181130T160000grib2ncDisplay.SelectionPointLabelFontFile = ''
aromeHD_SP1_DateRun_20181130T060000_DatePrev_20181130T160000grib2ncDisplay.PolarAxes = 'PolarAxesRepresentation'
aromeHD_SP1_DateRun_20181130T060000_DatePrev_20181130T160000grib2ncDisplay.ScalarOpacityUnitDistance = 0.1941905735298652
aromeHD_SP1_DateRun_20181130T060000_DatePrev_20181130T160000grib2ncDisplay.ScalarOpacityFunction = rH_2mabovegroundPWF

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
aromeHD_SP1_DateRun_20181130T060000_DatePrev_20181130T160000grib2ncDisplay.OSPRayScaleFunction.Points = [258.8880615234375, 0.0, 0.5, 0.0, 277.2615661621094, 0.45588234066963196, 0.5, 0.0, 297.7415771484375, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
aromeHD_SP1_DateRun_20181130T060000_DatePrev_20181130T160000grib2ncDisplay.ScaleTransferFunction.Points = [258.8880615234375, 0.0, 0.5, 0.0, 277.2615661621094, 0.45588234066963196, 0.5, 0.0, 297.7415771484375, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
aromeHD_SP1_DateRun_20181130T060000_DatePrev_20181130T160000grib2ncDisplay.OpacityTransferFunction.Points = [258.8880615234375, 0.0, 0.5, 0.0, 277.2615661621094, 0.45588234066963196, 0.5, 0.0, 297.7415771484375, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
aromeHD_SP1_DateRun_20181130T060000_DatePrev_20181130T160000grib2ncDisplay.DataAxesGrid.XTitleFontFile = ''
aromeHD_SP1_DateRun_20181130T060000_DatePrev_20181130T160000grib2ncDisplay.DataAxesGrid.YTitleFontFile = ''
aromeHD_SP1_DateRun_20181130T060000_DatePrev_20181130T160000grib2ncDisplay.DataAxesGrid.ZTitleFontFile = ''
aromeHD_SP1_DateRun_20181130T060000_DatePrev_20181130T160000grib2ncDisplay.DataAxesGrid.XLabelFontFile = ''
aromeHD_SP1_DateRun_20181130T060000_DatePrev_20181130T160000grib2ncDisplay.DataAxesGrid.YLabelFontFile = ''
aromeHD_SP1_DateRun_20181130T060000_DatePrev_20181130T160000grib2ncDisplay.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
aromeHD_SP1_DateRun_20181130T060000_DatePrev_20181130T160000grib2ncDisplay.PolarAxes.PolarAxisTitleFontFile = ''
aromeHD_SP1_DateRun_20181130T060000_DatePrev_20181130T160000grib2ncDisplay.PolarAxes.PolarAxisLabelFontFile = ''
aromeHD_SP1_DateRun_20181130T060000_DatePrev_20181130T160000grib2ncDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
aromeHD_SP1_DateRun_20181130T060000_DatePrev_20181130T160000grib2ncDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# setup the color legend parameters for each legend in this view

# get color legend/bar for rH_2mabovegroundLUT in view renderView1
rH_2mabovegroundLUTColorBar = GetScalarBar(rH_2mabovegroundLUT, renderView1)
rH_2mabovegroundLUTColorBar.Title = 'RH_2maboveground'
rH_2mabovegroundLUTColorBar.ComponentTitle = ''
rH_2mabovegroundLUTColorBar.TitleFontFile = ''
rH_2mabovegroundLUTColorBar.LabelFontFile = ''

# set color bar visibility
rH_2mabovegroundLUTColorBar.Visibility = 1

# show color legend
aromeHD_SP1_DateRun_20181130T060000_DatePrev_20181130T160000grib2ncDisplay.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(aromeHD_SP1_DateRun_20181130T060000_DatePrev_20181130T160000grib2nc)
SaveScreenshot(sys.argv[1]+".humidite.png",viewOrLayout=renderView1,TransparentBackground=1)

# ----------------------------------------------------------------
