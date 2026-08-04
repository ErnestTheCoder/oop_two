import java.util.Scanner;

public class BankAccount 
{
    private double balance;

    public BankAccount(double initialBalance) {
        if (initialBalance < 0) {
            throw new IllegalArgumentException("Initial Balance cannot be negative");
        }
        this.balance = initialBalance;
    }

    public double getBalance() {
        return balance;
    }

    public void setBalance(double amount) {
        if (amount < 0) {
            throw new IllegalArgumentException("Balance cannot be negative");
        }
        this.balance = amount;
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
       
       
        System.out.print("Enter Initial balance: ");
        double initialbalance = input.nextDouble();
        
        
        System.out.print("Enter Updated balance: ");
        double updatebalance = input.nextDouble(); 
        
       
        BankAccount acc = new BankAccount(updatebalance); 
        
        System.out.println("Initial Balance: "+ initialbalance  );
        System.out.println("Updated balance: " + acc.getBalance());
        
        input.close();
    }
}
