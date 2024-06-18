from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum
from datetime import datetime
import time

class Language(str, Enum):
    PY = "python"
    JAVA = "Java"
    GO = "go"

class Comment(BaseModel):
    text: Optional[str] = None
    

class Blog(BaseModel):
    title: str
    description: Optional[str] = None
    is_active: bool
    langiage: Language = Language.JAVA
    created_at: datetime = Field(default_factory=datetime.now)
    comments: Optional[list[Comment]]
    

first_blog = Blog(title="My title", is_active=True, comments=[{"text": "My first comment"}])
print(first_blog)

#time.sleep(5)

#second_blog = Blog(title="my title", is_active=True)    
#print(second_blog)