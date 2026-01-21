from pathlib import Path

home = Path.home()
print(home)

import ctypes

is_admin = ctypes.windll.shell32.IsUserAnAdmin()
print(is_admin)

# temp cleaner
# Downloads folder organizer
