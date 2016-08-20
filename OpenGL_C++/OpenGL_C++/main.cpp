#include <GL/glew.h>
#include <GLFW/glfw3.h>
#include <GL/glut.h>
#include <iostream>
#include <cstring>
#include <fstream>
#include <stdlib.h>
using namespace std;

#define SCREEN_WIDTH 800
#define SCREEN_HEIGHT 600


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

GLfloat xRotated, yRotated, zRotated;
GLdouble radius = 1;


fstream fArchive("Data.txt", ios::in | ios::out | ios::binary);
void menu() {
	
	printf("\n -> Press X to save position");
	printf("\n -> Press SQUARE to delete data");
	printf("\n -> Press CIRCLE to do the travel");
	printf("\n -> Press TRIANGLE to exit \n \n");

}

/*
	max x = -350        max y = 250                 min x =     350                     min y = -250
*/
int positionX = 0;
int positionY = 0;
int option = -1;

//struct used to be saved in the data file
struct data {
public:
	int savedPositionX;
	int savedPositionY;

	data() {
		savedPositionX = -1;
		savedPositionY = -1;
	}

}regData;


void createAFile() {
	fstream fArchive("Data.txt", ios::in | ios::out | ios::binary | ios::trunc );
}

//Function to save the position x and y in the data file, whith a struct format
void writeInFile() {
	regData.savedPositionX = positionX;
	regData.savedPositionY = positionY;
	fArchive.seekg(0, ios::end);
	fArchive.write(reinterpret_cast<char *> (&regData), sizeof(regData));
	printf("Position saved \n");
}



void idleFunc();

//function that recives a position x and a position y to move the sphere
void autoMove(int x, int y) {

	do{

		if (x > positionX)
		{
			positionX++;
		}
		if (x < positionX)
		{
			if (positionX ==0)
			{
				positionX = -1;
			}
			else
			{
				positionX--;
			}
		}
		if (y > positionY)
		{
			positionY++;
		}
		if (y < positionY)
		{
			if (positionY == 0)
			{
				positionY = -1;
			}
			else
			{
				positionY--;
			}
		}
		idleFunc();
		if (positionX == x && positionY == y)
		{
			return;
		}
	} while (true);

}

//fucntion to read the data file and call the automove Function
void readInFile() {
	system("cls");
	menu();
	int index = 0;
	fArchive.seekg(0, ios::end);
	int indexStop = fArchive.tellg();
	fstream fArchiveTemp("Data.txt", ios::in | ios::out | ios::binary);
	fArchiveTemp.seekg(0);
	do {
		fArchiveTemp.read(reinterpret_cast<char *> (&regData), sizeof(regData));
		if (regData.savedPositionX == -1 && regData.savedPositionY == -1) {
			printf("Track not saved \n");
			return;
		}
		cout << "Position X,    Position Y    " << endl;
		cout <<regData.savedPositionX << endl;
		cout <<regData.savedPositionY << endl;
		index += sizeof(regData);
		autoMove(regData.savedPositionX, regData.savedPositionY);
	} while (index < indexStop);

}

//Function to overwrite the data file 
void deleteDataInFile() {
	fstream fArchive("Data.txt", ios::in | ios::out | ios::binary | ios::trunc);
	regData.savedPositionX = -1;
	regData.savedPositionY = -1;
	system("cls");
	menu();
	printf("Data deleted \n");
}


//function to show the sphere in the projection matrix
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

	// Orange color used to draw.
	glColor3f(1.0 ,0.3, 0.0);
	
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

//function to create a projection matrix
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

//Function tho change the sphere's rotation direction
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
	if (option == 4)
	{
		yRotated, xRotated = 270;
	}
	redisplayFunc();
}

void joystick(unsigned int buttonmask, int x, int y, int z)
{
	
	
	int buttonCount;
	const unsigned char *buttons = glfwGetJoystickButtons(GLFW_JOYSTICK_1, &buttonCount);

	if (GLFW_RELEASE == buttons[0] ) {
		option = 4;
	}

	if (GLFW_PRESS == buttons[0]) {
		// button X
		writeInFile();
	}
	if (GLFW_PRESS == buttons[1]) {
		// button circle
		deleteDataInFile();
	}
	if (GLFW_PRESS == buttons[2]) {
		// button square
		readInFile();
	}
	if (GLFW_PRESS == buttons[3]) {
		// button tringle
		exit(0);
	}

	
	int axesCount;
	const float *axes = glfwGetJoystickAxes(GLFW_JOYSTICK_1, &axesCount);

	
	if (GLFW_PRESS == axes[0] ) {
		//move right 
		xRotated = 270;
		option = 1;
		if (positionX + 5 <= 350)
		{
			positionX += 5;
		}
	}
	if (GLFW_PRESS == axes[1]) {
		//move down		
		yRotated = 270;
		option = 3;
		if (positionY - 5 >= -250)
		{
			positionY -= 5;
		}
	}
	if (GLFW_PRESS == axes[2]) {
		//move up
		yRotated = 270;
		option = 2;
		if (positionY + 5 <= 250)
		{
			positionY += 5;
		}
	}
	if (GLFW_PRESS == axes[3]) {
		//move left
		xRotated = 270;
		option = 0;
		if (positionX - 5 >= -350) {
			positionX -= 5;
		}
	}


}

void keyboard(int key, int x, int y)
{
	switch (key)
	{
	case 100:
		//arrow left
		xRotated = 270;
		option = 0;
		if (positionX - 5 >= -350) {
			positionX -= 5;
		}
		break;

	case 101:
		//arrow up
		yRotated = 270;
		option = 2;
		if (positionY + 5 <= 250)
		{
			positionY += 5;
		}
		break;

	case 102:
		//arrow right
		xRotated = 270;
		option = 1;
		if (positionX + 5 <= 350)
		{
			positionX += 5;
		}
		break;

	case 103:
		//arrow down
		yRotated = 270;
		option = 3;
		if (positionY - 5 >= -250)
		{
			positionY -= 5;
		}
		break;
	}
}



///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
int main( int argc, char **argv) {
	
	if (!fArchive)
	{
		createAFile();
	}

	//Initialize GLUT
	glutInit(&argc, argv);
	//double buffering used to avoid flickering problem in animation
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB); 
	// window size
	glutInitWindowSize(SCREEN_WIDTH, SCREEN_HEIGHT);
	// create the window 
	glutCreateWindow("OpenGL and C++ Proyect");
	glPolygonMode(GL_FRONT_AND_BACK, GL_LINE);
	
	xRotated = yRotated = zRotated = 0;
	xRotated = 0;
	yRotated = 0;
	glClearColor( 0.563, 0.763, 0.500, 0.500);
	//Assign  the function used in events
	glutDisplayFunc(redisplayFunc);

	glutReshapeFunc(reshapeFunc);

	glutIdleFunc(idleFunc);

	//Function to catch the keyboard's buttons 
	glutSpecialFunc(keyboard);

	glfwInit();

	//Function to catch the joystick's buttons 
	glutJoystickFunc(joystick,100);

	system("cls");
	menu();

	//Let start glut loop
	glutMainLoop(); 

}