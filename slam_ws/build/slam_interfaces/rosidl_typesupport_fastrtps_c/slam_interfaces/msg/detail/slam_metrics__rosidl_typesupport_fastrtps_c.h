// generated from rosidl_typesupport_fastrtps_c/resource/idl__rosidl_typesupport_fastrtps_c.h.em
// with input from slam_interfaces:msg/SLAMMetrics.idl
// generated code does not contain a copyright notice
#ifndef SLAM_INTERFACES__MSG__DETAIL__SLAM_METRICS__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_
#define SLAM_INTERFACES__MSG__DETAIL__SLAM_METRICS__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_


#include <stddef.h>
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "slam_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "slam_interfaces/msg/detail/slam_metrics__struct.h"
#include "fastcdr/Cdr.h"

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_slam_interfaces
bool cdr_serialize_slam_interfaces__msg__SLAMMetrics(
  const slam_interfaces__msg__SLAMMetrics * ros_message,
  eprosima::fastcdr::Cdr & cdr);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_slam_interfaces
bool cdr_deserialize_slam_interfaces__msg__SLAMMetrics(
  eprosima::fastcdr::Cdr &,
  slam_interfaces__msg__SLAMMetrics * ros_message);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_slam_interfaces
size_t get_serialized_size_slam_interfaces__msg__SLAMMetrics(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_slam_interfaces
size_t max_serialized_size_slam_interfaces__msg__SLAMMetrics(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_slam_interfaces
bool cdr_serialize_key_slam_interfaces__msg__SLAMMetrics(
  const slam_interfaces__msg__SLAMMetrics * ros_message,
  eprosima::fastcdr::Cdr & cdr);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_slam_interfaces
size_t get_serialized_size_key_slam_interfaces__msg__SLAMMetrics(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_slam_interfaces
size_t max_serialized_size_key_slam_interfaces__msg__SLAMMetrics(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_slam_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, slam_interfaces, msg, SLAMMetrics)();

#ifdef __cplusplus
}
#endif

#endif  // SLAM_INTERFACES__MSG__DETAIL__SLAM_METRICS__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_
