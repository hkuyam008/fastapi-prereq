from fastapi import FastAPI, Depends, HTTPException, status

blogs = {
    "1": "FastAPI Prerequisite",
    "2": "Building APIs with FastAPI",
    "3": "Background Tasks | Celery X FastAPI"
}

users = {
    "8": "Jamie",
    "9": "Roman"
}


app = FastAPI(title = "Dependency Injection", version="1.0.0")

# def get_object_or_404(model: dict, id: str):
    
#     object = model.get(id)
    
#     if not object:
#         raise HTTPException(detail=f"Object with id {id} does not exist", status_code=status.HTTP_404_NOT_FOUND)
    
#     return object

class GetObject:
    
    def __init__(self, model) -> None:
        self.model = model
        
    def __call__(self,id: str):
        
        obj = self.model.get(id)
        
        if not obj:
             raise HTTPException(detail=f"Object with id {id} does not exist", status_code=status.HTTP_404_NOT_FOUND)
        
        return obj    

blog_dependency = GetObject(blogs)
@app.get("/blog/{id}")
def get_blog(blog_name: str = Depends(blog_dependency)):
    return blog_name

user_dependency = GetObject(users)
@app.get("/user/{id}")
def get_user(user_name: str = Depends(user_dependency)):
    return user_name