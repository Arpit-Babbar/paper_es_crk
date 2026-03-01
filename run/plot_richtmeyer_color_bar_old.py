# state file generated using paraview version 5.10.1

# uncomment the following three lines to ensure this script works in future versions
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [100, 600]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [-15.869999559364027, 21.818578498095953, 10000.0]
renderView1.CameraFocalPoint = [-15.869999559364027, 21.818578498095953, 0.0]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 20.394364747076896
renderView1.UseColorPaletteForBackground = 0
renderView1.Background = [1.0, 1.0, 1.0]

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(100, 600)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--number', type=str, default='100')
args = parser.parse_args()

number = args.number


# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XML Rectilinear Grid Reader'
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
data_file = 'richtmeyer_meshkov'
# create a new 'XML Rectilinear Grid Reader'
sol = XMLRectilinearGridReader(registrationName='sol*', FileName=[os.path.join(dir_path, data_file, f'sol{number}.vtr')])
sol.PointArrayStatus = sol.PointArrayStatus = ['sol']
sol.TimeArray = 'None'

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from sol
solDisplay = Show(sol, renderView1, 'UniformGridRepresentation')

# get color transfer function/color map for 'sol'
solLUT = GetColorTransferFunction('sol')
solLUT.RGBPoints = [0.12844446882361255, 0.231373, 0.298039, 0.752941, 1.2392425940595146, 0.865003, 0.865003, 0.865003, 2.3500407192954165, 0.705882, 0.0156863, 0.14902]
solLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'sol'
solPWF = GetOpacityTransferFunction('sol')
solPWF.Points = [0.12844446882361255, 0.0, 0.5, 0.0, 2.3500407192954165, 1.0, 0.5, 0.0]
solPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
solDisplay.Representation = 'Surface'
solDisplay.ColorArrayName = ['POINTS', 'sol']
solDisplay.LookupTable = solLUT
solDisplay.SelectTCoordArray = 'None'
solDisplay.SelectNormalArray = 'None'
solDisplay.SelectTangentArray = 'None'
solDisplay.OSPRayScaleArray = 'sol'
solDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
solDisplay.SelectOrientationVectors = 'None'
solDisplay.ScaleFactor = 4.0
solDisplay.SelectScaleArray = 'None'
solDisplay.GlyphType = 'Arrow'
solDisplay.GlyphTableIndexArray = 'None'
solDisplay.GaussianRadius = 0.2
solDisplay.SetScaleArray = ['POINTS', 'sol']
solDisplay.ScaleTransferFunction = 'PiecewiseFunction'
solDisplay.OpacityArray = ['POINTS', 'sol']
solDisplay.OpacityTransferFunction = 'PiecewiseFunction'
solDisplay.DataAxesGrid = 'GridAxesRepresentation'
solDisplay.PolarAxes = 'PolarAxesRepresentation'
solDisplay.ScalarOpacityUnitDistance = 1.1550600724453486
solDisplay.ScalarOpacityFunction = solPWF
solDisplay.OpacityArrayName = ['POINTS', 'sol']
solDisplay.SliceFunction = 'Plane'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
solDisplay.ScaleTransferFunction.Points = [0.19338503719266273, 0.0, 0.5, 0.0, 2.408252788785335, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
solDisplay.OpacityTransferFunction.Points = [0.19338503719266273, 0.0, 0.5, 0.0, 2.408252788785335, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
solDisplay.SliceFunction.Origin = [6.666666666666667, 20.0, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for solLUT in view renderView1
solLUTColorBar = GetScalarBar(solLUT, renderView1)
solLUTColorBar.WindowLocation = 'Any Location'
solLUTColorBar.Position = [0.1561309523809523, 0.03058823529411764]
solLUTColorBar.Title = ''
solLUTColorBar.ComponentTitle = ''
solLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
solLUTColorBar.TitleFontSize = 20
solLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
solLUTColorBar.LabelFontSize = 20
solLUTColorBar.RangeLabelFormat = '%2.1f'
solLUTColorBar.ScalarBarLength = 0.9329411764705877

# set color bar visibility
solLUTColorBar.Visibility = 1

# show color legend
solDisplay.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# restore active source
SetActiveSource(sol)
# ----------------------------------------------------------------

myview = GetActiveView()

ExportView('./richtmeyer_meshkov_color_bar.pdf', view=myview)

if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')