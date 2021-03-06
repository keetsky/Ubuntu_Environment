cmake_minimum_required(VERSION 2.8)
project(ORB_SLAM2)

#定义变量
SET(SRC_LIST main.c util.c reactor.c))
#message输出变量的值
message(${PROJECT_SOURCE_DIR})
#让CMAKE至此gdb
set(CMAKE_BUILD_TYPE "Debug")
set(CMAKE_CXX_FLAGS_DEBUG "$ENV{CXXFLAGS} -O0 -Wall -g -ggdb")
set(CMAKE_CXX_FLAGS_RELEASE "$ENV{CXXFLAGS} -O3 -Wall")
#设置cmake编译模式，必须为 cmake .. -DCMAKE_BUILD_TYPE=Release 形式
IF(NOT CMAKE_BUILD_TYPE)
  SET(CMAKE_BUILD_TYPE Release)
ENDIF()

MESSAGE("Build type: " ${CMAKE_BUILD_TYPE})

#设置编译器
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS}  -Wall  -O3 -march=native ")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall   -O3 -march=native")

# Check C++11 or C++0x support
include(CheckCXXCompilerFlag)
CHECK_CXX_COMPILER_FLAG("-std=c++11" COMPILER_SUPPORTS_CXX11)
CHECK_CXX_COMPILER_FLAG("-std=c++0x" COMPILER_SUPPORTS_CXX0X)
if(COMPILER_SUPPORTS_CXX11)
   set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
   add_definitions(-DCOMPILEDWITHC11)
   message(STATUS "Using flag -std=c++11.")
elseif(COMPILER_SUPPORTS_CXX0X)
   set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++0x")
   add_definitions(-DCOMPILEDWITHC0X)
   message(STATUS "Using flag -std=c++0x.")
else()
   message(FATAL_ERROR "The compiler ${CMAKE_CXX_COMPILER} has no C++11 support. Please use a different C++ compiler.")
endif()

LIST(APPEND CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/cmake_modules)

#依赖项
#######################
#ros
find_package(catkin REQUIRED COMPONENTS geometry_msgs
					      #orocos_kdl
					roscpp
					roslib
					message_generation
					#tf
					)
#opencv
#find_package(OpenCV REQUIRED)
find_package(OpenCV 3.0 QUIET)
if(NOT OpenCV_FOUND)
   find_package(OpenCV 2.4.3 QUIET)
   if(NOT OpenCV_FOUND)
      message(FATAL_ERROR "OpenCV > 2.4.3 not found.")
   endif()
endif()
#cuda
find_package(CUDA REQUIRED)
#Eigen
find_package(Eigen3 3.1.0 REQUIRED)
#pangolin
find_package(Pangolin REQUIRED)
#pcl
find_package(PCL REQUIRED)
#opengl
find_package(OpenGL REQUIRED)

find_package(GLUT REQUIRED)
FIND_PACKAGE(Freetype REQUIRED)
#boost
find_package( Boost REQUIRED )
include_directories( ${Boost_INCLUDE_DIR}  ./include/hello/) #指定头文件的搜索路径
add_subdirectory(dir)  #包含子目录
link_directories( ${Boost_LIBRARY_DIRS} )
set( Boost_USE_STATIC_LIBS        OFF )
set( Boost_USE_MULTITHREADED      ON )
set( Boost_USE_STATIC_RUNTIME     OFF )
set( BOOST_ALL_DYN_LINK ON )
##################3
#openni nite

find_path(OpenNI2_INCLUDEDIR
	  NAMES OpenNI.h
	  HINTS /usr/include/openni2
	)
find_library(OpenNI2_LIBRARIES
	     NAMES OpenNI2 DummyDevice OniFile PS1090
	     HINTS /usr/lib/ /usr/lib/OpenNI2/Drivers
	     PATH_SUFFIXES lib
		) 
message(STATUS ${OpenNI2_LIBRARIES})

# Find Nite2
message(status $ENV{NITE2_INCLUDE})
message(status $ENV{NITE2_REDIST64})
find_path(Nite2_INCLUDEDIR
	  NAMES NiTE.h
	  HINTS $ENV{NITE2_INCLUDE})
