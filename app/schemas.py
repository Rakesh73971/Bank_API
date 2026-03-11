from pydantic import BaseModel

class BankBase(BaseModel):
    name : str

class BankResponse(BankBase):
    id : int

    class Config:
        from_attributes = True

class BranchBase(BaseModel):
    bank_id : int
    branch_name : str
    city : str
    ifsc : str

class BranchResponse(BranchBase):
    id : int

    class Config:
        from_attributes = True
