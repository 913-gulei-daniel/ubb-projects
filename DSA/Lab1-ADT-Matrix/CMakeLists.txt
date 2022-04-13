cmake_minimum_required(VERSION 3.16)
project(Lab1_ADT_Matrix)

set(CMAKE_CXX_STANDARD 14)

include_directories(Headers)

add_executable(Lab1_ADT_Matrix
        Headers/ExtendedTest.h
        Headers/Matrix.h
        Headers/ShortTest.h
        "Source Files/App.cpp"
        "Source Files/ExtendedTest.cpp"
        "Source Files/Matrix.cpp"
        "Source Files/ShortTest.cpp")
