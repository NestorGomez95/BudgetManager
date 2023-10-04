class Budget_Manager:

    def __init__(self,amount):
        self.Available = amount
        self.budgets = {}
        self.expenditure = {}

    def add_budget(self,name, amount):        
        if name in self.budgets:
            raise ValueError("Budget exists") 
        if amount > self.Available:
            raise ValueError("insuficient funds")
        self.budgets[name] = amount
        self.Available -= amount
        self.expenditure[name]= []
        return self.Available
    
    def change_budget(self,name,new_amount):
        if name not in self.budgets:
            raise ValueError("Budget does not exists")
        old_amount = self.budgets[name]
        if new_amount > old_amount + self.Available:
            raise ValueError("insuficient funds")
        self.budgets[name]= new_amount
        self.Available -= new_amount - old_amount
        return self.Available


    def spend(self,name, amount):
        if name not in self.expenditure:
            raise ValueError("no such budget")
        self.expenditure[name].append(amount)
        budgeted=self.budgets[name]
        spent = sum(self.expenditure[name])
        return budgeted - spent

    def print_summary(self):
        print("Budget            Budgeted      Spent  Remaining")
        print("--------------- ---------- ---------- ----------")
        total_Budgeted = 0
        total_spent = 0
        total_remaining = 0
        for name in self.budgets:
            budgeted=self.budgets[name]
            spent=sum(self.expenditure[name])
            remaining = budgeted - spent
            print(f"{name:15s} {budgeted:10.2f} {spent:10.2f}" f"{remaining:10.2f}")
            total_Budgeted += budgeted
            total_spent += spent
            total_remaining += remaining
        print("--------------- --------- ---------- -----------")
        print(f'{"total":15s} {total_Budgeted:10.2f} {total_spent:10.2f} {total_Budgeted - total_spent:10.2f}')