find_library(Nite2_LIBRARY
	     NAMES NiTE2
	     HINTS $ENV{NITE2_REDIST64}
	     PATH_SUFFIXES lib) 
#或者
set(OPENNI2_DIR ~/OpenNI2)
set(NITE2_DIR ~/NiTE-Linux-x64-2.2/)
set(LIBRARY_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/lib)
link_directories(${OPENNI2_DIR}/Bin/x64-Release)
include_directories(${OPENNI2_DIR}/Include)
link_directories(${NITE2_DIR}/Redist)
include_directories(${NITE2_DIR}/Include)
#include_directories(../../../thirdparty/comm/include)  #添加头文件目录INCLUDE_DIRECTORIES,相当于g++选项中的-I参数的作用

add_executable(tracker src/tracker.cpp)
target_link_libraries(tracker OpenNI2 NiTE2)

############################
#set(
#    CUDA_NVCC_FLAGS
#    ${CUDA_NVCC_FLAGS};
#    -O3 -gencode arch=compute_50,code=sm_50
#    )
#GPU显卡选取
FIND_PACKAGE(CUDA)
if (CUDA_FOUND)
    message(STATUS "CUDA Version: " ${CUDA_VERSION_STRINGS})
    message(STATUS "CUDA Libararies: " ${CUDA_LIBRARIES})
    include_directories(SYSTEM ${CUDA_INCLUDE_DIRS})
    list(APPEND LIBRARIES ${CUDA_LIBRARIES} ${CUDA_CUBLAS_LIBRARIES} ${CUDA_curand_LIBRARY} ${CUDA_cusparse_LIBRARY})
    list(APPEND CUDA_NVCC_FLAGS "-std=c++11;-O2;-Xcompiler \"-fPIC\" ")
    list(APPEND CUDA_NVCC_FLAGS "-gencode arch=compute_20,code=compute_20 ")
    list(APPEND CUDA_NVCC_FLAGS "-gencode arch=compute_30,code=compute_30 ")
    list(APPEND CUDA_NVCC_FLAGS "-gencode arch=compute_35,code=compute_35 ")
    list(APPEND CUDA_NVCC_FLAGS "-gencode arch=compute_50,code=compute_50 ")
    list(APPEND CUDA_NVCC_FLAGS "-gencode arch=compute_52,code=compute_52 ")
    list(APPEND CUDA_NVCC_FLAGS "-gencode arch=compute_53,code=compute_53 ")#根据显卡参数增加此选项
    set(CUDA_PROPAGATE_HOST_FLAGS OFF)
#    set(CUDA_USE_STATIC_CUDA_RUNTIME OFF)
    add_definitions(-DGPU)
    cuda_include_directories(src)
else()
    list(APPEND LIBRARIES "m")
endif()
#简单的话可设置如下
#set(
#    CUDA_NVCC_FLAGS
#    ${CUDA_NVCC_FLAGS};
#    -O3 -gencode arch=compute_50,code=sm_50
#    )


#python
#FIND_PACKAGE(python REQUIRED)
FIND_PACKAGE(PythonLibs REQUIRED)
include_directories(SYSTEM ${PYTHON_INCLUDE_DIR})

########################


add_definitions(-DGPU -DOPENCV)

#包含目录
#它相当于g++选项中的-I参数的作用，也相当于环境变量中增加路径到CPLUS_INCLUDE_PATH变量的作用。
include_directories(
${PROJECT_SOURCE_DIR}
${PROJECT_SOURCE_DIR}/include
${EIGEN3_INCLUDE_DIR}
${Pangolin_INCLUDE_DIRS}
${OpenCV_INCLUDE_DIRS}
${OPENGL_INCLUDE_DIRS}  ${GLUT_INCLUDE_DIRS} ${FREETYPE_INCLUDE_DIRS}
${PCL_INCLUDE_DIRS}
/usr/include/python2.7
${catkin_INCLUDEDIR}
${OpenNI2_INCLUDEDIR}
${Nite2_INCLUDEDIR}
)

#设置动态链接库生成输出目录
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/lib)

