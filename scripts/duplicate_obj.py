import bpy

scn = bpy.context.scene
obj = bpy.context.active_object
mat = obj.active_material
mesh = obj.data

for x in range(7):
    dup = bpy.data.objects.new(obj.name, mesh.copy())
    dup.active_material = mat.copy()
    scn.objects.link(dup)
    dup.location.x = obj.location.x + 3