# RetopoSelectedDecimatePlanar.py
# Copyright (c). 2020 Daniel Patterson, MCSD (danielanywhere)
# Released for public access under the MIT License.
# http://www.opensource.org/licenses/mit-license.php
# Perform easy retopology of all selected items using Planar Decimation.
# Default angle is 15 degrees.
# This script has been tested in Blender 2.90.1.
# TODO: Create a self-registering script to allow the script to be installed.
# TODO: Create a section to attach the functionality to the Edit menu.

import bpy
import math

# Start with the currently selected objects.
selectedObjects = bpy.context.selected_objects;

# Add the decimation modifier to the specified object.
def addDecimateModifier(item):
	print("Add decimate modifier to ", item.name);
	modifier = item.modifiers.new(name = "Decimate", type = "DECIMATE");
	modifier.decimate_type = "DISSOLVE";
	# The following property is between 0 and 180 degrees.
	modifier.angle_limit = 15 * (math.pi / 180);
	# The Apply Modifier action uses the active object.
	bpy.context.view_layer.objects.active = item;
	# Apply the modifier.
	print(" Apply...");
	bpy.ops.object.modifier_apply(modifier = "Decimate");

# Remove previously defined decimate modifiers.
def removeDecimateModifiers(item):
	for modifierEntry in item.modifiers:
		if(modifierEntry.type == "DECIMATE"):
			print("Remove decimate modifier from ", item.name);
			item.modifiers.remove(modifier = modifierEntry);

# Main script.
for item in selectedObjects:
	if(item.type == "MESH"):
		# bpy.context.scene.objects.active = item;
		removeDecimateModifiers(item);
		addDecimateModifier(item);
