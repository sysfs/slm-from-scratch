#!/usr/bin/env python3

# downloaded from https://www.dbnl.org/nieuws/text.php?id=coup002elin01
with open("dbnl.coup002elin01.txt", encoding="utf-8") as file:
    text = file.read()

chars = sorted(set(text))
vocab_size = len(chars)

s_to_i = {c: i for i, c in enumerate(chars)}
i_to_s = {i: c for c, i in s_to_i.items()}


def encode(s: str) -> list[int]:
    return [s_to_i[c] for c in s]


def decode(ids: list[int]) -> str:
    return "".join(i_to_s[i] for i in ids)


if __name__ == "__main__":
    pass
