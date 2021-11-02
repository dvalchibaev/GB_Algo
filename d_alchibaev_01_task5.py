"""
https://app.diagrams.net/?src=about#G1_ybhflNhSgdjKr9pnmvfvuAVZttaYqhU
"""
symbol_one = input()
symbol_two = input()


place_one = ord(symbol_one) - ord('a') + 1
place_two = ord(symbol_two) - ord('a') + 1
distance = abs(place_one - place_two)
print(f"{place_one}, {place_two}, {distance}")
