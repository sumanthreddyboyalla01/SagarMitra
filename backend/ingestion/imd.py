from .base import DataIngestionSource

class IMDIngestion(DataIngestionSource):
    def __init__(self):
        super().__init__(source_name="IMD")
        
    async def fetch_data(self):
        # Stub: Implement scraping or API fetching for IMD Weather Data
        pass
        
    def parse_data(self, raw_data):
        # Stub: Convert raw data into backend.schemas.WeatherDataCreate
        pass
