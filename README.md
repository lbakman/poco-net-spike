# Spike for verifying poco/1.13.0 recipe issue

Conan: 2.11.0
Compiler: mingw-builds/14.2.0

Conan profile: mingw_host and mingw_build

Reproduce from current directory: `conan build . -pr:h=mingw_host -pr:b=mingw_build --build=missing`

