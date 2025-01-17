cmake_minimum_required(VERSION 3.15)
project(PocoTest CXX)

find_package(Poco REQUIRED Net)

add_executable(test_package src/test_package.cpp)
target_link_libraries(test_package Poco::Net Poco::Foundation)

