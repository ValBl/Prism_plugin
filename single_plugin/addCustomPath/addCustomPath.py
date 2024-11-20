name = "addCustomPath"
classname = "addCustomPath"

import os
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
        directory_path = QFileDialog.getExistingDirectory(None, "Select Local Folder for export")

        configData["Lc_Cache"] = os.path.normpath(f"{directory_path}\\{args[2]}")
        self.core.popup(configData)
        self.core.setConfig("export_paths", val=configData, configPath=configPath)
