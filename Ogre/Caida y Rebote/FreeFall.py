## -------------------------------------------------------------------------
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## -------------------------------------------------------------------------
## On python3.8: pip install wheel ogre-python
## -------------------------------------------------------------------------

import ctypes, os, struct, sys, math
import Plane, Sphere
import Ogre, Ogre.Bites, Ogre.Overlay, Ogre.RTShader

## -------------------------------------------------------------------------
'''
Main application class
'''
class Main( Ogre.Bites.ApplicationContext, Ogre.Bites.InputListener ):

  '''
  '''
  def __init__( self, main_dir ):
    Ogre.Bites.ApplicationContext.__init__( self, 'MyFancyGame' )
    Ogre.Bites.InputListener.__init__( self )
    self.MainDir = main_dir
    self.PhysicsOn = False
    self.Gravity = -9.8
    self.TotalTime = 0.0
    self.Bouncing = False
    self.Velocity = 0
    self.Radius = 1
  # end def

  '''
  '''
  def keyPressed( self, evt ):
    if evt.keysym.sym == Ogre.Bites.SDLK_ESCAPE:
      self.getRoot( ).queueEndRendering( )
    elif evt.keysym.sym == ord( 'g' ):
      self.PhysicsOn = not self.PhysicsOn
    # end if
    return True
  # end def

  '''
  '''
  def frameRenderingQueued( self, evt ):
    if self.PhysicsOn:
      self.TotalTime += evt.timeSinceLastFrame

      v = abs(self.Velocity) - abs(self.Gravity) * self.TotalTime
      d = self.Gravity * self.TotalTime * self.TotalTime / 2.0

      if not self.Bouncing:      
        self.SphereNode.setPosition(
          Ogre.Vector3( 0, d, 0 ) + self.StartPosition
        )
        if self.SphereNode.getPosition()[1] <= self.Radius:  
          self.SphereNode.setPosition(Ogre.Vector3(0, self.Radius, 0))
          self.Bouncing = True
          self.Velocity =  -self.Gravity * self.TotalTime * 0.8
          self.TotalTime = 0
        # end if
      else:         
        d = abs(self.Velocity) * self.TotalTime - (abs(self.Gravity) * pow(self.TotalTime, 2))/2
        self.SphereNode.setPosition(          
          Ogre.Vector3( 0, d%self.StartPosition[1] + self.Radius , 0 )
        )
        if v <= 0:         
          if d+1 <= self.Radius + 0.1:
            self.SphereNode.setPosition(Ogre.Vector3(0, self.Radius, 0))
            self.PhysicsOn = False
          else:
            self.Bouncing = False
            self.Velocity =  0
            self.TotalTime = 0
            self.StartPosition[1] = self.SphereNode.getPosition()[1]
          # end if
        # end if
      # end if

    # end if
    return True
  # end def

  '''
  '''
  def createResource( self, geometry, topology, name, group = 'General' ):
    mesh = Ogre.MeshManager.getSingleton( ).createManual( name, group )
    smesh = mesh.createSubMesh( )
    vbufCount = len( geometry )
    nVertices = int( vbufCount / 6 )
    ibufCount = len( topology )

    mesh.sharedVertexData = Ogre.VertexData( )
    mesh.sharedVertexData.vertexCount = nVertices
    decl = mesh.sharedVertexData.vertexDeclaration
    offset = 0

    # 1st buffer
    decl.addElement( 0, offset, Ogre.VET_FLOAT3, Ogre.VES_POSITION )
    offset += Ogre.VertexElement.getTypeSize( Ogre.VET_FLOAT3 )
    decl.addElement( 0, offset, Ogre.VET_FLOAT3, Ogre.VES_NORMAL )
    offset += Ogre.VertexElement.getTypeSize( Ogre.VET_FLOAT3 )
    vbuf = Ogre.HardwareBufferManager.getSingleton( ).createVertexBuffer(
      offset, mesh.sharedVertexData.vertexCount,
      Ogre.HardwareBuffer.HBU_STATIC_WRITE_ONLY
      )

    # Upload the vertex data to the card
    buf = ( ctypes.c_float * len( geometry ) ).from_buffer_copy(
      struct.pack( '%sf' % len( geometry ), *geometry )
      )
    vbuf.writeData( 0, vbuf.getSizeInBytes( ), buf, True )

    # Set vertex buffer binding so buffer 0 is bound to our vertex buffer
    bind = mesh.sharedVertexData.vertexBufferBinding
    bind.setBinding( 0, vbuf )

    # 2nd buffer
    offset = 0
    decl.addElement( 1, offset, Ogre.VET_COLOUR, Ogre.VES_DIFFUSE )
    offset += Ogre.VertexElement.getTypeSize( Ogre.VET_COLOUR )

    # Allocate index buffer of the requested number of vertices (ibufCount)
    ibuf = Ogre.HardwareBufferManager.getSingleton( ).createIndexBuffer(
      Ogre.HardwareIndexBuffer.IT_16BIT, ibufCount,
      Ogre.HardwareBuffer.HBU_STATIC_WRITE_ONLY
      )

    # Upload the index data to the card
    faces = ( ctypes.c_ushort * len( topology ) ).from_buffer_copy(
      struct.pack( '%sH' % len( topology ), *topology )
      )
    ibuf.writeData( 0, ibuf.getSizeInBytes( ), faces, True )

    # Set parameters of the submesh
    smesh.useSharedVertices = True
    smesh.indexData.indexBuffer = ibuf
    smesh.indexData.indexCount = ibufCount
    smesh.indexData.indexStart = 0

    # Set bounding information (for culling)
    mesh._setBounds( Ogre.AxisAlignedBox( -1, -1, -1, 1, 1, 1 ) )
    mesh._setBoundingSphereRadius( 1 )

    # Notify mesh object that it has been loaded
    mesh.load( )
  # end def

  '''
  '''
  def loadResources( self ):
    # Load resources from file
    self.enableShaderCache( )
    cf = Ogre.ConfigFile( )
    cf.loadDirect( os.path.join( self.MainDir, 'resources.cfg' ) )
    res_mgr = Ogre.ResourceGroupManager.getSingleton( )
    for k in cf.getSettingsBySection( ):
      s = cf.getSettings( k )
      for t, f in s.items( ):
        res_mgr.addResourceLocation( f, t, k )
      # end for
    # end for

    # Create manual meshes
    [ sphere_geometry, sphere_topology ] = Sphere.Build( 1, 100, 100 )
    [ plane_geometry, plane_topology ] = Plane.Build( 20, 20 )
    self.createResource( sphere_geometry, sphere_topology, 'Sphere' )
    self.createResource( plane_geometry, plane_topology, 'Floor' )

    # Finish loading
    res_mgr.initialiseAllResourceGroups( )
    res_mgr.loadResourceGroup( 'Essential' )
    #groups = res_mgr.getResourceGroups( )
    #for g in groups:
    #  res_mgr.loadResourceGroup( g )
    # end for
  # end def

  '''
  '''
  def setup( self ):
    Ogre.Bites.ApplicationContext.setup( self )
    self.addInputListener( self )

    root = self.getRoot( )
    scn_mgr = root.createSceneManager( )

    shadergen = Ogre.RTShader.ShaderGenerator.getSingleton( )
    shadergen.addSceneManager( scn_mgr )

    scn_mgr.addRenderQueueListener( self.getOverlaySystem( ) )

    scn_mgr.setAmbientLight( ( 0.1, 0.1, 0.1 ) )

    light = scn_mgr.createLight( 'MainLight' )
    lightnode = scn_mgr.getRootSceneNode( ).createChildSceneNode( )
    lightnode.setPosition( 0, 10, 15 )
    lightnode.attachObject( light )

    cam = scn_mgr.createCamera( 'myCam' )
    cam.setNearClipDistance( 0.5 )
    cam.setAutoAspectRatio( True )
    camnode = scn_mgr.getRootSceneNode( ).createChildSceneNode( )
    camnode.attachObject( cam )

    self.camman = Ogre.Bites.CameraMan( camnode )
    self.camman.setStyle( Ogre.Bites.CS_ORBIT )
    self.camman.setYawPitchDist( 0, 0.1, 25 )
    self.addInputListener( self.camman )

    vp = self.getRenderWindow( ).addViewport( cam )
    vp.setBackgroundColour( ( 0.1, 0.1, 0.1 ) )

    ent = scn_mgr.createEntity( 'Sphere' )
    node = scn_mgr.getRootSceneNode( ).createChildSceneNode( )
    node.attachObject( ent )
    self.StartPosition = Ogre.Vector3( 0, 10, 0 )
    node.setPosition( self.StartPosition )
    self.SphereNode = node

    ent = scn_mgr.createEntity( 'Floor' )
    node = scn_mgr.getRootSceneNode( ).createChildSceneNode( )
    node.attachObject( ent )
  # end def

  '''
  '''
  def shutdown( self ):
    Ogre.Bites.ApplicationContext.shutdown( self )
  # end def

  '''
  '''
  def go( self ):
    self.initApp( )
    self.getRoot( ).startRendering( )
    self.closeApp( )
  # end def

# end class

## -------------------------------------------------------------------------
if __name__ == '__main__':
  app = Main( os.path.split( os.path.abspath( sys.argv[ 0 ] ) )[ 0 ] )
  app.go( )
# end if

## eof - ParabollicMovement.py
