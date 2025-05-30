#!/usr/bin/python3


### ElementTree     https://stackabuse.com/reading-and-writing-xml-files-in-python/
### Api XML Notes:  https://docs.python.org/3/library/xml.dom.html#dom-node-objects

#from xml.dom.minidom import parse
import xml.etree.ElementTree as ET
# import xml.dom.minidom
import subprocess
import sys
import os
import re # regex

"""
Text To Speech
Written By: Saar.Nagar
Version 1.0

Changelog:
1.1 File name will be injected back to the comm track
    <mix track_type="comm" sound_file="" sound_vol=""/> 


===============================================================================
The following script will only work with Google Cloud "Text to speech".
===============================================================================

For the script to work you have to:
1. Run it from Linux (it can be tweaked to run on Windows too).
2. You have to install Google cloud Text To speech API: 
  Google client installer should be found: "https://cloud.google.com/sdk/docs/install"
3. Additional documentations:  "https://cloud.google.com/text-to-speech/", "https://cloud.google.com/text-to-speech/docs"
4. The current python script uses the COMMAND LINE approach and the REST API and few OS specific commands to decode/encode the receiving data.
  You must follow the "Before you begin" topic in: "https://cloud.google.com/text-to-speech/docs/create-audio-text-command-line"
  As far as I know you need to setup an account, but it won't charge you for less than 100000 words or characters (not sure exactly, check the documentation and it also depends on the voice quality you pick).

Step by Step Installation Example:  
==================================
1. Go over the topic "Create audio from text by using the command line" at: "https://cloud.google.com/text-to-speech/docs/create-audio-text-command-line".
   It has reference to the billing page, if you have not set one yet.
   If you need to set a billing account, you should check the "Before you begin" page: "https://cloud.google.com/text-to-speech/docs/before-you-begin"
   
   * Make sure to create a new project and generate a project key, you will use it later.
     For example: "text_to_speech" project name.

   * Once done, you should enable the "Text to speech API"

2. Go over the "Install the gcloud CLI" and install it: https://cloud.google.com/sdk/docs/install
   There are Eight steps (more or less) that you should easily follow. You only need the base installation.

3. Once all is set, make sure your "$GOOGLE_APPLICATION_CREDENTIALS" environment variable is set.

4. Place the "python script" someware.
4.1 Create subfolder: "output" in that folder.

5. Test the script on one of the mission files you created or downloaded.


"""

### Check availability of "output" folder
if not os.path.exists(os.path.join(os.getcwd(), 'output')):
    try:
        mode = 0o766
        os.mkdir(os.path.join(os.getcwd(), 'output'), mode)
    except FileExistsError:
        print ("Folder \"output\" is missing in {0} folder.\nAdd the missing folder.\nAborting script.".format(os.getcwd()))
        sys.exit(-1)


## The following string holds the content of the "download_request.sh" file
## You can disable this code and prepare the download_request.sh file as a permanent file
dounload_request_s="""#!/bin/bash
curl -X POST \
-H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
-H "Content-Type: application/json; charset=utf-8" \
-d @request.json \
https://texttospeech.googleapis.com/v1/text:synthesize
"""

f = open("download_request.sh","w")
f.write(dounload_request_s)
f.close()

##### End checking for output folder and "download_request.sh" creation file




# Open XML document using minidom parser
#DOMTree = xml.dom.minidom.parse("../../../src/the_artifact_01.xml")
seq=0

# file_name_to_parse = "" #"mission.xml"

tag_name_to_parse = ""
list_file_names = []



## Main Functions
def print_help():
    help01 = """ The script format:
        SCRIPT {filename} or {option=value} {option=value}
        
        {filename}: a string that represents One filename to parse. 
                    If you want a list of files, use the "list" option.
                    If you want to filter files, use "file_pattern" option
        
        OPTIONS:
            h or help: display this help text.
            
            
            path: Working Folder to search files from.
                  Default is current folder.
                  
            example:
                path=.
                path=/xp11/Custom Scenery/missionx/random/briefer
                
            file_pattern: A regular expression to filter files.
            Example:
                file_pattern=.xml    (all files ending with ".xml")
                
            list: predefined list files seperated with comma
            example:
                list=file1.xml,file2.xml,file3.xml...     
    """
    print("\n",sys.argv[0]," - Help:\n")
    print (help01)          
          
