
from sqlalchemy.orm import Session
from ..models import Bank, Branch


def get_bank_by_id(bank_id: int, db: Session):
    return db.query(Bank).filter(Bank.id == bank_id).first()


def get_all_banks(db: Session):
    return db.query(Bank).all()


def get_bank_branches(bank_id: int, db: Session):
    return db.query(Branch).filter(Branch.bank_id == bank_id).all()


def create_bank(bank_data, db: Session):
    bank = Bank(**bank_data.model_dump())
    db.add(bank)
    db.commit()
    db.refresh(bank)
    return bank