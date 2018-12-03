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
renderView1.CameraPosition = [1.999999999987267, 46.45, 9999.999999999989]
renderView1.CameraFocalPoint = [1.999999999987267, 46.45, 0.0]
renderView1.CameraViewUp = [0.010935749230021045, 0.999940202906543, 0.0]
renderView1.CameraParallelScale = 13.73250605533057
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

# create a new 'Glyph'
glyph1 = Glyph(Input=calculator2,
    GlyphType='2D Glyph')
glyph1.OrientationArray = ['POINTS', 'Vitesse du vent']
glyph1.ScaleArray = ['POINTS', 'No scale array']
glyph1.ScaleFactor = 0.7020000000000001
glyph1.GlyphTransform = 'Transform2'

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from glyph1
glyph1Display = Show(glyph1, renderView1)

# trace defaults for the display properties.
glyph1Display.Representation = 'Surface'
glyph1Display.ColorArrayName = ['POINTS', '']
glyph1Display.DiffuseColor = [0.0, 0.0, 0.0]
glyph1Display.OSPRayScaleArray = 'RH_2maboveground'
glyph1Display.OSPRayScaleFunction = 'PiecewiseFunction'
glyph1Display.SelectOrientationVectors = 'None'
glyph1Display.ScaleFactor = 2.7051781654357914
glyph1Display.SelectScaleArray = 'None'
glyph1Display.GlyphType = 'Arrow'
glyph1Display.GlyphTableIndexArray = 'None'
glyph1Display.GaussianRadius = 0.13525890827178955
glyph1Display.SetScaleArray = ['POINTS', 'RH_2maboveground']
glyph1Display.ScaleTransferFunction = 'PiecewiseFunction'
glyph1Display.OpacityArray = ['POINTS', 'RH_2maboveground']
glyph1Display.OpacityTransferFunction = 'PiecewiseFunction'
glyph1Display.DataAxesGrid = 'GridAxesRepresentation'
glyph1Display.SelectionCellLabelFontFile = ''
glyph1Display.SelectionPointLabelFontFile = ''
glyph1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
glyph1Display.OSPRayScaleFunction.Points = [258.8880615234375, 0.0, 0.5, 0.0, 277.2615661621094, 0.45588234066963196, 0.5, 0.0, 297.7415771484375, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
glyph1Display.ScaleTransferFunction.Points = [258.8880615234375, 0.0, 0.5, 0.0, 277.2615661621094, 0.45588234066963196, 0.5, 0.0, 297.7415771484375, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
glyph1Display.OpacityTransferFunction.Points = [258.8880615234375, 0.0, 0.5, 0.0, 277.2615661621094, 0.45588234066963196, 0.5, 0.0, 297.7415771484375, 1.0, 0.5, 0.0]

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
glyph1Display.DataAxesGrid.XTitleFontFile = ''
glyph1Display.DataAxesGrid.YTitleFontFile = ''
glyph1Display.DataAxesGrid.ZTitleFontFile = ''
glyph1Display.DataAxesGrid.XLabelFontFile = ''
glyph1Display.DataAxesGrid.YLabelFontFile = ''
glyph1Display.DataAxesGrid.ZLabelFontFile = ''

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
glyph1Display.PolarAxes.PolarAxisTitleFontFile = ''
glyph1Display.PolarAxes.PolarAxisLabelFontFile = ''
glyph1Display.PolarAxes.LastRadialAxisTextFontFile = ''
glyph1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(streamTracer1)
# ----------------------------------------------------------------