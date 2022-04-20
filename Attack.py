from flask_restful import Api,Resource
from flask import abort
from JsonHandler import getAllVmsInFolder, getVmTagAccordingToPath, getWhatTagsCanAccessVm, getMachinesThatCanAccessVm, \
    addRequestCount

vm_ids_matrix = getAllVmsInFolder()

class Attack(Resource):

    def get(self,vm_id_from_user):
        addRequestCount()
        index_can_access = -1
        index_that_needs_to_be_removed = -1

        # Check that the vm_id is valid
        for i in range(len(vm_ids_matrix)):
            for j in range(len(vm_ids_matrix[i])):
                if(vm_ids_matrix[i][j] == vm_id_from_user):
                    index_can_access = i
                    index_that_needs_to_be_removed = j
            if(index_can_access != -1):
                break

        if(index_can_access == -1):
            status_code = abort(404)
            return status_code

        else:
            vm_tags = getVmTagAccordingToPath(index_can_access,vm_id_from_user)
            tags_that_can_access = getWhatTagsCanAccessVm(index_can_access,vm_tags)
            vms_that_can_access = getMachinesThatCanAccessVm(index_can_access,tags_that_can_access,vm_id_from_user)
            return vms_that_can_access

            #pass
            #if the vm_id was valid, we now need to check who can access it.
            #vm_ids_copy = vm_ids_matrix[index_can_access].copy()
            #vm_ids_copy.pop(index_that_needs_to_be_removed)
            #return vm_ids_copy