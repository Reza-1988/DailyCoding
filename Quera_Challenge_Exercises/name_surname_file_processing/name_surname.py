import csv


# Global State (variables that hold the game status)
safe_list = {}   # Dictionary: category → list of valid/allowed words.
                 # Example: safe_list["esm"] = ["بردیا", "بابک", ...]
participants = {}# Dictionary: player → their submitted answers (raw form).
                 # Example: participants["ali"] = {"esm": "بابک", "famil": "اکبری", ...}
repeats = {}     # Dictionary: category → dictionary of word → count of how many players used it.
                 # Example: repeats["esm"]["بابک"] = 2 means two players wrote "بابک".
scores = {}      # Final scores of each player after calculation. player → score.
special = []     # List of categories where at least one player left the answer blank.
                 # ⚠️ Important: this affects scoring globally for that category (all players).


# Step 1: Read CSV file and initialize the game
def ready_up() -> None:
    """
    This function resets the game state and loads category names
    and their allowed words from a CSV file.
    - First row of the CSV contains category names (esm, famil, keshvar, ...).
    - Subsequent rows contain allowed/valid words for each category.
    """

    l = [] # Keeps the order of columns (maps each column index to category name).

    # Clear any leftover data from previous game
    safe_list.clear()
    special.clear()
    participants.clear()
    repeats.clear()
    scores.clear()

    with open('name_surname_data.csv', newline='', encoding='utf-8') as csvfile:
        file = csv.reader(csvfile)

        for i, row in enumerate(file):     # i = row index
            for j, ch in enumerate(row):   # j = column index, ch = cell content
                now = ch.replace(' ', '')  # Normalize: remove spaces from answers

                if i == 0:
                    # First row → category names (e.g., "esm", "famil", "rang", ...)
                    safe_list[now] = []    # Initialize category with empty list of valid words
                    l.append(now)          # Track category order (map j → category)
                    repeats[now] = {}      # Initialize empty dictionary to count repeats later

                elif ch != '':
                    # Other rows → valid/allowed words for each category
                    safe_list[l[j]].append(now)


# Step 2: Add a new player's answers
def add_participant(participant: str, answers: dict[str, str]):
    """
    Adds one player's answers to the game state.
    - Updates the `repeats` dictionary (word frequency per category).
    - Tracks blank answers by adding that category into `special`.
    - Stores the player's answers in `participants`.
    """

    for answer in answers:  # Loop over all categories (keys of answers dict)
        now = answers[answer].replace(' ', '')  # Normalize (remove spaces)

        if now == '':
            # If this category was left blank by the player:
            # Mark the category as "special".
            # NOTE: This means even one blank in this category
            # will affect scoring rules for ALL players in that category.
            special.append(answer)

        elif now not in repeats[answer]:
            # If this is the first time this word appears in this category
            repeats[answer][now] = 1
        else:
            # If this word already exists, increment its count
            repeats[answer][now] += 1

    # Save this player's answers (raw form, not normalized) for later scoring
    participants[participant] = answers


# Step 3: Calculate scores for all players
def calculate_all() -> dict[str, int]:
    """
    Calculates the score for each player based on rules:

    Rules:
    1. If the answer is NOT in the allowed list → 0 points.
    2. If the answer IS valid but was repeated by other players:
       - Normally: 5 points.
       - If the category is "special" (because someone left it blank): 10 points.
    3. If the answer IS valid and unique:
       - Normally: 10 points.
       - If the category is "special": 15 points.

    At the end, returns a dictionary of player → score.
    """

    for participant in participants:
        score = 0

        for category in participants[participant]:
            now = participants[participant][category].replace(' ', '')

            if now not in safe_list[category]:
                # Word is not in the allowed list at all → 0 points
                score += 0

            elif repeats[category][now] > 1:
                # Word is valid but repeated by more than one player
                if category in special:
                    score += 10  # Repeated + special bonus
                else:
                    score += 5   # Repeated (no bonus)

            else:
                # Word is valid AND unique (only one player wrote it)
                if category in special:
                    score += 15  # Unique + special bonus
                else:
                    score += 10  # Unique (no bonus)

        # Save final score for this player
        scores[participant] = score

    return scores
