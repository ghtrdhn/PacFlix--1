from dataclasses import dataclass
from datetime import datetime
from dateutil import relativedelta
from plan import Plan

@dataclass
class User:
    username: str
    plan: Plan
    start_subs_time: datetime
    referral_code: str=None

    def __post_init__(self):
        self.invoice = self.plan.price
        

    def upgrade_plan(self, new_plan):
        
        if new_plan.level <= self.plan.level:
            print("Plan tidak boleh turun atau sama!")
            return 
        
        
        discount = 1  
        difference = relativedelta.relativedelta(datetime.now(), self.start_subs_time)
        if difference.years > 1:        
            discount = 0.95  

        self.plan = new_plan
        self.start_subs_time = datetime.now()
        self.invoice = self.plan.price * discount
        
    def fungsi(objek_user):
        print(objek_user.username)