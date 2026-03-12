from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import BranchResponse,BranchBase
from typing import List
from ..services import branch_service

router = APIRouter(prefix="/branches", tags=["Branches"])

@router.get("/{id}",status_code=status.HTTP_200_OK, response_model=BranchResponse)
def get_branch(id: int, db: Session = Depends(get_db)):

    branch = branch_service.get_branch_by_id(id, db)

    if not branch:
        raise HTTPException(status_code=404, detail="Branch not found")

    return branch

@router.get('/',status_code=status.HTTP_200_OK,response_model=List[BranchResponse])
def get_branches(db:Session=Depends(get_db)):
    branches = branch_service.get_all_branches(db)
    return branches

@router.post('/',status_code=status.HTTP_201_CREATED,response_model=BranchResponse)
def create_branch(branch_data:BranchBase,db:Session=Depends(get_db)):
    return branch_service.create_branch(branch_data,db)