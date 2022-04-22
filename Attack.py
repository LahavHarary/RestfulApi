from flask_restful import Api,Resource
from flask import abort
from JsonHandler import getAllVmsInFolder, getVmTagAccordingToPath, getWhatTagsCanAccessVm, getMachinesThatCanAccessVm, \
    addRequestCount

# Matrix that contains every vm in every file
# For example: The matrix in index 0 will have all the vms in file 0.
vm_ids_matrix = getAllVmsInFolder()

class Attack(Resource):

    def get(self,vm_id_from_user):
        # Every request has to be counted.
        # I created a function named "addRequestCount" that does so.
        addRequestCount()

        # index_can_access will be used to determine if the user has entered
        # A wrong id for the machine - if not, it will be used to access the machine properties.
        index_can_access = -1

        # Check that the vm_id is valid, Run on the vm_ids_matrix
        # For every json file check if the machine appears there.
        for i in range(len(vm_ids_matrix)):
            for j in range(len(vm_ids_matrix[i])):
                if(vm_ids_matrix[i][j] == vm_id_from_user):
                    index_can_access = i
            # If after iterating trough a whole file we found out that the vm is in it
            # There is no need to further search and a break statment is used.
            if(index_can_access != -1):
                break

        # After iterating trough every value in our matrix.
        # If the index is still -1 it means that a machine with the id that the user gave us
        # Can not be found.
        # To deal with it we will return 404 (Page Not Found) to the user.
        if(index_can_access == -1):
            status_code = abort(404)
            return status_code

        # In every other case, we know that a machine is in some file and we have the file index.
        else:
            # Extract the VM tags and save them in vm_tags
            vm_tags = getVmTagAccordingToPath(index_can_access,vm_id_from_user)

            # Get the tags that can access the VM and save them in tags_that_can_access
            tags_that_can_access = getWhatTagsCanAccessVm(index_can_access,vm_tags)

            # Get the Vms that can access the vm that the user gave us
            # Save the result in vms_that_can_access and return it
            vms_that_can_access = getMachinesThatCanAccessVm(index_can_access,tags_that_can_access)
            return vms_that_can_access
