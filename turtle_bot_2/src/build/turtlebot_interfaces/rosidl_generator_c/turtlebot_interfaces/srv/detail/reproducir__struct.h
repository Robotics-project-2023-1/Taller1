// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from turtlebot_interfaces:srv/Reproducir.idl
// generated code does not contain a copyright notice

#ifndef TURTLEBOT_INTERFACES__SRV__DETAIL__REPRODUCIR__STRUCT_H_
#define TURTLEBOT_INTERFACES__SRV__DETAIL__REPRODUCIR__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'nombre'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/Reproducir in the package turtlebot_interfaces.
typedef struct turtlebot_interfaces__srv__Reproducir_Request
{
  rosidl_runtime_c__String nombre;
} turtlebot_interfaces__srv__Reproducir_Request;

// Struct for a sequence of turtlebot_interfaces__srv__Reproducir_Request.
typedef struct turtlebot_interfaces__srv__Reproducir_Request__Sequence
{
  turtlebot_interfaces__srv__Reproducir_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} turtlebot_interfaces__srv__Reproducir_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/Reproducir in the package turtlebot_interfaces.
typedef struct turtlebot_interfaces__srv__Reproducir_Response
{
  bool respuesta;
} turtlebot_interfaces__srv__Reproducir_Response;

// Struct for a sequence of turtlebot_interfaces__srv__Reproducir_Response.
typedef struct turtlebot_interfaces__srv__Reproducir_Response__Sequence
{
  turtlebot_interfaces__srv__Reproducir_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} turtlebot_interfaces__srv__Reproducir_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // TURTLEBOT_INTERFACES__SRV__DETAIL__REPRODUCIR__STRUCT_H_
