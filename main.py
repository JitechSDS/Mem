from Designable.ProcessableMember import ProcessableMember
import edit as EditorUI
from versions import versionControl
from kwargmixin.kwargmixin import KWArgMixin
from sds2.utility.gadget_protocol_member import GadgetMember

@versionControl
class mainMem(GadgetMember, ProcessableMember, KWArgMixin):
    Name = "JITECH mainMem"
    """
    Include a brief description of the member
    """

    def __init__(self, **kwargs):
        versionControl.init_factory()(self, **kwargs)

        ProcessableMember.__init__(self, **kwargs)

        # KWArgMixin is a class provided in the plugins distributed with
        # SDS/2
        KWArgMixin.__init__(self, **kwargs)

    def Add(self):
        """Take care of any user input needed to add the member
        
        Returns:
            bool: True allows the member to continue; False will stop the
                  process of adding the member
        """
        return True

    @classmethod
    def Factory(cls, left, right, universe, **kwargs):
        mainMem = cls(**kwargs)
        mainMem.SetLeftLocation(left)
        mainMem.SetRightLocation(right)
        return mainMem

    # @staticmethod is required for this method
    # this is part of the Gadget Protocol interface
    @staticmethod
    def CreateCustomMultiEditableUI(model, gadget_factory):
        EditorUI.build_ui(model, gadget_factory)
        return True

    def DesignForMember(self, mn):
        """Material creation should be done here
        
        Args:
            mn (int): The member number assigned to this member
        
        Returns:
            bool: False will cancel member add
        """
        # add any material in this method
        return True