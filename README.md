# Conc-Prop

Python module based on reading through Peter Norvig's [A Concrete Introduction to Probability](https://nbviewer.org/github/norvig/pytudes/blob/main/ipynb/Probability.ipynb)


## Vocab

__Classical__
- Trial: A single occurrence with an outcome that is uncertain until we observe it.  For example, rolling a single die.
- Outcome: A possible result of a trial; one particular state of the world. What Laplace calls a case.  For example: 4.
- Sample Space: The set of all possible outcomes for the trial.  For example, {1, 2, 3, 4, 5, 6}.
- Event: A subset of the sample space, a set of outcomes that together have some property we are interested in.  For example, the event "even die roll" is the set of outcomes {2, 4, 6}.
- Probability: As Laplace said, the probability of an event with respect to a sample space is the "number of favorable cases" (outcomes from the sample space that are in the event) divided by the "number of all the cases" in the sample space (assuming "nothing leads us to expect that any one of these cases should occur more than any other"). Since this is a proper fraction, probability will always be a number between 0 (representing an impossible event) and 1 (representing a certain event).  For example, the probability of an even die roll is 3/6 = 1/2.


__Distirbutions__
- Frequency: a non-negative number describing how often an outcome occurs. Can be a count like 5, or a ratio like 1/6.
- Distribution: A mapping from outcome to frequency of that outcome. We will allow sample spaces to be distributions.
- Probability Distribution: A probability distribution is a distribution whose frequencies sum to 1.

__Bayes__
> Why is Bayes Theorem recommended? Because we are asked about the probability of an outcome given the evidence—the probability the yellow came from the 94 bag, given that there is a yellow and a green. But the problem statement doesn't directly tell us the probability of that outcome given the evidence; it just tells us the probability of the evidence given the outcome.

Before we see the colors of the M&Ms, there are two hypotheses, A and B, both with equal probability:

    A: first M&M from 94 bag, second from 96 bag
    B: first M&M from 96 bag, second from 94 bag
    P(A) = P(B) = 0.5

Then we get some evidence:

    E: first M&M yellow, second green

We want to know the probability of hypothesis A, given the evidence:

    P(A | E)

That's not easy to calculate (except by enumerating the sample space, which our P function does). But Bayes Theorem says:

    P(A | E) = P(E | A) * P(A) / P(E)

The quantities on the right-hand-side are easier to calculate:

    P(E | A) = 0.20 * 0.20 = 0.04
    P(E | B) = 0.10 * 0.14 = 0.014
    P(A)     = 0.5
    P(B)     = 0.5
    P(E)     = P(E | A) * P(A) + P(E | B) * P(B) 
             = 0.04     * 0.5  + 0.014    * 0.5   =   0.027

And we can get a final answer:

      P(A | E) = P(E | A) * P(A) / P(E) 
               = 0.04     * 0.5  / 0.027 
               = 0.7407407407


> Bayes Theorem allows you to do less calculation at the cost of more algebra; that is a great trade-off if you are working with pencil and paper. Enumerating the sample space allows you to do less algebra at the cost of more calculation; usually a good trade-off if you have a computer. But regardless of the approach you use, it is important to understand Bayes theorem and how it works.

__Simulation__
> Sometimes it is inconvenient, difficult, or even impossible to explicitly enumerate a sample space. Perhaps the sample space is infinite, or perhaps it is just very large and complicated (perhaps with a bunch of low-probability outcomes that don't seem very important). In that case, we might feel more confident in writing a program to simulate a random outcome. Random sampling from such a simulation can give an accurate estimate of probability.

__Central Limit Theorem__

__Continuous Sample Spaces__
> Everything up to here has been about discrete, finite sample spaces, where we can enumerate all the possible outcomes.
> 
> But a reader asked about continuous sample spaces, such as the space of real numbers. The principles are the same: probability is still the ratio of the favorable cases to all the cases, but now instead of counting cases, we have to (in general) compute integrals to compare the sizes of cases
>
> The moral for continuous spaces is the same as for discrete spaces: be careful about defining your sample space; measure carefully, and let your code take care of the rest.

## Functions

```
# Input set arguments can be sets or callable predicates

# Classical (count from the entire space)
  P(set<T>, set<T>, fn, fn) -> Fraction  # Probability of success / outcomes
  combos(set<T>, int) -> set<T>     # combinations for a size n
  select(T, int, set<T>) -> set<T>  # subset selection of matching T of size n from sample space
  balls(T, int) -> set<T>           # specific for urn problem generation of T for size n
  choose(int, int) -> int           # arithmetic selection of n choose c

# Non-equiprobable Outcomes (distributions)
  Dist           # a class defining a distribution (count of event occurences)
  DistP          # since we need to change the spatiality of sample space, helper to overwrite "favorable" and "cases" calculations
  Dist.cases     # now sums the frequencies in a distribution (it previously counted the length).
  Dist.favorable # now returns a Dist of favorable outcomes and their frequencies (not a set).
  joint          # joint distribution of two independent distributions a and be where 'ab': freq(a) *  freq(b)

# Bayes
# Simulation
```
