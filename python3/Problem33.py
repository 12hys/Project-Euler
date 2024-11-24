from fractions import Fraction
from math import prod

numerators = range(10, 100)
denominators = range(99, 9, -1)

def curious_fraction(numerator, denominator):
    numerator_digits = [int(item) for item in list(str(numerator))]
    denominator_digits = [int(item) for item in list(str(denominator))]

    if len(numerator_digits) != len(denominator_digits):
        raise Exception("Numerator and denominator must have the same length")

    if numerator_digits[1] == 0 and denominator_digits[1] == 0:
        return False

    if numerator_digits[0] == denominator_digits[0]:
        return numerator_digits[1], denominator_digits[1]
    elif numerator_digits[0] == denominator_digits[1]:
        return numerator_digits[1], denominator_digits[0]
    elif numerator_digits[1] == denominator_digits[0]:
        return numerator_digits[0], denominator_digits[1]
    elif numerator_digits[1] == denominator_digits[1]:
        return numerator_digits[0], denominator_digits[0]
    else:
        return False

curious_fractions = []
for numerator in numerators:
    for denominator in denominators:
        if numerator/denominator >= 1:
            continue
        else:
            fraction_candidate = curious_fraction(numerator, denominator)

            if fraction_candidate:
                candidate_numerator = int(fraction_candidate[0])
                candidate_denominator = int(fraction_candidate[1])

                if candidate_denominator == 0:
                    continue

                if candidate_numerator == 0 and candidate_denominator == 0:
                    continue

                if numerator / denominator == candidate_numerator / candidate_denominator:
                    curious_fractions.append([numerator, denominator])

print(curious_fractions)

curious_fractions = [Fraction(fraction[0], fraction[1]) for fraction in curious_fractions]

print(prod(curious_fractions))



