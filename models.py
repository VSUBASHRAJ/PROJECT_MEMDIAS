# This file is not actively used as we're using Firebase for data storage
# But it's included for potential future database integration
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional


@dataclass
class Media:
    """Represents a media attachment in a memory entry."""
    id: str
    type: str  # 'image', 'video', or 'audio'
    data: str  # Base64 encoded data
    created_at: datetime


@dataclass
class Memory:
    """Represents a single memory entry."""
    id: str
    user_id: str
    title: str
    content: str
    date: str
    time: str
    media: List[Media]
    created_at: datetime
    updated_at: Optional[datetime] = None


@dataclass
class User:
    """Represents a user in the system."""
    id: str
    email: str
    display_name: Optional[str] = None
    photo_url: Optional[str] = None
    created_at: datetime = datetime.now()
