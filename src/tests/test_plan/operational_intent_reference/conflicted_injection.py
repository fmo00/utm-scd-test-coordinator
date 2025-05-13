from . import is_response_conflict
from . import UssClientAdapter, AuthenticationClientAdapter


class TestClassOirConflictedInjection:
    uss_client: UssClientAdapter

    def __test_setup__(self) -> None:
        bearer_token_response = AuthenticationClientAdapter().get_bearer_token(
            "utm.strategic_coordination",
            "core-service",
            "testinginstance",
        )
        bearer_token = bearer_token_response.json()["token"]
        self.uss_client = UssClientAdapter(bearer_token)

    def test_execution(self) -> None:
        self.__test_setup__()

        body = {
            "coordinates": [
                [-48.06078566642705, -22.092882881260763],
                [-48.063437163986976, -22.09376733091004],
                [-48.062871511170556, -22.09723956118171],
                [-48.05785134242063, -22.09701026559017],
                [-48.05820487543116, -22.093275970670405],
                [-48.06078566642705, -22.092882881260763],
            ]
        }

        response = self.uss_client.post_oir(body)
        assert is_response_conflict(response)
