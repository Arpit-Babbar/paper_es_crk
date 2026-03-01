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
renderView1.ViewSize = [800, 80]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [-1.9258357269334452, 5.569770952994148, 10000.0]
renderView1.CameraFocalPoint = [-1.9258357269334452, 5.569770952994148, 0.0]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 1.0142232364536228
renderView1.UseColorPaletteForBackground = 0
renderView1.Background = [1.0, 1.0, 1.0]

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(800, 80)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--number', type=str, default='15')
args = parser.parse_args()

number = args.number

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XML Rectilinear Grid Reader'
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
data_file = 'khi_chan2022'
# create a new 'XML Rectilinear Grid Reader'
sol0 = XMLRectilinearGridReader(registrationName='sol0*', FileName=[os.path.join(dir_path, data_file, f'sol0{number}.vtr')])
sol0.PointArrayStatus = ['sol']
sol0.TimeArray = 'None'
# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from sol0
sol0Display = Show(sol0, renderView1, 'UniformGridRepresentation')

# get color transfer function/color map for 'sol'
solLUT = GetColorTransferFunction('sol')
solLUT.RGBPoints = [0.5000004588533404, 0.231373, 0.298039, 0.752941, 1.2499997705733303, 0.865003, 0.865003, 0.865003, 1.9999990822933191, 0.705882, 0.0156863, 0.14902]
solLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'sol'
solPWF = GetOpacityTransferFunction('sol')
solPWF.Points = [0.5000004588533404, 0.0, 0.5, 0.0, 1.9999990822933191, 1.0, 0.5, 0.0]
solPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
sol0Display.Representation = 'Surface'
sol0Display.ColorArrayName = ['POINTS', 'sol']
sol0Display.LookupTable = solLUT
sol0Display.SelectTCoordArray = 'None'
sol0Display.SelectNormalArray = 'None'
sol0Display.SelectTangentArray = 'None'
sol0Display.OSPRayScaleArray = 'sol'
sol0Display.OSPRayScaleFunction = 'PiecewiseFunction'
sol0Display.SelectOrientationVectors = 'None'
sol0Display.ScaleFactor = 0.2
sol0Display.SelectScaleArray = 'None'
sol0Display.GlyphType = 'Arrow'
sol0Display.GlyphTableIndexArray = 'None'
sol0Display.GaussianRadius = 0.01
sol0Display.SetScaleArray = ['POINTS', 'sol']
sol0Display.ScaleTransferFunction = 'PiecewiseFunction'
sol0Display.OpacityArray = ['POINTS', 'sol']
sol0Display.OpacityTransferFunction = 'PiecewiseFunction'
sol0Display.DataAxesGrid = 'GridAxesRepresentation'
sol0Display.PolarAxes = 'PolarAxesRepresentation'
sol0Display.ScalarOpacityUnitDistance = 0.11194615448707361
sol0Display.ScalarOpacityFunction = solPWF
sol0Display.OpacityArrayName = ['POINTS', 'sol']
sol0Display.SliceFunction = 'Plane'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
sol0Display.ScaleTransferFunction.Points = [0.5000004588533404, 0.0, 0.5, 0.0, 1.9999990822933191, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
sol0Display.OpacityTransferFunction.Points = [0.5000004588533404, 0.0, 0.5, 0.0, 1.9999990822933191, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for solLUT in view renderView1
solLUTColorBar = GetScalarBar(solLUT, renderView1)
solLUTColorBar.Orientation = 'Horizontal'
solLUTColorBar.WindowLocation = 'Any Location'
solLUTColorBar.Position = [0.04324736321687506, 0.28718085106382996]
solLUTColorBar.Title = ''
solLUTColorBar.ComponentTitle = ''
solLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
solLUTColorBar.TitleFontSize = 20
solLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
solLUTColorBar.LabelFontSize = 20
solLUTColorBar.RangeLabelFormat = '%2.1f'
solLUTColorBar.ScalarBarLength = 0.9150000000000015

# set color bar visibility
solLUTColorBar.Visibility = 1

# show color legend
sol0Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# restore active source
SetActiveSource(sol0)
# ----------------------------------------------------------------

myview = GetActiveView()

ExportView('./khi_color_bar.pdf', view=myview)

if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')