from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Branch
from app.schemas import BranchBase,BranchResponse

router = APIRouter(
    prefix='/branches',
    tags=['Branches']
)

@router.get('/{branch_id}',status_code=status.HTTP_200_OK,response_model=BranchResponse)
def get_branch(branch_id:int,db:Session=Depends(get_db)):
    branch = db.query(Branch).filter(Branch.id == branch_id).first()
    if branch is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Branch with id {id} not found')
    return branch

@router.post('/',status_code=status.HTTP_201_CREATED,response_model=BranchResponse)
def create_branch(branch_data:BranchBase,db:Session=Depends(get_db)):
    branch = Branch(**branch_data.model_dump())
    db.add(branch)
    db.commit()
    db.refresh(branch)
    return branch


