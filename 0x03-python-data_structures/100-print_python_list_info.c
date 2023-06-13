#include <Python.h>

/**
 * print_python_list_info - prints some basic info
 * @p: pointer
 */
void print_python_list_info(PyObject *p)
{
	int s, a, i;
	PyObject *o;

	s = Py_SIZE(p);
	a = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", s);
	printf("[*] Allocated = %d\n", a);
	for (i = 0; i < s; i++)
	{
		printf("Element %d: ", i);

		o = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(o)->tp_name);
	}
}
