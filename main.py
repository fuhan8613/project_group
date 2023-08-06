import overheads,cash_on_hand,profit_loss
def main():
    with open("summary_report.txt","w") as file:
        file.write(f'{overheads.overheads()}\n')
        file.write(f'{cash_on_hand.cash_on_hand()}')
        file.write(f'{profit_loss.profit_loss()}')    
main()