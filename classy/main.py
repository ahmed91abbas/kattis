# https://open.kattis.com/problems/classy
import sys


def get_name_list_by_level(persons, longest_class):
    score_mapping = {"upper": 3, "middle": 2, "lower": 1}
    scored_names = []
    for name, class_list in persons.items():
        class_list = ["middle"] * (longest_class - len(class_list)) + class_list
        score = 0
        for i, class_type in enumerate(class_list):
            score = (10**i + 1) * score_mapping[class_type] + score
        scored_names.append((name, score))
    sorted_by_name = sorted(scored_names, key=lambda x: x[0])
    sorted_by_score = sorted(sorted_by_name, key=lambda x: x[1], reverse=True)
    return [elem[0] for elem in sorted_by_score]


def run(lines):
    test_cases = int(lines.pop(0))
    answer = ""
    while lines:
        persons = {}
        longest_class = 0
        for _ in range(int(lines.pop(0))):
            data = lines.pop(0).split(" ")
            class_list = data[1].split("-")
            persons[data[0].replace(":", "")] = class_list
            longest_class = len(class_list) if len(class_list) > longest_class else longest_class
        name_list = get_name_list_by_level(persons, longest_class)
        answer += "\n".join(name_list) + f"\n{'='*30}\n"
    return answer.rstrip()


if __name__ == "__main__":
    lines = [x.rstrip() for x in sys.stdin.readlines()]
    print(run(lines))
