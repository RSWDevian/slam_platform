// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from slam_interfaces:msg/SLAMMetrics.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "slam_interfaces/msg/slam_metrics.hpp"


#ifndef SLAM_INTERFACES__MSG__DETAIL__SLAM_METRICS__STRUCT_HPP_
#define SLAM_INTERFACES__MSG__DETAIL__SLAM_METRICS__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <cstdint>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__slam_interfaces__msg__SLAMMetrics __attribute__((deprecated))
#else
# define DEPRECATED__slam_interfaces__msg__SLAMMetrics __declspec(deprecated)
#endif

namespace slam_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct SLAMMetrics_
{
  using Type = SLAMMetrics_<ContainerAllocator>;

  explicit SLAMMetrics_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->ate = 0.0;
      this->rpe = 0.0;
      this->drift = 0.0;
      this->cpu_usage = 0.0;
      this->memory_usage = 0.0;
      this->runtime = 0.0;
      this->thread_count = 0l;
    }
  }

  explicit SLAMMetrics_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->ate = 0.0;
      this->rpe = 0.0;
      this->drift = 0.0;
      this->cpu_usage = 0.0;
      this->memory_usage = 0.0;
      this->runtime = 0.0;
      this->thread_count = 0l;
    }
  }

  // field types and members
  using _ate_type =
    double;
  _ate_type ate;
  using _rpe_type =
    double;
  _rpe_type rpe;
  using _drift_type =
    double;
  _drift_type drift;
  using _cpu_usage_type =
    double;
  _cpu_usage_type cpu_usage;
  using _memory_usage_type =
    double;
  _memory_usage_type memory_usage;
  using _runtime_type =
    double;
  _runtime_type runtime;
  using _thread_count_type =
    int32_t;
  _thread_count_type thread_count;

  // setters for named parameter idiom
  Type & set__ate(
    const double & _arg)
  {
    this->ate = _arg;
    return *this;
  }
  Type & set__rpe(
    const double & _arg)
  {
    this->rpe = _arg;
    return *this;
  }
  Type & set__drift(
    const double & _arg)
  {
    this->drift = _arg;
    return *this;
  }
  Type & set__cpu_usage(
    const double & _arg)
  {
    this->cpu_usage = _arg;
    return *this;
  }
  Type & set__memory_usage(
    const double & _arg)
  {
    this->memory_usage = _arg;
    return *this;
  }
  Type & set__runtime(
    const double & _arg)
  {
    this->runtime = _arg;
    return *this;
  }
  Type & set__thread_count(
    const int32_t & _arg)
  {
    this->thread_count = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    slam_interfaces::msg::SLAMMetrics_<ContainerAllocator> *;
  using ConstRawPtr =
    const slam_interfaces::msg::SLAMMetrics_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<slam_interfaces::msg::SLAMMetrics_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<slam_interfaces::msg::SLAMMetrics_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      slam_interfaces::msg::SLAMMetrics_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<slam_interfaces::msg::SLAMMetrics_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      slam_interfaces::msg::SLAMMetrics_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<slam_interfaces::msg::SLAMMetrics_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<slam_interfaces::msg::SLAMMetrics_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<slam_interfaces::msg::SLAMMetrics_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__slam_interfaces__msg__SLAMMetrics
    std::shared_ptr<slam_interfaces::msg::SLAMMetrics_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__slam_interfaces__msg__SLAMMetrics
    std::shared_ptr<slam_interfaces::msg::SLAMMetrics_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SLAMMetrics_ & other) const
  {
    if (this->ate != other.ate) {
      return false;
    }
    if (this->rpe != other.rpe) {
      return false;
    }
    if (this->drift != other.drift) {
      return false;
    }
    if (this->cpu_usage != other.cpu_usage) {
      return false;
    }
    if (this->memory_usage != other.memory_usage) {
      return false;
    }
    if (this->runtime != other.runtime) {
      return false;
    }
    if (this->thread_count != other.thread_count) {
      return false;
    }
    return true;
  }
  bool operator!=(const SLAMMetrics_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SLAMMetrics_

// alias to use template instance with default allocator
using SLAMMetrics =
  slam_interfaces::msg::SLAMMetrics_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace slam_interfaces

#endif  // SLAM_INTERFACES__MSG__DETAIL__SLAM_METRICS__STRUCT_HPP_
