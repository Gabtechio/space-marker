import cx_Freeze
import cx_Freeze.executable
executaveis = [ 
    cx_Freeze.Executable(script="main.py",icon = "assets/space.ico")]

cx_Freeze.setup(

name = "space",
options = {
    "build_exe":{
        "packages":["pygame"],
        "include_files":["assets"]
    }
}, executables = executaveis
)

#python setup.py build
#python setup.py bdist_msi