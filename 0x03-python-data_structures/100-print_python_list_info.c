#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - prints basic info about Python lists
 * @p: python object
 */

void print_python_list_info(PyObject *p)
{
	int i, size, alloc;
	PyObject *obj;

	alloc = ((PyListObject *))p->allocated;
	size = Py_SIZE(p);

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		obj = PyList_GetItem(p, i);

		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
