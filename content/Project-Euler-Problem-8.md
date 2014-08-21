Title: Project Euler Problem 8
Date: 2009-02-09 19:30
Author: Russell Gray
Slug: Project-Euler-Problem-8

<p>
[***Problem
8***](http://projecteuler.net/index.php?section=problems&id=8)  

> "Find the greatest product of five consecutive digits in the
> 1000-digit number.
>
> </p>
> 73167176531330624919225119674426574742355349194934  
> 96983520312774506326239578318016984801869478851843  
> 85861560789112949495459501737958331952853208805511  
> 12540698747158523863050715693290963295227443043557  
> 66896648950445244523161731856403098711121722383113  
> 62229893423380308135336276614282806444486645238749  
> 30358907296290491560440772390713810515859307960866  
> 70172427121883998797908792274921901699720888093776  
> 65727333001053367881220235421809751254540594752243  
> 52584907711670556013604839586446706324415722155397  
> 53697817977846174064955149290862569321978468622482  
> 83972241375657056057490261407972968652414535100474  
> 82166370484403199890008895243450658541227588666881  
> 16427171479924442928230863465674813919123162824586  
> 17866458359124566529476545682848912883142607690042  
> 24219022671055626321111109370544217506941658960408  
> 07198403850962455444362981230987879927244284909188  
> 84580156166097919133875499200524063689912560717606  
> 05886116467109405077541002256983155200055935729725  
> 71636269561882670428252483600823257530420752963450"

The first step here is to find a representation for that fairly
humungous number. Obviously it's not going to fit into a paltry 32-bit
int...but then we don't need it to. The problem description requires us
to think in terms of smaller (5-digit) numbers, not one giant 1000-digit
number.

<p>
So, it is sufficient for us to consider the number as an enumerable
stream of single digits, which we can conveniently represent as
IEnumerable<int>. I could use a macro to convert the number into a
collection initialiser, but it's much easier to treat the string as an
IEnumerable<char></char><char> and let LINQ do the heavy
lifting.</char></int>

~~~~ {name="code" language="csharp"}
var nums = Enumerable.AsEnumerable(        "73167176531330624919225119674426574742355349194934" +        "96983520312774506326239578318016984801869478851843" +        // ..... etc etc ......        "05886116467109405077541002256983155200055935729725" +        "71636269561882670428252483600823257530420752963450"        ).Select(x => Convert.ToInt32(x.ToString()));
~~~~

<p>
This gives us an IEnumerable<int></int><int> containing every digit in
the 1000-digit number. Now, the 'obvious' way to solve the problem is to
iterate through the collection, and at each index multiply the value
against the next four indexes. A simple loop should deal with it:</int>

~~~~ {name="code" language="csharp"}
private static int SimpleSolver(int[] ints){    int max = 0;    for (int i = 0; i < ints.Length - 4; i++)    {        int tmp = ints[i] * ints[i + 1] * ints[i + 2]            * ints[i + 3] * ints[i + 4];        max = Math.Max(max, tmp);    }    return max;}
~~~~

As ever, though, that's pretty ugly - the loop condition and product
calculation is tied to the sequence size of 5, and messing with an index
variable is tedious.

An alternative approach is to take advantage of LINQ's Skip and Take
methods to split the problem domain into overlapping 'slices'. Similar
to the for loop above, the core of the approach is to iterate through
the digits, and at each digit grab a number of subsequent digits and
calculate the product.

<p>
Lets look at the 5-digit slices available from the first 10 digits:

      7   3   1   6   7   1   7   6   5   3|       73167       |    |       31671       |        |       16717       |            |       67176       |                |       71765       |                    |       17653       |

<p>
We can use Skip to progressively move the starting index forward, and
Take to grab the 5 digits we need. So, starting with i=0, each
successive slice can be sliced from the whole with:

~~~~ {name="code" language="csharp"}
var slice = ints.Skip(i++).Take(5);
~~~~

<p>
To calculate the product of the digits in the slice, we can use the
Aggregate operation:

~~~~ {name="code" language="csharp"}
slice.Aggregate(1, (curr, next) => curr*next);
~~~~

We've met Aggregate before - it's basically a fold, which collapses a
sequence to a single item by repeatedly applying an operation to an
accumulating result.

<p>
This can all be wrapped up as an iterator block, like so:

~~~~ {name="code" language="csharp"}
private static IEnumerable EnumerateSlices(        IEnumerable ints, int sliceSize){    int i = 0;    while (true)    {        var slice = ints.Skip(i++).Take(sliceSize);        if (slice.Count() < sliceSize)            yield break; // end        yield return slice.Aggregate(1,                (curr, next) => curr*next);    }}
~~~~

Note the termination condition - when we have enumerated every slice,
our next slice will contain only 4 elements (3, 4, 5, and 0 from the end
of the sequence) - that's our cue to exit the loop.

Also note that this approach makes the algorithm trivial to parameterize
- it will work just as well with slice sizes other than 5.

<p>
This iterator will produce an IEnumerable<int> containing the products
of all slices, so the final step is to select the largest:</int>

~~~~ {name="code" language="csharp"}
var result = EnumerateSlices(nums, 5).Max();
~~~~
