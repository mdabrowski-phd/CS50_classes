#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

bool valid_key(string text);
char rotate(char c, string key);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    else
    {
        if (!valid_key(argv[1]))
        {
            printf("Key must contain 26 characters.\n");
            return 1;
        }
    }

    string text = get_string("plaintext:  ");
    printf("ciphertext: ");

    for (int i = 0; text[i] != '\0'; i++)
    {
        printf("%c", rotate(text[i], argv[1]));
    }

    printf("\n");
    return 0;
}

bool valid_key(string text)
{
    if (strlen(text) != 26)
    {
        return false;
    }
    else
    {
        bool tab[26];
        for (int i = 0; i < 26; i++)
        {
            tab[i] = false;
        }

        for (int i = 0; i < 26; i++)
        {
            if (!isalpha(text[i]))
            {
                return false;
            }
            else if (tab[toupper(text[i]) - 65])
            {
                return false;
            }
            else
            {
                tab[toupper(text[i]) - 65] = true;
            }
        }
    }

    return true;
}

char rotate(char c, string key)
{
    if (isupper(c))
    {
        return toupper(key[c - 65]);
    }
    else if (islower(c))
    {
        return tolower(key[c - 97]);
    }
    else
    {
        return c;
    }
}
