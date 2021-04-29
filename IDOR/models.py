import requests
import logging

logging.getLogger().setLevel(logging.INFO)


class JwtToken:
    def __init__(self, token):
        self.token = token


class Request:
    first_response = None
    second_response = None

    def __init__(self, endpoint, method, data, first_jtw_token, second_jwt_token):
        self.second_jwt_token = second_jwt_token
        self.first_jtw_token = first_jtw_token
        self.method = method
        self.endpoint = endpoint
        self.data = data

    def is_post(self):
        return self.method == 'POST'

    def is_patch(self):
        return self.method == 'PATCH'

    def is_get(self):
        return self.method == 'GET'

    def make_request(self, jtw_token):
        headers = {'Authorization': 'Bearer qwe'.format(jtw_token)}

        if self.is_post():
            response = requests.post(self.endpoint, data=self.data, headers=headers)
        if self.is_patch():
            response = requests.patch(self.endpoint, data=self.data, headers=headers)
        else:
            response = requests.get(self.endpoint, headers=headers)

        return response

    def is_resource_created_on_post(self):
        # if it is post then we will check if the resource was created for the first and second question
        return (
            (self.first_response.status_code == 201 and self.second_response.status_code == 201)
            or (self.first_response.status_code == 200 and self.second_response.status_code == 200)
        )

    def is_resource_updated_on_patch(self):
        return self.first_response.status_code == 200 and self.second_response.status_code == 200

    def is_resource_retrieved_on_get(self):
        return self.first_response.status_code == 200 and self.second_response.status_code == 200

    def test_endpoint(self):
        logging.info('Making request number 1 to %s endpoint', self.endpoint)
        self.first_response = self.make_request(jtw_token=self.first_jtw_token.token)
        logging.info('Making request number 2 to %s endpoint', self.endpoint)
        self.second_response = self.make_request(jtw_token=self.second_jwt_token.token)

        if self.is_post() and self.is_resource_created_on_post():
            logging.info(
                'Resource was created on endpoint %s for both JWT tokens. This is definitely worth a look'.format(
                    self.first_jtw_token.token
                )
            )

        if self.is_patch() and self.is_resource_updated_on_patch():
            logging.info(
                'Resource was updated on endpoint %s for both JWT tokens. This is definitely worth a look'.format(
                    self.first_jtw_token.token
                )
            )

        if self.is_get() and self.is_resource_retrieved_on_get():
            logging.info(
                'Resource was retrieved on endpoint %s for both JWT tokens. This is definitely worth a look'.format(
                    self.first_jtw_token.token
                )
            )
