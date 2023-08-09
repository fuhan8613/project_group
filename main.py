# main.py imports each python file as modules
import overheads,cash_on_hand,profit_loss
# main.py essentially acts as the coordinating program to execute each python file
def main():
    overheads.overheads() # Gives the Highest Overhead percentage
    cash_on_hand.cash_on_hand() # Gives the Highest Cash Surplus and the Day or the Cash Deficit and the Day
    profit_loss.profit_loss() # Gives the Highest Net Profit Surplus and the Day or the Profit Deficit and the Day
main()
