import os
import bpy

supported_file_types = '.png', '.jpg', '.tif', '.hdr'
scriptPath = os.path.dirname(bpy.context.space_data.text.filepath)

def add_background(filepath):
    img = bpy.data.images.load(filepath)
    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            space_data = area.spaces.active
            bg = space_data.background_images.new()
            bg.image = img
            space_data.show_background_images = True
            break

def path_iterator(path_name):
    for fp in os.listdir(path_name):
        if fp.endswith(supported_file_types):
            yield fp

for area in bpy.context.screen.areas:
    if (area.type == 'VIEW_3D'):
            for img in path_iterator(scriptPath + '/refs/cup'):
                add_background(scriptPath + '/refs/cup/' + img)