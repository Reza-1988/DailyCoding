import csv


safe_list = {} # List of allowed words for each category
participants = {} # Each player's answers
repeats = {} # Number of repetitions of each answer in each category.
scores = {} # Final score of each player
special = []


def ready_up() -> None:
    l = []
    safe_list.clear()
    special.clear()
    participants.clear()
    repeats.clear()
    scores.clear()
    with open('name_surname_data.csv', newline='', encoding='utf-8') as csvfile:
        file = csv.reader(csvfile)
        for i, row in enumerate(file):
            for j, ch in enumerate(row):
                now = ch.replace(' ', '')
                if i == 0:
                    # First line: Category names (keys)
                    safe_list[now] = []
                    l.append(now)
                    repeats[now] = {}
                elif ch != '':
                    safe_list[l[j]].append(now)


def add_participant(participant: str, answers: dict[str, str]):
    for answer in answers:
        now = answers[answer].replace(' ', '')
        if now == '':
            special.append(answer)
        elif now not in repeats[answer]:
            repeats[answer][now] = 1
        else:
            repeats[answer][now] += 1
    participants[participant] = answers


def calculate_all() -> dict[str, int]:
    for participant in participants:
        score = 0
        for category in participants[participant]:
            now = participants[participant][category].replace(' ', '')
            if now not in safe_list[category]:
                score += 0
            elif repeats[category][now] > 1:
                if category in special:
                    score += 10
                else:
                    score += 5
            else:
                if category in special:
                    score += 15
                else:
                    score += 10
        scores[participant] = score
    return scores

