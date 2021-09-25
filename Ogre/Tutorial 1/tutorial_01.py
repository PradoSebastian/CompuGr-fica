## -------------------------------------------------------------------------
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## -------------------------------------------------------------------------
## On python3.8: pip install wheel ogre-python
## -------------------------------------------------------------------------

import os, sys
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
  # end def

  '''
  '''
  def keyPressed( self, evt ):
    if evt.keysym.sym == Ogre.Bites.SDLK_ESCAPE:
      self.getRoot( ).queueEndRendering( )
    # end if
    return True
  # end def

  '''
  '''
  def loadResources( self ):
    self.enableShaderCache( )
    cf = Ogre.ConfigFile( )
    cf.loadDirect( os.path.join( self.MainDir, 'resources.cfg' ) )
    for k in cf.getSettingsBySection( ):
      s = cf.getSettings( k )
      for t, f in s.items( ):
        Ogre.ResourceGroupManager.getSingleton( ).addResourceLocation( f, t, k )
      # end for
    # end for
    return Ogre.Bites.ApplicationContext.loadResources( self )
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

    #light = scn_mgr.createLight( 'RedLight' )
    #light.setDiffuseColour( 1, 0, 0 )
    #lightnode = scn_mgr.getRootSceneNode( ).createChildSceneNode( )
    #lightnode.setPosition( 10, -10, 5 )
    #lightnode.attachObject( light )

    cam = scn_mgr.createCamera( 'myCam' )
    cam.setNearClipDistance( 0.5 )
    cam.setAutoAspectRatio( True )
    camnode = scn_mgr.getRootSceneNode( ).createChildSceneNode( )
    camnode.attachObject( cam )

    self.camman = Ogre.Bites.CameraMan( camnode )
    self.camman.setStyle( Ogre.Bites.CS_ORBIT )
    self.camman.setYawPitchDist( 0, 0.3, 15 )
    self.addInputListener( self.camman )

    vp = self.getRenderWindow( ).addViewport( cam )
    vp.setBackgroundColour( ( 0.3, 0.3, 0.3 ) )

    ent = scn_mgr.createEntity( 'Sinbad.mesh' )
    node = scn_mgr.getRootSceneNode( ).createChildSceneNode( )
    node.attachObject( ent )

    #ske = ent.getSkeleton( )
    #for i in range( ske.getNumBones( ) ):
    #  b = ske.getBone( i )
    #  print( b.getName( ) )
    #  b.setManuallyControlled( True )
    # end for

    #ske.getBone( 'Humerus.L' ).pitch( 1 )

    #ent = scn_mgr.createEntity( 'Sword.mesh' )
    #node2 = node.createChildSceneNode( )
    #node2.attachObject( ent )

    

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

## eof - tutorial_01.py
