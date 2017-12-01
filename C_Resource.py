from C_ListObject import ListObject


class Resource(ListObject):
     def __init__(self, name, baseComponents, timeUnitsToProduce, skillsRequiredToProduce, toolsRequiredToProduce, facilitiesRequiredToProduce):
          super().__init__(name)
          self.components = baseComponents
          self.timeUnitsToProduce = timeUnitsToProduce
          self.skillsRequiredToProduce = skillsRequiredToProduce
          self.toolsRequiredToProduce = toolsRequiredToProduce
          self.facilitiesRequiredToProduce = facilitiesRequiredToProduce

