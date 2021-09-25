## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

import math

'''
'''
def Build( radius = 1.0, theta_samples = 100, psi_samples = 100 ):
  # -- Vertices
  G  = [ 0.0, 1.0, 0.0 ]
  G += [ 0.0, 1.0, 0.0 ]
  for j in range( theta_samples - 1 ):
    theta = math.pi * float( j + 1 ) / float( theta_samples )
    st = math.sin( theta )
    ct = math.cos( theta )
    for i in range( psi_samples ):
      psi = 2.0 * math.pi * float( i ) / float( psi_samples )
      sp = math.sin( psi )
      cp = math.cos( psi )
      G += [ radius * st * cp, radius * ct, radius * st * sp ]
      G += [ st * cp, ct, st * sp ]
    # end for
  # end for
  G += [ 0.0, -1.0, 0.0 ]
  G += [ 0.0, -1.0, 0.0 ]

  # -- Top triangles
  F = []
  for i in range( psi_samples ):
    a = 0
    b = ( i + 1 ) % psi_samples + 1
    c = i + 1
    F += [ a, b, c ]
  # end for

  # -- Middle triangles
  for j in range( theta_samples - 2 ):
    aStart = j * psi_samples + 1
    bStart = ( j + 1 ) * psi_samples + 1
    for i in range( psi_samples ):
      a = aStart + i;
      a1 = aStart + ( i + 1 ) % psi_samples;
      b = bStart + i;
      b1 = bStart + ( i + 1 ) % psi_samples;
      F += [ a, a1, b1 ]
      F += [ a, b1, b ]
    # end for
  # end for

  # -- Bottom triangles
  for i in range( psi_samples ):
    a = int( len( G ) / 6 ) - 1
    b = i + psi_samples * ( theta_samples - 2 ) + 1
    c = ( i + 1 ) % psi_samples + psi_samples * ( theta_samples - 2 ) + 1
    F += [ a, b, c ]
  # end for

  return [ G, F ]
# end def

## eof - Sphere.py
