import os

from . import (
    QUERY_PARAM_API_KEY_NAME,
    QUERY_PARAM_INTENDED_AUDIENCE_NAME,
    QUERY_PARAM_SCOPE_NAME,
    QUERY_PARAM_SUB_NAME,
)


class TokenRequestQueryParamsBuilder:
    values: dict

    def __init__(self, scope: str, intended_audience: str, sub: str):
        self.values = self.__build(scope, intended_audience, sub)

    def __build(self, scope: str, intended_audience: str, sub: str) -> dict:
        return {
            QUERY_PARAM_SCOPE_NAME: scope,
            QUERY_PARAM_INTENDED_AUDIENCE_NAME: intended_audience,
            QUERY_PARAM_SUB_NAME: sub,
            QUERY_PARAM_API_KEY_NAME: os.getenv("DSS_API_KEY"),
        }
