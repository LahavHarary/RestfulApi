import requests

# A test class for every vm in input-x.json
# for example to test every vm in the file with index 0 call testInput0()

BASE = "http://127.0.0.1:5000/api/v1"

def testInput0():
    # Test for input-0-json
    vms = ['vm-a211de','vm-c7bac01a07']
    TestCounter = 0
    print("_________START OF TEST NO 0_________")

    for vm in vms:
        response = requests.get(BASE +"/attack/" + vm)
        if(response.json()[0] == 'vm-c7bac01a07'):
            print("test no " ,TestCounter," succeeded")
        else:
            print("test no ", TestCounter, " failed")
        TestCounter += 1
    print("")
def testInput1():
    # Test for input-1-json
    vms = ['vm-b8e6c350', 'vm-c1e6285f','vm-cf1f8621','vm-b462c04'
           ,'vm-8d2d12765','vm-9cbedf7c66','vm-ae24e37f8a','vm-e30d5fa49a'
        ,'vm-1b1cc9cd','vm-f270036588']
    TestCounter = 0
    print("_________START OF TEST NO 1_________")
    for vm in vms:
        response = requests.get(BASE + "/attack/" + vm)
        if (response.json() == []):
            print("test no ", TestCounter, " succeeded")
        else:
            print("test no ", TestCounter, " failed")
        TestCounter += 1
    print("")
def testInput2():
    # Test for input-2-json
    print("_________START OF TEST NO 2_________")
    vms = ['vm-ec02d5c153','vm-a3ed2eed23','vm-2ba4d2f87','vm-b35b501','vm-7d1ff7af47']
    TestCounter = 0
    for vm in vms:
        response = requests.get(BASE + "/attack/" + vm)
        if (response.json() == vms):
            print("test no ", TestCounter, " succeeded")
        else:
            print("test no ", TestCounter, " failed")
        TestCounter += 1
    print("")
def testInput3():
    # Test for input-3-json
    print("_________START OF TEST NO 3_________")
    vms = ['vm-9ea3998','vm-5f3ad2b','vm-d9e0825','vm-59574582',
           'vm-f00923','vm-575c4a','vm-0c1791','vm-2987241',
           'vm-ab51cba10','vm-a3660c','vm-864a94f']
    TestCounter = 0
    for i in range(len(vms)):
        response = requests.get(BASE + "/attack/" + vms[i])
        if (i == 8):
            temp_vms = vms.copy() # Copy VMS
            temp_vms.pop(8) # Drop vm-ab51cba10
            if(response.json() == temp_vms):
                print("test no ", TestCounter, " succeeded")
            else:
                print("test no ", TestCounter, " failed")
        else:
            if (response.json() == []):
                print("test no ", TestCounter, " succeeded")
            else:
                print("test no ", TestCounter, " failed")
        TestCounter += 1
    print("")

#testInput0()
#testInput1()
#testInput2()
#testInput3()
