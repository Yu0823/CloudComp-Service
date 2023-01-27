from memcache import webapp
import json

# basic response
def basic_res(status=True):
    if status:
        response = webapp.response_class(
            response=json.dumps("OK"),
            status=200,
            mimetype='application/json'
        )
    else:
        response = webapp.response_class(
            response=json.dumps("Error"),
            status=400,
            mimetype='application/json'
        )
    return response

# boxing the res
def build_res(status, content):
    response = webapp.response_class(
        response=json.dumps(content),
        status=status,
        mimetype='application/json'
    )
    return response
