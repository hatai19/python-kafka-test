from fastapi import APIRouter, Query

from applications.schemas import ApplicationCreateSchema
from applications.services import ApplicationService
from applications.dependencies import KafkaDepend, DatabaseDepend


applications_router = APIRouter(prefix='/applications', tags=['applications'])

@applications_router.post('')
async def create_applications(broker: KafkaDepend, application_data: ApplicationCreateSchema, db: DatabaseDepend):
    application_service = ApplicationService(db, broker)
    return await application_service.create_application(application_data)


@applications_router.get('')
async def get_applications(db: DatabaseDepend, page: int = Query(1, ge=1),
    size: int = Query(5, ge=1),user_name: str = Query(None)):
    application_service = ApplicationService(db)
    return await application_service.get_application(page, size, user_name)


