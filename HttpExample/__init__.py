import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    #Required Message Body variables
    name = req.params.get('name')
    code = req.params.get('code')
    country = req.params.get('country')
    
    #Text Variables for reply message.
    assignment = "Jose Mad Man Martinaz"
    status = "Dealdly"
    action = "KOS"

    #Get Required Body
    if not name and not code and not country:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else: #no error
            name = req_body.get('name')
            code = req_body.get('code')
            country = req_body.get('country')

    #Response
    if name and not code:
        return func.HttpResponse(f"Hello, {name}.\Please Supply Required Access Code\nThis HTTP triggered function executed successfully.")
    elif name and code and country:
        return func.HttpResponse(f"Hello, {name}.\Operative Department: {country}\nCode: {code}\nAssignment: {assignment}\nStatus: {status}\nRecomended Action: {action}\nThis HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
    
    