from pydantic import BaseModel

class BankCreate(BaseModel):
    name: str

class BankOut(BankCreate):
    id: int

    class Config:
        from_attributes = True

class BranchCreate(BaseModel):
    bank_id: int
    branch_name: str
    city: str
    ifsc: str

class BranchOut(BaseModel):
    id: int

    class Config:
        from_attributes = True
