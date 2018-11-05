'''
Created on 27 Oct. 2018

@author: craig
'''

import wx
from Utilities.OpenCVOperations import allOperations
from pylint.test.functional.bad_whitespace import function
import json


class OpenCVFunction():
    
    thisFunctionName = ""
    functionParams = {}
    paintNotify = None
    enabled = True
    
    def __init__(self, functionName, paintCallback=None):
        self.thisFunctionName = functionName
        if not paintCallback is None:
            self.paintNotify = paintCallback
     
    def DisableLayer(self):
        self.enabled = False
    
    def EnableLayer(self):
        self.enabled = True
       
    # Bind to the change event of property editors

    def ValueChangedEvent(self, event):
        paramName = event.EventObject.Name
        if hasattr(event.EventObject, 'Value'):
            self.functionParams[paramName] = event.EventObject.Value
            print('Changed {0} to {1}'.format(paramName,event.EventObject.Value))
            if not self.paintNotify is None:
                self.paintNotify()
            
    def ComboboxChoiceEvent(self, event):
        paramName = event.EventObject.Name
        if hasattr(event.EventObject, 'GetSelection'):
            nSel = event.EventObject.GetSelection()
            strSel = event.EventObject.GetString(nSel)
            (key,val) =strSel.split("=") 
            self.functionParams[paramName] = int(val)
            print('Changed {0} to {1}'.format(paramName,event.EventObject.Value))
            if not self.paintNotify is None:
                self.paintNotify()
    
    def IntSlider(self, panelTarget, config, funcDef):
        tmpPanel = wx.Panel(panelTarget, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE|wx.TAB_TRAVERSAL )
        tmpSizer = wx.BoxSizer( wx.HORIZONTAL )
        tmpSlider = wx.Slider( tmpPanel, wx.ID_ANY, 0, config['Min'], config['Max'], wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL|wx.SL_LABELS|wx.SL_VALUE_LABEL, name=config['ParamName'] )
        
        if config['ParamName'] in self.functionParams.keys() and not self.functionParams[config['ParamName']] is None:
            tmpSlider.SetValue(self.functionParams[config['ParamName']])
        
        tmpSlider.Bind(wx.EVT_SCROLL_THUMBRELEASE, self.ValueChangedEvent)
        tmpSlider.Bind(wx.EVT_SCROLL_CHANGED, self.ValueChangedEvent)
        tmpSizer.Add( tmpSlider, 1, wx.ALL|wx.EXPAND, 5 )
        tmpStaticText = wx.StaticText( tmpPanel, wx.ID_ANY, config['Label'], wx.DefaultPosition, wx.DefaultSize, 0 )
        tmpSizer.Add( tmpStaticText, 0, wx.ALL, 5 )
        tmpPanel.SetSizer(tmpSizer)
        tmpPanel.Layout()

        return tmpPanel
    
    def IntSpinner(self, panelTarget, config, funcDef):
        tmpPanel = wx.Panel(panelTarget, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE|wx.TAB_TRAVERSAL )
        tmpSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        tmpSpinner = wx.SpinCtrl(tmpPanel, wx.ID_ANY, '0', wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS|wx.SP_WRAP, config['Min'], config['Max'], name=config['ParamName'] )
        
        if config['ParamName'] in self.functionParams.keys() and not self.functionParams[config['ParamName']] is None:
            tmpSpinner.SetValue(self.functionParams[config['ParamName']])
        
        tmpSpinner.Bind(wx.EVT_SPINCTRL, self.ValueChangedEvent)
        tmpSizer.Add( tmpSpinner, 1, wx.ALL|wx.EXPAND, 5 )
        tmpStaticText = wx.StaticText( tmpPanel, wx.ID_ANY, config['Label'], wx.DefaultPosition, wx.DefaultSize, 0 )
        tmpSizer.Add( tmpStaticText, 0, wx.ALL, 5 )
        tmpPanel.SetSizer(tmpSizer)
        tmpPanel.Layout()

        return tmpPanel

    def FloatEditor(self, panelTarget, config, funcDef):
        return 'y'
    
    def DoubleEditor(self, panelTarget, config, funcDef):
        tmpPanel = wx.Panel(panelTarget, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE|wx.TAB_TRAVERSAL )
        tmpSizer = wx.BoxSizer( wx.HORIZONTAL )
        if 'Step' in config.keys():
            inc=config['Step']
        else:
            inc = 0.01
        tmpDblSpinner = wx.SpinCtrlDouble( tmpPanel, wx.ID_ANY, value=str(config['Value']), pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.SL_HORIZONTAL|wx.SL_LABELS|wx.SL_VALUE_LABEL, min=config['Min'], max=config['Max'], initial=config['Value'], inc=inc, name=config['ParamName'] )
        
        if config['ParamName'] in self.functionParams.keys() and not self.functionParams[config['ParamName']] is None:
            tmpDblSpinner.SetValue(self.functionParams[config['ParamName']])
            tmpDblSpinner.SetIncrement(config['Step'] if 'Step' in config.keys() else 1)
        else: # use default values if available in the base config spec
            tmpDblSpinner.SetValue(config['Value'] if 'Value' in config.keys() else 0)  
            tmpDblSpinner.SetIncrement(config['Step'] if 'Step' in config.keys() else 1)
        
        tmpDblSpinner.Bind(wx.EVT_SPINCTRLDOUBLE, self.ValueChangedEvent)
        tmpSizer.Add( tmpDblSpinner, 1, wx.ALL|wx.EXPAND, 5 )
        tmpStaticText = wx.StaticText( tmpPanel, wx.ID_ANY, config['Label'], wx.DefaultPosition, wx.DefaultSize, 0 )
        tmpSizer.Add( tmpStaticText, 0, wx.ALL, 5 )
        tmpPanel.SetSizer(tmpSizer)
        tmpPanel.Layout()

        return tmpPanel
    
    def BooleanEditor(self, panelTarget, config, funcDef):
        tmpPanel = wx.Panel(panelTarget, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE|wx.TAB_TRAVERSAL )
        tmpSizer = wx.BoxSizer( wx.HORIZONTAL )
        tmpCheckBox = wx.CheckBox( tmpPanel, wx.ID_ANY, config['Label'], wx.DefaultPosition, wx.DefaultSize, 0 , name=config['ParamName'])
        
        if config['ParamName'] in self.functionParams.keys() and not self.functionParams[config['ParamName']] is None:
            tmpCheckBox.SetValue(self.functionParams[config['ParamName']])
        
        tmpCheckBox.Bind(wx.EVT_CHECKBOX, self.ValueChangedEvent)
        tmpSizer.Add( tmpCheckBox, 0, wx.ALL, 5 )
        
        tmpPanel.Layout()
        return tmpPanel
    
    def EnumChooser(self, panelTarget, config, funcDef):
        tmpPanel = wx.Panel(panelTarget, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE|wx.TAB_TRAVERSAL )
        tmpSizer = wx.BoxSizer( wx.HORIZONTAL )
        m_comboboxChoices = []
        for optKey, optVal in config['EnumValues'].items():
            m_comboboxChoices.append('{0}={1}'.format(optKey, optVal))
        tmpCombobox = wx.ComboBox( tmpPanel, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboboxChoices, wx.CB_READONLY, name=config['ParamName'] )
        
        # 
        if config['ParamName'] in self.functionParams.keys() and not self.functionParams[config['ParamName']] is None:
            selVal = self.functionParams[config['ParamName']]
            selText = ''
            for optKey, optVal in config['EnumValues'].items():
                if optVal == selVal:
                    selText = '{0}={1}'.format(optKey, optVal)
            if len(selText) > 0:
                tmpCombobox.SetValue(selText)
        else:
            tmpCombobox.SetSelection(0)
