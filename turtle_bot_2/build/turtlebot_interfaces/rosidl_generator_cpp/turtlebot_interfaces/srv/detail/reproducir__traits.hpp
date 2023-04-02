// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from turtlebot_interfaces:srv/Reproducir.idl
// generated code does not contain a copyright notice

#ifndef TURTLEBOT_INTERFACES__SRV__DETAIL__REPRODUCIR__TRAITS_HPP_
#define TURTLEBOT_INTERFACES__SRV__DETAIL__REPRODUCIR__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "turtlebot_interfaces/srv/detail/reproducir__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace turtlebot_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const Reproducir_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: nombre
  {
    out << "nombre: ";
    rosidl_generator_traits::value_to_yaml(msg.nombre, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Reproducir_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: nombre
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "nombre: ";
    rosidl_generator_traits::value_to_yaml(msg.nombre, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Reproducir_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace turtlebot_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use turtlebot_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const turtlebot_interfaces::srv::Reproducir_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  turtlebot_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use turtlebot_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const turtlebot_interfaces::srv::Reproducir_Request & msg)
{
  return turtlebot_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<turtlebot_interfaces::srv::Reproducir_Request>()
{
  return "turtlebot_interfaces::srv::Reproducir_Request";
}

template<>
inline const char * name<turtlebot_interfaces::srv::Reproducir_Request>()
{
  return "turtlebot_interfaces/srv/Reproducir_Request";
}

template<>
struct has_fixed_size<turtlebot_interfaces::srv::Reproducir_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<turtlebot_interfaces::srv::Reproducir_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<turtlebot_interfaces::srv::Reproducir_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace turtlebot_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const Reproducir_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: respuesta
  {
    out << "respuesta: ";
    rosidl_generator_traits::value_to_yaml(msg.respuesta, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Reproducir_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: respuesta
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "respuesta: ";
    rosidl_generator_traits::value_to_yaml(msg.respuesta, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Reproducir_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace turtlebot_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use turtlebot_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const turtlebot_interfaces::srv::Reproducir_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  turtlebot_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use turtlebot_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const turtlebot_interfaces::srv::Reproducir_Response & msg)
{
  return turtlebot_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<turtlebot_interfaces::srv::Reproducir_Response>()
{
  return "turtlebot_interfaces::srv::Reproducir_Response";
}

template<>
inline const char * name<turtlebot_interfaces::srv::Reproducir_Response>()
{
  return "turtlebot_interfaces/srv/Reproducir_Response";
}

template<>
struct has_fixed_size<turtlebot_interfaces::srv::Reproducir_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<turtlebot_interfaces::srv::Reproducir_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<turtlebot_interfaces::srv::Reproducir_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<turtlebot_interfaces::srv::Reproducir>()
{
  return "turtlebot_interfaces::srv::Reproducir";
}

template<>
inline const char * name<turtlebot_interfaces::srv::Reproducir>()
{
  return "turtlebot_interfaces/srv/Reproducir";
}

template<>
struct has_fixed_size<turtlebot_interfaces::srv::Reproducir>
  : std::integral_constant<
    bool,
    has_fixed_size<turtlebot_interfaces::srv::Reproducir_Request>::value &&
    has_fixed_size<turtlebot_interfaces::srv::Reproducir_Response>::value
  >
{
};

template<>
struct has_bounded_size<turtlebot_interfaces::srv::Reproducir>
  : std::integral_constant<
    bool,
    has_bounded_size<turtlebot_interfaces::srv::Reproducir_Request>::value &&
    has_bounded_size<turtlebot_interfaces::srv::Reproducir_Response>::value
  >
{
};

template<>
struct is_service<turtlebot_interfaces::srv::Reproducir>
  : std::true_type
{
};

template<>
struct is_service_request<turtlebot_interfaces::srv::Reproducir_Request>
  : std::true_type
{
};

template<>
struct is_service_response<turtlebot_interfaces::srv::Reproducir_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // TURTLEBOT_INTERFACES__SRV__DETAIL__REPRODUCIR__TRAITS_HPP_
