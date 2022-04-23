import requests

BASE = "http://127.0.0.1:5000/api/v1/stats"


def checkVmCount():
    print("_________START OF TEST NAME: checkVmCount_________")
    # This test needs to check whether the first value is one of the 4:
    # After it, we need to check that the rest of the values are in oredr
    # For example if the result was 5 it means that the next resoult should be 11
    # later on 2 and later on 10.

    vm_count_list = [10,5,11,2]

    TestCounter = 0
    response = requests.get(BASE)
    first_val = response.json()["vm_count"]
    flag = 0
    for i in range(len(vm_count_list)):
        if(first_val == vm_count_list[i]):
            print("test no ", TestCounter, " succeeded")
            flag = 1
            next_val_to_check = i+1
            break
    if(flag == 0):
        print("test no ", TestCounter, " failed")

    TestCounter += 1

    for i in range(next_val_to_check,len(vm_count_list)):
        response = requests.get(BASE)
        val = response.json()["vm_count"]
        if(val == vm_count_list[i]):
            print("test no ", TestCounter, " succeeded")
        else:
            print("test no ", TestCounter, " failed")
        TestCounter += 1

    for i in range(0,next_val_to_check):
        response = requests.get(BASE)
        val = response.json()["vm_count"]
        if (val == vm_count_list[i]):
            print("test no ", TestCounter, " succeeded")
        else:
            print("test no ", TestCounter, " failed")
        TestCounter += 1
def checkRequestCount():
    print("_________START OF TEST NAME: checkVmCount_________")
    # Get the number of requests by sending a regular request, save the number
    # check if the number is incrementing -> do this 10 times.

    response = requests.get(BASE)
    first_val = response.json()["request_count"]

    TestCounter = 0
    for i in range(10):
        response = requests.get(BASE)
        if(first_val < response.json()["request_count"]):
            print("test no ", TestCounter, " succeeded")
        else:
            print("test no ", TestCounter, " failed")
        TestCounter += 1

checkVmCount()
checkRequestCount()