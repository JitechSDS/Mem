from metamorphoses import Attr
from metamorphoses import Metamorphoses
from metamorphoses import Version
#from sds2.componentmetamorphoses import ComponentMetamorphoses as CM
from variables import attributes

#goes through all attrbutes and sets makes them attributes in main and
#stores thier default value

class versionControl: # inherit from CM?
	versions = {}
	arg = []
	for k in attributes:
		arg.append(Attr(k,attributes[k]))
	versions[0] = Version(*arg)

	
	def attributes(self):
		args = {}
		for x in self.versions[0].attrs:
			args[x[0]] = x[1]
		return args
    