from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.dialects.postgresql import JSONB
from geoalchemy2 import Geometry
from datetime import datetime, timezone
from .database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

class Location(Base):
    __tablename__ = 'locations'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    name = Column(String(100))
    geom = Column(Geometry(geometry_type='POINT', srid=4326))
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

class PFZZone(Base):
    __tablename__ = 'pfz_zones'
    id = Column(Integer, primary_key=True, index=True)
    geom = Column(Geometry(geometry_type='POLYGON', srid=4326))
    source_metadata = Column(JSONB, default={})
    timestamp = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

class WeatherData(Base):
    __tablename__ = 'weather_data'
    id = Column(Integer, primary_key=True, index=True)
    geom = Column(Geometry(geometry_type='POINT', srid=4326))
    temperature = Column(Float)
    wind_speed = Column(Float)
    wind_direction = Column(Float)
    wave_height = Column(Float)
    source_metadata = Column(JSONB, default={})
    timestamp = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

class OceanData(Base):
    __tablename__ = 'ocean_data'
    id = Column(Integer, primary_key=True, index=True)
    geom = Column(Geometry(geometry_type='POINT', srid=4326))
    sst = Column(Float) # Sea Surface Temperature
    salinity = Column(Float)
    source_metadata = Column(JSONB, default={})
    timestamp = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

class MarineAdvisory(Base):
    __tablename__ = 'marine_advisories'
    id = Column(Integer, primary_key=True, index=True)
    message = Column(Text, nullable=False)
    valid_from = Column(DateTime, nullable=False)
    valid_to = Column(DateTime, nullable=False)
    source_metadata = Column(JSONB, default={})
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

class Hazard(Base):
    __tablename__ = 'hazards'
    id = Column(Integer, primary_key=True, index=True)
    hazard_type = Column(String(100)) # e.g. Cyclone, Tsunami, High Waves
    geom = Column(Geometry(geometry_type='POLYGON', srid=4326), nullable=True)
    description = Column(Text)
    source_metadata = Column(JSONB, default={})
    timestamp = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

class RestrictedZone(Base):
    __tablename__ = 'restricted_zones'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200))
    zone_type = Column(String(100))
    geom = Column(Geometry(geometry_type='POLYGON', srid=4326))
    source_metadata = Column(JSONB, default={})
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

class Evidence(Base):
    __tablename__ = 'evidence'
    id = Column(Integer, primary_key=True, index=True)
    decision_context = Column(String(255))
    data = Column(JSONB) # Store reasoning / references
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
