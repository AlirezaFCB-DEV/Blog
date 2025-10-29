import time

class Request_Timer_Middleware :
    def __init__(self , get_response):
        self.get_response = get_response
        
    def __call__(self, req):
        start_time = time.time()
        response = self.get_response(req)
        duration = round(time.time() - start_time , 4)
        print(f"Request took {duration} seconds")
        return response