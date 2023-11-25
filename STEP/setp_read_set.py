from OCC.Core.STEPControl import STEPControl_Reader
from OCC.Core.TopoDS import topods
from OCC.Core.BRep import BRep_Tool
from OCC.Core.GProp import GProp_GProps
from OCC.Core.BRepGProp import brepgprop_SurfaceProperties, brepgprop_VolumeProperties
from OCC.Core.TopAbs import TopAbs_FACE, TopAbs_SOLID

def read_step_file(file_path):
    step_reader = STEPControl_Reader()
    status = step_reader.ReadFile(file_path)

    if status == 1:
        print(f"Successfully opened {file_path}")
        step_reader.TransferRoot()
        nbr = step_reader.NbShapes()
        print(f"Number of shapes found: {nbr}")

        for i in range(1, nbr + 1):
            shape = step_reader.Shape(i)
            process_shape(shape)
    else:
        print(f"Failed to open {file_path}")

def process_shape(shape):
    if shape.ShapeType() == TopAbs_FACE:
        process_face(topods.Face(shape))
    elif shape.ShapeType() == TopAbs_SOLID:
        process_solid(topods.Solid(shape))

def process_face(face):
    properties = GProp_GProps()
    brepgprop_SurfaceProperties(face, properties)
    area = properties.Mass()
    print(f"Face area: {area}")

def process_solid(solid):
    properties = GProp_GProps()
    brepgprop_VolumeProperties(solid, properties)
    volume = properties.Mass()
    print(f"Solid volume: {volume}")

read_step_file("path_to_your_step_file.step")

