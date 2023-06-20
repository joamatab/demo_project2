# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: title,-all
#     custom_cell_magics: kql
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import gdsfactory as gf
from gdsfactory.generic_tech import get_generic_pdk

gf.config.rich_output()

PDK = get_generic_pdk()
PDK.activate()

# Create a blank component (essentially an empty GDS cell with some special features)
c = gf.Component("myComponent")

# Create and add a polygon from separate lists of x points and y points
# (Can also be added like [(x1,y1), (x2,y2), (x3,y3), ... ]
poly1 = c.add_polygon(
    [(-8, 6, 7, 9), (-6, 8, 17, 5)], layer=1
)  # GDS layers are tuples of ints (but if we use only one number it assumes the other number is 0)

# show it in matplotlib and KLayout (you need to have KLayout open and install gdsfactory from the git repo with make install)
c.plot()

# %%
# %%
c = gf.Component("myComponent2")
# Create some new geometry from the functions available in the geometry library
t = gf.components.text("Hello!")
r = gf.components.rectangle(size=[5, 10], layer=(2, 0))

# Add references to the new geometry to c, our blank component
text1 = c.add_ref(t)  # Add the text we created as a reference
# Using the << operator (identical to add_ref()), add the same geometry a second time
text2 = c << t
r = c << r  # Add the rectangle we created
s = c.to_3d()
s.show()

# %%

# %% [markdown]
# # Component
#
# A `Component` is like an empty canvas, where you can add polygons, references to other Components and ports (to connect to other components)
#
# ![](https://i.imgur.com/oeuKGsc.png)
#
# In gdsfactory **all dimensions** are in **microns**

# %% [markdown]
# ## Polygons
#
# You can add polygons to different layers.

# %%

gf.config.rich_output()

PDK = get_generic_pdk()
PDK.activate()

# Create a blank component (essentially an empty GDS cell with some special features)
c = gf.Component("myComponent")

# Create and add a polygon from separate lists of x points and y points
# (Can also be added like [(x1,y1), (x2,y2), (x3,y3), ... ]
poly1 = c.add_polygon(
    [(-8, 6, 7, 9), (-6, 8, 17, 5)], layer=1
)  # GDS layers are tuples of ints (but if we use only one number it assumes the other number is 0)

# show it in matplotlib and KLayout (you need to have KLayout open and install gdsfactory from the git repo with make install)
c

# %% [markdown]
# **Exercise** :
#
# Make a component similar to the one above that has a second polygon in layer (2, 0)

# %%
c = gf.Component("myComponent2")
# Create some new geometry from the functions available in the geometry library
t = gf.components.text("Hello!")
r = gf.components.rectangle(size=[5, 10], layer=(2, 0))

# Add references to the new geometry to c, our blank component
text1 = c.add_ref(t)  # Add the text we created as a reference
# Using the << operator (identical to add_ref()), add the same geometry a second time
text2 = c << t
r = c << r  # Add the rectangle we created
s = c.to_3d()
s.show()

# Now that the geometry has been added to "c", we can move everything around:
