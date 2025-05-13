from tests.config.geojson_to_object import convert
from . import UssClientAdapter, AuthenticationClientAdapter
from modules.model.area.polygon.outline import PolygonOutline


class TestClassPolygonAreaVerticesValidation:
    uss_client: UssClientAdapter
    polygon_area_outline: PolygonOutline

    def __test_setup__(self, json_config) -> None:
        bearer_token_response = AuthenticationClientAdapter().get_bearer_token(
            "utm.strategic_coordination",
            "core-service",
            "testing-instance",
        )
        bearer_token = bearer_token_response.json()["token"]
        self.uss_client = UssClientAdapter(bearer_token)
        self.polygon_area_outline = PolygonOutline(vertices=convert(json_config))

    def is_polygon_area_compliant(self, coordinates) -> bool:
        return len(coordinates) < 10000

    def test_execution(self, json_config) -> None:
        self.__test_setup__(json_config)
        assert self.is_polygon_area_compliant(self.polygon_area_outline.vertices)
