Here is a Java console application that solves the problem:

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the string:");
        String str = scanner.nextLine();
        System.out.println("Enter the pattern:");
        String pattern = scanner.nextLine();
        System.out.println("Does the string match the pattern? " + isMatch(str, pattern));
    }

    public static boolean isMatch(String s, String p) {
        int i = 0;
        int j = 0;
        int starIndex = -1;
        int iIndex = -1;

        while (i < s.length()) {
            if (j < p.length() && (p.charAt(j) == '?' || p.charAt(j) == s.charAt(i))) {
                ++i;
                ++j;
            } else if (j < p.length() && p.charAt(j) == '*') {
                starIndex = j;
                iIndex = i;
                j++;
            } else if (starIndex == -1) {
                return false;
            } else {
                j = starIndex + 1;
                i = iIndex+1;
                iIndex++;
            }
        }

        while (j < p.length() && p.charAt(j) == '*') {
            ++j;
        }

        return j == p.length();
    }
}
```

This console application reads a string and a pattern from the user, and then checks if the string matches the pattern. The `isMatch` method implements the wildcard pattern matching. It supports `?` which can match any single character, and `*` which can match any sequence of characters (including an empty sequence).