#include <cs50.h>
#include <stdio.h>

long get_card_number(void);
void check_validity(long number);
int calculate_length(long number);
int calculate_checksum(long number);

bool isAMEX(long number);
bool isMASTERCARD(long number);
bool isVISA(long number);

int main(void)
{
    long number = get_card_number();
    check_validity(number);
}

long get_card_number(void)
{
    long number = get_long("Number: ");
    return number;
}

void check_validity(long number)
{

    int checksum = calculate_checksum(number);

    if (checksum % 10 == 0)
    {
        if (isAMEX(number))
        {
            printf("AMEX\n");
        }

        else if (isMASTERCARD(number))
        {
            printf("MASTERCARD\n");
        }

        else if (isVISA(number))
        {
            printf("VISA\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }
}

int calculate_length(long number)
{
    int numDigits = 0;

    do
    {
        numDigits++;
        number = number / 10;
    }
    while (number);

    return numDigits;
}

int calculate_checksum(long number)
{
    int odd_sum = 0, even_sum = 0, idx = 0;

    do
    {
        if (idx % 2 == 0)
        {
            odd_sum += number % 10;
        }
        else
        {
            int tmp = 2 * (number % 10);
            if (tmp >= 10)
            {
                even_sum += (tmp % 10) + 1;
            }
            else
            {
                even_sum += tmp;
            }
        }
        number /= 10;
        idx++;
    }
    while (number);

    return odd_sum + even_sum;
}

bool isAMEX(long number)
{
    int length = calculate_length(number);

    if (length == 15)
    {
        int tmp = number / 10000000000000;
        if (tmp == 34 || tmp == 37)
        {
            return true;
        }
    }
    return false;
}

bool isMASTERCARD(long number)
{
    int length = calculate_length(number);
    if (length == 16)
    {
        int tmp = number / 100000000000000;
        if (tmp >= 51 && tmp <= 55)
        {
            return true;
        }
    }
    return false;
}

bool isVISA(long number)
{
    int length = calculate_length(number);
    if (length == 13)
    {
        int tmp = number / 1000000000000;
        if (tmp == 4)
        {
            return true;
        }
    }
    else if (length == 16)
    {
        int tmp = number / 1000000000000000;
        if (tmp == 4)
        {
            return true;
        }
    }
    return false;
}
