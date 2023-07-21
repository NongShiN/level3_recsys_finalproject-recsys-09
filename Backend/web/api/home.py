from fastapi import APIRouter, Request, Depends
from schemas.response import BaseResponse
from schemas.request import FeedbackRequest
from core.preload import get_template
from core.save_db import save_feedback

home_router = APIRouter(prefix="/home")

@home_router.post("/")
def home_page(request: Request,  feedback: FeedbackRequest = Depends(FeedbackRequest.as_form)):
    
    templates =  get_template()
    
    id = request.cookies.get("id")
    save_feedback(id, feedback)
    
    return templates.TemplateResponse("main.html", BaseResponse(request=request).__dict__)


@home_router.get("/")
def home_page(request: Request):
    """
        시작 화면을 return한다.
    """
    
    templates = get_template()
    
    response = templates.TemplateResponse("main.html", BaseResponse(request=request).__dict__)
    
    return response