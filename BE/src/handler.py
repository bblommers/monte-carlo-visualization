import json
from BE.src.montecarlo import black_scholes, monte_carlo


required_params = ["S0", "K", "T", "sigma", "r"]
cors_headers = {"Access-Control-Allow-Origin": "http://montecarlovisualization.s3-website.eu-west-2.amazonaws.com"}


def hello(event, context):
    input = json.loads(event["body"])
    for param in required_params:
        if param not in input:
            raise Exception

    #res = black_scholes(**input)
    res = monte_carlo(**input)
    response = {"result": res}
    response = {
        "statusCode": 200,
        "headers": cors_headers,
        "body": json.dumps(response)
    }

    return response
