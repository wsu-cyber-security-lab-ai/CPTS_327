#include <Python.h>
#include <string.h>

void vulnerable_function(char *user_input) {
    char buffer[32];
    strcpy(buffer, user_input);   
    printf("Received: %s\n", buffer);
}

static PyObject* py_vulnerable_function(PyObject* self, PyObject* args) {
    char *input_string;
    
    if (!PyArg_ParseTuple(args, "s", &input_string))
        return NULL;
    
    vulnerable_function(input_string);
    
    Py_RETURN_NONE;
}

static PyMethodDef VulnMethods[] = {
    {"vulnerable_function", py_vulnerable_function, METH_VARARGS, "A vulnerable function"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef vulnmoudle = {
    PyModuleDef_HEAD_INIT,
    "vuln_module",
    NULL,
    -1,
    VulnMethods
};

PyMODINIT_FUNC PyInit_vuln_module(void) {
    return PyModule_Create(&vulnmoudle);
}
