Here is a C# console application that implements a wildcard pattern matcher with support for `?` and `*`.

```C#
using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Enter the string:");
        string str = Console.ReadLine();
        Console.WriteLine("Enter the pattern:");
        string pattern = Console.ReadLine();
        Console.WriteLine(IsMatch(str, pattern));
    }

    static bool IsMatch(string str, string pattern)
    {
        int s = 0, p = 0, match = 0, starIdx = -1;
        while (s < str.Length)
        {
            if (p < pattern.Length && (pattern[p] == '?' || str[s] == pattern[p]))
            {
                s++;
                p++;
            }
            else if (p < pattern.Length && pattern[p] == '*')
            {
                starIdx = p;
                match = s;
                p++;
            }
            else if (starIdx != -1)
            {
                p = starIdx + 1;
                match++;
                s = match;
            }
            else return false;
        }

        while (p < pattern.Length && pattern[p] == '*')
            p++;

        return p == pattern.Length;
    }
}
```

This console application reads a string and a pattern from the user. It then checks if the string matches the pattern using the `IsMatch` function. The `IsMatch` function uses two pointers to traverse the string and the pattern. If the current characters in the string and the pattern match or the current character in the pattern is a '?', it moves both pointers. If the current character in the pattern is a '*', it checks the next character. If the next character does not match the current character in the string, it moves the string pointer. If none of these conditions are met, it returns false. After traversing the string, it checks if there are any remaining '*' characters in the pattern. If there are, it moves the pattern pointer. If the pattern pointer has reached the end of the pattern, it returns true, indicating that the string matches the pattern.