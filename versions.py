from metamorphoses import Attr
from metamorphoses import Metamorphoses
from metamorphoses import Version

class versionControl(Metamorphoses):
    versions = {}
    versions[0] = Version(
        Attr('x', False),
        Attr('y', 25.),
        Attr('z', "this is a string")
    )