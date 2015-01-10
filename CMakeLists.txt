project(cberry)

set(CMAKE_TOOLCHAIN_FILE $ENV{HOME}/pi/pi.cmake)
target_link_libraries(${PROJECT_NAME} -lbcm2835 -lrt -lm)
add_library(${PROJECT_NAME} SHARED tft.c RAIO8870.c)
