cmake_minimum_required(VERSION 3.10)

project(DsAndAlgo)

# 设置 C++ 标准（可选，建议明确指定）
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 添加可执行文件，列出所有源文件
add_executable(DsAndAlgo
    Main.cpp
    List/LinkedList.cpp
    List/ArrayList.cpp
    Stack/LinkedStack.cpp
    Stack/ArrayStack.cpp
    Queue/LinkedQueue.cpp
    Queue/ArrayQueue.cpp
)

target_include_directories(DsAndAlgo PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}        
    ${CMAKE_CURRENT_SOURCE_DIR}/utils
    ${CMAKE_CURRENT_SOURCE_DIR}/List
    ${CMAKE_CURRENT_SOURCE_DIR}/Stack
    ${CMAKE_CURRENT_SOURCE_DIR}/Queue
)