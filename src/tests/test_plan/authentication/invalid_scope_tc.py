from . import AuthenticationClientAdapter, UssClientAdapter
from . import is_response_forbidden
from . import ENTITY_ID


class TestClassAutenticationInvaliScope:
    uss_client: UssClientAdapter

    def __test_setup__(self) -> None:
        bearer_token = AuthenticationClientAdapter().get_bearer_token(
            "utm.invalid_scope", "icea", "speedbird"
        )
        self.uss_client = UssClientAdapter(bearer_token)

    def test_execution(self) -> None:
        self.__test_setup__()

        ussp_response = self.uss_client.get_oir_by_id(ENTITY_ID)
        assert is_response_forbidden(ussp_response)
