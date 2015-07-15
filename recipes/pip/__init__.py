from toolchain import Recipe, shprint
from os.path import join, exists
import sh
import os
import fnmatch
import shutil


class HostPip(Recipe):
    depends = ["hostpython"]
    archs = 'i386'
    url = ""

    def prebuild_arch(self, arch):
        hostpython = sh.Command(self.ctx.hostpython)
        sh.curl("-O",  "https://bootstrap.pypa.io/get-pip.py")
        shprint(hostpython, "./get-pip.py")

recipe = HostPip()


