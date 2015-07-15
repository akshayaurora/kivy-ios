from toolchain import Recipe, shprint
from os.path import join, exists
import sh
import os


class GMPRecipe(Recipe):
    version = "6.0.0a"
    #url = "https://gmplib.org/download/gmp/gmp-{version}.tar.bz2"
    url = 'src'
    library = ".libs/libgmp.a"
    #include_dir = [
    #    ("jmorecfg.h", ""),
    #    ]
    include_per_arch = True


    def build_arch(self, arch):
        build_env = arch.get_env()
        configure = sh.Command(join(self.build_dir, "configure"))
        shprint(configure,
                "CC={}".format(build_env["CC"]),
                "LD={}".format(build_env["LD"]),
                "CFLAGS={}".format(build_env["CFLAGS"]),
                "LDFLAGS={}".format(build_env["LDFLAGS"]),
                "--prefix=/",
                "--host={}".format(arch.triple),
                "--disable-shared",
                "--enable-static")
        shprint(sh.make, "clean")
        shprint(sh.make)

recipe = GMPRecipe()


