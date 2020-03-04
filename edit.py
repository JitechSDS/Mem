#custom libraries
import version
#SDS libraries
from sds2.utility.gadget_protocol import SubdialogController as gp
#dialog libraries
from dialog.label import Label
from dialog.value import Value
from dialog.entry import Entry
from dialog.listbox import Listbox
from dialog.combobox import Combobox
from dialog.checkbox import Checkbox
from dialog.image import Image
from dialog.dimension import DimensionStyled
import model
import sys
import os.path


def graphical(frame):
    Label(frame, 'This is a bare Member UI')

def build_ui(model, gadget_factory):
    controller = gp(model)
    gadget_factory.Banner(
        controller,
        graphical,
        'Graphical',
        '',
        ''
        )
    # columns and leaves can be added under the banner, but the banner will
    # always be at the top