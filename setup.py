from cx_Freeze import setup, Executable

base = None    

executables = [Executable("app.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "GPT-3",
    options = options,
    version = "3.5",
    description = 'Windows co-pilot free version for programming tasks',
    executables = executables
)