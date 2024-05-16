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