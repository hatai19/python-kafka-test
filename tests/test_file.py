import pytest
from src.applications.repositories import ApplicationRepository
from src.applications.schemas import ApplicationCreateSchema
from tests.conftest import async_session_maker_new


@pytest.mark.parametrize("user_name, description", [
    ("test_user_1", "Test application description 1"),
    ("test_user_2", "Test application description 2"),
    ("test_user_3", "Test application description 3"),
])
async def test_create_applications(user_name, description):
    application_data = ApplicationCreateSchema(
        user_name=user_name,
        description=description
    )

    async with async_session_maker_new() as session:
        application_repository = ApplicationRepository(session)

        created_application = await application_repository.create_application(application_data)

        assert created_application is not None
        assert created_application.user_name == application_data.user_name
        assert created_application.description == application_data.description


async def test_get_applications():
    async with async_session_maker_new() as session:
        application_repository = ApplicationRepository(session)
        retrieved_applications = await application_repository.get_applications(limit=10, offset=0)

        assert retrieved_applications is not None
        assert len(retrieved_applications) == 3

