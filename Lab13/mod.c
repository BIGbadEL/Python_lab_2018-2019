#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdlib.h>
#include "sort.h"
#include "nwd.h"
#include "srednia.h"

static PyObject *mod_met(PyObject *self, PyObject *args){
	int a=0,b=0;
	int c = 0;

	if(!PyArg_ParseTuple(args, "i|ii", &a, &b, &c)){ //jezeli do stringa wstawi sie | to po sa opcjonalne
		//docs.python.org/3.5/c-pi/arg.html
		//docs.python.org/3.5/c-api/concrete.html
		//docs.python.org/3.5/c-api/object.html
		//docs.python.org/3.5/c-api/exceptions.html
		return NULL;	//zwracane w przypadku bledu; interpreter zglasza wyjatek wywolania funkcji
	}
	//Py_RETURN_NONE; //jesli nic nie zwraca
	return Py_BuildValue("i", a+b+ c);
}

static PyObject *mod_mysort(PyObject *self, PyObject *args){
	int size = 0;
	PyObject *list;
	if(!PyArg_ParseTuple(args, "O", &list)){ //jezeli do stringa wstawi sie | to po sa opcjonalne
		//docs.python.org/3.5/c-pi/arg.html
		//docs.python.org/3.5/c-api/concrete.html
		//docs.python.org/3.5/c-api/object.html
		//docs.python.org/3.5/c-api/exceptions.html
		return NULL;	//zwracane w przypadku bledu; interpreter zglasza wyjatek wywolania funkcji
	}
	size = PyList_GET_SIZE(list);
	int * tab = (int*) malloc(sizeof(int) * size);

	for(int i = 0; i < size; i++){
		tab[i] = PyLong_AsLong(PyList_GetItem(list, i));
	}

	mysort(tab, size);
	for(int i = 0; i < size; i++){
		PyList_SetItem(list, i, PyLong_FromLong(tab[i]));
	}
	free(tab);
	//Py_RETURN_NONE; //jesli nic nie zwraca
	return Py_BuildValue("O", list);
}

static PyObject *mod_mynwd(PyObject *self, PyObject *args){
	PyObject *d;
	if(!PyArg_ParseTuple(args, "O", &d)){ //jezeli do stringa wstawi sie | to po sa opcjonalne
		//docs.python.org/3.5/c-pi/arg.html
		//docs.python.org/3.5/c-api/concrete.html
		//docs.python.org/3.5/c-api/object.html
		//docs.python.org/3.5/c-api/exceptions.html
		return NULL;	//zwracane w przypadku bledu; interpreter zglasza wyjatek wywolania funkcji
	}
	int size = PyDict_Size(d);
	PyObject* result = PyTuple_New(size);
	PyObject *key, *value;
	Py_ssize_t pos = 0;

	while (PyDict_Next(d, &pos, &key, &value)) {
		int temp = mynwd(PyLong_AsLong(key), PyLong_AsLong(value));
		PyTuple_SetItem(result, pos - 1, PyLong_FromLong(temp));
	}

	//Py_RETURN_NONE; //jesli nic nie zwraca
	return Py_BuildValue("O", result);
}

static PyObject *mod_sednia(PyObject *self, PyObject *args){
	int size = 0;
	PyObject *list;
	if(!PyArg_ParseTuple(args, "O", &list)){ 	
		return NULL;	//zwracane w przypadku bledu; interpreter zglasza wyjatek wywolania funkcji
	}
	size = PyList_GET_SIZE(list);
	int * tab = (int*) malloc(sizeof(int) * size);
	for(int i = 0; i < size; i++){
		tab[i] = PyLong_AsLong(PyList_GetItem(list, i));
	}

	double result = srednia(tab, size);
	free(tab);
	//Py_RETURN_NONE; //jesli nic nie zwraca
	return Py_BuildValue("d", result);
}

static PyObject *mod_med(PyObject *self, PyObject *args){
	int size = 0;
	PyObject *list;
	if(!PyArg_ParseTuple(args, "O", &list)){ 	
		return NULL;	//zwracane w przypadku bledu; interpreter zglasza wyjatek wywolania funkcji
	}
	size = PyList_Size(list);
	int * tab = (int*) malloc(sizeof(int) * size);
	for(int i = 0; i < size; i++){
		tab[i] = PyLong_AsLong(PyList_GetItem(list, i));
	}

	int result = mediand(tab, size);
	free(tab);
	//Py_RETURN_NONE; //jesli nic nie zwraca
	return Py_BuildValue("i", result);
}

//tablica metod
static PyMethodDef mod_metody[]={
	{"met", mod_met, METH_VARARGS, "Funkcja ..."}, 
	{"mysort", mod_mysort, METH_VARARGS, "Funkcja ..."},
	{"mynwd", mod_mynwd, METH_VARARGS, "Funkcja ..."},
	{"mysrd", mod_sednia, METH_VARARGS, "Funkcja ..."},
	{"mymed", mod_med, METH_VARARGS, "Funkcja ..."},
	//nazwa funkcja stosowana w Pythonie, adres funkcji , j.w. lub METH_KEYWORDS lub METH_NOARGS, lancuch dokumentacyjny
	{NULL, NULL, 0, NULL}	//wartownik
};




static struct PyModuleDef modmodule={
        PyModuleDef_HEAD_INIT,
        "mod",
        NULL,
        -1,
        mod_metody
};

//funkcja inicjalizujaca
PyMODINIT_FUNC PyInit_mod(void){
        return PyModule_Create(&modmodule);
}
