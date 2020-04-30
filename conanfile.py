from conans import ConanFile, tools
from conans.errors import ConanInvalidConfiguration
import os


class ImmerConan(ConanFile):
    name = "immer"
    description = "Postmodern immutable and persistent data structures for C++"
    topics = ("conan", "immer", "data structures")
    url = "https://github.com/bincrafters/conan-immer"
    homepage = "https://github.com/arximboldi/immer"
    license = "MIT"
    settings = "compiler"
    no_copy_source = True

    @property
    def _source_subfolder(self):
        return "source_subfolder"

    def configure(self):
        minimal_cpp_standard = "14"
        if self.settings.compiler.cppstd:
            tools.check_min_cppstd(self, minimal_cpp_standard)
        minimal_version = {
            "gcc": "5",
            "clang": "3.4",
            "apple-clang": "10",
            "Visual Studio": "14"
        }
        compiler = str(self.settings.compiler)
        if compiler not in minimal_version:
            self.output.warn(
                "%s recipe lacks information about the %s compiler standard version support." % (self.name, compiler))
            self.output.warn(
                "%s requires a compiler that supports at least C++%s." % (self.name, minimal_cpp_standard))
            return
        version = tools.Version(self.settings.compiler.version)
        if version < minimal_version[compiler]:
            raise ConanInvalidConfiguration("%s requires a compiler that supports at least C++%s." % (self.name, minimal_cpp_standard))

    def source(self):
        tools.get(**self.conan_data["sources"][self.version])
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package(self):
        include_folder = os.path.join(self._source_subfolder, "immer")
        self.copy(pattern="LICENSE", dst="licenses", src=self._source_subfolder)
        self.copy(pattern="*", dst=os.path.join("include", "immer"), src=include_folder)

    def package_id(self):
        self.info.header_only()
