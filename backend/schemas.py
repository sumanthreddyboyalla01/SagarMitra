from pydantic import BaseModel, ConfigDict
from typing import Optional, Dict, Any
from datetime import datetime

# Common response for geometry items (using WKT or GeoJSON representation)
class GeometryMixin(BaseModel):
    geom: Optional[str] = None # WKT format

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

class PFZZoneBase(BaseModel):
    geom: str
    source_metadata: Dict[str, Any] = {}
    timestamp: datetime

class PFZZoneResponse(PFZZoneBase):
    id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

class WeatherDataBase(BaseModel):
    geom: str
    temperature: Optional[float] = None
    wind_speed: Optional[float] = None
    wind_direction: Optional[float] = None
    wave_height: Optional[float] = None
    source_metadata: Dict[str, Any] = {}
    timestamp: datetime

class WeatherDataResponse(WeatherDataBase):
    id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

class OceanDataBase(BaseModel):
    geom: str
    sst: Optional[float] = None
    salinity: Optional[float] = None
    source_metadata: Dict[str, Any] = {}
    timestamp: datetime

class OceanDataResponse(OceanDataBase):
    id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

class MarineAdvisoryBase(BaseModel):
    message: str
    valid_from: datetime
    valid_to: datetime
    source_metadata: Dict[str, Any] = {}

class MarineAdvisoryResponse(MarineAdvisoryBase):
    id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)