#             tmpCombobox.SetValue(m_comboboxChoices[0])
        
        tmpCombobox.Bind(wx.EVT_COMBOBOX, self.ComboboxChoiceEvent)
        
        tmpSizer.Add( tmpCombobox, 0, wx.ALL, 5)
        tmpPanel.Layout()
        return tmpPanel
        
    switcher = {
        'Int':IntSlider,
        'IntSpin':IntSpinner,
        'Float':FloatEditor,
        'Boolean':BooleanEditor,
        'Double':DoubleEditor,
        'Enum':EnumChooser
        }
    
    def layoutFunctionPanel(self, panelTarget):
        funcDef = allOperations[self.thisFunctionName]
        
        panelTarget.DestroyChildren()
        bszFuncLayout = wx.BoxSizer( wx.VERTICAL )
        panelTarget.SetSizer(bszFuncLayout)
        
        txtLabel = wx.StaticText(panelTarget, id=wx.ID_ANY, label=funcDef['Name'], pos=(0,0),size=(20,20), name="Name")
        bszFuncLayout.Add(txtLabel, 0, wx.EXPAND, 3)
        
        totalHeight = 0
        for param in funcDef['Parameters']:
            if param['control']:
                func = self.switcher.get(param['ParamType'])
#                 if param['ParamType'] == 'Int':
                res = func(self, panelTarget, param, funcDef)
                totalHeight += res.GetRect().height
                # Done afterwards because if this is setting to a previous value, i.e. already previously set, want it to be absent from functionParams to trigger defauls in above
                if not param['ParamName'] in self.functionParams:
                    self.functionParams[param['ParamName']] = param['Value']
                bszFuncLayout.Add(res, 0, wx.EXPAND, 3)
        
        bszFuncLayout.Layout()
        panelTarget.Layout()
    
    def execFunc(self, inputImage):
        funcDef = allOperations[self.thisFunctionName]
        targetFunc = funcDef['Function']
        paramList = {}
        paramList['image'] = inputImage
        
        for param in funcDef['Parameters']:
            if param['control']:
                if not self.functionParams[param['ParamName']] is None:
                    paramList[param['ParamName']] = self.functionParams[param['ParamName']]
                    print('{0}={1}'.format(param['ParamName'], self.functionParams[param['ParamName']]))
        result = targetFunc(**paramList)
        
        return result
        
    def getParamsAsPython(self):
        funcDef = allOperations[self.thisFunctionName]
        
        paramValues = json.dumps(self.functionParams)
        
        strFull = "{0} \r\n {1} \r\n".format(funcDef['Name'], paramValues)
        return strFull