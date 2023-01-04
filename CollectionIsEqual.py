class CollectionIsEqual :
    def __init__(self) :
        pass

    #Checks if both objects contain the same content regaurdless of type
    def isEqual(self, obj1, obj2) :
        return obj1 == obj2

    #Checks if both objects have the same unique content, regaurdles of lengths
    def sharesUnique(self, obj1, obj2):
        return obj1 == obj2
    