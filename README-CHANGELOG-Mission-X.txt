Installation:
==================================================================
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!! Pick the X-Plane Main Folder (not any sub folder in it)  
!!!
!!! Examples:
!!! "D:\X-Plane" (Windows)
!!! or
!!! "/home/{user}/X-Plane" (Linux or OSX)
!!! Remember to read the README.txt file in the plugin folder.
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

v25.03.3
=========
1. [new] Added Simbrief support. You have to add your "pilot id" in the setup screen.
2. [new] You can generate a mission based on Simbrief. Currently it only supports building the " Departure + Arrival" waypoints.
3. [ui] Minor "external FPLN" screen re-design.
4. [bug] Rear CTD related to internal formatting of the SQL query.
5. [ui] For channel based approaches, like: LPV/WAAS, I added the "ident" field which represents the "approach procedure identifier".
6. [ui] Minor redesign the "FLight plan + Notes" screen.
7. [ui] Added "commit + close" and "cg" to the Inventory screen.
8. [bug] DME/VOR data failed to fetch due to wrong "container" sent to "format" function.




v25.03.2
=========
1. [bug] Fixed inventory element is not reading correctly when layout is xp12 in the mission file.
2. [bug] Fixed item re-locating into the stations when switching plane in the middle of a mission.

v25.03.1
=========
1. [bug] Fixed "acf station" parsing, when stations numbers are not sequential.
2. [bug] Fixed Inventory not initialize correctly between missions.
3. [ui] Changing plane mid mission, should correctly handle item transition. Best done in an inventory area, if you are using the xp12 inventory layout.
4. [bug ui] Template option for legacy <opt> nodes, were displayed even if none defined in the template file.
5. [setup] The cycle of the "mission.log" file, between xp sessions, has an enable/disable option.
6. [fix] when using templates, the "link_to" attribute should not hold duplicate task names.
7. [bug] Fixed "ATTRIB_SET_OTHER_TASKS_AS_SUCCESS" and the other two "set" attributes not read from the <outcome> element.
8. Some grammar fixes.
9. [template] Added "mission_file_format" to the <template> node. It will be used in the target mission file "version" attribute <MISSION version=''>.
10. [save/load] Better support for inventory layout during save and load checkpoints.





v25.02.1
=========
1. Changed "helos + medevac" task rules. You can either "hover" or "land" to finish the "flight leg".
1.1 Added special "markers" to show the landing and hover areas. You can hide them using the "show/hide" target markers (you will need the new "random_pack" file that can be found in the root plugin folder).
2. [ui] You can now define the "starting weights" for the "pilot, passengers and cargo".
    These payloads are best use with XP11 inventory layout. In XP12 inventory layout only the pilot weight will be added to the payload weight.
    Please do remember that the weights you define are on top of any item you move "to the plane".
3. [setup] You can suppress the "distance messages" that are created by the "Random Engine".


v25.01.1
=========
1. [ui] Inventory layout supports X-Plane 11 and 12, Check designer guide for more detail information.
2. [embedded] The old inventory functions were modified to support the XP12 layout (stations), check "designer guide" for more information.
3. [designer] Items can be marked as mandatory, and be restricted to only move to specific external inventories.
4. [templates] In the "Designing Templates" document, Please check the "planned deprecation attributes" in the "Breaking Changes" topic.
5. [new][templates] Added support to "multi-option" in the "templates" screen. It supports the "old" and "new" formats, but the "old" format will be deprecated in the near future (asked by @RandomUser).

The extended feature allows you to define few "option groups" with their specific options (<opt>), that way you can allow the simmer to tailor their missions. Example: "weather group" or "inventory compatibility" group.

Quick fix, to be compatible with the new format, you need to enclose all "<opt>" elements with <option_group name="short group name"> element.
Check the "Designing Templates" document for more information under the "Dynamic Templates topic".

6. [win_x64] Refreshed the libraries.

[known issues] Sometime an item with "zero" amount is not cleared from the inventory, but it does not break anything either.


v24.12.2 
========
Beta2:
------
1. More Inventory refinments.  
   [script] Added and modified existing function inventories. All should be compatible with both inventory types. Check designer guide.


Beta1:
------
1. [ui] Inventory Layout supports X-Plane 12 "stations" feature. This will directly affect the CG. Currently only works with "Random Generated" missions (see designer documentation).
2. [bug] Fixed "runway centre" stats query. Did not set all bind variables.
3. [bug] Fixed a case where a template mission and default radius definition did not pick the "default radius length". That failed the mission to be created due to radius of "0" nm (thanks @RandomUser).
4. [inv] Duplicate items in the inventory, will be merged to one instance. No duplicate items in inventories, yay.
5. [setup] Added XP11 Inventory compatibility option (should force the layout were there is one big container for all of our items = "no xp12 station shananigans").


v24.12.1
========
1. [ui] Added "jets" and "heavies" planes to the "create mission screen".
2. Mainly internal modifications that will help with future features.


v24.06.1
========
1. Removed most of the templates. You can still find them as a compressed file at the same plugin folder.
2. [os] Plugin should work correctly for Ubuntu/Fedora distros (According to my tests).
3. [bug] Fixed cases where missions that were generated from the "ILS or External FPLN", did not create GPS information.
4. [bug] Fixed localizer information not showing in the "Nav Information" screen.
        Localizer information will display ILS and LOC first and then the other types, like GLS, LPV etc.
