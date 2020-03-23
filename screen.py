from dialog.checkbox import Checkbox
from dialog.entry import Entry
from dialog.dimension import DimensionStyled

from sds2.utility.gadget_protocol import ModelCompleteSubdialogController

def MainBanner(parent):
    Checkbox(parent, 'x', 'x:')
    Entry(parent, 'y', DimensionStyled(), 'y:')
    Entry(parent, 'z', str, 'z:')

def BuildMemberUI(model, gadget_factory):
    # the model complete controller will manage the model
    # complete attribute, which is hariy to do by hand
    mc_controller = ModelCompleteSubdialogController(
        'DateModelCompleted',
        model
    )

    gadget_factory.LoadSaveBanner(
        controller=mc_controller,
        callback=MainBanner,
        displayname="General Settings",
        sortname='',
        foldname='unique-fold-id',
        save_name='unique-form-name',
        ignore=(),  # tuple of items to ignore; changes will not for process
        defaultfold=True
    )

    # columns and leaves can be added under the banner, but the banner will
    # always be at the top