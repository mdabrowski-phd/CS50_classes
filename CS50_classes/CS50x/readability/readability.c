#include <cs50.h>
#include <math.h>
#include <stdio.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    string text = get_string("Text: ");

    float L = (float) (count_letters(text)) / count_words(text) * 100;
    float S = (float) (count_sentences(text)) / count_words(text) * 100;

    int index = round(0.0588 * L - 0.296 * S - 15.8);

    if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}

int count_letters(string text)
{
    int counter = 0;

    for (int i = 0; text[i] != '\0'; i++)
    {
        if ((text[i] >= 65 && text[i] <= 90) || (text[i] >= 97 && text[i] <= 122))
        {
            counter++;
        }
    }

    return counter;
}

int count_words(string text)
{
    int counter = 1;

    for (int i = 0; text[i] != '\0'; i++)
    {
        if (text[i] == 32)
        {
            counter++;
        }
    }

    return counter;
}

int count_sentences(string text)
{
    int counter = 0;

    for (int i = 0; text[i] != '\0'; i++)
    {
        if (text[i] == 33 || text[i] == 46 || text[i] == 63)
        {
            counter++;
        }
    }

    return counter;
}