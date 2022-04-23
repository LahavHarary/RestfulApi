import json
import os

def getVmIdAccordingToPath(path):
    # A function that receives a path and returns every VM inside the file.
    with open(path) as f:
        data = json.load(f)
        vm_id_list = []
        for vm in data['vms']:
            vm_id_list.append(vm["vm_id"])

        return vm_id_list
def getAllVmsInFolder():
    # Open a folder name resources and get every VM inside the files in it
    path = "resources"
    listPaths = os.listdir(path)

    vm_ids_matrix = []

    for p in listPaths:
        vm_ids_matrix.append(getVmIdAccordingToPath(path +"/" +p))

    return vm_ids_matrix
def getVmTagAccordingToPath(index_of_file,vm_id):
    # The function user has to send the file that he wants to open and the vm_id
    # The function takes the VM tags and returns them to the user.
    path = "resources/input-" + str(index_of_file) + ".json"
    with open(path) as f:
        data = json.load(f)
        # Iterating through the json file
        for vm_data in data['vms']:
            if(vm_data['vm_id'] == vm_id):
                return vm_data['tags']
def getWhatTagsCanAccessVm(index_of_file,tags_from_vm):
    # Opening JSON file
    path = "resources/input-" +str(index_of_file) +".json"
    with open(path) as f:
        data = json.load(f)

        ac_list = []
        # tags_from_vm can be a single tag (string) or a list of strings.
        # In order to properly check the tag/s an if statment is used to check the type of
        # the variable.
        # If the type is list it means that we should iterate on it as well.
        # Else, there is no need to iterate over it (because it is a string and it will return
        # a single char in every iteration).
        if(type(tags_from_vm) == type([])):
            for obj in data["fw_rules"]:
                for tag in tags_from_vm:
                    if (obj["dest_tag"] == tag):
                        ac_list.append(obj["source_tag"])
        else:
            for obj in data["fw_rules"]:
                if (obj["dest_tag"] == tags_from_vm):
                    ac_list.append(obj["source_tag"])
        return ac_list
def getMachinesThatCanAccessVm(index_of_file,tags_that_can_access):
    # This function is used to get the machines that can access the specified VM.
    # The function receives a file index and tags that can access the vm
    # Our goal here is to iterate trough every vm in the file and check if one (or more)
    # of her tags is one (or more) of the tags that can access.

    path = "resources/input-" + str(index_of_file) + ".json"
    with open(path) as f:
        data = json.load(f)

        # Iterating through the json
        ac_list = []
        for vm in data["vms"]:
            for tag_from_current_machine in vm["tags"]:
                for tag in tags_that_can_access:
                    if(tag_from_current_machine == tag):
                        ac_list.append(vm["vm_id"])

        ac_list = list(dict.fromkeys(ac_list))
        return ac_list
def getRequestCount():
    # A function that gets data from a file named "request_count" and returns it to the user.
    path = "server_res/request_count.json"
    with open(path) as f:
        data = json.load(f)
        return data['count']
def addRequestCount():
    # A function that adds one to the data in a file named "request_count"
    # The function is being called every time a user is asking for something from the API
    path = "server_res/request_count.json"

    with open(path,'r+') as f:
        data = json.load(f)
        data['count'] += 1

        f.seek(0)
        # convert back to json.
        json.dump(data, f, indent=4)
def getStat():
    # A function that gets data from a file named "statToPresent"
    # The function is responsible for updating the state and returning the old state to the
    # function user.

    # For example: if the current status is 0 -> it means that the user should look at
    # the statistics of the file with index 0.
    # The function is responsible to return 0 to the function user and update the value to 1.
    path = "server_res/statToPresent.json"

    with open(path,'r+') as f:
        data = json.load(f)
        fileToShow = data['show']

        # There are currently only 4 folders that have indexes 0-3.
        # If index is 3 it means that the next file to show needs to be 0.
        if(data['show'] < 3):
            data['show'] += 1
        else:
            data['show'] = 0
        f.seek(0)
        # convert back to json.
        json.dump(data, f, indent=4)

        return fileToShow
def getAverageTime():
    # A function that gets data from a file named "averageTime" and returns it to the user.
    path = "server_res/averageTime.json"
    with open(path,'r') as f:
        data = json.load(f)
        avg_time = data['avg_time']
        return avg_time
def setAverageTime(new_time):
    # A function that updates the average time in a folder named "averageTime"

    # first we get the data from request_count
    # later on we get the data from averageTime
    # After we have those we will use a simple equation to get the new average.
    # the equation is:
    # avgTime * amountRequests = total
    # (total + newTime) / (amountRequests + 1) = the new avg

    path = "server_res/request_count.json"
    with open(path,'r') as f:
        data = json.load(f)
        amount_requests = data['count']

    averageTime = getAverageTime()
    newAvgTime = ((averageTime*amount_requests) + new_time) / (amount_requests + 1)

    path = "server_res/averageTime.json"
    f = open(path, 'r+')
    with open(path,'r+') as f:
        data = json.load(f)
        data['avg_time'] = newAvgTime

        f.seek(0)
        # convert back to json.
        json.dump(data, f,indent=4)
        f.truncate()