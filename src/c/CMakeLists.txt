cmake_minimum_required(VERSION 3.10)
project(ds_and_algo)

set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)

set(SOURCE_FILES
    list/LinkedList.c
    list/ArrayList.c
    map/ChainingHashMap.c
    map/OpenAddressingHashMap.c
    map/HashSet.c
    queue/LinkedQueue.c
    queue/LinkedDeque.c
    queue/ArrayQueue.c
    queue/ArrayDeque.c
    stack/LinkedStack.c
    stack/ArrayStack.c
    Main.c
)

add_executable(ds_and_algo ${SOURCE_FILES})
target_include_directories(ds_and_algo PRIVATE lib)

