from typing import List
from modules.model.area.polygon.vertices import PolygonVertices

LAT_INDEX = 0
LONG_INDEX = 1


def convert(json_config) -> List[PolygonVertices]:
    formated_vertices = []
    vertices = json_config["features"][0]["geometry"]["coordinates"][0][0]
    for i in range(0, len(vertices)):
        coordinate = PolygonVertices(
            lat=vertices[i][LAT_INDEX], lng=vertices[i][LONG_INDEX]
        )
        formated_vertices.append(coordinate)

    return formated_vertices
