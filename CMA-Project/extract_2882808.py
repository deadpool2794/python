import sqlite3
import json

def getCreatorDetails(cur, artwork_id):
    creatorList =  []
    cur.execute(artworkXcreator.format(artwork_id))
    creatorTable = cur.fetchall()
    for row in creatorTable:
        creatorDict = {}
        for i in range(len(row)):
            creatorDict[tableColoumns["creator"][i]] = row[i]
        creatorList.append(creatorDict)
    return creatorList

def getDepartmentDetails(cur, artwork_id):
    cur.execute(artworkXdepartment.format(artwork_id))
    departmentTable = cur.fetchall()
    departmentDict = {}
    for row in departmentTable:
        for i in range(len(row)):
            departmentDict[tableColoumns["department"][i]] = row[i]
    return departmentDict


def convertToJSON(tableColoumns):
    cur = con.cursor()
    cur.execute(selectQuery.format("artwork"))
    completeList = []
    artworkTable = cur.fetchall()
    i = 0
    for row in artworkTable:
        jsonObject = {}
        artworkDict,  departmentDict  = {}, {}
        for i in range(len(row)):
            artworkDict[tableColoumns["artwork"][i]] = row[i]
        jsonObject["artwork"] = artworkDict
        jsonObject["creator"] = getCreatorDetails(cur, row[0])
        jsonObject["department"] = getDepartmentDetails(cur, row[0])
        completeList.append(jsonObject)
    

        
    parsedJSON = json.dumps(completeList)
    jsonfile = open("cma_artworks.json", "w")
    print(parsedJSON)
    jsonfile.write(parsedJSON)
    jsonfile.close()
        

def getTableColoumnsMapping():
    cur = con.cursor()
    cur.execute(tableListQuery)
    tableColoumns = {tableName[0]:[] for tableName in cur.fetchall()}
    for tableName in tableColoumns:
        cur.execute(infoQuery.format(tableName))
        coloumnsList = [coloumnName[0] for coloumnName in cur.fetchall()]
        tableColoumns[tableName] = coloumnsList
    return tableColoumns

if(__name__ == '__main__'):
    tableListQuery = "SELECT name FROM sqlite_master WHERE type = 'table';"
    selectQuery = "SELECT * FROM '{}';"
    infoQuery = "SELECT name FROM PRAGMA_TABLE_INFO('{}');"
    artworkXcreator = "SELECT C.id, C.role, C.description FROM creator C join artwork__creator AC ON C.id = AC.creator_id WHERE artwork_id = '{}';"
    artworkXdepartment = "SELECT D.id, D.name FROM department D join artwork__department AD ON D.id = AD.department_id WHERE artwork_id = '{}';"
    con = sqlite3.connect("cma-artworks.db")
    tableColoumns = getTableColoumnsMapping()
    convertToJSON(tableColoumns)
    con.close()
   