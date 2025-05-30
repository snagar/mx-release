
Manual Installation Explanation:
================================
Extract the "missionx_xxx.7z" file into the "{X-Plane}/Resources/plugins" folder.

Examples: 
---------
"D:\X-Plane]Resources\plugins" (Windows)
or
"/home/{user}/X-Plane/Resources/plugins" (Linux or OSX)



Random Mission Pack Installation:
=================================
1. The "random pack" should be inside the "missionx" plugin folder, search for "random_pack_xxx" file
   or
   Download the latest Random Package from: "https://forums.x-plane.org/index.php?/files/file/41874-mission-x/"
   Click the "Download File" button and search for a file with the highest "random" version name in it.
2. Create the folder: "{XP}/Custom Scenery/missionx".
3. Extract the random_vX.xxx" file into that folder.



< ========= END OF Installation ======================


======================================================
======================================================
Troubleshooting:
======================================================


======================================================
=== Troubleshooting Libraries For Windows OS
======================================================
If the plugin won't load and you face an error, in the Log.txt file, similar to:
    missionx/win_x64/missionx.xpl : Error Code = 126 : The specified module could not be found.

That might point to missing libraries from the latest redistributable visual studio file.

Solutions:
----------
Please download "https://aka.ms/vs/17/release/vc_redist.x64.exe" file and install.
The main page for this file can be found in: "https://learn.microsoft.com/en-US/cpp/windows/latest-supported-vc-redist?view=msvc-170#visual-studio-2015-2017-2019-and-2022"
or 
search for "visual c ++ redistributable for visual studio download".
You should download the "vc_redist.x64.exe" in the "Visual Studio 2015, 2017, 2019, and 2022" section.




======================================================
=== Troubleshooting Library issues on a Linux OS 
======================================================
Newer versions of Linux distributions might not need these additional steps, so validate first if the plugin loads and only then condiser adding symbolic links or add the "missing" libraries.                     

If you have "ldd" installed then do the following first:
$ cd {X-Plane Install Folder}, this is the root folder, not the plugin one.
$ ldd Resources/plugins/missionx/lin_x64/missionx.xpl

You should see a list of libraries names and from which location it is being used. All libraries should have a used location.
Snippet Output Example:


	linux-vdso.so.1 (0x00007ffcc171a000)
	libfmod.so.13 => ./Resources/plugins/missionx/libs/64/libfmod.so.13 (0x00007f4c75e04000)
	libcurl.so.4 => ./Resources/plugins/missionx/libs/64/libcurl.so.4 (0x00007f4c75d75000)
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
In rare cases, the cURL will be pointing to the plugins "libs/64" folder.
The latest linking will search for libraries in the following order: "/usr/local/lib64", "/usr/local/lib", "/usr/local/lib", "/usr/lib64", "/usr/lib", "/lib64", "/lib/x86_64-linux-gnu" and "/usr/lib/x86_64-linux-gnu", in the hope that it will find the "native" os library.
In the worst case, it will search in "./Resources/plugins/missionx/libs/64" folder too.
For best stability, the crypto and ssl libraries should be from the same location, either taken from the OS or from the plugin but not mixed.

Before using the "shared" libraries in the plugin, I suggest you to check if the same library is missing in the default symbolic link, for example:
The "libssl.so.3" might have a missing "libssl.so" symbolic link, hence it fails to find it. The easy solution is to add that symbolic link in the same folder using "root".
Example:
$ cd /lib/x86_64-linux-gnu/
$ ln -s /lib/x86_64-linux-gnu/libssl.so.3 libssl.so

 
If a library is missing and you want it to be shared with the whole system then place it in one of the "/lib" or "/usr/lib" folders using "root".
If you just want it to be available for Mission-X plugin, then place it in the "{XP}/Resources/plugins/missionx/libs/64" folder and check if that works for you.

----------------------------------------------
--- How to share libraries at system level ---
----------------------------------------------


Run the commands as root (at your own risk)
-------------------------------------------
$ sudo su -   
$ cd "/lib/x86_64-linux-gnu"  (In Mint 20.1. Search library folders can be different in other distributions)
  Or
$ cd "/lib/" or "/usr/lib"  (In other distros, but your mileage may vary)

## You have 2 options, either copy the libraries from the plugin to the OS lib folder or create symbolic links to the libraries in the plugin.
Option I - Copy lib to OS library:
----------------------------------
$ cp {XP}/Resources/plugins/missionx/libs/64/libssl.so.3      /lib/x86_64-linux-gnu
$ cp {XP}/Resources/plugins/missionx/libs/64/libcrypto.so.3   /lib/x86_64-linux-gnu
$ cp {XP}/Resources/plugins/missionx/libs/64/libcurl.so.4.8.0 /lib/x86_64-linux-gnu

$ ln -s /lib/x86_64-linux-gnu/libssl.so.3      /lib/x86_64-linux-gnu/libssl.so
$ ln -s /lib/x86_64-linux-gnu/libcrypto.so.3   /lib/x86_64-linux-gnu/libcrypto.so
$ ln -s /lib/x86_64-linux-gnu/libcurl.so.4.8.0 /lib/x86_64-linux-gnu/libcurl.so
$ ln -s /lib/x86_64-linux-gnu/libcurl.so.4.8.0 /lib/x86_64-linux-gnu/libcurl.so.4
 
Option II - create symbolic links to the plugin library:
----------------------------------
$ ln -s {xp}/Resources/plugins/missionx/libs/64/libssl.so.3  /lib/x86_64-linux-gnu/libssl.so.3
$ ln -s {xp}/Resources/plugins/missionx/libs/64/libssl.so.3  /lib/x86_64-linux-gnu/libssl.so

$ ln -s {xp}/Resources/plugins/missionx/libs/64/libcrypto.so.3  /lib/x86_64-linux-gnu/libcrypto.so.3
$ ln -s {xp}/Resources/plugins/missionx/libs/64/libcrypto.so.3  /lib/x86_64-linux-gnu/libcrypto.so

$ ln -s {xp}/Resources/plugins/missionx/libs/64/libcurl.so.4.8.0  /lib/x86_64-linux-gnu/libcurl.so.4.8.0
$ ln -s {xp}/Resources/plugins/missionx/libs/64/libcurl.so.4.8.0  /lib/x86_64-linux-gnu/libcurl.so.4
$ ln -s {xp}/Resources/plugins/missionx/libs/64/libcurl.so.4.8.0  /lib/x86_64-linux-gnu/libcurl.so


 FMOD Library 
----------------
If FMOD library is missing too from your Linux Distro, you  can do the same with it:
$ ln -s {xp}/Resources/plugins/missionx/libs/64/libfmod.so.13.3  /lib/x86_64-linux-gnu/libfmod.so.13

To validate pluign sees all needed libraries, execute:
$ cd {xp}   installation folder
$ ldd Resources/plugins/missionx/lin_x64/missionx.xpl




======================================================
=== Troubleshooting Library issues on a OSX
======================================================
The cURL library should use the shared MacOS libarry, so no need for custom build of this library.
        
If plugin does not load, you can use the "otool" application to check the library.
If you have "otool" installed, you can run the following command from {XP} installation folder:
$ cd {XP} installation folder
$ otool -L Resources/plugins/missionx/mac_x64/missionx.xpl


















