from toolchain import CythonRecipe


class PhotoRecipe(CythonRecipe):
    version = "master"
    url = "src"
    library = "libphotolibrary.a"
    depends = ["python"]
    pbx_frameworks = ["UIKit", "Photos", "MobileCoreServices"]

    def install(self):
        self.install_python_package(name="photolibrary.so", is_dir=False)

recipe = PhotoRecipe()


