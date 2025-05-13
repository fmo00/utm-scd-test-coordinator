import os
from requests import Request, Response, Session


class UssClientAdapter:
    session = Session()

    def __init__(self, bearer_token: str):
        self.base_url: str = os.getenv("USS_API_URL")
        self.session.headers.update({"Authorization": "Bearer " + bearer_token})

    def post_oir(
        self,
        body: any,
    ) -> Response:
        url = self.base_url + f"/uss/v1/operational_intents"
        req = Request("POST", url, data=body)
        prepped_req = self.session.prepare_request(req)

        try:
            return self.session.send(prepped_req)
        except Exception as err:
            raise err

    def get_oir_by_id(
        self,
        entity_id: str,
    ) -> Response:
        url = self.base_url + f"/uss/v1/operational_intents/{entity_id}"
        req = Request("GET", url)
        prepped_req = self.session.prepare_request(req)

        try:
            return self.session.send(prepped_req)
        except Exception as err:
            raise err
