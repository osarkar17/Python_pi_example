cmake_minimum_required(VERSION 3.10)

# Project Name
project(myProgram)

# C++ Standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Find OpenCASCADE
find_package(OpenCASCADE REQUIRED)
include_directories(${OpenCASCADE_INCLUDE_DIR})

# Find VTK
find_package(VTK REQUIRED)
include(${VTK_USE_FILE})

# Add the executable
add_executable(${PROJECT_NAME} main.cpp)

# Link libraries
target_link_libraries(${PROJECT_NAME} ${OpenCASCADE_LIBRARIES} ${VTK_LIBRARIES})

