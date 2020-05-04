class Town:
	def __init__(self);
		pass

class Property:
	def __init__(self);
		self.Value = None
        
		
# Character can be lord, mercenary souldier merchant scienntis or just some leader of vilage  
class Character:
	def __init__(self):
		self.Name = None
        self.Old = None
        self.Race None
        self.Traits = {'Power':50,"Intelegent":50, "Agility":50, 
                       "Social":50, "Precision":50}
        self.Property = {}
        self.Relations = {}
    
    def setName(self, name):
        self.Name = name
    def setName(self, old):
        self.Old = old
    def setName(self, race):
        self.Race = race
    def setTraits(self, power = None, intelegent = None,
                  agility = None, social = None, precision = None,)
        if type(power) == tuple:
            i = 0
            for traitName in self.CharacterTraits:
                self.Traits[traitName] = power[i]
                i += 1 
            self.Traits = {}
        if type(power) == dict:
            self.Traits = power
        if type(power) == int:
            self.Traits['Power'] = power
            self.Traits['Intelegent'] = intelegent
            self.Traits['Agility'] = agility
            self.Traits['Social'] = social
            self.Traits['Precision'] = precisionpower
    
    def addRelation(character ,  relation):
        self.Relations[character] = relation
    