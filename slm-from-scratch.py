#!/usr/bin/env python3

import argparse

import torch

# downloaded from https://www.dbnl.org/nieuws/text.php?id=coup002elin01
with open("dbnl.coup002elin01.txt", encoding="utf-8") as file:
    text = file.read()


def encode(s: str) -> list[int]:
    return [s_to_i[c] for c in s]


def decode(ids: list[int]) -> str:
    return "".join(i_to_s[i] for i in ids)


def build_tokenizer(text: str) -> tuple[int, dict[str, int], dict[int, str]]:
    chars = sorted(set(text))
    s_to_i = {c: i for i, c in enumerate(chars)}
    i_to_s = {i: c for c, i in s_to_i.items()}
    return len(chars), s_to_i, i_to_s


def build_data_split(
    text: str,
) -> tuple[
    torch.Tensor,
    torch.Tensor,
    torch.Tensor,
]:
    data = torch.tensor(encode(text), dtype=torch.long)
    split_index = int(0.9 * len(data))
    train_data = data[:split_index]
    val_data = data[split_index:]
    return train_data, val_data, data


vocab_size, s_to_i, i_to_s = build_tokenizer(text)
train_data, val_data, data = build_data_split(text)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Toy character-level text encoder/decoder.",
    )
    parser.add_argument(
        "--mode",
        choices=("encode", "decode"),
        default="encode",
        help="Choose whether to encode text or decode token IDs.",
    )
    parser.add_argument(
        "value",
        nargs="?",
        help="Text to encode or comma-separated token IDs to decode.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.value is None:
        raise SystemExit("Provide a value to encode or decode.")

    print(f"vocab_size={vocab_size}")
    print(f"train={len(train_data)}, val={len(val_data)}, total={len(data)}")

    if args.mode == "encode":
        print(encode(args.value))
    else:
        tokens = [int(part.strip()) for part in args.value.split(",") if part.strip()]
        print(decode(tokens))


if __name__ == "__main__":
    main()
