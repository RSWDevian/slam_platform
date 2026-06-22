// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from slam_interfaces:msg/SLAMMetrics.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "slam_interfaces/msg/slam_metrics.hpp"


#ifndef SLAM_INTERFACES__MSG__DETAIL__SLAM_METRICS__TRAITS_HPP_
#define SLAM_INTERFACES__MSG__DETAIL__SLAM_METRICS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "slam_interfaces/msg/detail/slam_metrics__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace slam_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const SLAMMetrics & msg,
  std::ostream & out)
{
  out << "{";
  // member: ate
  {
    out << "ate: ";
    rosidl_generator_traits::value_to_yaml(msg.ate, out);
    out << ", ";
  }

  // member: rpe
  {
    out << "rpe: ";
    rosidl_generator_traits::value_to_yaml(msg.rpe, out);
    out << ", ";
  }

  // member: drift
  {
    out << "drift: ";
    rosidl_generator_traits::value_to_yaml(msg.drift, out);
    out << ", ";
  }

  // member: cpu_usage
  {
    out << "cpu_usage: ";
    rosidl_generator_traits::value_to_yaml(msg.cpu_usage, out);
    out << ", ";
  }

  // member: memory_usage
  {
    out << "memory_usage: ";
    rosidl_generator_traits::value_to_yaml(msg.memory_usage, out);
    out << ", ";
  }

  // member: runtime
  {
    out << "runtime: ";
    rosidl_generator_traits::value_to_yaml(msg.runtime, out);
    out << ", ";
  }

  // member: thread_count
  {
    out << "thread_count: ";
    rosidl_generator_traits::value_to_yaml(msg.thread_count, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const SLAMMetrics & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: ate
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ate: ";
    rosidl_generator_traits::value_to_yaml(msg.ate, out);
    out << "\n";
  }

  // member: rpe
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "rpe: ";
    rosidl_generator_traits::value_to_yaml(msg.rpe, out);
    out << "\n";
  }

  // member: drift
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "drift: ";
    rosidl_generator_traits::value_to_yaml(msg.drift, out);
    out << "\n";
  }

  // member: cpu_usage
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "cpu_usage: ";
    rosidl_generator_traits::value_to_yaml(msg.cpu_usage, out);
    out << "\n";
  }

  // member: memory_usage
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "memory_usage: ";
    rosidl_generator_traits::value_to_yaml(msg.memory_usage, out);
    out << "\n";
  }

  // member: runtime
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "runtime: ";
    rosidl_generator_traits::value_to_yaml(msg.runtime, out);
    out << "\n";
  }

  // member: thread_count
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "thread_count: ";
    rosidl_generator_traits::value_to_yaml(msg.thread_count, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const SLAMMetrics & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace slam_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use slam_interfaces::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const slam_interfaces::msg::SLAMMetrics & msg,
  std::ostream & out, size_t indentation = 0)
{
  slam_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use slam_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const slam_interfaces::msg::SLAMMetrics & msg)
{
  return slam_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<slam_interfaces::msg::SLAMMetrics>()
{
  return "slam_interfaces::msg::SLAMMetrics";
}

template<>
inline const char * name<slam_interfaces::msg::SLAMMetrics>()
{
  return "slam_interfaces/msg/SLAMMetrics";
}

template<>
struct has_fixed_size<slam_interfaces::msg::SLAMMetrics>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<slam_interfaces::msg::SLAMMetrics>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<slam_interfaces::msg::SLAMMetrics>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // SLAM_INTERFACES__MSG__DETAIL__SLAM_METRICS__TRAITS_HPP_
