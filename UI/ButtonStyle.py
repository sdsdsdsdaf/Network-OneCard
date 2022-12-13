import sys,os
sys.path.append(os.path.abspath(os.path.join(os.getcwd()+"/UI")))

from PyQt5 import QtGui
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt

class ButtonStyle:

    @staticmethod
    def setButtonStyle(pushButton, font_style = 'Georgia', bold = False, size = 40):
        
        """
        Args:
            pushButton `QPushButton`: Setting Button
            font_style : font_style -> Default = 'Georgia
            bold `bool`: -> Default = False
            size `int` : Font size  -> Default = 40 
        """

        true_or_false = {False: 'normal', True: 'bold'}
        cmd_str =("""QPushButton{
            background-color: rgb(249, 228, 183);
            color: black;
            border-radius: 25px;
            font-family: %s;
            font-size: %dpx;
            font-weight: %s;
            margin-bottom: 5px;
            padding: 8px 0;}"""
             %(font_style, size, true_or_false[bold])
             + 
            """QPushButton::hover
            {
                background-color : white;
            }
            """
            )
         

        pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        pushButton.setStyleSheet(cmd_str)