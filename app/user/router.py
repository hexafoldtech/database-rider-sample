from typing import Dict, Optional

from fastapi import APIRouter, Query

user_router = APIRouter()


@user_router.get("/login", response_model=Dict, tags=["User"])
async def calculate_dashboard_single_card_widget(
        email: Optional[str] = Query(None, example="test@gmail.com"),
        password: Optional[str] = Query(None, example="1234"),
) -> Dict:
    if email == "test@gmail.com" and password == "1234":
        return {
            "message": "Success"
        }
    else:
        return {
            "message": "Failure"
        }
