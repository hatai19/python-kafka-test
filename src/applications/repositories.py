from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
import logging
from applications.models import Application

logger = logging.getLogger(__name__)

class ApplicationRepository:
    def __init__(self, session):
        self.session = session

    async def create_application(self, application_data):
        new_application = Application(
            user_name=application_data.user_name,
            description=application_data.description
        )
        self.session.add(new_application)
        try:
            await self.session.commit()
            await self.session.refresh(new_application)
            logger.info("Заявка успешно создана: id:%s, user_name:%s",
                        new_application.id,
                        new_application.user_name)
            return new_application
        except SQLAlchemyError as e:
            await self.session.rollback()
            logger.error("Ошибка при создании заявки: %s", e)
            return None

    async def get_applications(self, limit, offset, user_name=None):
        try:
            query = select(Application).offset(offset).limit(limit)
            if user_name:
                query = query.where(Application.user_name == user_name)

            applications = await self.session.execute(query)
            logger.info("Заявки успешно получены с limit: %d, offset: %d",
                        limit, offset)
            return applications.scalars().all()
        except SQLAlchemyError as e:
            logger.error("Ошибка при получении заявок: %s", e)
            return None

