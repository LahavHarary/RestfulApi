from flask_restful import Api, Resource, abort
import time
from JsonHandler import getAllVmsInFolder, getRequestCount, addRequestCount, getStat, setAverageTime, getAverageTime

# Matrix that contains every vm in every file
# For example: The matrix in index 0 will have all the vms in file 0.
vm_ids_matrix = getAllVmsInFolder()

class Stats(Resource):
    def get(self):
        # tic is the start time for this function.
        tic = time.perf_counter()

        # addRequestCount is being called because a new request came from the user.
        addRequestCount()

        # In order to understand which file needs to be presented to the user
        # we are using a function named getStat.
        num_of_file_to_present = getStat()

        # Sanity check - if from some reason a number which isn't between 0-3 came back
        # it means that getStat gave us a wrong file number and the user will see an internal
        # error status (500)
        if(num_of_file_to_present < 0 or 3 < num_of_file_to_present):
            status_code = abort(500)
            return status_code

        # Counting the numbers of VM inside the file
        vm_count = 0
        for vm_id in vm_ids_matrix[num_of_file_to_present]:
            vm_count += 1

        # toc = the end time of the function
        toc = time.perf_counter()

        # Total time = endTime - startTime
        total_time_for_request = toc - tic

        # we are setting the new average with a function named setAverageTime
        setAverageTime(total_time_for_request)

        # Return all the data to the user
        return {"vm_count": vm_count, "request_count":getRequestCount(),"average_request_time":getAverageTime()}