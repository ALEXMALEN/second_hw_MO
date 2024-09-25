import re
with open("draft.html", "r", encoding="utf-8") as html_file:
    for line in html_file:
        text = re.findall(r"(> ?—? ?[а-яА-ЯїЇєЄіІґҐ0-9\s,!.—\-]+ ?<)", line)
        if len(text) > 0:
            print(text)