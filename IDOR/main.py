import json
from models import JwtToken, Request
import argparse


def parse_arguments():
    parse = argparse.ArgumentParser(
        description="Make requests to endpoints using two different JWT tokens allowing to check for IDOR "
                    "vulnerabilities "
    )

    parse.add_argument(
        '--file',
        help='File containing the endpoints. An example can be seen in this project folder',
        type=str,
        required=True
    )

    return parse.parse_args()


if __name__ == '__main__':
    args = parse_arguments()

    file = open(args.file, )

    data = json.load(file)

    first_token = JwtToken(data['first_token'])
    second_token = JwtToken(data['second_token'])

    endpoints = []

    for endpoint in data['endpoints']:
        endpoints.append(
            Request(
                endpoint=endpoint['endpoint'],
                method=endpoint['method'],
                data=endpoint['data'],
                first_jtw_token=first_token,
                second_jwt_token=second_token,
            )
        )

    for request in endpoints:
        request.test_endpoint()
