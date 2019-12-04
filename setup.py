from cx_Freeze import setup, Executable

base = None    

executables = [Executable("main.py", base=base)]

packages = [
    "idna", 
    "os", 
    "sys", 
    "appscript", 
    "time",
    "modules.api", 
    "modules.rpc", 
    "modules.MacClient",
    "modules.WinClient",
    "json", 
    "logging", 
    "socket", 
    "struct", 
    "uuid",
    "urllib.request",
    "abc"
    ]
includefiles = ['README.md', 'data/settings.json']
options = {
    'build_exe': {    
        'include_files': includefiles,
        'packages':packages,
    },    
}

setup(
    name = "Stadia Rich Presence",
    options = options,
    version = "1.0",
    description = 'This integration sets a Discord Rich Presence of your current Stadia Game.',
    executables = executables
)
