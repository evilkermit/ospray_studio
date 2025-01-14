#Copyright 2021 Intel Corporation
#SPDX-License-Identifier: Apache-2.0

import sys
import pysg as sg
from pysg import Any, vec3f, Data, FileName, Importer, MaterialRegistry, ArcballCamera, vec2i, box3f

files  = sg.init(sys.argv)

W = 1920
H = 1080

window_size = vec2i(W, H)
aspect = Any(float(W) / H)

frame = sg.Frame()
frame.createChild("windowSize", "vec2i", Any(window_size))
world = frame.child("world")

lightsMan = frame.child("lights")
baseMaterialRegistry = frame.child("baseMaterialRegistry")

if len(files) > 0:
    for file in files:
        importer = sg.getImporter(world, FileName(file))
        importer.setLightsManager(lightsMan)
        importer.setMaterialRegistry(baseMaterialRegistry)
        importer.importScene()

world.render()
bounds = world.bounds()

arcballCamera = ArcballCamera(bounds, window_size)
cam = frame.child("camera")
cam.createChild("aspect", "float", aspect)
sg.updateCamera(cam, arcballCamera)

frame.startNewFrame()
frame.waitOnFrame()
frame.saveFrame("studio_import.png", 0)
