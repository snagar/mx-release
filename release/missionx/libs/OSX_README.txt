Latest Universal cURL Dynamic libraries needed for MacOS - x86_64 and arm64.
============================================================================
The cURL library should use the shared MacOS library, so no need for custom build of this library.
        
If plugin does not load, you can use the "otool" application to check the library.
If you have "otool" installed, you can run the following command from {XP} installation folder:
$ cd {XP} installation folder
$ otool -L Resources/plugins/missionx/mac_x64/missionx.xpl