def read_attribute (inNode, attribName, defaultValue = "", bForceDefaultValueIfEmpty = False):
    attributes = inNode.attrib  ## debug
    if attribName in inNode.attrib :
        if bForceDefaultValueIfEmpty and attributes[attribName] == "":
            return defaultValue
        
        return inNode.attrib[attribName] # if there is no "replace value if attribute is empty" and we are not forcing the default value then return the attribute value even if it is empty
    
    return defaultValue;


def parse_mix_node (inNode, inParent):
    global seq
    global tag_name_to_parse
    file_name_to_return = ""
    seq += 1
    
    node_tag = inNode.tag ## am I <mix> or <dynamic_message>
    file_name = ""; 
    text = ""; 
    voice_lang_code  = read_attribute(inNode,'voice_lang_code', "en-gb", True); # en-gb
    voice_name       = read_attribute(inNode,'voice_name', "en-GB-Standard-A", True); # "en-GB-Standard-A"
    voice_gender     = read_attribute(inNode,'voice_gender', "FEMALE", True); # FEMALE / MALE
    voice_pitch      = read_attribute(inNode,'voice_pitch', "0.0", True); # number between -20..+20. default should be 0.0. Added to original pitch
    volume_gain_db   = read_attribute(inNode,'voice_vol_gain', "0.0", True); # voice_vol_gain is an attribute in the missionx <mix> element number -96.0 .. 16.0. Default 0.0. "volume_gain_db:" is a json attribute that google cloud needs
    voice_speak_rate = read_attribute(inNode,'voice_speak_rate', "0.0", True); # number 0.25-4.0 default 1.0 or 0.0

    ### Handle each <element> type so we should have "text" and "file_name"
    # <mix> element
    if node_tag == "mix" :
        type = inNode.attrib['track_type'] # read <mix track_type> attribute
        if type == "text":             
            #file_name = inNode.find("..").attrib["name"]  
            #print (inParent.tag, inParent.attrib)            
            file_name = inParent.attrib["name"]
            text = inNode.text ## get text/CDATA data
            if ( file_name == "" ): # check name attribute, if it is empty then skip 
                text = ""; # this will cause the download to be skipped
                print ("skipping, not valid filename found ...\n");
        else:
            file_name = ""
    # <dynamic_message> element
    elif node_tag == "dynamic_message":  ## You should not use dynamic messages with "text_to_speech", since the ".mp3" file generated might not be used ever by the plugin. The best approach is to pre-define a "message" and the dynamic message will point to it.
        print ("Processing dynamic message element")
        attrib_msg_name_to_call = read_attribute(inNode, "message_name_to_call") ## get the message name
        attrib_name = read_attribute(inNode, "name") ## get the attrib name         
        text = inNode.text 
        if (tag_name_to_parse != "" and tag_name_to_parse != attrib_name):
            text = "" # this will cause the download to be skipped
            print ("skipping ...\n")
        elif (attrib_msg_name_to_call != ""):
            text = ""  ## if we base dynamic_message on  <message> then we need to skip the next step, therefore we reset "text" parameter
        elif (text != ""):
            sound_file_name = read_attribute(inNode, "sound_file", "", True);
            if sound_file_name != "" :
                file_name = sound_file_name
            
            if (file_name == ""):
                parent_attrib_name = read_attribute(inParent, "name", True) # inParent.attrib["name"] 
                file_name = "msg_4_dyn_message_" + parent_attrib_name + "_" + str(seq) # construct name from flight leg name + sequence number. I use same rules as Mission-X plugin. The only problem is with the seq number, it might not be the same as the generated one, this is why I suggest to use "message_name_to_call" attribute in <dynamic_message>



    ## Start request and MP3 conversion
    #print "start request\n";
    text = text.strip() # perl regular expression: "s/^\s+|\s+$//g"  ### remove spaces ?
    text = text.replace('"', '') ## perl reg: 's/["]//g'; # remove any occurence of double quotes.

    if text != "":
        print ("Processing file: ", file_name)
        ### read the REQUEST template
        # f = open("request.tmpl","r")
        # lines_list = f.readlines()
        # f.close();
        #
        # # replace in memory strings 
        # request_text = ""
        # for line in lines_list:
        #     request_text += line;

        request_text = """{
  "input":{
    "text":"%text%"
  },
  "voice":{
    "languageCode":"%voice_lang_code%",
    "name":"%voice_name%",
    "ssmlGender":"%voice_gender%"
  },
  "audioConfig":{
    "audioEncoding":"MP3",
    "speakingRate":"%voice_speak_rate%",
    "pitch": "%voice_pitch%",
    "volumeGainDb": "%volume_gain_db%",
    "effectsProfileId": [ "large-home-entertainment-class-device" ]
  }
}
"""
        

        request_text = request_text.replace("%voice_lang_code%", voice_lang_code)
        request_text = request_text.replace("%voice_name%", voice_name)
        request_text = request_text.replace("%voice_gender%", voice_gender)
        request_text = request_text.replace("%voice_pitch%", voice_pitch)
        request_text = request_text.replace("%volume_gain_db%", volume_gain_db)
        request_text = request_text.replace("%voice_speak_rate%", voice_speak_rate)

        request_text = request_text.replace("%text%", text)

        print (request_text) # debug

        ## Write the request string into a new request file in "convert" sub-folder
        request_json_file_name = "request.json"
        request_file_name = file_name + ".request.json"
        output_file_path = "output/" + request_file_name

        ## create the "request.json" file for the "download_request.sh" script 
        f = open(request_json_file_name,"w")
        f.write(request_text)
        f.close()
        
        ## create the "{file_name}.request.json" file for debug in the output folder
        f = open(output_file_path,"w")
        f.write(request_text)
        f.close()


        ## Download the text 
