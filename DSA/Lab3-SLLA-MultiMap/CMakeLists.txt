cmake_minimum_required(VERSION 3.16)
project(Lab3_SLLA_MultiMap)

set(CMAKE_CXX_STANDARD 14)

include_directories(Headers)

add_executable(Lab3_SLLA_MultiMap
        Headers/ExtendedTest.h
        Headers/MultiMap.h
        Headers/MultiMapIterator.h
        Headers/ShortTest.h
        Sources/ExtendedTest.cpp
        Sources/MultiMap.cpp
        Sources/MultiMapIterator.cpp
        Sources/ShortTest.cpp
        App.cpp)
