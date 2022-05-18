cmake_minimum_required(VERSION 3.16)
project(Lab4_Hash_Bag)

set(CMAKE_CXX_STANDARD 14)

include_directories(Headers)

add_executable(Lab4_Hash_Bag
        Headers/Bag.h
        Headers/BagIterator.h
        Headers/ExtendedTest.h
        Headers/ShortTest.h
        Sources/Bag.cpp
        Sources/BagIterator.cpp
        Sources/ExtendedTest.cpp
        Sources/ShortTest.cpp
        App.cpp)
