// =========================================================================
// @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
// =========================================================================
// g++ -std=c++17 Scene3D.cxx -lGL -LGLU -lglut -o Scene3D
// =========================================================================

#include <cmath>
#include <GL/gl.h>
#include <GL/glu.h>
#include <GL/glut.h>
#include <math.h>
#include <iostream>

// -------------------------------------------------------------------------
// Some global variables: DON'T DO THIS IN REAL LIFE APPLICATIONS!!!!
// -------------------------------------------------------------------------
double cube_geometry[ 8 ][ 3 ] =
{
  { -1, -1,  1 }, {  1, -1,  1 }, {  1, -1, -1 }, { -1, -1, -1 },
  { -1,  1,  1 }, {  1,  1,  1 }, {  1,  1, -1 }, { -1,  1, -1 }
};

unsigned int cube_topology[ 12 ][ 3 ] =
{
  { 0, 1, 3 }, { 1, 2, 3 },
  { 1, 5, 2 }, { 5, 6, 2 },
  { 4, 7, 5 }, { 7, 6, 5 },
  { 2, 6, 7 }, { 7, 3, 2 },
  { 3, 7, 4 }, { 0, 3, 4 },
  { 1, 0, 4 }, { 1, 4, 5 }
};

float posCamara [3] = {4, 4, 4}; // pos camara
float vista [3] = {0, 0, 0}; // hacia a donde estoy viendo
float normal [3] = {0, 1, 0}; // mi cabeza esta en que direccion hacia arriba

float pi2 = atan( 1.0 ) * 8.0;
float radio = sqrt(pow(posCamara[0], 2) + pow(posCamara[2], 2));
float tetha = acos(posCamara[0] / radio) * 360/pi2;
float phi = acos(posCamara[0] / radio) * 360/pi2;

// -------------------------------------------------------------------------
void init( )
{
  glClearColor( 0.0, 0.0, 0.0, 0.0 );
  glEnable( GL_DEPTH_TEST );
}

// -------------------------------------------------------------------------
void drawOrthoBase( )
{
  glPushMatrix( );

  float cur_color[ 4 ];
  float lw;

  glGetFloatv( GL_CURRENT_COLOR, cur_color );
  glGetFloatv( GL_LINE_WIDTH, &lw );

  glLineWidth( 4 );
  glBegin( GL_LINES );

  glColor3f( 1, 0, 0 );
  glVertex3f( 0, 0, 0 );
  glVertex3f( 1, 0, 0 );

  glColor3f( 0, 1, 0 );
  glVertex3f( 0, 0, 0 );
  glVertex3f( 0, 1, 0 );

  glColor3f( 0, 0, 1 );
  glVertex3f( 0, 0, 0 );
  glVertex3f( 0, 0, 1 );

  glEnd( );

  glColor3fv( cur_color );
  glLineWidth( lw );

  glPopMatrix( );
}

// -------------------------------------------------------------------------
void drawCube( )
{
  glColor3f( 1, 1, 1 );
  for( unsigned int* t: cube_topology )
  {
    glBegin( GL_LINE_LOOP );
    glVertex3dv( cube_geometry[ t[ 0 ] ] );
    glVertex3dv( cube_geometry[ t[ 1 ] ] );
    glVertex3dv( cube_geometry[ t[ 2 ] ] );
    glEnd( );
  } // end for
}

// -------------------------------------------------------------------------
void draw( )
{
  // -- Clear framebuffer
  glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT );

  // -- Draw stuff
  glMatrixMode( GL_MODELVIEW );
  glLoadIdentity( );

  // -- Camera
  gluLookAt(
    posCamara[0], posCamara[1], posCamara[2], // pos camara
    0, 0, 0, // hacia a donde estoy viendo
    0, 1, 0  // mi cabeza esta en que direccion hacia arriba
    );

  // -- Scene
  drawOrthoBase( );
  drawCube( );

  // -- Prepare next frame
  glFlush( );
  glutSwapBuffers( );
}

// -------------------------------------------------------------------------
void reshape( int width, int height )
{
  // Compute aspect ratio of the new window
  double aspect = double( width );
  if( height != 0 )
    aspect /= double( height );

  // Set the viewport to cover the new window
  glViewport( 0, 0, width, height );

  // Compute projection
  glMatrixMode( GL_PROJECTION );
  glLoadIdentity( );
  gluPerspective( 45, aspect, 1e-2, 30 );
  //glOrtho( -5, 5, -5, 5, -10, 10 );
}

void moverCamaraXZ() {

  posCamara[0] = radio * cos(tetha * pi2 / 360);
  posCamara[2] = radio * sin(tetha * pi2 / 360);
  draw();
}

void moverCamaraNormal() {
  posCamara[0] = radio * cos(phi * pi2 / 360);
  posCamara[1] = radio * sin(phi * pi2 / 360);
  draw();
}

void contrEvntTeclado(unsigned char tecla, int x, int y) {

  int angMov = 5;

  switch (tecla)
  {
  case 'a':

    tetha += angMov;
    moverCamaraXZ();
    break;
  
  case 'd':

    tetha -= angMov;
    moverCamaraXZ();
    break;
  
  case 's':
    phi += angMov;
    moverCamaraNormal();
    break;

  case 'w':
    phi -= angMov;
    moverCamaraNormal();
    break;

  default:
    break;
  }
  
}

// -------------------------------------------------------------------------
int main( int argc, char** argv )
{
  // Prepare window
  glutInit( &argc, argv );
  glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH );
  glutInitWindowSize( 700, 700 );
  glutInitWindowPosition( 0, 0 );
  glutCreateWindow( "A simple room" );

  // Prepare OpenGL
  init( );

  // Associate callbacks
  glutDisplayFunc( draw );
  glutReshapeFunc( reshape );

  glutKeyboardFunc(contrEvntTeclado);

  // Main loop
  glutMainLoop( );
  return( EXIT_SUCCESS );
}

// eof - Scene3D.cxx
