# app/routers/banks.py

from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import BankBase, BankResponse, BranchResponse
from ..services import bank_service


router = APIRouter(prefix="/banks", tags=["Banks"])


@router.get("/",status_code=status.HTTP_200_OK ,response_model=list[BankResponse])
def get_banks(db: Session = Depends(get_db)):
    return bank_service.get_all_banks(db)



@router.get("/{bank_id}",status_code=status.HTTP_200_OK,response_model=BankResponse)
def get_bank(bank_id: int, db: Session = Depends(get_db)):
    bank = bank_service.get_bank_by_id(bank_id, db)

    if not bank:
        raise HTTPException(status_code=404, detail="Bank not found")

    return bank


@router.get("/{bank_id}/branches",status_code=status.HTTP_200_OK ,response_model=list[BranchResponse])
def get_bank_branches(bank_id: int, db: Session = Depends(get_db)):

    branches = bank_service.get_bank_branches(bank_id, db)

    if not branches:
        raise HTTPException(status_code=404, detail="No branches found")

    return branches


@router.post("/",status_code=status.HTTP_201_CREATED, response_model=BankResponse)
def create_bank(bank: BankBase, db: Session = Depends(get_db)):
    return bank_service.create_bank(bank, db)