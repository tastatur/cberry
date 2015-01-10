project(cberry)

include_directories($ENV{HOME}/pi/rootfs/usr/local/include/)
add_library(${PROJECT_NAME} SHARED tft.c RAIO8870.c)
target_link_libraries(${PROJECT_NAME} -L$ENV{HOME}/pi/rootfs/usr/local/lib -lbcm2835 -lrt -lm)
