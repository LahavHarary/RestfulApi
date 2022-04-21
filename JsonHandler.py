import json
import os

def getVmIdAccordingToPath(path):
    # Opening JSON file
    f = open(path)

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Iterating through the json
    # list
    vm_id_list = []
    for vm in data['vms']:
        vm_id_list.append(vm["vm_id"])

    # Closing file
    f.close()

    return vm_id_list
def getAllVmsInFolder():
    path = "resources"
    listPaths = os.listdir(path)

    vm_ids_matrix = []

    for p in listPaths:
        vm_ids_matrix.append(getVmIdAccordingToPath(path +"/" +p))

    return vm_ids_matrix
def getVmTagAccordingToPath(index_of_file,vm_id):
    # Opening JSON file
    path = "resources/input-" +str(index_of_file) +".json"
    f = open(path)

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Iterating through the json
    for vm_data in data['vms']:
        if(vm_data['vm_id'] == vm_id):
            return vm_data['tags']
def getWhatTagsCanAccessVm(index_of_file,tags_from_vm):
    # Opening JSON file
    path = "resources/input-" +str(index_of_file) +".json"
    f = open(path)

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Iterating through the json
    # list
    ac_list = []
    if(type(tags_from_vm) == type([])):
        for obj in data["fw_rules"]:
            for tag in tags_from_vm:
                if (obj["dest_tag"] == tag):
                    ac_list.append(obj["source_tag"])
    else:
        for obj in data["fw_rules"]:
            if (obj["dest_tag"] == tags_from_vm):
                ac_list.append(obj["source_tag"])
    # Closing file
    f.close()

    return ac_list
def getMachinesThatCanAccessVm(index_of_file,tags_from_vm):
    # Opening JSON file
    path = "resources/input-" + str(index_of_file) + ".json"
    f = open(path)

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Iterating through the json
    # list
    ac_list = []
    for vm in data["vms"]:
        for tag_from_current_machine in vm["tags"]:
            for tag in tags_from_vm:
                if(tag_from_current_machine == tag):
                    ac_list.append(vm["vm_id"])

    # Closing file
    f.close()

    ac_list = list(dict.fromkeys(ac_list))
    return ac_list
def getRequestCount():
    path = "server_res/request_count.json"
    # Opening JSON file
    f = open(path)

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Closing file
    f.close()

    return data['count']
    # Iterating through the json
def addRequestCount():
    path = "server_res/request_count.json"
    # Opening JSON file
    f = open(path,'r+')

    # returns JSON object as
    # a dictionary
    data = json.load(f)
    data['count'] += 1

    f.seek(0)
    # convert back to json.
    json.dump(data, f, indent=4)

    # Closing file
    f.close()
def getStat():
    path = "server_res/statToPresent.json"

    f = open(path, 'r+')

    # returns JSON object as
    # a dictionary
    data = json.load(f)
    fileToShow = data['show']

    if(data['show'] < 3):
        data['show'] += 1
    else:
        data['show'] = 0
    f.seek(0)
    # convert back to json.
    json.dump(data, f, indent=4)

    # Closing file
    f.close()

    return fileToShow
def getAverageTime():
    path = "server_res/averageTime.json"
    f = open(path, 'r')
    data = json.load(f)
    avg_time = data['avg_time']
    # Closing file
    f.close()
    return avg_time
def setAverageTime(new_time):
    path = "server_res/request_count.json"
    f = open(path, 'r')
    data = json.load(f)
    amount_requests = data['count']
    # Closing file
    f.close()

    averageTime = getAverageTime()
    newAvgTime = ((averageTime*amount_requests) + new_time) / (amount_requests + 1)

    path = "server_res/averageTime.json"
    f = open(path, 'r+')
    data = json.load(f)
    data['avg_time'] = newAvgTime

    f.seek(0)
    # convert back to json.
    json.dump(data, f,indent=4)
    f.truncate()
    # Closing file
    f.close()