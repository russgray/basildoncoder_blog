Title: Project Euler Problem 4: Extra
Date: 2008-04-22 13:10
Author: Russell Gray
Slug: project-euler-problem-4-extra

Couple of things to add to [yesterday's post][1] about [problem 4][2]. As is
so often the case in life, no sooner had I finished the article than I
realised there was an obvious additional step I could make, which I'd somehow
failed to spot.

Regarding the C# solution, an easy win having implemented the Reverse
extension method would be to add an IsPalindrome extension to the string class
too. The implementation is straightforward:

    :::csharp
    public static bool IsPalindrome(this string s)
    {
        return s == s.Reverse();
    }

With this done, the where clause in the LINQ query is more readable, and
we have a couple of handy reusable string extensions into the bargain.

    :::csharp
    var result = (from product in AllProducts.From(100).To(999)
                  where product.ToString().IsPalindrome()
                  select product).Max();

Also, Sol commented that the C code could have a direct implementation of a
palindrome function, rather than messing about with strrev, since the
implementations are very similar. Whilst this series isn't really focussed on
the performance benefit of this approach, it does also make the code more
expressive, so I'll include it:

    :::c
    int strpalindrome(char* s) {
        char *s1, *s2;
        s1 = s2 = s;
        while (*s2)
            s2++;
        while (s1 < s2) {
            if (*(s1++) != *(--s2))
                return 0;
        }
        return 1;
    }

The loop now looks like this:

    :::c
    for (i = 100; i < 1000; ++i) {
        for (j = i; j < 1000; ++j) {
            int sum = i * j;
            sprintf(s1, "%d", sum);
            if (strpalindrome(s1) && sum > largest) {
                largest = sum;
            }
        }
    }

If you are interested in the Project Euler problems but craving more detailed
analysis, [Joel Neely][3] is [working through][4] at a similar rate to me, but
focusing his efforts on Scala and studying each problem and its solution in
greater depth rather than flitting from language to language. Highly
recommended.


[1]: {filename}/projecteuler/Project-Euler-Problem-4.md
[2]: http://projecteuler.net/index.php?section=problems&id=4
[3]: http://joelneely.wordpress.com/
[4]: http://joelneely.wordpress.com/category/project-euler/