def size(cms):
    if cms < 38:
        return 'S'
    elif cms > 38 and cms < 42:
        return 'M'
    else:
        return 'L'

assert(size(37) == 'S')
assert(size(40) == 'M')
assert(size(43) == 'L')

# Enhanced tests
assert(size(38) == 'M')  # Should fail, as the function currently skips this edge case
assert(size(42) == 'L')  # Should fail, as the function currently skips this edge case
assert(size(41) == 'M')  # Ensure boundary is correct

print("All is well (maybe!)\n")
