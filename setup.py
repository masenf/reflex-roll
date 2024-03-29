from pathlib import Path
from setuptools import setup
from setuptools.command.build_py import build_py


class build_py_with_pth_file(build_py):
     """Include the .pth file for this project, in the generated wheel."""

     def run(self):
         super().run()

         destination_in_wheel = "reflex_roll_hook.pth"
         location_in_source_tree = Path("src", "reflex_roll_hook.pth")
 
         outfile = Path(self.build_lib, destination_in_wheel)
         self.copy_file(location_in_source_tree, outfile, preserve_mode=0)


setup(
   cmdclass={"build_py": build_py_with_pth_file},
)