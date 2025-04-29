cards = 52
red_cards = 26

# 1. Probability of drawing a red card
print(f"1. Probability of drawing a red card: {red_cards / cards}")

hearts = 13

# 2. Given drawn a red card, probability it's a heart
print(f"2. Given drawn a red card, probability it's a heart: {hearts / red_cards}")

total_face_cards = 12  
diamond_face_cards = 3 

# 3. Given drawn a face card, probability it's a diamond
print(f"3. Given drawn a face card, probability it's a diamond: {diamond_face_cards / total_face_cards}")

# 4. Given drawn a face card, probability it's a spade or queen
spade_face_cards = 3  
queens = 4  

spade_or_queen_face_cards = spade_face_cards + queens - 1

print(f"4. Given drawn a face card, probability it's a spade or queen: {spade_or_queen_face_cards / total_face_cards}")

