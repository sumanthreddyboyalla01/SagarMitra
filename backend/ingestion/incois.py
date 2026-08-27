from .base import DataIngestionSource

class INCOISIngestion(DataIngestionSource):
    def __init__(self):
        super().__init__(source_name="INCOIS")
        
    async def fetch_data(self):
        # Stub: Implement scraping or API fetching for INCOIS PFZ and Ocean State Forecast
        pass
        
    def parse_data(self, raw_data):
        # Stub: Convert raw XML/HTML into backend.schemas.PFZZoneCreate
        pass
