import jwt

from . import is_response_forbidden
from . import UssClientAdapter
from . import ENTITY_ID


class TestClassAuthenticationInvalidTokenSignature:
    uss_client: UssClientAdapter

    def __generate_invalid_token(self) -> str:
        return jwt.encode({"value": "payload"}, "secret", algorithm="HS256")

    def __test_setup__(self) -> None:
        bearer_token = self.__generate_invalid_token()
        self.uss_client = UssClientAdapter(bearer_token)

    def test_execution(self) -> None:
        self.__test_setup__()

        ussp_response = self.uss_client.get_oir_by_id(ENTITY_ID)

        assert is_response_forbidden(ussp_response)
