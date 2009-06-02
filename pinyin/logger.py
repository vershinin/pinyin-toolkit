import os
import logging

import utils

# Output to file
logfilepath = os.path.join(utils.pinyindir(), "../Pinyin Toolkit.log")

try:
    # Try to use a rotating file if possible:
    import logging.handlers
    loghandler = logging.handlers.RotatingFileHandler(logfilepath, maxBytes=40000, backupCount=0)
except ImportError:
    # Fall back on non-rotating handler
    loghandler = logging.FileHandler(logfilepath)

# Format quite verbosely, so we can grep for WARN
loghandler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

# Create logger with that handler
log = logging.getLogger('Pinyin Toolkit')
log.setLevel(utils.debugmode() and logging.DEBUG or logging.WARNING)
log.addHandler(loghandler)