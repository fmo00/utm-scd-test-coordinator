from . import UssClientAdapter, AuthenticationClientAdapter
from . import is_response_not_found
from . import ENTITY_ID


class TestClassAuthenticationSuccessful:
    uss_client: UssClientAdapter

    def __test_setup__(self) -> None:
        bearer_token = AuthenticationClientAdapter().get_bearer_token(
            "utm.invalid_scope", "icea", "aerospy"
        )
        self.uss_client = UssClientAdapter(bearer_token)

    def execute(self) -> None:
        self.__test_setup__()

        ussp_response = self.uss_client.get_oir_by_id(ENTITY_ID)
        assert is_response_not_found(ussp_response)
