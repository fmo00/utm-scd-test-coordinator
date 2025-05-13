import pytest
import logging
import os

from dotenv import load_dotenv
from uuid import uuid4


@pytest.fixture(scope="session", autouse=True)
def load_environment():
    load_dotenv()

@pytest.fixture(autouse=True)
def dump_metadata():
    execution_identifier = uuid4()
    uss_provider_alias = os.getenv("USS_PROVIDER_ALIAS")

    logger = logging.getLogger()
    logger.info(f"Test execution identifier - {execution_identifier}")
    logger.info(f"UTM Service Suplier alias - {uss_provider_alias}")
