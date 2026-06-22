// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from slam_interfaces:msg/SLAMMetrics.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "slam_interfaces/msg/detail/slam_metrics__rosidl_typesupport_introspection_c.h"
#include "slam_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "slam_interfaces/msg/detail/slam_metrics__functions.h"
#include "slam_interfaces/msg/detail/slam_metrics__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void slam_interfaces__msg__SLAMMetrics__rosidl_typesupport_introspection_c__SLAMMetrics_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  slam_interfaces__msg__SLAMMetrics__init(message_memory);
}

void slam_interfaces__msg__SLAMMetrics__rosidl_typesupport_introspection_c__SLAMMetrics_fini_function(void * message_memory)
{
  slam_interfaces__msg__SLAMMetrics__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember slam_interfaces__msg__SLAMMetrics__rosidl_typesupport_introspection_c__SLAMMetrics_message_member_array[7] = {
  {
    "ate",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(slam_interfaces__msg__SLAMMetrics, ate),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "rpe",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(slam_interfaces__msg__SLAMMetrics, rpe),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "drift",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(slam_interfaces__msg__SLAMMetrics, drift),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "cpu_usage",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(slam_interfaces__msg__SLAMMetrics, cpu_usage),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "memory_usage",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(slam_interfaces__msg__SLAMMetrics, memory_usage),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "runtime",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(slam_interfaces__msg__SLAMMetrics, runtime),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "thread_count",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(slam_interfaces__msg__SLAMMetrics, thread_count),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers slam_interfaces__msg__SLAMMetrics__rosidl_typesupport_introspection_c__SLAMMetrics_message_members = {
  "slam_interfaces__msg",  // message namespace
  "SLAMMetrics",  // message name
  7,  // number of fields
  sizeof(slam_interfaces__msg__SLAMMetrics),
  false,  // has_any_key_member_
  slam_interfaces__msg__SLAMMetrics__rosidl_typesupport_introspection_c__SLAMMetrics_message_member_array,  // message members
  slam_interfaces__msg__SLAMMetrics__rosidl_typesupport_introspection_c__SLAMMetrics_init_function,  // function to initialize message memory (memory has to be allocated)
  slam_interfaces__msg__SLAMMetrics__rosidl_typesupport_introspection_c__SLAMMetrics_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t slam_interfaces__msg__SLAMMetrics__rosidl_typesupport_introspection_c__SLAMMetrics_message_type_support_handle = {
  0,
  &slam_interfaces__msg__SLAMMetrics__rosidl_typesupport_introspection_c__SLAMMetrics_message_members,
  get_message_typesupport_handle_function,
  &slam_interfaces__msg__SLAMMetrics__get_type_hash,
  &slam_interfaces__msg__SLAMMetrics__get_type_description,
  &slam_interfaces__msg__SLAMMetrics__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_slam_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, slam_interfaces, msg, SLAMMetrics)() {
  if (!slam_interfaces__msg__SLAMMetrics__rosidl_typesupport_introspection_c__SLAMMetrics_message_type_support_handle.typesupport_identifier) {
    slam_interfaces__msg__SLAMMetrics__rosidl_typesupport_introspection_c__SLAMMetrics_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &slam_interfaces__msg__SLAMMetrics__rosidl_typesupport_introspection_c__SLAMMetrics_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
