GUI plugin for ExtensiveAutomation server
===================================================

Introduction
------------

This plugin enable to interact with user interface 
Selenium, sikulix or adb for android mobile are used to do that.

Installing from pypi
--------------------

1. Run the following command

        pip install extensiveautomation_plugin_gui

2. Execute the following command to take in account this new plugin

        ./extensiveautomation --reload
        
3. Samples are deployed on data storage

Installing from source
----------------------

1. Clone the following repository 

        git clone https://github.com/ExtensiveAutomation/extensiveautomation-plugin-gui.git
  
2. Copy the folder `sutadapters` to /home/extensiveautomation/ and overwrite-it

        cp -rf sutadapters /home/extensiveautomation/
        
3. Copy the folder `var` to /home/extensiveautomation/ and overwrite-it

        cp -rf var /home/extensiveautomation/
        
4. Finally execute the following command to install depandencies

        cd /home/extensiveautomation/
        python extensiveautomation.py --install_adapter GUI