#        curl_cmdList = ["curl", "-X", "POST", r"-H Authorization: Bearer $(gcloud auth application-default print-access-token)", r"-H Content-Type: application/json; charset=utf-8", "-d @"+output_file_path, "https://texttospeech.googleapis.com/v1/text:synthesize"]
        
        
        try:
            mp3_file_name_path = "output/"+file_name+".base64.txt"
            mp3_err_path = "output/"+file_name+".err.txt"
            # get the path of the current directory
            current_path = os.getcwd()
            # print("Path of the current directory : " + current_path)
            
#            curl_cmdList = ["sh " + current_path +"/download_request.sh > "+ current_path + "/" + mp3_file_name_path]
#            curl_cmdList = [". ~/.bash_profile;" + "sh " + current_path +"/download_request.sh > "+ current_path + "/" + mp3_file_name_path]
            curl_cmdList = [". ~/.bash_profile;. ~/.bashrc;" + "sh " + "download_request.sh > "+ mp3_file_name_path]
            print ("curl command args: ", curl_cmdList)
            
            with open(mp3_file_name_path,"wb") as out, open(mp3_err_path,"wb") as err:
                subprocess.run(curl_cmdList,stdout=out,stderr=err, check=True, text=True, shell=True)
            #subprocess.run(curl_cmdList, check=True, text=True, shell=True)
            
            ## Convert the txt downloaded file to MP3 using base64 converter
            fileExtension_s = ""
            if not file_name.endswith(".mp3"):
                fileExtension_s = ".mp3"
                
            convert_base64_to_mp3_cmdList = ["/usr/bin/base64 " + mp3_file_name_path + " -di > output/"+file_name+fileExtension_s]
            print ("base64 command args: ", convert_base64_to_mp3_cmdList)
            try:
                subprocess.run(convert_base64_to_mp3_cmdList, check=True, text=True, shell=True)
                file_name_to_return = file_name + fileExtension_s ## return the original file name without the extension

            except subprocess.CalledProcessError:
                print ("Failed MP3 conversion")

            print ("\n")

        except subprocess.CalledProcessError:
            print ("Failed cURL download")
           
            
    return file_name_to_return


