name = "addCustomPath"
classname = "addCustomPath"

from threading import Timer
from qtpy.QtWidgets import *

class addCustomPath:
    def __init__(self, core):
        self.core = core
        self.version = "v1.0.0"

        self.core.registerCallback("onProjectCreated", self.onProjectCreated, plugin=self)
        
        
    def onProjectCreated(self, *args):
        
        self.core.popup(str(args))
        configPath = self.core.configs.getProjectConfigPath(args[1])
        configData = self.core.getConfig("export_paths", configPath=configPath) or {}
        configData["myLoc"] = "C:/custom/loc"
        self.core.popup(configData)
        self.core.setConfig("export_paths", val=configData, configPath=configPath)
