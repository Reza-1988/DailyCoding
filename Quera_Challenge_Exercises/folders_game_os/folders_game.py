import os

repeat = {}

def extension_combat(salib_format: str, sajjad_format: str, path: str) -> str:
    salib = 0
    sajjad = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            file_name = file.split(".")[0]
            if file.endswith(salib_format):
                salib += 1
            elif file.endswith(sajjad_format):
                sajjad += 1
            if not file.endswith(sajjad_format):
                if file_name not in repeat:
                    repeat[file_name] = 1
                else:
                    repeat[file_name] += 1

    if sajjad > salib:
        return "Win! Normally!"

    else:
        cheat_name = ""
        count = 0
        for f_name in repeat:
            if repeat[f_name] > 1:
                cheat_name = f_name
                count += repeat[f_name]
        sajjad += count
        salib -= count
        if sajjad > salib:
            return f"Win! you can win if you cheat on '{cheat_name}'!"
        else:
            return "Lose! you can't win this game!"



print(extension_combat("jpg", "mp4", "./test/test_sample"))

# x = {'sajjad': {'video1': 1, 'video2': 1, 'video': 1}, 'salib': {'image': 1}}
# print(x["sajjad"]["video1"])