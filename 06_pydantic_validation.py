from pydantic import BaseModel, field_validator, model_validator

class CreateUer(BaseModel):
    email: str
    password: str
    confirm_password: str
    
    @field_validator("email")
    def validate_email(cls, value):
        
        if "admin" in value:
            raise(ValueError, "This email is not allowed")
        
        return value

    @model_validator(mode="after")
    def validate_password(self):
        
        password = self.password
        confirm_password = self.confirm_password
        
        if password != confirm_password:
            raise(ValueError, "The two passwords do not match")
        
        return self

CreateUer(email="ping@fastapitutorial.com", password="123", confirm_password="123")