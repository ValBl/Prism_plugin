name = "autoLoadPlugin"
classname = "autoLoadPlugin"


import os
from qtpy.QtWidgets import *


class autoLoadPlugin:
    def __init__(self, core):
        self.core = core
        self.version = "v1.0.0"

        self.core.registerCallback("postInitialize", self.postInitialize, plugin=self)

    def postInitialize(self):
        pluginName = "addCustomPath"
        pluginPath = ...
        plugin = self.core.plugins.getPlugin(pluginName)
        isLoaded = plugin is not None
        if isLoaded:
            pass
        else:
            self.core.plugins.loadPlugin(path=pluginPath)
        