5. [ui] Solved the flickering table information in the "External FPLN" and "ILS" screen.
6. [ui] Inventory image item sizes were changed 45x65 to 50x40.
7. [ui] Added more feedbacks when fetching information from the external flight plan site.
8. [ui] Fixed OSM filter popup window size.
9. [ui] When "airports information" is running, the home labels under the icons will be disabled with their respective image button.
10. [internal] Shorten the "request" timeout to external sites.
11. [lib] New Imgui 1.91.1, libCURL and OpenSSL. Removed support to OpenSSL 1.x
12. Added the random pack with the compressed plugin. You still need to copy and extract it in "{xp}/Xustom Scenery/missionx" folder.


v24.05.2
========
1. [internal] Compiled with C++20 support.

v24.05.1
========
1. [bug] Localizer filter not working.
2. First implementation - Exposed the "Cargo" categories of the dynamic mission screen inside an XML file so user can define their own cargo mission type and items.
2.1 Added "cargo_data.xml" file that holds the "cargo" drop down categories .
2.2 In the "cargo_data.xml" file there are also "item_blueprints" for each type of the mission categories. You can have multiple multiple category type for each "item_blueprint" element but the plugin will pick the first it will find, so you can't define same category type in multiple "item_blueprints".
3. Moved the "sql.xml" file to root "libs" folder, next to the "cargo_data.xml"


v24.03.2
========
1.  Added "designer mode" option to manipulate the state from the setup and creation mission screens. Any definition in the XML file though, will have precedence.
2.  [bug] Fixed long standing bug/error, where the mission file "weight attributes" were not read correctly.
    - Fixed all templates to have the correct weights attributes.
    - Added compatibility code to the old attribute names.
3.  [bug] Fixed a rare crash that could happen if you quite a mission and tried to generate a cargo based helos mission.
4.  [bug] Fixed the RGB Hex color translation.
5.  [bug] Fixed debug "flight leg" does not show correctly the status of the trigger it is link to.
6.  [bug] Fixed "info and error" messages not displayed after loading a mission.
7.  [bug] Fixed "Setup screen" displayed "Linux Troubleshooting" title instead of "Designer" title.
8.  [bug] Fixed a crash caused by METAR thread not cleaned and another thread is being called. Added activity test before allowing the search to be re-executed.
9.  [ui] Added "Abort Metar Request" button, to stop the METAR thread.



v24.03.1
========
1. [ui] Added "Flight Planning/Notes" screen for easier IFR planning. Can be useful in VR.
  - The "Briefer" button was renamed to "Flight Planning/Progress" and it is available all the time.
  - When a mission is in progress, there will be different active color around that button.
  - The saved "Flight planning" info, is stored in the "properties" file and not in the plugin folder.
  - You can directly open the NavData screen once you enter the "Departure/Arrival" ICAOs.

2. [apt.dat] Fixed boundary reading from apt.dat files.
3. [NavData] Added frequency data per airport.
4. [NavData] Integrated METAR reading from "flightplandatabase.com". I suggest to add the API key in the "external FPLN" screen.
5. [NavData] Modified the VOR/DME/NDB query to "concolidate" VOR & DME navaids if they are on the same freq and name.
6. [NavData] Added the "To ICAO" filter option in the NAV Data and ILS Search.
   - It will look for all ICAOs containing the entered string.
   - You can ignore distance filtering if you entered more than 2 characters.
7. [ui] ILS and External FPLN screen can now open the NavData directly when clicking on the ICAO column.
8. [ui] Flight Leg title is wrapped if it is too long.
9. [ui] Removed the scale font button from the "flight leg" screen, can be modified through the "setup" screen though.
10. [ils] Added row limitation up to 2000 rows (performance hit dependent on your machine capabilities).
11. [ils] Fixes the behavior of the "ILS elevation slider" auto scroll.
12. [lib] Implemented nlohmann json lib.
13. [lib] Updated GLM lib from v0.99 to v1.0.1
14. [sql] Made the base "ILS Search query" a custom one, meaning we read it from sql.xml file.
15. [bug] Fixed [start mission] button not immediately visible after generating ILS mission.


v24.02.7
========
1. VR fixes.
2. Added airport elevation to Nav Data.
3. Hopefuly fix a CTD when DB stats data are too many (at the end of a mission).

v24.02.6
========
1. Last minute bug fixes.
2. [bug] Repeating a background sound file fails due to its length.
3. [bug] Fixed a CTD in "debug" mode when trying to open the "message" tab.
4. [setup] Minor ui reorganization in the "setup -> advanced settings" section.
5. [debug] Added "abort all channels" in "message" debug tab.


v24.02.5
========
1. New Nav Data screen integrated with the ILS screen. You can use it during flight too.
2. Cleaned the bitmap folder and replaced few textures.
3. Apt.dat optimization will store navigation data like VOR, DME and NDB with the ILS table data.
4. [script] Added "fn_update_end()" function to directly modify the <end_mission> attributes, check "designer guide" documentation.
5. sql.txt has new Nav data search queries.
6. Syntax fixes.


v24.02.4
========
1. [map 2D] Added support for CueInfo to be displayed inside the 2D map. This could be very useful for designers when working in XP12, since only in XP11 you can see the cue info in the 3D world.
   This is a compromise until I figure out how to to do the same in XP12.
   You have to "opt-in" to see the CueInfo. You can turn it on from the "menu" or from the "setup screen" (toggle designer + toggle Cue Info).
   You need both options to be checked to see the Cues.
2. [fix] After changing the order that the plugin reads the "description" text, we need to make sure to ignore "comment" tags, since "<![cdata" nad "<!--" belongs to same category.
3. ILS screen is available during active mission.
   - When mission is active - you can search for ILS runways of any airport (entered manually).
   - When No mission is active - you can build a simple mission to practice ILS landings. 

