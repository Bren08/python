def count_upper_case(message):
    count = 0
    for c in message:
        if c.isupper():
            count += 1
    return sum([1 for c in message if c.isupper()])
    
assert count_upper_case("") == 0, "Empty string"
assert count_upper_case("A") == 1, "One uppercase"
assert count_upper_case("a") == 0, "One lowercase"
assert count_upper_case("£$%^") == 0, "Special characters"
assert count_upper_case("B") == 1, "Two uppercase"

print("All the tests passed!")