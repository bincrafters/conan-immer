from conans import ConanFile, tools
import os


class ImmerConan(ConanFile):
    name = "immer"
    description = "Postmodern immutable and persistent data structures for C++"
    topics = ("conan", "immer", "data structures")
    url = "https://github.com/bincrafters/conan-immer"
    homepage = "https://github.com/arximboldi/immer"
    license = "MIT"  # Indicates license type of the packaged library; please use SPDX Identifiers https://spdx.org/licenses/
    no_copy_source = True

    _source_subfolder = "source_subfolder"

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
