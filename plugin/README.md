Manual Installation Explanation:
================================
Extract the "missionx_xxx.7z" file into the "{X-Plane}/Resources/plugins" folder.

__Example__: 

"D:\X-Plane\Resources\plugins" (Windows)
or
"/home/{user}/X-Plane/Resources/plugins" (Linux or OSX)



Random Mission Pack Installation:
=================================
1. The "random pack" should be inside the "missionx" plugin folder, search for "random_pack_xxx" file
   or
   Download the latest Random Package from: "https://forums.x-plane.org/index.php?/files/file/41874-mission-x/"
   Click the "Download File" button and search for a file with the highest "random" version name in it.
2. Create the folder: "{XP}/Custom Scenery/missionx".
3. Extract the missionx_random_pack_vX.xxx" file into that folder.
4. You should use Skunkcrafts utility to update the "random pack" once it is installed.

Suggested Libraries:

* mx_library:  https://forums.x-plane.org/files/file/97944-mx_library/

* R2_Library
* MisterX_Library
* 3D People Library
* openscenery-x (has installer)
* RescueX_Library:
Extract the compress file into a "temporary" folder.
You should see two sub folders: RescueX_Lib and RescueX_Terrain (If after extracting the package you see one main folder, only copy the two folders in it).
Copy the two folders into the "Custom Scenery" directory.



END OF Installation
===================

---

Troubleshooting:
======================================================


Troubleshooting Libraries For Windows OS
-----------------------------------------
If the plugin won't load and you face an error, in the Log.txt file, similar to:
    missionx/win_x64/missionx.xpl : Error Code = 126 : The specified module could not be found.

That might point to missing libraries from the latest redistributable visual studio file.

Solutions:
----------
Navigate to: https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist page.
Pick the "latest version of the "Latest supported Redistributable version"
Download the latest "vc_redist.x64.exe" file and install it.
or 
search for "visual c ++ redistributable for visual studio download".
You should download the "vc_redist.x64.exe" in the "Visual Studio 2015, 2017, 2019, and 2022" section.


---

Troubleshooting Library issues on a Linux OS 
--------------------------------------------
The minimal version for X-Plane should be Ubuntu 24.04 LTS.

If you have "ldd" installed then do the following first:
> cd {X-Plane Install Folder} # This is the root folder, not the plugin one.

>ldd Resources/plugins/missionx/lin_x64/missionx.xpl

You should see a list of libraries names and from which location it is being used. All libraries should have a used location.
Snippet Output Example:


	linux-vdso.so.1 (0x00007ffcc171a000)
	libfmod.so.13 => ./Resources/plugins/missionx/libs/64/libfmod.so.13 (0x00007f4c75e04000)
	libcurl.so.4 => /lib/x86_64-linux-gnu/libcurl.so.4 (0x00007f4c75d75000)
	libstdc++.so.6 => /lib/x86_64-linux-gnu/libstdc++.so.6 (0x00007f4c75b37000)
	libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007f4c75a50000)
	libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007f4c75a30000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f4c75806000)
	/lib64/ld-linux-x86-64.so.2 (0x00007f4c76c1d000)
	libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007f4c75801000)
	librt.so.1 => /lib/x86_64-linux-gnu/librt.so.1 (0x00007f4c757fc000)
	libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007f4c757f7000)
	libssl.so.3 => /lib/x86_64-linux-gnu/libssl.so.3 (0x00007f4c75753000)
	libcrypto.so.3 => /lib/x86_64-linux-gnu/libcrypto.so.3 (0x00007f4c75311000)
	libz.so.1 => /lib/x86_64-linux-gnu/libz.so.1 (0x00007f4c752f3000)

The libfmod could be pointing to the X-Plane "dll" folder while the libcurl, crypt and ssl should be taken from the OS.
The latest linking will search for libraries in the following order: 
"/usr/local/lib64", 
"/usr/local/lib", 
"/usr/local/lib", 
"/usr/lib64", 
"/usr/lib", 
"/lib64", 
"/lib/x86_64-linux-gnu" and
"/usr/lib/x86_64-linux-gnu" in the hope that it will find the "native" os library.

__For example:__
If the "ldd" command points to "libssl.so" library but you have "libssl.so.3", then you can add a symbolic link to it. This is also a reason why it fails to "find" the library. 
The easy solution is to add that symbolic link in the same folder using "root".
_Example:_
$ cd /lib/x86_64-linux-gnu/
$ ln -s /lib/x86_64-linux-gnu/libssl.so.3 libssl.so

How to share libraries at system level
--------------------------------------

If the OS is missing a library, consult the internet hot to install it.
If you just want it to be available for Mission-X plugin, then place it in the "{XP}/Resources/plugins/missionx/libs/64" folder and check if that works for you.

__Run the commands as root (at your own risk)__

> sudo su -   
cd "/lib/x86_64-linux-gnu"  (In Mint 20.1. Search library folders can be different in other distributions)

Or

> cd "/lib/" or "/usr/lib"  (In other distros, but your mileage may vary)

 FMOD Library 
-------------
If FMOD library is missing too from your Linux Distro and the "ldd" command does not point to the plugin "./libs/64" folder, you  can do the same with it:
> ln -s {xp}/Resources/plugins/missionx/libs/64/libfmod.so.13.3  /lib/x86_64-linux-gnu/libfmod.so.13

To validate pluign sees all needed libraries, execute:

> cd {xp}   installation folder 
 
>ldd Resources/plugins/missionx/lin_x64/missionx.xpl


---

Troubleshooting Library issues on a OSX
========================================
The cURL library should use the shared MacOS library, so no need for custom build of this library.
        
If plugin does not load, you can use the "otool" application to check the library.
If you have "otool" installed, you can run the following command from {XP} installation folder:
$ cd {XP} installation folder
$ otool -L Resources/plugins/missionx/mac_x64/missionx.xpl

