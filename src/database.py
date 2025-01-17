from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

database_url = f'postgresql+asyncpg://postgres:postgres@db:5432/postgres'

async_engine = create_async_engine(database_url)
async_session_maker = async_sessionmaker(async_engine)

async def get_db() -> AsyncSession:
    async with async_session_maker() as session:
        yield session