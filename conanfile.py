from conans import ConanFile, tools
import os

required_conan_version = ">=1.33.0"


class ZstrConan(ConanFile):
    name = "zstr"
    description = "A C++ header-only ZLib wrapper."
    license = "MIT"
    topics = ("conan", "zstr", "zlib", "compression")
    homepage = "https://github.com/mateidavid/zstr"
    url = "https://github.com/conan-io/conan-center-index"
    no_copy_source = True

    @property
    def _source_subfolder(self):
        return "source_subfolder"

    def requirements(self):
        self.requires("zlib/1.2.11")

    def source(self):
        tools.get(**self.conan_data["sources"][self.version],
                  destination=self._source_subfolder, strip_root=True)

    def package(self):
        self.copy("LICENSE", dst="licenses", src=self._source_subfolder)
        self.copy("*", dst="include", src=os.path.join(self._source_subfolder, "src"))
