#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    string msg = get_string("Message: ");

    int dec = 0;

    for (int i = 0; msg[i] != '\0'; i++)
    {
        dec = msg[i];
        bool bin[8];

        for (int j = 0; j < 8; j++)
        {
            bin[7 - j] = dec % 2;
            dec /= 2;
        }
        for (int j = 0; j < 8; j++)
        {
            print_bulb(bin[j]);
        }

        printf("\n");
    }
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}
