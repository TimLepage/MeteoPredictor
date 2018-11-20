# state file generated using paraview version 5.4.1

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

#### import the simple module from the paraview
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
renderView1.CameraParallelScale = 9.379486411673074
renderView1.Background = [0.32, 0.34, 0.43]

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'NetCDF Reader'
donnesmeteonc = NetCDFReader(FileName=['/home/terrier/Documents/RICM5/VISU/ParaviewOtherData/donnesmeteo.nc'])
donnesmeteonc.Dimensions = '(latitude, longitude)'
donnesmeteonc.SphericalCoordinates = 0
donnesmeteonc.ReplaceFillValueWithNan = 1

# create a new 'Threshold'
threshold1 = Threshold(Input=donnesmeteonc)
threshold1.Scalars = ['POINTS', 'RH_2maboveground']
threshold1.ThresholdRange = [19.5445556640625, 101.0133056640625]

# create a new 'Calculator'
calculduvent = Calculator(Input=threshold1)
calculduvent.ResultArrayName = 'Wind'
calculduvent.Function = 'UGRD_10maboveground*iHat+VGRD_10maboveground*jHat'

# create a new 'Stream Tracer'
dessinlignedecourant = StreamTracer(Input=calculduvent,
    SeedType='High Resolution Line Source')
dessinlignedecourant.Vectors = ['POINTS', 'Wind']
dessinlignedecourant.MaximumStreamlineLength = 28.0

# init the 'High Resolution Line Source' selected for 'SeedType'
dessinlignedecourant.SeedType.Point1 = [-12.0, 37.5, 0.0]
dessinlignedecourant.SeedType.Point2 = [16.0, 55.3899993896484, 0.0]

# create a new 'Glyph'
dessinpetitvecteurvent = Glyph(Input=calculduvent,
    GlyphType='2D Glyph')
dessinpetitvecteurvent.Scalars = ['POINTS', 'None']
dessinpetitvecteurvent.Vectors = ['POINTS', 'Wind']
dessinpetitvecteurvent.ScaleFactor = 0.1
dessinpetitvecteurvent.GlyphTransform = 'Transform2'

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get color transfer function/color map for 'RH_2maboveground'
rH_2mabovegroundLUT = GetColorTransferFunction('RH_2maboveground')
rH_2mabovegroundLUT.RGBPoints = [19.5445556640625, 0.231373, 0.298039, 0.752941, 60.2789306640625, 0.865003, 0.865003, 0.865003, 101.0133056640625, 0.705882, 0.0156863, 0.14902]
rH_2mabovegroundLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'RH_2maboveground'
rH_2mabovegroundPWF = GetOpacityTransferFunction('RH_2maboveground')
rH_2mabovegroundPWF.Points = [19.5445556640625, 0.0, 0.5, 0.0, 101.0133056640625, 1.0, 0.5, 0.0]
rH_2mabovegroundPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from threshold1
threshold1Display = Show(threshold1, renderView1)
# trace defaults for the display properties.
threshold1Display.Representation = 'Surface'
threshold1Display.ColorArrayName = ['POINTS', 'RH_2maboveground']
threshold1Display.LookupTable = rH_2mabovegroundLUT
threshold1Display.OSPRayScaleArray = 'RH_2maboveground'
threshold1Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold1Display.SelectOrientationVectors = 'None'
threshold1Display.ScaleFactor = 2.8000000000000003
threshold1Display.SelectScaleArray = 'None'
threshold1Display.GlyphType = 'Arrow'
threshold1Display.GlyphTableIndexArray = 'None'
threshold1Display.DataAxesGrid = 'GridAxesRepresentation'
threshold1Display.PolarAxes = 'PolarAxesRepresentation'
threshold1Display.ScalarOpacityFunction = rH_2mabovegroundPWF
threshold1Display.ScalarOpacityUnitDistance = 0.20666834150287358

# show color legend
threshold1Display.SetScalarBarVisibility(renderView1, True)

# show data from dessinpetitvecteurvent
dessinpetitvecteurventDisplay = Show(dessinpetitvecteurvent, renderView1)
# trace defaults for the display properties.
dessinpetitvecteurventDisplay.Representation = 'Surface'
dessinpetitvecteurventDisplay.ColorArrayName = ['POINTS', 'RH_2maboveground']
dessinpetitvecteurventDisplay.LookupTable = rH_2mabovegroundLUT
dessinpetitvecteurventDisplay.OSPRayScaleArray = 'GlyphVector'
dessinpetitvecteurventDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
dessinpetitvecteurventDisplay.SelectOrientationVectors = 'GlyphVector'
dessinpetitvecteurventDisplay.ScaleFactor = 2.7941198348999023
dessinpetitvecteurventDisplay.SelectScaleArray = 'GlyphVector'
dessinpetitvecteurventDisplay.GlyphType = 'Arrow'
dessinpetitvecteurventDisplay.GlyphTableIndexArray = 'GlyphVector'
dessinpetitvecteurventDisplay.DataAxesGrid = 'GridAxesRepresentation'
dessinpetitvecteurventDisplay.PolarAxes = 'PolarAxesRepresentation'

# show color legend
dessinpetitvecteurventDisplay.SetScalarBarVisibility(renderView1, True)

# show data from dessinlignedecourant
dessinlignedecourantDisplay = Show(dessinlignedecourant, renderView1)
# trace defaults for the display properties.
dessinlignedecourantDisplay.Representation = 'Surface'
dessinlignedecourantDisplay.ColorArrayName = ['POINTS', '']
dessinlignedecourantDisplay.OSPRayScaleArray = 'AngularVelocity'
dessinlignedecourantDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
dessinlignedecourantDisplay.SelectOrientationVectors = 'Normals'
dessinlignedecourantDisplay.ScaleFactor = 2.453986644744873
dessinlignedecourantDisplay.SelectScaleArray = 'AngularVelocity'
dessinlignedecourantDisplay.GlyphType = 'Arrow'
dessinlignedecourantDisplay.GlyphTableIndexArray = 'AngularVelocity'
dessinlignedecourantDisplay.DataAxesGrid = 'GridAxesRepresentation'
dessinlignedecourantDisplay.PolarAxes = 'PolarAxesRepresentation'

# setup the color legend parameters for each legend in this view

# get color legend/bar for rH_2mabovegroundLUT in view renderView1
rH_2mabovegroundLUTColorBar = GetScalarBar(rH_2mabovegroundLUT, renderView1)
rH_2mabovegroundLUTColorBar.Title = 'RH_2maboveground'
rH_2mabovegroundLUTColorBar.ComponentTitle = ''

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(dessinlignedecourant)
# ----------------------------------------------------------------

WriteImage("MonImage.png")
