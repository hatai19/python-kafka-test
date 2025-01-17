from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

database_url = f'postgresql+asyncpg://postgres:postgres@db:5432/postgres'

async_engine = create_async_engine(database_url)
async_session_maker = async_sessionmaker(async_engine)