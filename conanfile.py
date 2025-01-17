from conan import ConanFile
from conan.tools.files import copy
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain, cmake_layout


class PocoTestConan(ConanFile):
    name = "poco_test"
    version = "1.0.0"
    exports_sources = "src/*", "CMakeLists.txt"
    settings = "os", "arch", "compiler", "build_type"
    license = "Proprietary"
    package_type = "application"

    requires = (
        "poco/1.13.3"
    )

    default_options = {
        # Disable poco modules that we do not use.
        "poco/*:enable_json": False,
        "poco/*:enable_util": False,
        "poco/*:enable_crypto": False,
        "poco/*:enable_data": False,
        "poco/*:enable_data_mysql": False,
        "poco/*:enable_data_postgresql": False,
        "poco/*:enable_data_sqlite": False,
        "poco/*:enable_encodings": False,
        "poco/*:enable_jwt": False,
        "poco/*:enable_mongodb": False,
        "poco/*:enable_netssl": False,
        "poco/*:enable_redis": False,
        "poco/*:enable_xml": False,
        "poco/*:enable_zip": False,
        "poco/*:enable_activerecord": False,
    }

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

        deps = CMakeDeps(self)
        deps.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