def modify_comm_node_with_file_name (inNode, inSoundFile="", inVol="0.5"):
    print ("modify_comm_node_with_file_name")
    inNode.set("sound_file", inSoundFile)
    inNode.set("sound_vol", inVol)


##########################################################
##########################################################
##########################################################
##########################################################


# https://www.geeksforgeeks.org/command-line-arguments-in-python/
# total arguments
n = len(sys.argv)
if (n == 1):
    print_help()
    sys.exit(0)



# print("\nArguments passed:", end = " ")
argvDict = {} ## key value stored argv
for i in range(1, n):
    listSplitArg = sys.argv[i].split('=')
    
    if (len(listSplitArg) == 1):
        k=listSplitArg[0] 
        if k == "h" or k == "help" or k == "-h" or k == "-help":
            print_help()
            sys.exit(0)
        
        else:
            list_file_names.append(k)  ## treat the passed string as a file name
        
        
    if (len(listSplitArg) > 1):
        k,*v=listSplitArg # copy the list value as follow: k=list[0] v=[1..n-1] (the rest)
        if (k.lower() == "list" ):
            list_file_names = v[0].split(",")
            break;
        if (k.lower() == "path" ):
            argvDict["path"] = v[0]
            continue            
        if (  k.lower() == "file_pattern" ):
            pattern = v[0]
            # pattern = "r\""+v[0]+"\"" 
            searchPath="."
            if "path" in argvDict:
                searchPath = argvDict["path"]
            
            fileList = os.listdir(searchPath)
            for f in fileList:
                if re.search(r''+pattern, f) != None:
                    list_file_names.append(f)
            break;
    else:
        continue  # skip this Arg


# sys.exit(0)

## Main Code Loop over list_file_names
path_s = "."
if "path" in argvDict:
    path_s = argvDict["path"]
    
for file_name_to_parse in list_file_names:

    if file_name_to_parse == "":
        print_help()
        sys.exit(-1)
        
    if file_name_to_parse.endswith(".new.xml"):
        print ("Skipping file \"{0}\", Script won't handle files with extension '.new.xml'".format(file_name_to_parse))
        continue
    
    # concatenate the work folder with the file name. It is relative to the script folder
    file_name_to_parse = path_s + "/" + file_name_to_parse
    
    print (">"*30 + "\n")
    print ("Parsing: ", file_name_to_parse, "\n")
    
    DOMTree = ET.parse(file_name_to_parse)
    
    root = DOMTree.getroot()
    
    print ("\n")
    print ("Root element name in file: '{0}' is '{1}'\n".format(file_name_to_parse, root.tag))
    
    ### Main Parsing code
    messages = root.findall(".//message")
    for msg in messages:
        #print (msg.tag, msg.attrib)
        for mix in msg.findall(".//mix[@track_type='text']"):
            print (mix.tag, mix.attrib)
            output_file_name = parse_mix_node( mix, msg )
            print (output_file_name)
            if output_file_name != "":
               for mix_comm in msg.findall(".//mix[@track_type='comm']"):
                   modify_comm_node_with_file_name (mix_comm, output_file_name)
                   # # get work folder path
                   # work_folder_path = "."
                   # if "path" in argvDict:
                   #     work_folder_path = argvDict["path"]
                                          
                   new_xml_file_name = file_name_to_parse+".new.xml"
                   DOMTree.write(new_xml_file_name)
    messages = root.findall(".//dynamic_message")
    for node in messages:
        print (node.tag, node.attrib)
        output_file_name = parse_mix_node( node, msg )
        print (output_file_name)
        # if output_file_name != "":
        #    for mix_comm in msg.findall(".//mix[@track_type='comm']"):
        #        modify_comm_node_with_file_name (mix_comm, output_file_name)
        #        new_xml_file_name = file_name_to_parse+".new.xml"
            #        DOMTree.write(new_xml_file_name)
        







