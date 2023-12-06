# GCD Methods

We explore various algorithms to compute the greatest common divisor (GCD) in Python.

1. **Naive Algorithm**: We first start with the naive algorithm that calculate from the min of the two number until it hits zero and verfie if both devide one of the numbers

2. **Euclidean Algorithm**: We use the mathematical formule of euclidienne that it says if `d | a` and `d | b` so `d | a - b` so if we do it again substructing the min from the max and assin it to the max until we hit zero we will get the result

3. **Using Remainders**: we adjacted the algorithme by using the the rest of two number if we have a formila that has two distance values as `(933790548, 7)` we can quiqly have the result by have the rest rather that than substracting again and again, and it is the same thing mathematically cause substracting again and again will give us the rest at the end

4. **Recursive Approach**: Modifies the algorithm to call itself with altered parameters. The first parameter becomes `b`, and the second becomes `a % b`. Upon reaching zero with `b`, the GCD is obtained.

5. **Utilizing a Lemma**: Applies a lemma stating that if `d | a` and `d | b`, and `d = ax + by`, then `d` is the GCD. In this implementation, we check if `b == 0`; if true, `a` becomes the GCD. Else, we recursively call the function with adjusted parameters using the lemma:

    we verify if `b == 0` cause if it is then a is the gcd also when we will call the recursive function this condition is what it ends series of calling, then if it is not the case we call the function and get the arguments, d, p,q that we need so we can verify get the d at the end (the d in this case is not the gcd we just verify if it equal to `d == a * x + b * y` but it is still not devide both of arguments), we use the fact that `gcd(a, b) = gcd(b, a%b)` so we can repeat the calling of function until we arrive to when `a%b` hit zero, so now we return `x `that is `q` and `y` that is `p - q (a//b)` (is the equivalence of the formila when we change a and b by b and a%b so d = ax + by will be d = bx + (a%b)y that it is d = bx + (a - a//b * b)*y) and so on

These algorithms aim to test the runtime efficiency of different GCD calculation methods in Python.
