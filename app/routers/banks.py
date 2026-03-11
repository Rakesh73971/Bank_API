from fastapi import APIRouter,Depends,status,HTTPException
from app.models import Bank,Branch
from app.schemas import BankBase,BankResponse,BranchResponse
from sqlalchemy.orm import Session
from app.database import get_db
from typing import List

router = APIRouter(
    prefix='/banks',
    tags=['Banks']
)


@router.post('/',status_code=status.HTTP_201_CREATED,response_model=BankResponse)
def create_bank(bank_data:BankBase,db:Session=Depends(get_db)):
    bank = Bank(**bank_data.model_dump())
    db.add(bank)
    db.commit()
    db.refresh(bank)
    return bank

@router.get('/',status_code=status.HTTP_200_OK,response_model=List[BankResponse])
def get_banks(db:Session=Depends(get_db)):
    banks = db.query(Bank).all()
    return banks


@router.get('/{bank_id}',status_code=status.HTTP_200_OK,response_model=BankResponse)
def get_bank(bank_id:int,db:Session=Depends(get_db)):
    bank = db.query(Bank).filter(Bank.id == bank_id).first()
    if bank is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'bank with id {id} not found')
    return bank

@router.get("/{bank_id}/branches", response_model=list[BranchResponse])
def get_bank_branches(bank_id: int, db: Session = Depends(get_db)):

    bank = db.query(Bank).filter(Bank.id == bank_id).first()

    if bank is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Bank with id {bank_id} not found"
        )

    branches = db.query(Branch).filter(Branch.bank_id == bank_id).all()

    return branches