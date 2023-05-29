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



