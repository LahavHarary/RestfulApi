from flask_restful import Api, Resource, abort

from JsonHandler import getAllVmsInFolder, getRequestCount, addRequestCount

vm_ids_matrix = getAllVmsInFolder()

class Stats(Resource):
    def get(self,num_of_file_from_user):
        addRequestCount()

        if(num_of_file_from_user < 0 or 3 < num_of_file_from_user):
            status_code = abort(404)
            return status_code

        vm_count = 0

        for vm_id in vm_ids_matrix[num_of_file_from_user]:
            vm_count += 1

        return {"vm_count": vm_count, "request_count":getRequestCount()}