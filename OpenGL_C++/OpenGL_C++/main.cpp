#include <GL/glew.h>
#include <GLFW/glfw3.h>

int main(void) {
	GLFWwindow *window;

	//initialise glfw
	if (!glfwInit())
	{
		return -1;
	}

	//create a windiws mode and its OpenGL context

	window = glfwCreateWindow(600, 400, "OpenGL and C++ Proyect", NULL, NULL);

	if (!window)
	{
		glfwTerminate();
		return -1;
	}

	//Make window's context current

	//loop intil the user closes the window
	while (! glfwWindowShouldClose(window))
	{
		glClear(GL_COLOR_BUFFER_BIT);
		//render the open gl here

		//sweap front and back buffers
		glfwSwapBuffers(window);
		//poll for and process events

		glfwPollEvents();
	}
}