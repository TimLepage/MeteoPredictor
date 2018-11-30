# state file generated using paraview version 5.0.1

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
Monechelle = 0.5
renderView1.ViewSize = [(int)(2801*Monechelle),(int) (1791*Monechelle)]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [1.999999999987267, 46.45, 0.0]
renderView1.StereoType = 0
renderView1.CameraPosition = [1.3694900800914644, 45.59695716719981, 10000.0]
renderView1.CameraFocalPoint = [1.3694900800914644, 45.59695716719981, 0.0]
renderView1.CameraParallelScale = 15.25834006147841
renderView1.Background = [0.32, 0.34, 0.43]

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'NetCDF Reader'
a2011nc = NetCDFReader(FileName=['/home/utilisateur/Bureau/S9/VISU/Projet/METEO_VISUALISATION_SIMPLE/PYTHON/2011.nc'])
a2011nc.Dimensions = '(latitude, longitude)'
a2011nc.SphericalCoordinates = 0
a2011nc.ReplaceFillValueWithNan = 1

# create a new 'Extract Subset'
cadrillage80 = ExtractSubset(Input=a2011nc)
cadrillage80.VOI = [0, 2800, 0, 1790, 0, 0]
cadrillage80.SampleRateI = 80
cadrillage80.SampleRateJ = 80

# create a new 'Threshold'
deleteNanCadrillage = Threshold(Input=cadrillage80)
deleteNanCadrillage.Scalars = ['POINTS', 'RH_2maboveground']
deleteNanCadrillage.ThresholdRange = [46.53235626220703, 100.31360626220703]

# create a new 'Threshold'
deleteNan = Threshold(Input=a2011nc)
deleteNan.Scalars = ['POINTS', 'RH_2maboveground']
deleteNan.ThresholdRange = [25.93860626220703, 101.00110626220703]

# create a new 'Calculator'
calculWind = Calculator(Input=deleteNanCadrillage)
calculWind.ResultArrayName = 'Wind'
calculWind.Function = 'iHat*UGRD_10maboveground+jHat*VGRD_10maboveground'

# create a new 'Glyph'
arrows = Glyph(Input=calculWind,
    GlyphType='2D Glyph')
arrows.Scalars = ['POINTS', 'None']
arrows.Vectors = ['POINTS', 'Wind']
arrows.ScaleFactor = 0.4
arrows.GlyphMode = 'All Points'
arrows.GlyphTransform = 'Transform2'

# create a new 'Stream Tracer'
streamTracer = StreamTracer(Input=calculWind,
    SeedType='High Resolution Line Source')
streamTracer.Vectors = ['POINTS', 'Wind']
streamTracer.MaximumStreamlineLength = 26.399999618530273

# init the 'High Resolution Line Source' selected for 'SeedType'
streamTracer.SeedType.Point1 = [-11.199999809265137, 38.29999923706055, 0.0]
streamTracer.SeedType.Point2 = [15.199999809265137, 55.099998474121094, 0.0]

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get color transfer function/color map for 'TMP2maboveground'
tMP2mabovegroundLUT = GetColorTransferFunction('TMP2maboveground')
tMP2mabovegroundLUT.RGBPoints = [251.40696716308594, 0.0, 0.0, 0.5625, 256.2313997979584, 0.0, 0.0, 1.0, 267.2586961019211, 0.0, 1.0, 1.0, 272.7723333989182, 0.5, 1.0, 0.5, 278.28597069591524, 1.0, 1.0, 0.0, 289.313266999878, 1.0, 0.0, 0.0, 294.82690429687506, 0.5, 0.0, 0.0]
tMP2mabovegroundLUT.ColorSpace = 'RGB'
tMP2mabovegroundLUT.NumberOfTableValues = 10
tMP2mabovegroundLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'TMP2maboveground'
tMP2mabovegroundPWF = GetOpacityTransferFunction('TMP2maboveground')
tMP2mabovegroundPWF.Points = [251.40696716308594, 0.0, 0.5, 0.0, 294.826904296875, 0.9802631735801697, 0.5, 0.0]
tMP2mabovegroundPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from deleteNan
deleteNanDisplay = Show(deleteNan, renderView1)
# trace defaults for the display properties.
deleteNanDisplay.ColorArrayName = ['POINTS', 'TMP_2maboveground']
deleteNanDisplay.LookupTable = tMP2mabovegroundLUT
deleteNanDisplay.GlyphType = 'Arrow'
deleteNanDisplay.ScalarOpacityUnitDistance = 0.20666834150287358

# show data from arrows
arrowsDisplay = Show(arrows, renderView1)
# trace defaults for the display properties.
arrowsDisplay.ColorArrayName = ['POINTS', '']
arrowsDisplay.DiffuseColor = [1.0, 0.8352941176470589, 0.8392156862745098]
arrowsDisplay.GlyphType = 'Arrow'

# show data from streamTracer
streamTracerDisplay = Show(streamTracer, renderView1)
# trace defaults for the display properties.
streamTracerDisplay.ColorArrayName = ['POINTS', '']
streamTracerDisplay.GlyphType = 'Arrow'
WriteImage("TTTT.png")
