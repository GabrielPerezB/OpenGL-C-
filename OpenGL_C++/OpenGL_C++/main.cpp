#include <GL/glew.h>
#include <GLFW/glfw3.h>
#include <GL/glut.h>
#include <math.h>
#include <iostream>
#include <cstring>

#define M_PI       3.14159265358979323846   // pi
#define SCREEN_WIDTH 800
#define SCREEN_HEIGHT 600


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

GLfloat xRotated, yRotated, zRotated;
GLdouble radius = 1;
/*
	max x = -350        max y = 250                 min x =     350                     min y = -250
*/
int positionX = 0;
int positionY = 0;
int option = -1;

void redisplayFunc(void)
{

	glMatrixMode(GL_MODELVIEW);
	glViewport(positionX,positionY,SCREEN_WIDTH,SCREEN_HEIGHT);
	// clear the drawing buffer.
	glClear(GL_COLOR_BUFFER_BIT);

	// clear the identity matrix.
	glLoadIdentity();

	// traslate the draw by z = -4.0
	// Note this when you decrease z like -8.0 the drawing will looks far , or smaller.
	glTranslatef(0.0, 0.0, -20.0);

	// Red color used to draw.
	glColor3f(0.8, 0.2, 0.1);//0.8, 0.2, 0.1

	// changing in transformation matrix.
	// rotation about X axis
	glRotatef(xRotated, 1.0, 0.0, 0.0);
	// rotation about Y axis
	glRotatef(yRotated, 0.0, 1.0, 0.0);
	// rotation about Z axis
	glRotatef(zRotated, 0.0, 0.0, 1.0);

	// scaling transfomation 
	glScalef(1.0, 1.0, 1.0);

	// built-in (glut library) function , draw you a sphere.
	glutSolidSphere(radius, 20, 20);

	// Flush buffers to screen
	glFlush();
	// sawp buffers called because we are using double buffering 
	 glutSwapBuffers();
}

void reshapeFunc(int x, int y)
{
	if (y == 0 || x == 0) return;  //Nothing is visible then, so return
								   //Set a new projection matrix
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	//Angle of view:40 degrees
	//Near clipping plane distance: 0.5
	//Far clipping plane distance: 20.0

	gluPerspective(40.0, (GLdouble)x / (GLdouble)y, 0.5, 20.0);
	glMatrixMode(GL_MODELVIEW);
	glViewport(positionX, positionY, x, y);  //Use the whole window for rendering
}

void idleFunc(void)
{
	if (option == 0)
	{
		yRotated -= 0.1;
	}
	if (option == 1)
	{
		yRotated += 0.1;
	}
	if (option == 2)
	{
		xRotated -= 0.1;
	}
	if (option == 3)
	{
		xRotated += 0.1;
	}
	redisplayFunc();
}

void joystick(unsigned int buttonmask, int x, int y, int z)
{


	if (buttonmask & GLUT_JOYSTICK_BUTTON_D) {
		xRotated = 270;
		option = 0;
		if (positionX - 5 >= -350) {
			positionX -= 5;
		}
	}
	if (buttonmask & GLUT_JOYSTICK_BUTTON_A) {
		yRotated = 270;
		option = 2;
		if (positionY + 5 <= 250)
		{
			positionY += 5;
		}
	}

	if (buttonmask & GLUT_JOYSTICK_BUTTON_B) {
		xRotated = 270;
		option = 1;
		if (positionX + 5 <= 350)
		{
			positionX += 5;
		}
	}

	if (buttonmask & GLUT_JOYSTICK_BUTTON_C) {
		yRotated = 270;
		option = 3;
		if (positionY - 5 >= -250)
		{
			positionY -= 5;
		}
	}
}

void keyboard(int key, int x, int y)
{
	switch (key)
	{
	case 100:
		//left
		printf("button pressed: left \n");
		xRotated = 270;
		option = 0;
		if (positionX - 5 >= -350) {
			positionX -= 5;
		}
		break;
	case 101:
		//up
		printf("button pressed: up \n");
		yRotated = 270;
		option = 2;
		if (positionY + 5 <=250)
		{
			positionY += 5;
		}
		break;
	case 102:
		//right
		printf("button pressed: right \n");
		xRotated = 270;
		option = 1;
		if (positionX + 5 <= 350)
		{
			positionX += 5;
		}
		break;
	case 103:
		//down
		printf("button pressed: down \n");
		yRotated = 270;
		option = 3;
		if (positionY-5 >=-250)
		{
			positionY -= 5;
		}
		break;
	case 32:
		//space
		printf("button pressed: space \n");
		exit(0);
		break;
	}

}


///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
int main( int argc, char **argv) {
	

	//Initialize GLUT
	glutInit(&argc, argv);
	//double buffering used to avoid flickering problem in animation
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB); 
	// window size
	glutInitWindowSize(SCREEN_WIDTH, SCREEN_HEIGHT);
	// create the window 
	glutCreateWindow("OpenGL and C++ Proyect");
	glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);
	xRotated = yRotated = zRotated = 0;//30.0
	xRotated = 0;//33
	yRotated = 0;//40
	glClearColor(0.2, 0.2, 0.2, 0.2); 
	//Assign  the function used in events
	glutDisplayFunc(redisplayFunc);
	glutReshapeFunc(reshapeFunc);
	glutIdleFunc(idleFunc);
	//glutSpecialFunc(keyboard);
	glutJoystickFunc(joystick,25);
	//Let start glut loop
	glutMainLoop(); 
	
	return 0;
}