

依赖库lib:
cc_library(
    name = "bread",
    srcs = ["bread.cc"],
    hdrs = ["bread.h"],
    deps = [":flour"],
)

cc_library(
    name = "flour",
    srcs = ["flour.cc"],
    hdrs = ["flour.h"],
)

测试test:
   cc_test(
       name = "mylib_test",
       srcs = ["mylib_test.cc"],
       deps = [":bread"]
   )
/*********************************************************************/

└── my-project
    ├── lib
    │   ├── BUILD
    │   ├── hello-greet.cc
    │   └── hello-greet.h
    ├── main
    │   ├── BUILD
    │   ├── hello-time.cc
    │   ├── hello-time.h
    │   └── hello-world.cc
    └── WORKSPACE
/* lib BUILD编写 */
cc_library(
    name = "hello-greet",
    srcs = ["hello-greet.cc"],
    hdrs = ["hello-greet.h"],
    visibility = ["//main:__pkg__"],    //表示hello-greet对于main/BUILD是可见的,"//"表示工程目录
)
/* main BUILD编写 */
cc_library(
    name = "hello-time",
    srcs = ["hello-time.cc"],
    hdrs = ["hello-time.h"],
)

cc_binary(
    name = "hello-world",        
    srcs = ["hello-world.cc"],
    deps = [
        ":hello-time",                //当依赖在站同目录下
        "//lib:hello-greet",　　　　　　　　　//依赖不同目录下需要全路径
    ],
)
/* 编译运行*/
$bazel build main:hello-world
$./bazel-bin/main/hello-world Bazel
/**************************传递依赖****************************/
如果一个文件包含一个头文件，那么这个文件的规则也应该依赖与头文件的库，相反的，只有直接依赖需要被指定为依赖。例如，假设sandwich.h包括bread.h，而且bread.h包括flour.h，sandwich.h不包括flour.h，因此这个BUILD文件应该是这样

cc_library(
    name = "sandwich",
    srcs = ["sandwich.cc"],
    hdrs = ["sandwich.h"],
    deps = [":bread"],
)

cc_library(
    name = "bread",
    srcs = ["bread.cc"],
    hdrs = ["bread.h"],
    deps = [":flour"],
)

cc_library(
    name = "flour",
    srcs = ["flour.cc"],
    hdrs = ["flour.h"],
)
    2. /****多个依赖***/
    cc_library(
    name = "build-all-the-files",
    srcs = glob(["*.cc"])
    hdrs = glob(["*.h"]),
    )
    

    cc_library(
    name="gggg"
    srcs=["a.cc","b.cc"]
    hdrs=["a.h","b.h"]
    )




/**************************添加包含路径****************************/
└── my-project
    ├── third_party
    │   └── some_lib
    │       ├── BUILD
    │       ├── include
    │       │   └── some_lib.h
    │       └── some_lib.cc
    └── WORKSPACE


cc_library(
    name = "some_lib",
    srcs = ["some_lib.cc"],
    hdrs = ["some_lib.h"],
    copts = ["-Ithird_party/some_lib"],
)







