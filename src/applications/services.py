import logging

from faststream.kafka import KafkaBroker
from sqlalchemy.ext.asyncio import AsyncSession

from applications.repositories import ApplicationRepository

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ApplicationService:
    def __init__(self, session: AsyncSession, broker: KafkaBroker = None):
        self.application_repository = ApplicationRepository(session)
        self.broker = broker

    async def create_application(self, application_data):
        logger.info("Создаем новую заявку: %s", application_data)
        new_application = await self.application_repository.create_application(application_data)

        await self.broker.publish(
            f'{new_application.id}, {new_application.user_name}, '
            f'{new_application.description}, {new_application.created_at}',
            'my_topic'
        )

        application_json = self.application_to_json(new_application)

        return application_json

    async def get_application(self, page, size, user_name):
        logger.info("Получаем заявки с user_name: %s, page: %s, size: %s", user_name, page, size)

        if page < 1:
            logger.warning("Номер страницы меньше 1, устанавливаем страницу 1")
            page = 1

        offset = (page - 1) * size
        applications = await self.application_repository.get_applications(size, offset, user_name)

        if applications:
            applications_json = [self.application_to_json(app) for app in applications]
        else:
            applications_json = []

        return applications_json

    def application_to_json(self, application):
        if application is None:
            logger.warning("Заявки не получены")
            return None

        application_json = {
            "id": application.id,
            "user_name": application.user_name,
            "description": application.description,
            "created_at": application.created_at
        }

        return application_json