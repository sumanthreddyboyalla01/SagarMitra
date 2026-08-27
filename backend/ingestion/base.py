from abc import ABC, abstractmethod
import httpx
from datetime import datetime

class DataIngestionSource(ABC):
    """
    Abstract base class for all marine data ingestion sources.
    """
    
    def __init__(self, source_name: str):
        self.source_name = source_name
        self.client = httpx.AsyncClient()

    @abstractmethod
    async def fetch_data(self):
        """Fetch raw data from the external source."""
        pass
    
    @abstractmethod
    def parse_data(self, raw_data):
        """Parse raw data into structured models (e.g., Pydantic schemas)."""
        pass
    
    def generate_metadata(self) -> dict:
        """Generate provenance metadata."""
        return {
            "source": self.source_name,
            "fetched_at": datetime.utcnow().isoformat(),
            "version": "1.0"
        }
