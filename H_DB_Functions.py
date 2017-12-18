'''

    Consumer_Resources: //includes tools weapons and armor (store of owned items in world)
        ownerID
        resourceType
        stores
        want
        importance
        consumptionRate

    Resources:
        resourceType
        name *will be removed later*
        requiredSkill
        requiredTools(Max 3) *tools are simply IDs of other resources.*
        requiredIngredients(Max 5)
        timeUnitsToProduceOneUnit

    P_Skills: *&**********************
        skillType
        ownerID
        resourceType
        skill

    E_Armor:
        armorType
        resourceType
        armorValue

    E_Weapon:
        weaponType
        P_ResourcesID
        AttackOptions (Max 5)

    AttackOption:
        attackOptionType
        range
        damage
        my_movement
        his_movement
        StatusesAdded (Max 3)

    MapObjects:
        id
        locationX
        locationY
        symbol
    Race:
        id
        name
    Actor:
        id
        name
        raceID
    CombatUnits:
        ActorID
        strength
        agility
        constitution
        equippedWeaponID
        attackOptions max 5
        currentStatuses as booleans

''''''

db = MySQLdb.connect(host="localhost",  # your host
                     user="root",  # username
                     passwd="p2950",  # password
                     db="testDB")  # name of the database

cur = db.cursor()



def createTables():

CREATE TABLE C_Resources (
    ID int NOT NULL AUTO_INCREMENT,
    resourceID int NOT NULL,
    quantity int NOT NULL,
    consumptionRate int NOT NULL,

    PRIMARY KEY (ID)
);
'''