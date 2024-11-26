name = "autoLoadPlugin"
classname = "autoLoadPlugin"

import json

import os
from qtpy.QtWidgets import *



class autoLoadPlugin:
    def __init__(self, core):
        self.core = core
        self.version = "v1.0.0"

        self.core.registerCallback("postInitialize", self.postInitialize, plugin=self)

    def postInitialize(self):
        
        with open('plugin_list_for_Auto_Load.json') as f:
            plugin = json.load(f)

        for pluginName, pluginPath in plugin.items():

            self.addplugin(pluginName, pluginPath)
    
    
    def addplugin(self, pluginName, pluginPath):
        plugin = self.core.plugins.getPlugin(pluginName)
        isLoaded = plugin is not None
        if isLoaded:
            pass
        else:
            self.core.plugins.loadPlugin(path=pluginPath)
        

class autoLoadPlugin:
    def __init__(self, core):
        self.core = core
        self.version = "v1.0.0"

        self.core.registerCallback("postInitialize", self.postInitialize, plugin=self)

    def postInitialize(self):
        plugin ={"addCustomPath": r"\\10.0.1.31\zorba-inter\ZORBAGROUP_EXT\00_MOON_PIPELINE\00_Pipeline\PRISM_PLUGIN\Custom\addCustomPath.py", "addDeadlineOption": r"\\10.0.1.31\zorba-inter\ZORBAGROUP_EXT\00_MOON_PIPELINE\00_Pipeline\PRISM_PLUGIN\Custom\addDeadlineOption\addDeadlineOption.py"}
        
        for pluginName, pluginPath in plugin.items():
            self.addplugin(pluginName, pluginPath)
    
    
    def addplugin(self, pluginName, pluginPath):
        plugin = self.core.plugins.getPlugin(pluginName)
        isLoaded = plugin is not None
        if isLoaded:
            pass
        else:
            self.core.plugins.loadPlugin(path=pluginPath)
        
