from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class CreatePaymentResponse(BaseModel):
    id_pagamento:int
