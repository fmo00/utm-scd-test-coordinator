from http import HTTPStatus
from requests import Response


def is_response_successful(response: Response) -> bool:
    return response.status_code == HTTPStatus.OK


def is_response_forbidden(response: Response) -> bool:
    return response.status_code == HTTPStatus.FORBIDDEN


def is_response_unauthorized(response: Response) -> bool:
    return response.status_code == HTTPStatus.UNAUTHORIZED


def is_response_not_found(response: Response) -> bool:
    return response.status_code == HTTPStatus.NOT_FOUND


def is_response_conflict(response: Response) -> bool:
    return response.status_code == HTTPStatus.CONFLICT


def is_response_bad_request(response: Response) -> bool:
    return response.status_code == HTTPStatus.BAD_REQUEST
