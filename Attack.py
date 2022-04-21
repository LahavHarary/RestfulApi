from flask_restful import Api,Resource
from flask import abort
from JsonHandler import getAllVmsInFolder, getVmTagAccordingToPath, getWhatTagsCanAccessVm, getMachinesThatCanAccessVm, \
    addRequestCount

vm_ids_matrix = getAllVmsInFolder()

class Attack(Resource):

    def get(self,vm_id_from_user):
        addRequestCount()
        index_can_access = -1

        # Check that the vm_id is valid
        for i in range(len(vm_ids_matrix)):
            for j in range(len(vm_ids_matrix[i])):
                if(vm_ids_matrix[i][j] == vm_id_from_user):
                    index_can_access = i
            if(index_can_access != -1):
                break

        if(index_can_access == -1):
            status_code = abort(404)
            return status_code

        else:
            vm_tags = getVmTagAccordingToPath(index_can_access,vm_id_from_user)
            tags_that_can_access = getWhatTagsCanAccessVm(index_can_access,vm_tags)
            vms_that_can_access = getMachinesThatCanAccessVm(index_can_access,tags_that_can_access)
            return vms_that_can_access
