## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

'''
'''
def Build( width = 1.0, depth = 1.0 ):
  # -- Vertices
  G  = [ -width / 2.0, 0.0, depth / 2.0 ]
  G += [ 0.0, 1.0, 0.0 ]
  G += [ width / 2.0, 0.0, depth / 2.0 ]
  G += [ 0.0, 1.0, 0.0 ]
  G += [ width / 2.0, 0.0, -depth / 2.0 ]
  G += [ 0.0, 1.0, 0.0 ]
  G += [ -width / 2.0, 0.0, -depth / 2.0 ]
  G += [ 0.0, 1.0, 0.0 ]

  # 3 ---2
  # |   /|
  # |  / |
  # | /  |
  # |/   |
  # 0 ---1

  F  = [ 0, 2, 3 ]
  F += [ 0, 1, 2 ]

  return [ G, F ]
# end def

## eof - Plane.py
