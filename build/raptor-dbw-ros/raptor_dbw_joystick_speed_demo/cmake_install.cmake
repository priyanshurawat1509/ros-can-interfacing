# Install script for directory: /home/administrator/Documents/DEEPORANGE14/deeporange14_control/src/raptor-dbw-ros/raptor_dbw_joystick_speed_demo

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/administrator/Documents/DEEPORANGE14/deeporange14_control/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/administrator/Documents/DEEPORANGE14/deeporange14_control/build/raptor-dbw-ros/raptor_dbw_joystick_speed_demo/catkin_generated/installspace/raptor_dbw_joystick_speed_demo.pc")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/raptor_dbw_joystick_speed_demo/cmake" TYPE FILE FILES
    "/home/administrator/Documents/DEEPORANGE14/deeporange14_control/build/raptor-dbw-ros/raptor_dbw_joystick_speed_demo/catkin_generated/installspace/raptor_dbw_joystick_speed_demoConfig.cmake"
    "/home/administrator/Documents/DEEPORANGE14/deeporange14_control/build/raptor-dbw-ros/raptor_dbw_joystick_speed_demo/catkin_generated/installspace/raptor_dbw_joystick_speed_demoConfig-version.cmake"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/raptor_dbw_joystick_speed_demo" TYPE FILE FILES "/home/administrator/Documents/DEEPORANGE14/deeporange14_control/src/raptor-dbw-ros/raptor_dbw_joystick_speed_demo/package.xml")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/raptor_dbw_joystick_speed_demo/joystick_speed_demo" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/raptor_dbw_joystick_speed_demo/joystick_speed_demo")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/raptor_dbw_joystick_speed_demo/joystick_speed_demo"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/raptor_dbw_joystick_speed_demo" TYPE EXECUTABLE FILES "/home/administrator/Documents/DEEPORANGE14/deeporange14_control/devel/lib/raptor_dbw_joystick_speed_demo/joystick_speed_demo")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/raptor_dbw_joystick_speed_demo/joystick_speed_demo" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/raptor_dbw_joystick_speed_demo/joystick_speed_demo")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/raptor_dbw_joystick_speed_demo/joystick_speed_demo"
         OLD_RPATH "/opt/ros/noetic/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/raptor_dbw_joystick_speed_demo/joystick_speed_demo")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/raptor_dbw_joystick_speed_demo" TYPE DIRECTORY FILES "/home/administrator/Documents/DEEPORANGE14/deeporange14_control/src/raptor-dbw-ros/raptor_dbw_joystick_speed_demo/launch")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/administrator/Documents/DEEPORANGE14/deeporange14_control/build/raptor-dbw-ros/raptor_dbw_joystick_speed_demo/tests/cmake_install.cmake")

endif()

