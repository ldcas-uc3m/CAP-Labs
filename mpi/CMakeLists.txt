cmake_minimum_required(VERSION 3.1)

project(
  mpi
  VERSION 1.0
  LANGUAGES C)


find_package(MPI)

find_package(OpenMP)
if (OPENMP_FOUND)
    set (CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${OpenMP_C_FLAGS}")
    set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${OpenMP_CXX_FLAGS}")
    set (CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} ${OpenMP_EXE_LINKER_FLAGS}")
endif()

include_directories(SYSTEM ${MPI_INCLUDE_PATH})

add_executable(e1-hello_world  e1-hello_world.c)
add_executable(e2-ping e2-ping.c)
add_executable(e3-Bsend  e3-Bsend.c)
add_executable(e4-NBsendrec  e4-NBsendrec.c)
add_executable(e5-pi  e5-pi.c)
add_executable(e6-sum_reduce  e6-sum_reduce.c)
add_executable(e7-array_decomposition  e7-array_decomposition.c)
add_executable(e8-primos  e8-primos.c)
add_executable(e9-random  e9-random.c)
add_executable(e10-ring  e10-ring.c)
add_executable(e11-broadcast  e11-broadcast.c)
add_executable(e12-barrier  e12-barrier.c)
add_executable(e13-scatter  e13-scatter.c)
add_executable(e14-gather  e14-gather.c)
add_executable(e15-hibrido  e15-hibrido.c)


target_link_libraries(e1-hello_world  ${MPI_C_LIBRARIES})
target_link_libraries(e2-ping ${MPI_C_LIBRARIES})
target_link_libraries(e3-Bsend  ${MPI_C_LIBRARIES})
target_link_libraries(e4-NBsendrec  ${MPI_C_LIBRARIES})
target_link_libraries(e5-pi  ${MPI_C_LIBRARIES})
target_link_libraries(e6-sum_reduce  ${MPI_C_LIBRARIES})
target_link_libraries(e7-array_decomposition  ${MPI_C_LIBRARIES})
target_link_libraries(e8-primos  ${MPI_C_LIBRARIES})
target_link_libraries(e9-random  ${MPI_C_LIBRARIES})
target_link_libraries(e10-ring  ${MPI_C_LIBRARIES})
target_link_libraries(e11-broadcast  ${MPI_C_LIBRARIES})
target_link_libraries(e12-barrier  ${MPI_C_LIBRARIES})
target_link_libraries(e13-scatter  ${MPI_C_LIBRARIES})
target_link_libraries(e14-gather  ${MPI_C_LIBRARIES})
target_link_libraries(e15-hibrido  ${MPI_C_LIBRARIES})



