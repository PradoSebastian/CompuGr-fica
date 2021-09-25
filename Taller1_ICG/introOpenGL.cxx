// =========================================================================
// Taller 1 - Introd. Computación Gráfica
// @author Juan Sebastián Prado Valero
// =========================================================================

// =========================================================================
// Plantilla creada por:
// =========================================================================
// @author Andrea Rueda-Olarte (rueda-andrea@javeriana.edu.co )
// @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co )
// =========================================================================
// compilation: g++ -std=c++17 introOpenGL.cxx -lglut -lGLU -lGL
// =========================================================================

#include <GL/freeglut.h>
#include <GL/gl.h>

// -------------------------------------------------------------------------
void myInit( )
{
  glClearColor( 0.0, 0.0, 0.0, 0.0 );
  glMatrixMode( GL_PROJECTION );
  glLoadIdentity( );
  gluOrtho2D( 0, 640, 0, 480 );
}

// -------------------------------------------------------------------------
void myDisplay( )
{
  glClear( GL_COLOR_BUFFER_BIT );
  glPointSize(20.0);
  //glEnable(GL_POINT_SMOOTH);
  glBegin( GL_POINTS );
  {
    
    // Color: RGB(255,241,218)  --------------------------------------------
    glColor3f( 1.0, 0.945, 0.855);
    
    glVertex2i(210.0,550.0);
    glVertex2i(230.0,550.0);
    glVertex2i(250.0,550.0);
    glVertex2i(270.0,550.0);
    glVertex2i(290.0,550.0);
    glVertex2i(310.0,550.0);
    glVertex2i(330.0,550.0);
    glVertex2i(350.0,550.0);
    glVertex2i(370.0,550.0);
    glVertex2i(390.0,550.0);
    glVertex2i(170.0,530.0);
    glVertex2i(190.0,530.0);
    glVertex2i(210.0,530.0);
    glVertex2i(390.0,530.0);
    glVertex2i(410.0,530.0);
    glVertex2i(430.0,530.0);
    glVertex2i(150.0,510.0);
    glVertex2i(170.0,510.0);
    glVertex2i(190.0,510.0);
    glVertex2i(450.0,510.0);
    glVertex2i(130.0,490.0);
    glVertex2i(150.0,490.0);
    glVertex2i(170.0,490.0);
    glVertex2i(190.0,490.0);
    glVertex2i(210.0,490.0);
    glVertex2i(470.0,490.0);
    glVertex2i(110.0,470.0);
    glVertex2i(130.0,470.0);
    glVertex2i(150.0,470.0);
    glVertex2i(170.0,470.0);
    glVertex2i(190.0,470.0);
    glVertex2i(210.0,470.0);
    glVertex2i(490.0,470.0);
    glVertex2i(90.0,450.0);
    glVertex2i(110.0,450.0);
    glVertex2i(130.0,450.0);
    glVertex2i(150.0,450.0);
    glVertex2i(170.0,450.0);
    glVertex2i(190.0,450.0);
    glVertex2i(510.0,450.0);
    glVertex2i(70.0,430.0);
    glVertex2i(90.0,430.0);
    glVertex2i(130.0,430.0);
    glVertex2i(150.0,430.0);
    glVertex2i(170.0,430.0);
    glVertex2i(530.0,430.0);
    glVertex2i(70.0,410.0);
    glVertex2i(130.0,410.0);
    glVertex2i(530.0,410.0);
    glVertex2i(70.0,390.0);
    glVertex2i(50.0,370.0);
    glVertex2i(50.0,350.0);
    glVertex2i(50.0,330.0);
    glVertex2i(50.0,310.0);
    glVertex2i(50.0,290.0);
    glVertex2i(50.0,270.0);
    glVertex2i(50.0,250.0);
    glVertex2i(50.0,230.0);
    glVertex2i(70.0,210.0);

    // ---------------------------------------------------------------------

    // Color: RGB(255,236,196)  --------------------------------------------
    glColor3f( 1.0, 0.925, 0.767);

    glVertex2i(210.0,450.0);
    glVertex2i(190.0,430.0);
    glVertex2i(210.0,430.0);
    glVertex2i(170.0,410.0);
    glVertex2i(190.0,410.0);
    glVertex2i(210.0,410.0);

    // ---------------------------------------------------------------------

    // Color: RGB(255,216,131)  --------------------------------------------
    glColor3f( 1.0, 0.847, 0.514);

    glVertex2i(230.0,450.0);
    glVertex2i(230.0,430.0);

    // ---------------------------------------------------------------------

    // Color: RGB(255,242,222)  --------------------------------------------
    glColor3f( 1.0, 0.949, 0.871);

    glVertex2i(150.0,390.0);
    glVertex2i(130.0,370.0);
    glVertex2i(150.0,370.0);

    // ---------------------------------------------------------------------

    // Color: RGB(255,166,9)  --------------------------------------------
    glColor3f( 1.0, 0.651, 0.035);

    glVertex2i(230.0,530.0);
    glVertex2i(250.0,530.0);
    glVertex2i(270.0,530.0);
    glVertex2i(290.0,530.0);
    glVertex2i(310.0,530.0);
    glVertex2i(330.0,530.0);
    glVertex2i(350.0,530.0);
    glVertex2i(370.0,530.0);
    glVertex2i(390.0,510.0);
    glVertex2i(410.0,510.0);
    glVertex2i(430.0,510.0);
    glVertex2i(390.0,490.0);
    glVertex2i(410.0,490.0);
    glVertex2i(430.0,490.0);
    glVertex2i(450.0,490.0);
    glVertex2i(450.0,470.0);
    glVertex2i(470.0,470.0);
    glVertex2i(470.0,450.0);
    glVertex2i(490.0,450.0);
    glVertex2i(110.0,430.0);
    glVertex2i(490.0,430.0);
    glVertex2i(510.0,430.0);
    glVertex2i(90.0,410.0);
    glVertex2i(110.0,410.0);
    glVertex2i(510.0,410.0);
    glVertex2i(90.0,390.0);
    glVertex2i(510.0,390.0);
    glVertex2i(530.0,390.0);
    glVertex2i(70.0,370.0);
    glVertex2i(530.0,370.0);
    glVertex2i(70.0,350.0);
    glVertex2i(530.0,350.0);
    glVertex2i(70.0,330.0);
    glVertex2i(530.0,330.0);
    glVertex2i(70.0,310.0);
    glVertex2i(530.0,310.0);
    glVertex2i(70.0,290.0);
    glVertex2i(530.0,290.0);
    glVertex2i(70.0,270.0);
    glVertex2i(530.0,270.0);
    glVertex2i(70.0,250.0);
    glVertex2i(530.0,250.0);
    glVertex2i(70.0,230.0);
    glVertex2i(510.0,230.0);
    glVertex2i(530.0,230.0);
    glVertex2i(90.0,210.0);
    glVertex2i(510.0,210.0);
    glVertex2i(530.0,210.0);
    glVertex2i(90.0,190.0);
    glVertex2i(490.0,190.0);
    glVertex2i(510.0,190.0);
    glVertex2i(90.0,170.0);
    glVertex2i(110.0,170.0);
    glVertex2i(470.0,170.0);
    glVertex2i(490.0,170.0);
    glVertex2i(510.0,170.0);
    glVertex2i(110.0,150.0);
    glVertex2i(130.0,150.0);
    glVertex2i(450.0,150.0);
    glVertex2i(470.0,150.0);
    glVertex2i(490.0,150.0);
    glVertex2i(130.0,130.0);
    glVertex2i(150.0,130.0);
    glVertex2i(430.0,130.0);
    glVertex2i(450.0,130.0);
    glVertex2i(470.0,130.0);
    glVertex2i(150.0,110.0);
    glVertex2i(170.0,110.0);
    glVertex2i(190.0,110.0);
    glVertex2i(390.0,110.0);
    glVertex2i(410.0,110.0);
    glVertex2i(430.0,110.0);
    glVertex2i(450.0,110.0);
    glVertex2i(170.0,90.0);
    glVertex2i(190.0,90.0);
    glVertex2i(210.0,90.0);
    glVertex2i(230.0,90.0);
    glVertex2i(250.0,90.0);
    glVertex2i(270.0,90.0);
    glVertex2i(290.0,90.0);
    glVertex2i(310.0,90.0);
    glVertex2i(330.0,90.0);
    glVertex2i(350.0,90.0);
    glVertex2i(370.0,90.0);
    glVertex2i(390.0,90.0);
    glVertex2i(410.0,90.0);
    glVertex2i(210.0,70.0);
    glVertex2i(230.0,70.0);
    glVertex2i(250.0,70.0);
    glVertex2i(270.0,70.0);
    glVertex2i(290.0,70.0);
    glVertex2i(310.0,70.0);
    glVertex2i(330.0,70.0);
    glVertex2i(350.0,70.0);
    glVertex2i(370.0,70.0);

    // ---------------------------------------------------------------------

    // Color: RGB(255,146,0)  --------------------------------------------
    glColor3f( 1.0, 0.572, 0.0);

    glVertex2i(210.0,510.0);
    glVertex2i(230.0,510.0);
    glVertex2i(250.0,510.0);
    glVertex2i(270.0,510.0);
    glVertex2i(290.0,510.0);
    glVertex2i(310.0,510.0);
    glVertex2i(330.0,510.0);
    glVertex2i(350.0,510.0);
    glVertex2i(370.0,510.0);
    glVertex2i(230.0,490.0);
    glVertex2i(250.0,490.0);
    glVertex2i(270.0,490.0);
    glVertex2i(290.0,490.0);
    glVertex2i(310.0,490.0);
    glVertex2i(330.0,490.0);
    glVertex2i(350.0,490.0);
    glVertex2i(370.0,490.0);
    glVertex2i(270.0,470.0);
    glVertex2i(290.0,470.0);
    glVertex2i(310.0,470.0);
    glVertex2i(330.0,470.0);
    glVertex2i(410.0,470.0);
    glVertex2i(430.0,470.0);
    glVertex2i(370.0,450.0);
    glVertex2i(390.0,450.0);
    glVertex2i(410.0,450.0);
    glVertex2i(430.0,450.0);
    glVertex2i(450.0,450.0);
    glVertex2i(370.0,430.0);
    glVertex2i(390.0,430.0);
    glVertex2i(410.0,430.0);
    glVertex2i(430.0,430.0);
    glVertex2i(390.0,410.0);
    glVertex2i(410.0,410.0);
    glVertex2i(430.0,410.0);
    glVertex2i(110.0,390.0);
    glVertex2i(410.0,390.0);
    glVertex2i(430.0,390.0);
    glVertex2i(450.0,390.0);
    glVertex2i(90.0,370.0);
    glVertex2i(110.0,370.0);
    glVertex2i(410.0,370.0);
    glVertex2i(430.0,370.0);
    glVertex2i(450.0,370.0);
    glVertex2i(90.0,350.0);
    glVertex2i(110.0,350.0);
    glVertex2i(410.0,350.0);
    glVertex2i(430.0,350.0);
    glVertex2i(450.0,350.0);
    glVertex2i(90.0,330.0);
    glVertex2i(110.0,330.0);
    glVertex2i(410.0,330.0);
    glVertex2i(430.0,330.0);
    glVertex2i(450.0,330.0);
    glVertex2i(90.0,310.0);
    glVertex2i(110.0,310.0);
    glVertex2i(370.0,310.0);
    glVertex2i(410.0,310.0);
    glVertex2i(430.0,310.0);
    glVertex2i(90.0,290.0);
    glVertex2i(110.0,290.0);
    glVertex2i(130.0,290.0);
    glVertex2i(410.0,290.0);
    glVertex2i(430.0,290.0);
    glVertex2i(110.0,270.0);
    glVertex2i(130.0,270.0);
    glVertex2i(350.0,270.0);
    glVertex2i(390.0,270.0);
    glVertex2i(410.0,270.0);
    glVertex2i(430.0,270.0);
    glVertex2i(130.0,250.0);
    glVertex2i(150.0,250.0);
    glVertex2i(430.0,250.0);
    glVertex2i(150.0,230.0);
    glVertex2i(170.0,230.0);
    glVertex2i(190.0,230.0);
    glVertex2i(310.0,230.0);
    glVertex2i(330.0,230.0);
    glVertex2i(410.0,230.0);
    glVertex2i(170.0,210.0);
    glVertex2i(190.0,210.0);
    glVertex2i(210.0,210.0);
    glVertex2i(250.0,210.0);
    glVertex2i(290.0,210.0);
    glVertex2i(310.0,210.0);
    glVertex2i(330.0,210.0);
    glVertex2i(370.0,210.0);
    glVertex2i(210.0,190.0);
    glVertex2i(230.0,190.0);
    glVertex2i(250.0,190.0);
    glVertex2i(270.0,190.0);
    glVertex2i(290.0,190.0);
    glVertex2i(310.0,190.0);
    glVertex2i(330.0,190.0);
    glVertex2i(350.0,190.0);
    glVertex2i(190.0,170.0);
    glVertex2i(210.0,170.0);
    glVertex2i(250.0,170.0);
    glVertex2i(270.0,170.0);
    glVertex2i(290.0,170.0);
    glVertex2i(310.0,170.0);

    // ---------------------------------------------------------------------
    
    // Color: RGB(255,177,10)  --------------------------------------------
    glColor3f( 1.0, 0.694, 0.039);

    glVertex2i(230.0,470.0);
    glVertex2i(250.0,470.0);
    glVertex2i(350.0,470.0);
    glVertex2i(370.0,470.0);
    glVertex2i(390.0,470.0);
    glVertex2i(250.0,450.0);
    glVertex2i(270.0,450.0);
    glVertex2i(290.0,450.0);
    glVertex2i(310.0,450.0);
    glVertex2i(330.0,450.0);
    glVertex2i(350.0,450.0);
    glVertex2i(250.0,430.0);
    glVertex2i(270.0,430.0);
    glVertex2i(290.0,430.0);
    glVertex2i(310.0,430.0);
    glVertex2i(330.0,430.0);
    glVertex2i(350.0,430.0);
    glVertex2i(150.0,410.0);
    glVertex2i(250.0,410.0);
    glVertex2i(270.0,410.0);
    glVertex2i(290.0,410.0);
    glVertex2i(310.0,410.0);
    glVertex2i(330.0,410.0);
    glVertex2i(370.0,410.0);
    glVertex2i(130.0,390.0);
    glVertex2i(170.0,390.0);
    glVertex2i(190.0,390.0);
    glVertex2i(210.0,390.0);
    glVertex2i(250.0,390.0);
    glVertex2i(270.0,390.0);
    glVertex2i(290.0,390.0);
    glVertex2i(310.0,390.0);
    glVertex2i(330.0,390.0);
    glVertex2i(370.0,390.0);
    glVertex2i(390.0,390.0);
    glVertex2i(170.0,370.0);
    glVertex2i(290.0,370.0);
    glVertex2i(130.0,350.0);
    glVertex2i(150.0,350.0);
    glVertex2i(170.0,350.0);
    glVertex2i(190.0,350.0);
    glVertex2i(270.0,350.0);
    glVertex2i(290.0,350.0);
    glVertex2i(310.0,350.0);
    glVertex2i(390.0,350.0);
    glVertex2i(130.0,330.0);
    glVertex2i(150.0,330.0);
    glVertex2i(170.0,330.0);
    glVertex2i(190.0,330.0);
    glVertex2i(230.0,330.0);
    glVertex2i(270.0,330.0);
    glVertex2i(290.0,330.0);
    glVertex2i(310.0,330.0);
    glVertex2i(350.0,330.0);
    glVertex2i(390.0,330.0);
    glVertex2i(130.0,310.0);
    glVertex2i(150.0,310.0);
    glVertex2i(170.0,310.0);
    glVertex2i(190.0,310.0);
    glVertex2i(210.0,310.0);
    glVertex2i(230.0,310.0);
    glVertex2i(250.0,310.0);
    glVertex2i(270.0,310.0);
    glVertex2i(290.0,310.0);
    glVertex2i(310.0,310.0);
    glVertex2i(330.0,310.0);
    glVertex2i(350.0,310.0);
    glVertex2i(390.0,310.0);
    glVertex2i(150.0,290.0);
    glVertex2i(170.0,290.0);
    glVertex2i(190.0,290.0);
    glVertex2i(210.0,290.0);
    glVertex2i(230.0,290.0);
    glVertex2i(270.0,290.0);
    glVertex2i(290.0,290.0);
    glVertex2i(310.0,290.0);
    glVertex2i(330.0,290.0);
    glVertex2i(350.0,290.0);
    glVertex2i(390.0,290.0);
    glVertex2i(150.0,270.0);
    glVertex2i(170.0,270.0);
    glVertex2i(190.0,270.0);
    glVertex2i(210.0,270.0);
    glVertex2i(230.0,270.0);
    glVertex2i(270.0,270.0);
    glVertex2i(290.0,270.0);
    glVertex2i(310.0,270.0);
    glVertex2i(330.0,270.0);
    glVertex2i(170.0,250.0);
    glVertex2i(190.0,250.0);
    glVertex2i(310.0,250.0);
    glVertex2i(210.0,230.0);
    glVertex2i(290.0,230.0);

    // ---------------------------------------------------------------------

    // Color: RGB(230,94,0)  --------------------------------------------
    glColor3f( 0.902, 0.037, 0.0);

    glVertex2i(450.0,430.0);
    glVertex2i(450.0,410.0);
    glVertex2i(470.0,410.0);
    glVertex2i(470.0,390.0);
    glVertex2i(470.0,370.0);
    glVertex2i(470.0,350.0);
    glVertex2i(470.0,330.0);
    glVertex2i(450.0,310.0);
    glVertex2i(470.0,310.0);
    glVertex2i(450.0,290.0);
    glVertex2i(470.0,290.0);
    glVertex2i(450.0,270.0);
    glVertex2i(470.0,270.0);
    glVertex2i(450.0,250.0);
    glVertex2i(470.0,250.0);
    glVertex2i(130.0,230.0);
    glVertex2i(430.0,230.0);
    glVertex2i(450.0,230.0);
    glVertex2i(130.0,210.0);
    glVertex2i(150.0,210.0);
    glVertex2i(410.0,210.0);
    glVertex2i(430.0,210.0);
    glVertex2i(450.0,210.0);
    glVertex2i(150.0,190.0);
    glVertex2i(170.0,190.0);
    glVertex2i(190.0,190.0);
    glVertex2i(370.0,190.0);
    glVertex2i(390.0,190.0);
    glVertex2i(410.0,190.0);
    glVertex2i(430.0,190.0);
    glVertex2i(170.0,170.0);
    glVertex2i(230.0,170.0);
    glVertex2i(330.0,170.0);
    glVertex2i(350.0,170.0);
    glVertex2i(370.0,170.0);
    glVertex2i(390.0,170.0);
    glVertex2i(410.0,170.0);
    glVertex2i(190.0,150.0);
    glVertex2i(210.0,150.0);
    glVertex2i(230.0,150.0);
    glVertex2i(250.0,150.0);
    glVertex2i(270.0,150.0);
    glVertex2i(290.0,150.0);
    glVertex2i(310.0,150.0);
    glVertex2i(330.0,150.0);
    glVertex2i(350.0,150.0);
    glVertex2i(370.0,150.0);
    glVertex2i(390.0,150.0);
    glVertex2i(210.0,130.0);
    glVertex2i(230.0,130.0);
    glVertex2i(250.0,130.0);
    glVertex2i(270.0,130.0);
    glVertex2i(290.0,130.0);
    glVertex2i(310.0,130.0);
    glVertex2i(330.0,130.0);
    glVertex2i(350.0,130.0);

    // ---------------------------------------------------------------------

    // Color: RGB(255,109,0)  --------------------------------------------
    glColor3f( 1.0, 0.427, 0.0);

    glVertex2i(470.0,430.0);
    glVertex2i(490.0,410.0);
    glVertex2i(490.0,390.0);
    glVertex2i(490.0,370.0);
    glVertex2i(510.0,370.0);
    glVertex2i(490.0,350.0);
    glVertex2i(510.0,350.0);
    glVertex2i(490.0,330.0);
    glVertex2i(510.0,330.0);
    glVertex2i(490.0,310.0);
    glVertex2i(510.0,310.0);
    glVertex2i(490.0,290.0);
    glVertex2i(510.0,290.0);
    glVertex2i(90.0,270.0);
    glVertex2i(490.0,270.0);
    glVertex2i(510.0,270.0);
    glVertex2i(90.0,250.0);
    glVertex2i(110.0,250.0);
    glVertex2i(490.0,250.0);
    glVertex2i(510.0,250.0);
    glVertex2i(90.0,230.0);
    glVertex2i(110.0,230.0);
    glVertex2i(470.0,230.0);
    glVertex2i(490.0,230.0);
    glVertex2i(110.0,210.0);
    glVertex2i(470.0,210.0);
    glVertex2i(490.0,210.0);
    glVertex2i(110.0,190.0);
    glVertex2i(130.0,190.0);
    glVertex2i(450.0,190.0);
    glVertex2i(470.0,190.0);
    glVertex2i(130.0,170.0);
    glVertex2i(150.0,170.0);
    glVertex2i(430.0,170.0);
    glVertex2i(450.0,170.0);
    glVertex2i(150.0,150.0);
    glVertex2i(170.0,150.0);
    glVertex2i(410.0,150.0);
    glVertex2i(430.0,150.0);
    glVertex2i(170.0,130.0);
    glVertex2i(190.0,130.0);
    glVertex2i(370.0,130.0);
    glVertex2i(390.0,130.0);
    glVertex2i(410.0,130.0);
    glVertex2i(210.0,110.0);
    glVertex2i(230.0,110.0);
    glVertex2i(250.0,110.0);
    glVertex2i(270.0,110.0);
    glVertex2i(290.0,110.0);
    glVertex2i(310.0,110.0);
    glVertex2i(330.0,110.0);
    glVertex2i(350.0,110.0);
    glVertex2i(370.0,110.0);

    // ---------------------------------------------------------------------

    // Color: RGB(140,4,0)  --------------------------------------------
    glColor3f( 0.579, 0.016, 0.0);

    glVertex2i(230.0,410.0);
    glVertex2i(350.0,410.0);
    glVertex2i(230.0,390.0);
    glVertex2i(350.0,390.0);
    glVertex2i(190.0,370.0);
    glVertex2i(210.0,370.0);
    glVertex2i(230.0,370.0);
    glVertex2i(250.0,370.0);
    glVertex2i(270.0,370.0);
    glVertex2i(310.0,370.0);
    glVertex2i(330.0,370.0);
    glVertex2i(350.0,370.0);
    glVertex2i(370.0,370.0);
    glVertex2i(390.0,370.0);
    glVertex2i(210.0,350.0);
    glVertex2i(230.0,350.0);
    glVertex2i(250.0,350.0);
    glVertex2i(330.0,350.0);
    glVertex2i(350.0,350.0);
    glVertex2i(370.0,350.0);
    glVertex2i(210.0,330.0);
    glVertex2i(250.0,330.0);
    glVertex2i(330.0,330.0);
    glVertex2i(370.0,330.0);
    glVertex2i(250.0,290.0);
    glVertex2i(370.0,290.0);
    glVertex2i(250.0,270.0);
    glVertex2i(370.0,270.0);
    glVertex2i(210.0,250.0);
    glVertex2i(230.0,250.0);
    glVertex2i(250.0,250.0);
    glVertex2i(270.0,250.0);
    glVertex2i(290.0,250.0);
    glVertex2i(330.0,250.0);
    glVertex2i(350.0,250.0);
    glVertex2i(370.0,250.0);
    glVertex2i(390.0,250.0);
    glVertex2i(410.0,250.0);
    glVertex2i(230.0,230.0);
    glVertex2i(250.0,230.0);
    glVertex2i(270.0,230.0);
    glVertex2i(350.0,230.0);
    glVertex2i(370.0,230.0);
    glVertex2i(390.0,230.0);
    glVertex2i(230.0,210.0);
    glVertex2i(270.0,210.0);
    glVertex2i(350.0,210.0);
    glVertex2i(390.0,210.0);

    // ---------------------------------------------------------------------


  }
  glEnd( );
  glFlush( );
}

// -------------------------------------------------------------------------
void myResize( int w, int h )
{
  glViewport( 0, 0, w, h );
  glMatrixMode( GL_PROJECTION );
  glLoadIdentity( );
  gluOrtho2D( 0, w, 0, h );
}

// -------------------------------------------------------------------------
int main( int argc, char** argv )
{
  glutInit( &argc, argv );
  glutInitDisplayMode( GLUT_SINGLE | GLUT_RGB );
  glutInitWindowSize( 600, 600 );
  glutInitWindowPosition( 100, 100 );

  glutCreateWindow( "Taller 1" );

  glutDisplayFunc( myDisplay );
  glutReshapeFunc( myResize );
  myInit( );

  glutMainLoop( );

  return( 0 );
}

// eof - introOpenGL.cxx
