cmake_minimum_required(VERSION 3.16)
project(Lab2_DLL_SortedMultiMap)

set(CMAKE_CXX_STANDARD 14)

include_directories(Headers)

add_executable(Lab2_DLL_SortedMultiMap
        Headers/ExtendedTest.h
        Headers/ShortTest.h
        Headers/SMMIterator.h
        Headers/SortedMultiMap.h
        Sources/ExtendedTest.cpp
        Sources/ShortTest.cpp
        Sources/SMMIterator.cpp
        Sources/SortedMultiMap.cpp
        App.cpp)
