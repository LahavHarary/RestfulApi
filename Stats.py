from flask_restful import Api, Resource, abort
import time
from JsonHandler import getAllVmsInFolder, getRequestCount, addRequestCount, getStat, setAverageTime, getAverageTime

vm_ids_matrix = getAllVmsInFolder()

class Stats(Resource):
    def get(self):
        tic = time.perf_counter()
        addRequestCount()
        num_of_file_to_present = getStat()

        if(num_of_file_to_present < 0 or 3 < num_of_file_to_present):
            status_code = abort(404)
            return status_code

        vm_count = 0
        for vm_id in vm_ids_matrix[num_of_file_to_present]:
            vm_count += 1

        toc = time.perf_counter()
        total_time_for_request = toc - tic
        setAverageTime(total_time_for_request)
        return {"vm_count": vm_count, "request_count":getRequestCount(),"average_request_time":getAverageTime()}