# GUI plugin for ExtensiveAutomation server

This plugin enable to interact with user interface 
Selenium, sikulix or adb for android mobile are used to do that.

## Table of contents
* [Installing from pypi](#installing-from-pypi)
* [Installing from source](#installing-from-source)
* [About actions](#about-actions)
    * [Selenium](#selenium)
        * [selenium/openbrowser.yml](#seleniumopenbrowseryml)
        * [selenium/closebrowser.yml](#seleniumclosebrowseryml)
        * [selenium/typetext.yml](#seleniumtypetextyml)
        * [selenium/waitelement.yml](#seleniumwaitelementyml)
        * [selenium/clickelement.yml](#seleniumclickelementsyml)
    * [Sikulix](#sikulix)
        * [sikulix/run_code.yml](#sikulixrun_codeyml)
        * [sikulix/type_path.yml](#sikulixtype_pathyml)
        * [sikulix/type_shortcut.yml](#sikulixtype_shortcutyml)
        * [sikulix/type_text.yml](#sikulixtype_textyml)
        * [sikulix/get_text_clipboard.yml](#sikulixget_text_clipboardyml)
* [About workflows](#about-workflows)
    * [Selenium](#selenium)
        * [selenium/google_search.yml](#seleniumgoogle_searchyml)
        * [selenium/google_create_account.yml](#seleniumgoogle_create_accountyml)
    * [Sikulix](#sikulix)
        * [sikulix/keyboard.yml](#sikulixkeyboardyml)
        
## Installing from pypi

1. Run the following command

        pip install extensiveautomation_plugin_gui

2. Execute the following command to take in account this new plugin

        ./extensiveautomation --reload
        
3. Samples are deployed on data storage

## Installing from source

1. Clone the following repository 

        git clone https://github.com/ExtensiveAutomation/extensiveautomation-plugin-gui.git
  
2. Copy the folder `sutadapters` to /home/extensiveautomation/ and overwrite-it

        cp -rf sutadapters /home/extensiveautomation/
        
3. Copy the folder `var` to /home/extensiveautomation/ and overwrite-it

        cp -rf var /home/extensiveautomation/
        
4. Finally execute the following command to install depandencies

        cd /home/extensiveautomation/
        python3 extensiveautomation.py --install-adapter GUI
        python3 extensiveautomation.py --reload
        
## About actions

### Selenium

#### selenium/openbrowser.yml

Open a browser like firefox or chrome

Parameter(s):
- agent (text): agent name
- url (text): url to load
- browser (text): type of browser to open (firefox, chrome or edge)
  
#### selenium/closebrowser.yml

Close the browser

Parameter(s):
- agent (text): agent name

#### selenium/typetext.yml

Type text on the html element.

Parameter(s):
- agent (text): agent name
- xpath (text): xpath expression to find the html element
- text (text): text to send in the element

#### selenium/waitelement.yml

Wait html element to appear on the page.

Parameter(s):
- agent (text): agent name
- xpath (text): xpath expression to find the html element

#### selenium/clickelement.yml

Click on html element.

Parameter(s):
- agent (text): agent name
- xpath (text): xpath expression to find the html element

### Sikulix

#### sikulix/run_code.yml

Run sikulix code

Parameter(s):
- agent (text): agent name
- code (text): sikulix code

#### sikulix/type_path.yml

Type path text

Parameter(s):
- agent (text): agent name
- text (text): path text

#### selenium/type_text.yml

Type text

Parameter(s):
- agent (text): agent name
- text (text): text to send

#### sikulix/type_shortcut.yml

Send keyboard shorcut

Parameter(s):
- agent (text): agent name
- key (text): press on key (KEY_WIN, etc..)
- other-key (text): press on a second key

#### sikulix/get_text_clipboard.yml

Get the text from the clipboard

Parameter(s):
- agent (text): agent name
- key-cache (text): save result on cache with the provided name

## About workflows

### Selenium

#### selenium/google_search.yml

This workflow shows how to use selenium actions 

#### selenium/google_create_account.yml

This is a more advanced worflow to use selenium actions

### Sikulix

#### sikulix/keyboard.yml

This workflow shows how to use sikulix actions 