#生成动态链接库.so
add_library(${PROJECT_NAME} SHARED #SHARED生成动态库，STATIC生成静态库
src/System.cc
src/Tracking.cc
src/LocalMapping.cc
src/LoopClosing.cc
src/ORBextractor.cc
src/ORBmatcher.cc
src/FrameDrawer.cc
src/Converter.cc
src/MapPoint.cc
src/KeyFrame.cc
src/Map.cc
src/MapDrawer.cc
src/Optimizer.cc
src/PnPsolver.cc
src/Frame.cc
src/KeyFrameDatabase.cc
src/Sim3Solver.cc
src/Initializer.cc
src/Viewer.cc
)
#同时生成名字相同不冲突的libhello.so libhello.a两个库
SET_TARGET_PROPERTIES(HELLO PROPERTIES OUTPUT_NAME "hello")
#链接库  库查询终端$pkg-config --libs opencv
link_libraries( 
	-lstdc++ 
	-lcuda 
	-lcudart 
	-lcublas 
	-lcurand
	${OpenCV_LIBS}
	${Boost_LIBRARIES}
        ${catkin_LIBRARIES}
        -lpython2.7   #或者libpython2.7.so 
        libboost_python.so 
        /home/server/third/lib/libcommon.a
        ${OpenNI2_LIBRARIES} ${Nite2_LIBRARY}
         ${PYTHON_LIBRARIES} 
	hello #或 libhello.so  或-lhello
		)
#上面这段可放入下面target_link_libraries？
#添加需要链接的库文件目录,相当于g++命令的-L选项的作用,把该路径添加到第三方库搜索路径中，这样就可以使用相对路径了，使用TARGET_LINK_LIBRARIES的时候，只需要给出动态链接库的名字就行了，#指定动态链接库的搜索路径

#它相当于g++命令的-L选项的作用，也相当于环境变量中增加LD_LIBRARY_PATH的路径的作用。
link_directories(
  /usr/local/cuda/lib    
 /usr/local/cuda/lib64
 /usr/lib/python2.7
   
)
#下面这段一般放在可执行文件后
target_link_libraries(${PROJECT_NAME}
${OpenCV_LIBS}
${Boost_LIBRARIES}
${EIGEN3_LIBS}
${Pangolin_LIBRARIES}
${PROJECT_SOURCE_DIR}/Thirdparty/DBoW2/lib/libDBoW2.so
${PROJECT_SOURCE_DIR}/Thirdparty/g2o/lib/libg2o.so
${OPENGL_LIBRARIES} ${GLUT_LIBRARY} ${GLUT_glut_LIBRARY}
${FREETYPE_LIBRARIES} 
${PCL_LIBRARIES}
${PYTHON_LIBRARIES}
   pthread #线程
   stdc++
   cuda 
   cudart 
   cublas 
   curand
   ${catkin_LIBRARIES}

)
#如果需要放前可
set(LIBS
${OpenCV_LIBS}
${EIGEN3_LIBS}
${Pangolin_LIBRARIES}
)
add_executable(rgbd_tum   xxx.cc)
target_link_libraries(rgbd_tum ${LIBS})


#生成可执行文件
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/Examples/RGB-D)
#或
#set the default path for built executables to the "bin" directory
set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)
#set the default path for built libraries to the "lib" directory
set(LIBRARY_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/lib)

add_executable(rgbd_tum
Examples/RGB-D/rgbd_tum.cc)
target_link_libraries(rgbd_tum ${PROJECT_NAME})


set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR}/Examples/Monocular)

add_executable(mono_tum
Examples/Monocular/mono_tum.cc ${SRC_LIST})
target_link_libraries(mono_tum ${PROJECT_NAME} )

# 查找当前目录下的所有源文件
# 并将名称保存到 DIR_SRCS 变量
aux_source_directory(. DIR_SRCS)
add_executable(Demo ${DIR_SRCS})

#一般为
cuda_add_executable(ROS_interface 
  src/ROS_interface.cpp   cccccc.c   ccccs.cpp）
#下面其实可以不写，因为上面写了link_libraries    #添加链接库
target_link_libraries(ROS_interface
   m
   pthread
   stdc++
   cuda 
   cudart 
   cublas 
   curand
   ${catkin_LIBRARIES}
   python2.7
)



























