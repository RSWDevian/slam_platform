// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from slam_interfaces:msg/SLAMMetrics.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "slam_interfaces/msg/detail/slam_metrics__struct.h"
#include "slam_interfaces/msg/detail/slam_metrics__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool slam_interfaces__msg__slam_metrics__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[46];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("slam_interfaces.msg._slam_metrics.SLAMMetrics", full_classname_dest, 45) == 0);
  }
  slam_interfaces__msg__SLAMMetrics * ros_message = _ros_message;
  {  // ate
    PyObject * field = PyObject_GetAttrString(_pymsg, "ate");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->ate = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // rpe
    PyObject * field = PyObject_GetAttrString(_pymsg, "rpe");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->rpe = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // drift
    PyObject * field = PyObject_GetAttrString(_pymsg, "drift");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->drift = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // cpu_usage
    PyObject * field = PyObject_GetAttrString(_pymsg, "cpu_usage");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->cpu_usage = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // memory_usage
    PyObject * field = PyObject_GetAttrString(_pymsg, "memory_usage");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->memory_usage = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // runtime
    PyObject * field = PyObject_GetAttrString(_pymsg, "runtime");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->runtime = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // thread_count
    PyObject * field = PyObject_GetAttrString(_pymsg, "thread_count");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->thread_count = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * slam_interfaces__msg__slam_metrics__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of SLAMMetrics */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("slam_interfaces.msg._slam_metrics");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "SLAMMetrics");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  slam_interfaces__msg__SLAMMetrics * ros_message = (slam_interfaces__msg__SLAMMetrics *)raw_ros_message;
  {  // ate
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->ate);
    {
      int rc = PyObject_SetAttrString(_pymessage, "ate", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // rpe
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->rpe);
    {
      int rc = PyObject_SetAttrString(_pymessage, "rpe", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // drift
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->drift);
    {
      int rc = PyObject_SetAttrString(_pymessage, "drift", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // cpu_usage
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->cpu_usage);
    {
      int rc = PyObject_SetAttrString(_pymessage, "cpu_usage", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // memory_usage
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->memory_usage);
    {
      int rc = PyObject_SetAttrString(_pymessage, "memory_usage", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // runtime
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->runtime);
    {
      int rc = PyObject_SetAttrString(_pymessage, "runtime", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // thread_count
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->thread_count);
    {
      int rc = PyObject_SetAttrString(_pymessage, "thread_count", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
