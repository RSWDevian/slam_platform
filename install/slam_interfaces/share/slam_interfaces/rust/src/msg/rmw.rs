#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};


#[link(name = "slam_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__slam_interfaces__msg__SLAMMetrics() -> *const std::ffi::c_void;
}

#[link(name = "slam_interfaces__rosidl_generator_c")]
extern "C" {
    fn slam_interfaces__msg__SLAMMetrics__init(msg: *mut SLAMMetrics) -> bool;
    fn slam_interfaces__msg__SLAMMetrics__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<SLAMMetrics>, size: usize) -> bool;
    fn slam_interfaces__msg__SLAMMetrics__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<SLAMMetrics>);
    fn slam_interfaces__msg__SLAMMetrics__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<SLAMMetrics>, out_seq: *mut rosidl_runtime_rs::Sequence<SLAMMetrics>) -> bool;
}

// Corresponds to slam_interfaces__msg__SLAMMetrics
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct SLAMMetrics {

    // This member is not documented.
    #[allow(missing_docs)]
    pub ate: f64,


    // This member is not documented.
    #[allow(missing_docs)]
    pub rpe: f64,


    // This member is not documented.
    #[allow(missing_docs)]
    pub drift: f64,


    // This member is not documented.
    #[allow(missing_docs)]
    pub cpu_usage: f64,


    // This member is not documented.
    #[allow(missing_docs)]
    pub memory_usage: f64,


    // This member is not documented.
    #[allow(missing_docs)]
    pub runtime: f64,


    // This member is not documented.
    #[allow(missing_docs)]
    pub thread_count: i32,

}



impl Default for SLAMMetrics {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !slam_interfaces__msg__SLAMMetrics__init(&mut msg as *mut _) {
        panic!("Call to slam_interfaces__msg__SLAMMetrics__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for SLAMMetrics {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { slam_interfaces__msg__SLAMMetrics__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { slam_interfaces__msg__SLAMMetrics__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { slam_interfaces__msg__SLAMMetrics__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for SLAMMetrics {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for SLAMMetrics where Self: Sized {
  const TYPE_NAME: &'static str = "slam_interfaces/msg/SLAMMetrics";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__slam_interfaces__msg__SLAMMetrics() }
  }
}


