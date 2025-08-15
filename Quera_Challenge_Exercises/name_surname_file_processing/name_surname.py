
name_surname = {
    "esm" : [],
    "famil" : [],
    "keshvar" : [],
    "rang" : [],
    "ashia": [],
    "gaza" : []
}

participants_answers = dict()


def ready_up() -> None:
    with open('name_surname_data.csv', 'r', encoding="utf-8") as file:

        for i, line in enumerate(file):
            if i == 0:
                continue
            parts = line.rstrip('\n').split(',')
            if len(parts) < 6:
                continue
            name_surname["esm"].append(parts[0].replace(" ", ""))
            name_surname["famil"].append(parts[1].replace(" ", ""))
            name_surname["keshvar"].append(parts[2].replace(" ", ""))
            name_surname["rang"].append(parts[3].replace(" ", ""))
            name_surname["ashia"].append(parts[4].replace(" ", ""))
            name_surname["gaza"].append(parts[5].replace(" ", ""))

def add_participant(participant: str, answers: dict[str, str]):
    cleaned_answers = dict()
    for k, v in answers.items():
        k_ = k.replace(" ", "")
        v_ = v.replace(" ", "")
        cleaned_answers[k_] = v_
    participants_answers[participant] = cleaned_answers


def calculate_all() -> dict[str, int]:
    pass

