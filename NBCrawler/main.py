import settings
import platform

## os_valdation ##
if (platform.system() != 'Darwin'):
    print('your OS is not supported')
    exit()

