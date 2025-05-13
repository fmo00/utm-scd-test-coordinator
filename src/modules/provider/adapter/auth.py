import os
from requests import Request, Response, Session

from . import GET_TOKEN_ENDPOINT_PATH, TokenRequestQueryParamsBuilder


class AuthenticationClientAdapter:
    session = Session()

    def __init__(self):
        self.base_url: str = os.getenv("AUTH_API_URL")
        self.token = ""

    def __build_get_token_query_params(
        self, scope: str, intended_audience: str, sub: str
    ) -> dict:
        return TokenRequestQueryParamsBuilder(scope, intended_audience, sub).values

    def get_bearer_token(
        self, scope: str, intended_audience: str, sub: str
    ) -> Response:
        url = self.base_url + GET_TOKEN_ENDPOINT_PATH
        params = self.__build_get_token_query_params(scope, intended_audience, sub)

        req = Request("GET", url, data={}, params=params, headers=self.session.headers)
        prepped_req = self.session.prepare_request(req)

        try:
            return self.session.send(prepped_req)
        except Exception as err:
            raise err
