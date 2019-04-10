from .base import *

from .crispy_forms import *
from .localflavor import *
from .sagii import *

def update_db_config():
    global DATABASES
    db_globals = { k: v for k, v in globals().items() if k.startswith('DB_')}
    d = {}
    for k, v in db_globals.items():
        splited = k.split('_')
        kname = splited[1].lower()
        d[kname] = d.get(kname, { splited[2]: v })
        d[kname].update({ splited[2]: v})

    DATABASES.update(d)
