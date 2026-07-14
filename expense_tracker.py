import sys
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.total_expenses = 0.0
        self.expense_count = 0
        self.expense_history = []
        self.is_running = True
        self.SENTINEL = 'done'
        
    def validate_input(self, user_input):
        user_input = user_input.strip()
        
        if not user_input:
            return False, None, "❌ Input cannot be empty. Please enter a valid amount."
        
        if user_input.lower() == self.SENTINEL:
            return True, None, "SHUTDOWN_SIGNAL"
        
        cleaned_input = user_input.replace('$', '').replace('₹', '').replace(',', '')
        
        try:
            expense_value = float(cleaned_input)
            
            if expense_value < 0:
                return False, None, "❌ Expense cannot be negative. Please enter a positive amount."
            
            if expense_value > 1_000_000_000:
                return False, None, "⚠️ Amount exceeds maximum limit. Please enter a reasonable expense."
            
            return True, expense_value, "Valid input"
            
        except ValueError:
            return False, None, f"❌ Invalid input: '{user_input}' is not a valid number. Please enter numeric values only."
    
    def process_expense(self, expense_amount):
        self.total_expenses += expense_amount
        self.expense_count += 1
        self.expense_history.append(expense_amount)
        
        print(f"\n✅ Expense added: ${expense_amount:,.2f}")
        print(f"📊 Running total: ${self.total_expenses:,.2f} ({self.expense_count} entries)")
        print("-" * 50)
    
    def display_summary(self):
        print("\n" + "=" * 60)
        print("📋 EXPENSE TRACKER - FINAL SUMMARY".center(60))
        print("=" * 60)
        
        print(f"\n📈 Total Expenses:  ${self.total_expenses:,.2f}")
        print(f"📊 Number of Entries: {self.expense_count}")
        
        if self.expense_count > 0:
            average = self.total_expenses / self.expense_count
            print(f"📉 Average Expense:  ${average:,.2f}")
            
            print(f"\n🔍 Expense Details:")
            print(f"   • Minimum expense: ${min(self.expense_history):,.2f}")
            print(f"   • Maximum expense: ${max(self.expense_history):,.2f}")
            
            if len(self.expense_history) <= 10:
                print(f"\n📝 Transaction History:")
                for i, amount in enumerate(self.expense_history, 1):
                    print(f"   {i}. ${amount:,.2f}")
            else:
                print(f"\n📝 Last 5 transactions:")
                for i, amount in enumerate(self.expense_history[-5:], len(self.expense_history) - 4):
                    print(f"   {i}. ${amount:,.2f}")
        
        print(f"\n🕐 Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 60)
        
        self.quality_validation()
    
    def quality_validation(self):
        print("\n🔒 QUALITY VALIDATION CHECK:")
        
        calculated_total = sum(self.expense_history)
        if abs(calculated_total - self.total_expenses) < 0.01:
            print("   ✅ Data integrity verified - all accumulations match")
        else:
            print("   ⚠️ Data integrity alert - mismatch detected")
        
        if self.expense_count == 0:
            print("   ⚠️ No expenses recorded - system idle")
        else:
            print(f"   ✅ Processing complete - {self.expense_count} transactions processed")
        
    def run(self):
        print("=" * 60)
        print("💰 EXPENSE TRACKER v2.0 - Batch 2026".center(60))
        print("=" * 60)
        print("\n📌 INSTRUCTIONS:")
        print("   • Enter expense amounts (e.g., 100, 50.50, 1000)")
        print("   • Type 'DONE' when finished")
        print("   • Your data is processed in real-time\n")
        print("📍 SYSTEM STATUS: ACTIVE - Ready for input\n")
        print("-" * 60)
        
        while self.is_running:
            try:
                user_input = input("\n💵 Enter expense amount: ")
                
                is_valid, value, message = self.validate_input(user_input)
                
                if is_valid and message == "SHUTDOWN_SIGNAL":
                    print("\n🛑 THE KILL SWITCH: Graceful shutdown initiated...")
                    self.is_running = False
                    break
                
                if not is_valid:
                    print(f"\n{message}")
                    print("💡 Tip: Enter numbers only (e.g., 100, 45.50, 2000)")
                    continue
                
                self.process_expense(value)
                
            except KeyboardInterrupt:
                print("\n\n🛑 Execution halted via keyboard interrupt")
                self.is_running = False
                break
            except Exception as e:
                print(f"\n⚠️ Unexpected error occurred: {e}")
                print("🔄 System continues...")
        
        self.display_summary()
        
        print("\n✨ TRANSACTION COMPLETE - Thank you for using Expense Tracker")
        print("🏢 DecodeLabs - Building Your First State-Preserving Backend Engine\n")
        
        return self.total_expenses

def main():
    tracker = ExpenseTracker()
    final_total = tracker.run()
    return 0

if __name__ == "__main__":
    sys.exit(main())