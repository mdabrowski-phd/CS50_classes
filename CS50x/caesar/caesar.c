#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

bool only_digits(string text);
char rotate(char c, int k);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    else
    {
        if (!only_digits(argv[1]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    int k = atoi(argv[1]);

    string text = get_string("plaintext:  ");
    printf("ciphertext: ");

    for (int i = 0; text[i] != '\0'; i++)
    {
        printf("%c", rotate(text[i], k));
    }

    printf("\n");
    return 0;
}

bool only_digits(string text)
{
    for (int i = 0; text[i] != '\0'; i++)
    {
        if (text[i] < 48 || text[i] > 57)
        {
            return false;
        }
    }
    return true;
}

char rotate(char c, int k)
{
    if (c >= 65 && c <= 90)
    {
        return (c - 65 + k) % 26 + 65;
    }
    else if (c >= 97 && c <= 122)
    {
        return (c - 97 + k) % 26 + 97;
    }
    else
    {
        return c;
    }
}
