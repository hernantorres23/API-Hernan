from pathlib import Path
 
path = Path(r"C:\Users\hernan\Desktop\Tribal\tribal\Lib")

 
for dirs in path.iterdir():
    if dirs.is_dir():
        print(dirs.name)