from distutils.cmd import Command

class build_py(Command):
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...