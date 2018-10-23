from .databases import Users, Data
import json, simplejson, ipaddress
from flask import jsonify

def mergeJSON(jsonA, jsonB):
    for i in range(len(jsonB["data"])):
        jsonA["data"].append(jsonB["data"][int(i)])

    return jsonA

class IPContainer():

    def existUser(_username):
        return Users.exist(_username)

    def addUser(_username):
        ret = False
        if not Users.exist(_username):
            Users.insert(_username)
            ret = True

        return ret

    def removeUser(_username):
        ret = False
        if Users.exist(_username):
            Users.delete(_username)
            ret = True

        return ret

    def getNumberOfUsers():
        return Users.tableSize()

    def getNumberOfNetworks():
        return Data.tableSize()

    def existNetwork(_username, _type):
        return Data.exist(_username, _type)

    def createNetwork(_username, _type):
        ret = False
        if Users.exist(_username):
            if not Data.exist(_username, _type):
                Data.createNetwork(_username, _type)
                ret = True

        return ret

    def removeNetwork(_username, _type):
        ret = False
        if Users.exist(_username):
            if Data.exist(_username, _type):
                Data.delete(_username, _type)
                ret = True

        return ret

    def addIPtoNetwork(_username, _type, _data):
        ret = False
        if Users.exist(_username):
            if Data.exist(_username, _type):
                jsonA = Data.getData(_username, _type)
                jsonMerged = mergeJSON(jsonA, _data)
                Data.updateData(_username, _type, jsonMerged)
                ret = True

        return ret

    def removeIPfromNetwork(_username, _type, _ip):
        ret = False
        if Users.exist(_username):
            if Data.exist(_username, _type):
                data = Data.getData(_username, _type)

                if _type == "dns":
                    for i in range(len(data["data"]) - 1):
                        print(len(data["data"]))
                        if data["data"][int(i)]["dns1"] == _ip or data["data"][int(i)]["dns2"] == _ip:
                            data["data"].pop(int(i))
                            ret = True

                else:
                    for i in range(len(data["data"]) - 1):
                        if data["data"][int(i)]["ip"] == _ip:
                            data["data"].pop(int(i))
                            ret = True

                if ret:
                    Data.updateData(_username, _type, data)

        return ret

    def getNetworkSize(_username, _type):
        if Users.exist(_username):
            if Data.exist(_username, _type):
                return len(Data.getData(_username, _type)["data"])

        return None

    def getData(_username, _type):
        if Users.exist(_username):
            if Data.exist(_username, _type):
                return Data.getData(_username, _type)

        return None

    def getAllData(_username):
        djson = {'username':_username, 'noofnetworks':0, 'networks':[]}
        if Users.exist(_username):
            data = Data.getAllData(_username)
            djson['noofnetworks'] = len(data)
            for i in range (len(data)):
                djson['networks'].append({'type':data[i]._type, 'network':data[i]._data})

        return json.dumps(djson)

    def getStatus():
        types = ['dns', 'wlan', 'vlan', 'pan', 'lan', 'san', 'wan']
        networks = {'dns':Data.countType('dns'), 'wlan':Data.countType('wlan'), 'vlan':Data.countType('vlan'), 'pan':Data.countType('pan'), 'lan':Data.countType('lan'), 'wan':Data.countType('wan'), 'san':Data.countType('san')}
        djson = {'users':IPContainer.getNumberOfUsers(), 'noofnetworks':IPContainer.getNumberOfNetworks(), 'networks':networks}

        return json.dumps(djson)

    def _dropUsers():
        Users._dropTable()

    def _dropData():
        Data._dropTable()
