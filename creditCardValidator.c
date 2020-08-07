#include <stdio.h>
#include <cs50.h>
#include <math.h>

string cardType(long num);
int checkValid(long num);

int main(void)
{
    long card = get_long("Number: ");
    
    if (checkValid(card) == 1)
    {
        printf("%s", cardType(card));
    }
    else
    {
        printf("INVALID\n");
    }
}

// function to identify the card type
string cardType(long num)
{
    if (num >= pow(10, 12) && num < pow(10, 13)) // 13 digits <= num < 14 digits
    {
        return "VISA\n";
    }
    else if (num >= pow(10, 14) && num < pow(10, 15)) // 15 digits <= num < 16 digits
    {
        if ((int)(num / pow(10, 13)) == 34 || (int)(num / pow(10, 13)) == 37)
        {
            return "AMEX\n";
        }
    }
    else if (num >= pow(10, 15) && num < pow(10, 16)) // 16 digits <= num < 17 digits
    {
        if ((int)(num / pow(10, 15)) == 4) // first digit = 4
        {
            return "VISA\n";
        }
        else if ((int)(num / pow(10, 14)) > 50 && (int)(num / pow(10, 14)) < 56) // 50 < first digit < 56
        {
            return "MASTERCARD\n";
        }
    }
    return "INVALID\n";
}

// a function to check if the card is valid
int checkValid(long num)
{
    // calculates the sum of every other digit multiplied by 2
    long numA = num / 10;
    int totalA = 0;
    while(numA > 0)
    {
        int result = (numA % 10) * 2;
        
        // if numA's last digit*2 consists of 2 digits, separates them and adds the separated digits to totalA
        if (result >= 10)
        {
            totalA += result % 10;
            totalA += result / 10;
        }
        else
        {
            totalA += result; // adds numA's last digit*2 to totalA
        }
        
        numA = numA / 100; // removes last 2 digits of numA
    }
    
    // calculates sum of the digits that werent multiplied by 2 
    int totalB = 0;
    while (num > 0)
    {
        totalB += num % 10; // adds num's last digit to totalB
        
        num = num / 100; // removes last 2 digits of num
    }
    
    // adds the two totals and checks that last digit is 0
    int total = totalA + totalB;
    if (total % 10 == 0)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
