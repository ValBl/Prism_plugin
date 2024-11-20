# addDeadlineOption.py

name = "addDeadlineOption"
classname = "addDeadlineOption"

import os
from qtpy.QtWidgets import *
from qtpy.QtGui import *

class addDeadlineOption:
    def __init__(self, core):
        self.core = core
        self.version = "v1.0.0"

        # register callbacks
        # use a lower priority than 50 to make sure the function gets called after the "onStateStartup" function of the Deadline plugin
        self.core.registerCallback("onStateStartup", self.onStateStartup, plugin=self, priority=40)
        self.core.registerCallback("sm_render_getDeadlineParams", self.sm_render_getDeadlineParams, plugin=self)
        #self.core.registerCallback("preExport", self.preExport, plugin=self)
        #self.core.registerCallback("postExport", self.postExport, plugin=self)

    def sm_render_getDeadlineParams(self, origin, dlParams, homeDir):
        print("PARAM :  ", origin, dlParams, homeDir)
        # custom code here...

        machineList = self.stateUI.le_machinelist.text()
        
        if machineList:
            is_deny = self.stateUI.chb_machinelist.isChecked()
            if is_deny == True:
                dlParams["jobInfos"]["Denylist"] = machineList           
            else:
                dlParams["jobInfos"]["Allowlist"] = machineList

        comment = self.stateUI.le_comment.text()
        if comment:
            dlParams["jobInfos"]["Comment"] = comment
        
        dlParams["jobInfos"]["BatchName"] = "TESTBATCH"
        
        batchName = self.stateUI.le_batch_name.text()
        if batchName:
            dlParams["jobInfos"]["BatchName"] = batchName
            
        return origin, dlParams, homeDir

    #StateManager

    def onStateStartup(self, state):
        # this function is used to create the GUI widgets every time a state gets created
        folder = os.path.dirname(__file__)

        # create the "Settings2" widgets only when the state has job submission widgets (for Deadline job submissions)
        if hasattr(state, "gb_submit"):

            # get the layout of the state settings, which the new widgets will be added to
            lo = state.gb_submit.layout()

            # create a widget with a label and a combobox
           
            state.w_batch_name = QWidget()
            state.lo_batch_name = QHBoxLayout()
            state.lo_batch_name.setContentsMargins(9, 0, 9, 0)
            state.l_batch_name = QLabel("Batch Name:")
            state.le_batch_name = QLineEdit()
            
            state.w_comment = QWidget()
            state.lo_comment = QHBoxLayout()
            state.lo_comment.setContentsMargins(9, 0, 9, 0)
            state.l_comment = QLabel("Comment:")
            state.le_comment = QLineEdit()

            state.w_machinelist_chn = QWidget()
            state.lv_machinelist = QHBoxLayout()
            state.lv_machinelist.setContentsMargins(9, 0, 9, 0)
            state.l_machinelist_chb = QLabel("Machine List is A Deny List:")
            state.chb_machinelist = QCheckBox()
            
            state.w_machinelist = QWidget()
            state.lo_machinelist = QHBoxLayout()
            state.lo_machinelist.setContentsMargins(9, 0, 9, 0)
            state.l_machinelist = QLabel("Machine List:")
            state.le_machinelist = QLineEdit()
            state.bt_list = QPushButton()
            icone_path = os.path.join(os.path.dirname(__file__), "icone", "gear.ico")
            state.bt_list.setIcon(QIcon(icone_path))

            state.w_batch_name.setLayout(state.lo_batch_name)
            state.lo_batch_name.addWidget(state.l_batch_name)
            state.lo_batch_name.addStretch()
            state.le_batch_name.setMinimumWidth(175)
            state.lo_batch_name.addWidget(state.le_batch_name)
            
            state.w_comment.setLayout(state.lo_comment)
            state.lo_comment.addWidget(state.l_comment)
            state.lo_comment.addStretch()
            state.le_comment.setMinimumWidth(175)
            state.lo_comment.addWidget(state.le_comment)

            state.w_machinelist_chn.setLayout(state.lv_machinelist)
            state.lv_machinelist.addWidget(state.l_machinelist_chb)
            state.lv_machinelist.addStretch()
            state.lv_machinelist.addWidget(state.chb_machinelist)
            
            state.w_machinelist.setLayout(state.lo_machinelist)
            state.le_machinelist.setMinimumWidth(175)
            state.lo_machinelist.addWidget(state.l_machinelist)
            state.lo_machinelist.addStretch()
            state.lo_machinelist.addWidget(state.le_machinelist)
            state.bt_list.setMaximumWidth(25)
            state.lo_machinelist.addWidget(state.bt_list)

            lo.insertWidget(10, state.w_batch_name)
            lo.insertWidget(11, state.w_comment)
            lo.insertWidget(12, state.w_machinelist_chn)
            lo.insertWidget(13, state.w_machinelist)
            # save the state settings when the current dropdown item gets changed
            state.bt_list.clicked.connect(lambda f: self.machineListEdit(state))
            state.le_machinelist.textChanged.connect(lambda s: state.stateManager.saveStatesToScene())
            
            self.stateUI = state

    def machineListEdit(self, state):
        from CallDeadlineCommand import CallDeadlineCommand

        curMachineList = state.le_machinelist.text()

        output = CallDeadlineCommand( ["-selectmachinelist", curMachineList], False )
        print(output)
        output = output.replace( "\r", "" ).replace( "\n", "" )
        if output == "Action was cancelled by user":
            output = curMachineList
        print(output)
        state.le_machinelist.setText(output)
