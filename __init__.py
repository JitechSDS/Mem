from MemberBase import RegisterMemberType
#from component_tools import RegisterComponentAddCommand
from member import mainMem
import Commands
import os.path

image32 = os.path.join( os.path.dirname( __file__ ), "32x32.png" )
image64 = os.path.join( os.path.dirname( __file__ ), "64x64.png" )
icon32 = Commands.Icon(image32)
icon64 = Commands.Icon(image64)

RegisterMemberType(mainMem, mainMem.Name)
#RegisterComponentAddCommand(mainMem, icons = Commands.IconSet((icon32,icon64)))
