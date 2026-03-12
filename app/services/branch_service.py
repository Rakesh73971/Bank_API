
from sqlalchemy.orm import Session
from ..models import Branch


def get_branch_by_id(branch_id: int, db: Session):
    return db.query(Branch).filter(Branch.id == branch_id).first()


def get_all_branches(db: Session):
    return db.query(Branch).all()

def create_branch(branch_data,db:Session):
    branch = Branch(**branch_data.model_dump())
    db.add(branch)
    db.commit()
    db.refresh(branch)
    return branch