v24.02.3
========
1. [critical bug medevac triggers] Fixed a nasty bug that failed triggers based elevation. Should affect any random medevac mission that needed hovering.
2. [mix] Added loop command ("L"/"l") to the background <mix> instructions.
3. [msg] fade_bg_channel attribute supports "%self%".
4. [bug] Fix sound file fail to load due to racing state.
5. [debug] Added "debug message" tab. Good for:
  - test messages without the need to fly the mission route itself.
  - test standard messages sound files.
  - test new background sounds with story messages. You play the message, and then play in the background the sound file and see if they "fit".
6. [bug] If sound file is not opening, it will now flag it as "invlalid" and it will continue progressing message preparation. Old behavior, message state was stuck at the sound file loading state.
7. Added the ILS types: "GLS, LP and LPV" to the ILS search screen and the database.


v3.2402.1
=========
1. [ui debug] Debug tab now has "script", "global params" and "interpolation" new sub tabs.
2. [ui debug] script/trigger debug enhancements:
     - Errors can be ignored in the "setup screen" (mission won't abort on script failure).
     - You can edit the script in memory and test it until you fix the issue. It won't be stored in the original mission file, only in savepoint.
     - Added Force trigger event fire to manually test a trigger outcome, instead of flying the whole route just to make it fire. You can only force triggers linked to the <leg> and not part of tasks, for example.
3. [ui debug] The debug tab received a bigger vertical window space to show more information.
4. [ui debug] Added more information on the trigger and task nodes.
5. [designer dump data] In the setup screen in the "designer" tab, you now have buttons that will dump each "in memory" loaded mission part into the log file.
  You can achieve similar effect when creating a savepoint, the save file stores the in memory information.
  This should provide insight regarding what the plugin uses or what you think it is using.

6. [story mode] Fixed cases where last line in the message was not displaying correctly.
7. [story mode] Added "Auto skip" message checkbox, for story mission writers. You can manage it from the "Setup" window or map a key/button as a command.
  The option will be hidden in release binaries, but you can toggle it, and shown in the debug binary build.
8. [story mode log] When loading a mission with a story mode message, the plugin will try to evaluate the time it will take it to display the lines for each message.
  This is only an estimation but a good starting point for managing the background sound files while displaying the message itself.
9. [story mode, interpolation] Added log messages to better understand when interpolation occurred. You can also use the "[debug]<interpolation>" tab to see the same.

10. [script] you can send a predefined parameters to any script using a the pipe symbol "|" and then a set of parameters in the format "in{Name1}=value,in{Name2}=value" string.
  - The ad-hoc parameter must start with the "in" prefix.
  - Added support for "%self%" keyword as the "value" of a predefined parameter. This is mainly useful with "dynamic_message"s that creates triggers and we do not know them ahead of time.
    It is also depends on how you write your script.
    In most cases, you better use the mxCurrentTrigger which is seeded in every script that was called from a trigger.
11. [script] Added "fn_set_leg_desc()" and "fn_get_current_leg_desc()". You can now modify the flight leg description during the mission.
12. [script] Added more seeded info when calling "fn_get_message_info()" function.
13. [script] Added fn_get_active_choice_name()                

14. [message] Added "ATTRIB_FADE_BG_CHANNEL" attribute to <message> to auto fade the background channel once message is done.
  This can also be achieved through a script.
15. [message] Extended the properties you can modify from a script using the "fn_set_message_property()" function.

16. [ui] Some ui modification for better readability.
17. [ui] Added some more icons to the story mode window and quit popup window.

18. [timer] Extended <timer> element.
   You can flag it to not abort: fail_on_timeout_b.
   Added "post_script" call only on timer failure.
   Added: "stop_on_leg_end_b" attribute that can replace the "run_until_leg".
   
19. [bug] fixed cases where trigger "enabled" attribute was not taken into account, so it was always in "enabled" mode.
20. [bug] Fixed a bug where dynamic messages retain the <outcome> source attributes.
21. [regression] Fixed <choice> is not being read correctly after loading a savepoint.
22. [regression] "fn_get_global_bool" was not registered with the correct naming.
23. [bug] When generating a mission file from LittleNavMap, the <gps> sub elements were named <node> instead of <point>.
24. [bug db] Fixed rear case where there is icao_id in metadata table and not in the xp_airports. This fail one of the post parse fixes to sync icao names based on xp_airports back over the metadata table.

25. Changed the order the code reads and store "next_msg" vs "post_script".
   Old behavior: "post_script" was execute last.
   New behavior: "next_msg" is read last and "post_script" is read first (before all other attributes).
                 You can branch the message using "post_script" and fn_set_message_properties() -
                 Modify the "next_msg" property with the new msg name.
26. Changed the order how we read the description from a "flight leg" element. The new order is: "read [cdata] under leg and only then under <desc> sub element."
27. The plugin load mission messages has been re-formated but it is still a w.i.p.
                 
28. [plugin] The plugin is using a newish version schema in the format: {major}.{YearMonth}. The full version will be displayed in the "about" screen.
29. [plugin] The plugin is using the "new" folder names for the binary files. Also moved some folders inside other ones to reduce the folder clutter.
30. [lib] Latest ImGui v1.9.0.1
31. [save] interpolation data is written into the save file.
32. [log] the plugin will retain the last three missionx.log files in cycle order.




v3.306.2
=========
1. [ui] Added "debug" tab. Can be toggled in the "setup > developer" options.
2. [log] Mission-X now has its own dedicated log file in the root folder of the plugin.
        Most messages are now written from a thread.
        This reduces file writing in the main flight loop back, which makes the DEBUG build run smoother.
3. [internal] re-written how to handle the "output" from "print" commands from external scripts.
4. [internal] Added internal code to display function timing to better find performance bottlenecks.


v3.306.1c
=========
1. [bug] When using cached images the story logic is not advancing.
2. [trig] Better handling triggers that rely on "exiting" from the trigger area rather than "entering" the trigger area.
   This solved false positive triggers, when positioning plane due to XP own "limitations".
3. [sound] Better sound cancelation handling.  
4. Removed "timer_type" attribute that was added in v3.306.1. Should always be "os" based.


v3.306.1b
=========
1. [embedded] New functions: "fn_get_xp_version()", "fn_abort_bg_channel()" and "fn_fade_out_bg_channel()"
2. [doc] Updated both Designer and Template documents.
3. [break] Renamed "fn_is_mxpad_queue_empty()" to "fn_is_msg_queue_empty()"
4. [break] Removed function: "fn_end_current_message_and_background()"; you can use "fn_abort_message()" instead.
5. [trig] Added attribute: "message_name_when_entering_physical_area" to the <outcome> trigger sub-element.
   Although it is a long one, the idea behind it is to kill two birds with one trigger.
   Should be used only when we want to send an immediate notification to the simmer, even if not all conditions are met.
   Example:
     Case: When the pilot reaches their destination, we might want the pilot to shut down the engine for the task to be completed.
    Before, we created two triggers that shared the exact same location that fired the message in the attribute   "message_name_when_fired".
             One trigger for the "quick message" that the pilot needs to shutdown the engine,
             and the second to check the engine state and then flag the task as successful.
             Each trigger had to be linked to a "task" or "leg" element.
     After, we add the attribute "message_name_when_entering_physical_area" to the main trigger task.
            This will call the "quick message" once the plane is in the physical area (pos+elev) -
            while retaining the original "message_name_when_fired" action to be called when all the trigger conditions are met.
            We save a trigger definition and probably one "trigger link" or "task" to manage the "quick message".
           
6. [bug] fixed sound repeat is not working properly.
7. [story] To make it simpler to "calculate" message time,
   The plugin will write to the "Log.txt" file the time it took for the message to be complete.
   This can assist in determining background music time (if you want).
8. [regular msg]  Added "fallthrough_b" attribute to the "message" element.
   This is an edge case where you would like the flight leg to not wait for the message timer to complete
   but continue its evaluation, like transitioning to the next flight leg.
   This attribute won't work on "story" messages.
9. [demo] Updated the "demo mission" with some of the new features. 





v3.306.1a
==========
1. [hotfix] Wrong position for Right Medium image, in story mode.
2. Resized the story mode text.


v3.306.1
==========
1. [feature] New "story mode". Triggered when sending a message. The main screen is divided into a big upper image area and a lower text message area. This is a temporary screen and in the end it will return to the usual flight leg information.
Please read the "Designer Guide" for more information (search for "story mode").
2. [ui] More font tweaking. Setup screen now uses the newer fonts for better readability.
3. [ui] MxPad and Choice windows received some Font face lift.
4. [ui] Some ui tweaks in "Dynamic Mission", "ILS" and "External Flight" screens.
5. [setup] Added "pilot nickname" in setup, can be used in "Story mode".
6. [internal] Lots of code refactoring and code cleanup.
7. [ui] When opening the main plugin screen for the first time, it will force centering and then will revert to free mode.
       Should help resolve cases where we have more than one screen and the window is positioned outside the X-Plane visible view area.
8. [bug] Fixed cases where loaded "CheckPoint" was not able to progress because we saved in the middle of "story mode" message, or Time-lapse was active.
9. [bug] Messages won't progress until the previous message will fully complete, including post actions. This solves cases where the flight leg transitioned to the next one before cleaning the current one.
10. [ui] Plugin main window was decreased back to 800px from 900px but height was increased to 460px from 450px.
11. [bug] When dumping "weather" datarefs, the "change_mode" won't be stored with the other weather datarefs.
12. [lib] Implemented ImGui v1.89.9
13. [lib] Implemented Implot to v0.17.
14. [conv] Conversion screen now has "GlobalSettings" node support if the "save" file includes one.
15. [mix] added "timer_type" to background <mix> so designer can force OS timer (not affected by pause) instead of XP timer.

Known issue:
1. Copy paste works best in Windows. In MacOS only paste seems to work and in Linux no support.



v3.304.14 - final
=================
1. [ui] Continue font integration in the screens. Removed font preference from the setup screen.
2. [internal] removed un-needed properties from the preference file.
3. [ui] Fixed the missing stats info when in VR
4. [ui] Fonts are handled from the libs/fonts/fonts.ini file.
5. Added more stats.
6. [ui] Resized Mission-X main window.



v3.304.14r3
============
1. [ui] New font integration.
2. [ui] Replaced default fonts in many locations so the text should be sharper (no scaling).
3. [bug] Fixed a crash related to ImGui and key handling. Cause: failed to handle special characters.
         Solution: implemented the latest "ImGui::io" key handling.
4. [ui] ICAOs fields now force upper case.
5. [ui] Fixed options window positioning.
6. [lib] Implemented latest MY-BASIC library.
7. [bug] Same map file name was not displaying more than once in two different flight legs.
8. [stats] Added more stats data to the stats table in the DB.
9. [lib] MacOS cURL lib is now using the OS library so no need for my custom cURL library anymore.
        

v3.304.14r2
===========
1. [MacOS] New universal build, compatible with Apple Silicon (tested by @Captain Krasus - thanks).
2. [script] Extended few global related functions to make handling their initialisation simpler.
3. [script] Modified the "fn_get_global_{type}" functions to use a more flexible logic. The main difference is: You can send a default value as a second argument and if the "variable" is not set already, then it will be created it and return the value you sent as initialisation or a default value the plugin sets (if not).
4. [script] All "fn_store_global_{type}" are now deprecated and we should use "fn_set_global_{type}" instead.
5. [cmake] Added "cmake" compilation file that used from "QT Creator", it is not located like most standard project in the root of the project.
6. [internal] Fixed "assert" logic never checked when using "debug" build.
7. [lib] Reimplemented FreeType library and used the latest build (2.13.1)
8. [MacOS] cURL library was compiled as universal binary (support for x86_64,arm64)
9. [doc] Added "First things First" topic for new designers.
10. [lib] Updated library SQlite to v3.42.0.
11. [debug] Added better validation stoppers during mission load. This should assist in finding mission failure loads by the plugin in the Log.txt file.
12. [internal] Fixed when generating a mission from the same template, some "message" and "script" elements were multiplied and not printed just once. This did not break the mission but is confusing.
13. [script] When calling "fn_get_trigger_info()" we now also have: "mx_plane_in_physical_area_b" and "mx_plane_in_elev_volume_b" seeded attributes that can be addressed in the script itself.
14. [bug] Resolved a crash caused by missing <outcome> or <condition> sub-elements in the <trigger> definition.
15. [ui] Designer and Cue sub menu won't be displayed in XP12.
16. [ui] Added "write plane / camera" position  to Log in the menu.
17. [ui] Added "tabs" in the "flight info" screen. Now it also have "stats" tab to the flight leg, still w.i.p
18. [bug] Hopefully solved the "end stats" screen from crashing, related to how it handled data from a text column.
19. [internal] Better burst time "transition" data for "take off and ladings".
20. [internal] Gather_stats Queue read is now better handle. Solves crashes when there is no time rule for flushing to DB.
21. [bug] Fixed weight calculation when starting mission and there is no "weight" element in global settings.
22. [ui] Added "add default weight" checkbox in "generate" popup windows of the ILS and EXTERNAL missions, so user don't have to use the advanced option window.


v3.304.14r1
===========
1. [ui] Modified the "user creation script" with collapse headers to expose more options.
       Medevac missions are now only "helos" based.
2. [ui] Added sub categories to the main mission types. This is still a work in progress (w.i.p).
3. [template] Modified the "blank" template to deal with oil rigs and 3D objects for these mission types.
4. Added "HSF_lib" as a pre-requisite for Random Missions. Mainly used with Oil Rig missions.
5. [internal] Changed the OSM source prioritizing. OSM WEB is default for accidents but OSM DB will be tested first before the OSM WEB if it was flagged.
6. [internal] 3D objects will be first search as "virtual files" and only then as "physical ones".
7. [break] "is_virtual_b" attribute will be deprecated (see 1).
8. [bug] 3D object displayed at the beginning of the mission relative to plane after generating a random mission, instead near the target location.
    Cause: If display object retain the attribute "RELATIVE_POS_BEARING_DEG_DISTANCE_MT" with a valid value, it would immediately translate it to display an object relative to plane. This behavior breaks the 3D object placement in "medevac" missions or templates that used this attribute.
    The fix: When generating the mission those attribute values will be removed but will be written to a "debug_relative_pos" attribute for reference.
9. [regression] RandomMisssion engine ignored "disable_auto_message_b" if it was not numeric value. Now also reads "text boolean values" like "true" or "false". 


v3.304.14 B1
============
1. [feature] Implemented Oil Rig missions - Will work only on X-Plane 12.05 and up.
2. Better ramp search filter.
3. [ui] Added "ignore weight", in the "advanced settings" window, when generating a mission. This is usefull when the weight should be determined by other tool or the simmer like "FSCharter".
4. [db] The airports ICAO now being renamed according to the metadata table. Tables affected "xp_ap_metadata" and "xp_airports".
5. [ui] Added the [advance settings] screen to the "LittleNavMap conversion screen" (feature request by @jkeye).
6. [imgui] Upgraded imgui library to v1.89.5

>> OIL Rig mission notes <<
1. Generated Oil Rig missions are highly dependent on the quality of your apt.dat files. As of this writing only from X-Plane 12.05 and up there are Oil Rig data but it is still in early adoption, so there are many missing Oil Rig information.
2. Each time you will generate a mission, it will randomly pick between the oil rigs and then will try to figure out from which airport to start the mission.
It is up to you to decide if to fly the suggested route, or to generate a new one due to the distance factor.
3. All missions "force" a "helos" type plane when it is being generated.
4. Scenery: I suggest to install all earth regions so no missing tiles will be found.

Last - The Oil Rig mission is still a work in progress, and there are some UI tweaks needs to be done and also template optimisations.



v3.304.13
==========
1. [ui] Fixed flight leg info scroll bar in MXPAD and VR mode too.
2. [ui] In 2D mode, the MX-PAD won't auto hide itself if "options" window is displayed.
3. [ui] modifiled the "load checkpoint" popup window.

4. [random] When generating a Random mission, you can now decide if to store the "current" weather state or not inside the "random.xml" mission file. 
   That way you can prepare a specific set of settings for your random mission and load it next time you will fly it.

5. [bas] Added two external functions: "fn_set_predefine_weather_code()" and "fn_set_datarefs()".
   "fn_set_predefine_weather_code()": allow you to set weather using codes 0..8 in XP12 and 0..7 in XP11.
   "fn_set_datarefs()" is a better implementation of "fn_set_dref_value()". You send one string in the format "key=value|key2=value|...".
6. [bas] Added "fn_load_image_to_leg()" function.
7. [bas] Added "fn_set_datarefs_interpolation()" function to allow a designer to interpolate one or more datarefs.
        You provide the "seconds" and "cycle number" to run the interpolation. The delta values in each cycle is linear.
8. [bas] Added support for 3 "stoppers" by the names "1,2 and 3".
        You can manage them using the new functions: "fn_start_timer", "fn_stop_timer", "fn_get_timer_ended" and "fn_get_timer_time_passed".
        This way you can postpone some actions for later time, based on the timer state.
		Example:
		> Fail certain instrument after 20min of flying.
    > Send a message 5min after take off.
		
		Do remember to stop the timer if you don't need it anymore.

9. [bug] Fixed wrong initialization for int based array datarefs. 
10. [bug] Fixed element duplication when repeatedly generating a mission from a template. This did not break anything, but now it is cleaner.
11. [internal]  ACF datarefs will be gathered on ACF change too.
12. [bas internal] resized SYMBOL max length from 512 to 4098 characters. Useful mailnly for long strings like in "fn_set_datarefs()" function.
13. [save] Weather state will be added to the "save checkpoint" file. 
    The plugin can't promisse to have the exact same weather depiction.

14. Added an option to write the weather state into the Log.txt file for use in scripts or for debug.
  You can call this option from:
  1. Setup screen, in the tools tree.
  2. Command: there is a new command to "dump weather" information.
  3. Menu: there is a new "tools > write weather state to Log.txt file"


v3.304.12 R3
============
1. Fixed plane heading when picking random ramp.
2. [ui] Added popup warning before loading a saved CheckPoint.


v3.304.12 R2
============
1. [internal] Stopped using the cached NavAid file, instead the plugin uses the sqlite db tables.
              Benefits: consistent lookup when searching local NavAids, has less effect when using OSM data.
2. [ui] Minor UI fix for the ILS screen.
3. [ui] Added "force position plane" to the setup screen. Might be useful for designers... and myself.
4. [sqlite] Added "mx_get_point_based_on_bearing_and_length_in_meters(lat,lon,bearing,distance in meters)" will return a string "lat,lon" for the new position. 
5. [sqlite] Added "mx_get_center_between_2_points()" function. Send lat1,lon1,lat2,lon2,
6. [sqlite] renamed: "mx_distance_nm()" to "mx_calc_distance()"
7. [sqlite bug] Fixed the "ramps_vu" query. Wrong field was used for the "jet" search. 
8. [internal] The new filter ramp function will search for valid ramps in the airport based on the plane type, if fails then weill search "jet"/"turbo prop" and then "prop" ramps.
   If all failed and it is the start location, it will pick the begining of the RW OR center of the longest runway if it is the not the starting position.
9. Added SQLiteStudio DLL extension to the libs plugin folder (if you would like to add it to your client).
10. Added the "fighter" ramp data to the tables/views, but as of now does not use it directly in the UI.


v3.304.12 R1
============
1. Added "is_dummy" attribute to <leg> element.
2. Added support for <weather> element in <leg> and <global_settings>.
3. [break] Changed the "dataref" syntax guidelines in <weather>, <datarefs_start_cold_and_dark> and "dataref_to_modify_when_fired" and "dataref_to_modify_when_left" attributes.
4. [bug] Fixed a rare crash when starting a new mission.
5. Added sub elements <set_datarefs> and <set_datarefs_on_exit> to the trigger <outcome> element.
6. [ui] Added weather support for mission creation, it is still a work in progress. Seems not to work from the "templates" screen but should work fine from the other ones.
7. [internal] When a new X-Plane build is installed, the plugin will automatically re-read all apt.dat files (won't work for new custom sceneries, you will have to run it manually).



v3.304.11
==========
1. [template] 
Added new element <display_object_near_plane> to allow designer a more granular control over 3D Object placement near plane. This element is a special case of <display_object> (read all about it in the "Designer Guide" document. 
Best used when plane on ground. Contact me for any questions or clarifications regarding this addition.

2. [save] Better "obj3d" support when "saving" and "loading" a saved checkpoint.
3. [internal] Done lots of internal modifications to the code design so edge cases may occur. My tests, so far, found most of them but who knows.

Please notify me of any crash or unexpected behavior. 


v3.304.10
=========
1. [ui] Added random day/time to the "User create mission", "ILS" and "External FMS" screens.
2. [ui] Some syntax corrections.
3. [ui] Extended "External FPLN" max search to 9000nm, same as in the ILS screen.
4. [ui] Auto filter out duplicate airports in "External FPLN" (can be toggled).
5. [fix] Navaid name should not be "briefer" in the mission description.
6. Updated User Guide.


v3.304.9.1
==========
1. [break] Changed <rank> element to <scoring>
2. Disabled the dedicated XP12 code for positioning plane after XP12b9 since the "XPLMPlaceUserAtLocation()" regresion was fixed by Laminar.
3. Fixed "runway center" landing score. Issue was with the Query.
4. New integration of the acf "*.obj" custom dataref search and save.
   [ui] Save checkpoint button will be available only once the "custom dataref search" is done.
5. [internal] Fixed bug where positioning a plane failed due to missing ICAO value, the plugin should have picked the closest one by itself.
6. Added default <scoring> if none is present in the mission file.


v3.304.9
========
1. First support for adding score to the flight, based on gathered stats.
   Currently it will allow the designer to score: "pitch, roll, gForce and center line (not landing)" (see Designer guide).
2. [ui] At the end of the mission, stats screen will now show the scores based on your stats. The score is based on designer
3. [feature] When using the flightplandatabase screen, you now have a new option to filter results by "ICAO + Name", This should provide the simmer with more route options.
4. [regression bug] Fixed Cue Lines not showing in XP11, should not work on XP12.
5. [save] When saving a checkpoint your stats will also be saved and used when you are loading from save checkpoint (needs more tests, but looks solid so far).
6. [bug] Fixed stats database is not available if we loaded a checkpoint after finishing a mission.
7. [bug] When loading a saved checkpoint, local time is now set correctly.
8. [internal] Better support for draw callbacks that will be compatible for OpenGL/Vulkan/Metal and XP12 (Currently the XP12 support is temporary until final version and XPSDK will go out and maybe there will be a better flag).
9. [internal] Added more stats and airport information to have more precise information for the "score" and airport recognition logic.

10. [non plugin related] LR confirmed my bug report and it is now named: XPD-13148



v3.304.8.1
===========
The following build is mainly damage control for Linux users, especially Arch based distros.
It seems that in X-Plane 12 and Arch Linux distro, the fmod library crashes the simulator during "Release" function call.
I have added a new "setup" option, just for Linux OS to pick which distro you are using.
Use it only if X-Plane crashes during "Mission Quit" or "Application Quit".

I did not encounter that issue on Windows and in the following Linux distributions: Mint, Ubuntu, Pop!OS and I think Kubuntu is also fine.



v3.0.304.8 (Linux/OSX users, please also read the troubleshoot part)

1. XP12 compatibility.
2. Changed the version numbering fom: "3.0.xxx" to 3.xxx"
3. [os compatibility] Linux and OSX builds where done on Mint 21.0 and OSX 10.15 respectively. This means that the plugin might not function as expected.
                       Please contact me in - snagar.dev@proton.me and describe the problem, attaching the Log.txt file will help.

4. [lib] Implemented FMOD 2.0.3 (compatibility with XP12)
5. [lib] cURL - Compiled v7.84.0 against OpenSSL 3.0.5 - Older Linux distributions might need to manually create symbolic links from "/lib/x86_64-linux-gnu" to the new libraries since they might not have the OpenSSL3.x libraries.
        ==> See below for more explanation <==

6. [lib] Implemented imgui v1.88
7. [bug] Fixed countdown failer after loading a checkpoint with a countdown settings.
8. [xp12 limitation] Automatic Metar file injection won't work. The file will be copied to the {xp home} but no automatic load will occur, you will have to do that manually.
                     This should not be an issue in XP11.
9. [ui] Added "date/time" widget to the "user creation mission" screen. You can also change X-Plane time and then manually sync it in the screen.
10. [ui] The "Last F.Plan" message should not be seen in the conversion screen.

v3.0.304.7
1. [enhancement] Added "open_choice" attribute to the message
2. [embed] Added "fn_hide_3d_markers()" and "fn_show_3d_markers()" embedded script functions.
3. [embed] Implemented "fn_position_camera()" embedded function to position the camera in X-Plane world.
       In 2D mode it works well,
       In VR we need to take into consideration that "Mission-X" window does not follow you in VR world, therefore you need to carefully design the mission to 
       suite 2D and VR users.
4. [embed] Removed mxCurrentGoal seeded parameter.
5. [embed] added 2 script functions: "fn_open_inventory_screen()" and "fn_open_image_Screen()" (were not tested)
6. [bug] Fixed fail timer.
7. [bug] Better default mission time handling if it is not set by the designer. Will prefer local time from dataref as day in year, hours, min 
8. [3D] Added new markers (smaller ones).
9. [bug] Fixed the random "start/end" leg messages duplication after running the first generate mission button.
10. [attrib] Added new task type attribute: "is_placeholder". This is a new task type that basically allows the designer to define a mandatory task without
       direct relying on script/trigger.
       The state of the task must be fulfilled from other script, for example from a "choice" or "message" or a trigger.
11. [bug] Fixed crash when item image is missing.
12. [bug] Fixed Inventory::createNewItem() function, it will now create a valid Item object and will copy the original item node and information while resetting 
        quantity to zero.
13. [bug] When calling "post_script" from a "message" element, the functions: "set_task_xxx()" 
        could not be fulfill because it has to have the "current leg name" seeded.
        Fix: Before calling QMM::flc() we seed the "current leg name" so "post_script" scripts can be used to manipulate "tasks" if they are called from "message" elements.
There is no "currentTrigger/Task" awareness though, so you should use the functions: "fn_set_task_property_in_objective()" for best results.
This is an edge case if you try to manipulate tasks from "message" element.        

14. [enhancement] In the conversion screen, Added support for triggers based camera and scripts.
15. [bug fix] Updated triggers won't reset the "type" to "rad".
16. [bug] Loaded converted saved file will now read correctly "scriptlet" and will store them in the "flight_plan" element.



v3.0.304.6 - Background Sound control
1. [designer] Added new <mix> attribute that works only for "back"ground tracks ("track_instructions").
   The new attribute allows you to have control on "sound volume" and "repeat" commands.
   Check designer guide for more information.
2. [designer] Added visual cue to moving 3D objects. This will only work with the DEBUG plugin build, and not the release build.
3. [bug] In "<display_object>" attribute "link_task" was not applying correctly.
4. [ui] Added "normalized volume" to the "setup" screen, so you can override communication tracks but not background tracks.
5. [log] When releasing an unused sound channel it won't write to the Log if there is an error, since the channel was released beforehand.
6. [obj3d] Minor modifications to the 3D markers textures. I suggest to install the latest random pack too.



v3.0.304.5 - Inventory images
1. [new] Inventory item now supports images. You can also click the image to zoom.
2. [bug fix] 2D maps in different flight legs will now be displayed correctly and not just the first image from the first "flight leg".


v3.0.304.4 - Save conversion state
1. Added ability to save your conversion state to a later time.
   You can only have 1 save at a time.
2. Minor UI modifications to the "conversion screen".
3. Added the latest 3D Markers to the "conversion screen" and to the random pack.



v3.0.304.3 - mainly bug fixes
1. [bug] Fixed 3D object instance display rule not read correctly from the XML node during flight.
2. [ui] Added support for markers and marker radius display to the conversion screen.
        You will have to install the latest random pack to support all markers.
3. [obj] Added more 3D Object markers into the random pack. Useful in the conversion screen.
         You can also use them in your mission packs instead of the original 3D marker.
4. [bug] fixed tasks that handle sling load with scripts, scripts were not read correctly and so task was skipped.
5. [bug] Fixed stats speed not showing in graph (wrong dataref name).
6. [bug] Fixed <obj3D> duplication in Random Engine when using "copy_leg_as_is_b=yes"


v3.0.304.2
1. Added support for 3D Markers in the LittleNavMap conversion screen (only uses the same marker in Random folder,
   but can be modified after generating the mission file).
2. [bug] Fixed 3D Object instance not using "elev_ft" attribute but only above ground.
3. [bug] Fixed <display_object> not picked corectly in Obj3D::parse_node().
4. Fixed tooltip in the home screen
5. Added WPn for instead of lat/lon numbers in the XP11 external FMS.
6. Another external XP11 FMS modification is to better reflect navaids names like VOR/NDBs.
  Plugin will try to guess and pick only NavAids that are ~280mt from WayPoint.
7. Fixed "base_on_sling_load" task when it depends only on scripts and not using the plugin own logic.
8. [RandomEngine] Fixed GlobalSettings not copied correctly in case "copy_as_is_b" is set.
9. [ui] Fixed multi option template combo box length,
   it is now defined based on the longest text and not by only calculating the first text in the list.
10. [GPS] Plugin will search if "location_type" is set to "plane", if so then first location will be lat/lon and not the icao.
     This is important for generated missions since in some cases the closest ICAO to plane might not be the actual
     ICAO you are in its bounderies.
     This way you won't see in the FMS an icao that might not reflect your real one.
     Example:
     if you will place your plane at the start of the runway in Anchorage,
     you might get the seaport that is near it instead.


v3.0.304.1
1. [bug] fixed Mission-X overrides DLLs search for other plugins like: "GroundTraffic".
2. [bug] Fixed mission list when there are only 2 missions in the list.
3. [new] First implementation with the "Sling Load" plugin. You still need to download the forked plugin since it is not in the official one yet.
4. [new] Added new task attribute and rules to implement a task based on Cargo sling load (see the new Townsvile and back" demo.
5. [new] Added documentation explanation for the Sling Load plugin integration.
6. [new] Added support for special keyword: "{navaid_lat}" and "{navaid_lon}" in "dataref_start_cold_and_dark" element.
7. [new] Implemented new attribute: "copy_leg_as_is_b" into templates to make it simpler to convert a stand alone mission to a template or to create a main mission file and just add some randomization to it using a template structure.
8. [internal] Some internal changes to parameter handling in the embedded class.

v3.0.302 - final
1. Enhanced Mission-X triggers <rectangle> element with attribute: "first_point_is_center".
Now we have 2 rectangular trigger types.
The default one: "first point" is left bottom point.
The second one(new): "first point" is the center of the rectangle, dimensions are treated as radius.
Example: dimensions of 100|50 length will be translated to rectangle of "200x100"
2. Modified the "conversion screen" to use the new <rectangle> enhancement, which means:
it won't calculate all <point>s of the rectangle, only the first one and the designer will pick between first point is center or not, in the trigger creation screen.
3. Added "position_pref" to the <briefer>, so now we can use code logic from xp11 or xp10.
The benefit of xp10 logic is that after positioning the plane, it won't force engine start.
This attribute can be used in templates too, check "Designing Templates" documentation.
4. Added "force_heading_b" attribute was added to the <location_adjust> element, and it is mainly for designer use (can be forced in the setup screen also).
The idea behind this attribute: when plane is 20m from starting location, the positioning code is ignored. The new flag will at least, force the heading positioning.
5. Some internal fixes.



v3.0.302 B3 - Beta
1. Added support for "boxed" triggers and "script" based triggers.
2. Added new function: "fn_get_aircraft_model()"
3. More UI tweaks.

v3.0.302 B2 - Beta
1. New Trigger option in the "flight_leg" screen.
   You can only create but not edit created triggers, yet.
2. Tested some Ugly colors to the popup tables ;-)
3. Mainly internal work.


v3.0.302 B1 - Beta
1. New screen to convert LittleNavMap flight plan to a mission-x file (base implementation).
2. Fixed a bug where plane and camera view returned same headings.
3. [designers] Minor <leg> element extended, you no longer need <desc> subelement to write the flight leg description, you can use <![[CDATA ]]> directly under <leg>.


v3.0.256.4.4 - Hopefully the last tweak of this build tree.
1. Another tweak for the external file read when using replace element in a template.
2. Fixed the stats graph at the end of the mission.
3. Added new functionality to write the current GPS to the external FPLN files. No need for an active mission anymore.
   It can now behave as a tool. You can use it from the "setup" screen or through the "missionx=>tools" menu.
