// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from slam_interfaces:msg/SLAMMetrics.idl
// generated code does not contain a copyright notice
#include "slam_interfaces/msg/detail/slam_metrics__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <cstddef>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/serialization_helpers.hpp"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "slam_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "slam_interfaces/msg/detail/slam_metrics__struct.h"
#include "slam_interfaces/msg/detail/slam_metrics__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif


// forward declare type support functions


using _SLAMMetrics__ros_msg_type = slam_interfaces__msg__SLAMMetrics;


ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_slam_interfaces
bool cdr_serialize_slam_interfaces__msg__SLAMMetrics(
  const slam_interfaces__msg__SLAMMetrics * ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Field name: ate
  {
    cdr << ros_message->ate;
  }

  // Field name: rpe
  {
    cdr << ros_message->rpe;
  }

  // Field name: drift
  {
    cdr << ros_message->drift;
  }

  // Field name: cpu_usage
  {
    cdr << ros_message->cpu_usage;
  }

  // Field name: memory_usage
  {
    cdr << ros_message->memory_usage;
  }

  // Field name: runtime
  {
    cdr << ros_message->runtime;
  }

  // Field name: thread_count
  {
    cdr << ros_message->thread_count;
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_slam_interfaces
bool cdr_deserialize_slam_interfaces__msg__SLAMMetrics(
  eprosima::fastcdr::Cdr & cdr,
  slam_interfaces__msg__SLAMMetrics * ros_message)
{
  // Field name: ate
  {
    cdr >> ros_message->ate;
  }

  // Field name: rpe
  {
    cdr >> ros_message->rpe;
  }

  // Field name: drift
  {
    cdr >> ros_message->drift;
  }

  // Field name: cpu_usage
  {
    cdr >> ros_message->cpu_usage;
  }

  // Field name: memory_usage
  {
    cdr >> ros_message->memory_usage;
  }

  // Field name: runtime
  {
    cdr >> ros_message->runtime;
  }

  // Field name: thread_count
  {
    cdr >> ros_message->thread_count;
  }

  return true;
}  // NOLINT(readability/fn_size)


ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_slam_interfaces
size_t get_serialized_size_slam_interfaces__msg__SLAMMetrics(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _SLAMMetrics__ros_msg_type * ros_message = static_cast<const _SLAMMetrics__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Field name: ate
  {
    size_t item_size = sizeof(ros_message->ate);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Field name: rpe
  {
    size_t item_size = sizeof(ros_message->rpe);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Field name: drift
  {
    size_t item_size = sizeof(ros_message->drift);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Field name: cpu_usage
  {
    size_t item_size = sizeof(ros_message->cpu_usage);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Field name: memory_usage
  {
    size_t item_size = sizeof(ros_message->memory_usage);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Field name: runtime
  {
    size_t item_size = sizeof(ros_message->runtime);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Field name: thread_count
  {
    size_t item_size = sizeof(ros_message->thread_count);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}


ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_slam_interfaces
size_t max_serialized_size_slam_interfaces__msg__SLAMMetrics(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;

  // Field name: ate
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Field name: rpe
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Field name: drift
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Field name: cpu_usage
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Field name: memory_usage
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Field name: runtime
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Field name: thread_count
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }


  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = slam_interfaces__msg__SLAMMetrics;
    is_plain =
      (
      offsetof(DataType, thread_count) +
      last_member_size
      ) == ret_val;
  }
  return ret_val;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_slam_interfaces
bool cdr_serialize_key_slam_interfaces__msg__SLAMMetrics(
  const slam_interfaces__msg__SLAMMetrics * ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Field name: ate
  {
    cdr << ros_message->ate;
  }

  // Field name: rpe
  {
    cdr << ros_message->rpe;
  }

  // Field name: drift
  {
    cdr << ros_message->drift;
  }

  // Field name: cpu_usage
  {
    cdr << ros_message->cpu_usage;
  }

  // Field name: memory_usage
  {
    cdr << ros_message->memory_usage;
  }

  // Field name: runtime
  {
    cdr << ros_message->runtime;
  }

  // Field name: thread_count
  {
    cdr << ros_message->thread_count;
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_slam_interfaces
size_t get_serialized_size_key_slam_interfaces__msg__SLAMMetrics(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _SLAMMetrics__ros_msg_type * ros_message = static_cast<const _SLAMMetrics__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;

  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Field name: ate
  {
    size_t item_size = sizeof(ros_message->ate);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Field name: rpe
  {
    size_t item_size = sizeof(ros_message->rpe);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Field name: drift
  {
    size_t item_size = sizeof(ros_message->drift);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Field name: cpu_usage
  {
    size_t item_size = sizeof(ros_message->cpu_usage);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Field name: memory_usage
  {
    size_t item_size = sizeof(ros_message->memory_usage);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Field name: runtime
  {
    size_t item_size = sizeof(ros_message->runtime);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  // Field name: thread_count
  {
    size_t item_size = sizeof(ros_message->thread_count);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_slam_interfaces
size_t max_serialized_size_key_slam_interfaces__msg__SLAMMetrics(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;
  // Field name: ate
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Field name: rpe
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Field name: drift
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Field name: cpu_usage
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Field name: memory_usage
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Field name: runtime
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Field name: thread_count
  {
    size_t array_size = 1;
    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = slam_interfaces__msg__SLAMMetrics;
    is_plain =
      (
      offsetof(DataType, thread_count) +
      last_member_size
      ) == ret_val;
  }
  return ret_val;
}


static bool _SLAMMetrics__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const slam_interfaces__msg__SLAMMetrics * ros_message = static_cast<const slam_interfaces__msg__SLAMMetrics *>(untyped_ros_message);
  (void)ros_message;
  return cdr_serialize_slam_interfaces__msg__SLAMMetrics(ros_message, cdr);
}

static bool _SLAMMetrics__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  slam_interfaces__msg__SLAMMetrics * ros_message = static_cast<slam_interfaces__msg__SLAMMetrics *>(untyped_ros_message);
  (void)ros_message;
  return cdr_deserialize_slam_interfaces__msg__SLAMMetrics(cdr, ros_message);
}

static uint32_t _SLAMMetrics__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_slam_interfaces__msg__SLAMMetrics(
      untyped_ros_message, 0));
}

static size_t _SLAMMetrics__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_slam_interfaces__msg__SLAMMetrics(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_SLAMMetrics = {
  "slam_interfaces::msg",
  "SLAMMetrics",
  _SLAMMetrics__cdr_serialize,
  _SLAMMetrics__cdr_deserialize,
  _SLAMMetrics__get_serialized_size,
  _SLAMMetrics__max_serialized_size,
  nullptr
};

static rosidl_message_type_support_t _SLAMMetrics__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_SLAMMetrics,
  get_message_typesupport_handle_function,
  &slam_interfaces__msg__SLAMMetrics__get_type_hash,
  &slam_interfaces__msg__SLAMMetrics__get_type_description,
  &slam_interfaces__msg__SLAMMetrics__get_type_description_sources,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, slam_interfaces, msg, SLAMMetrics)() {
  return &_SLAMMetrics__type_support;
}

#if defined(__cplusplus)
}
#endif
