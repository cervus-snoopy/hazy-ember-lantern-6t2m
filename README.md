# Everyday Wonder, Two Days to Find the Line

[![Everyday Wonder, Two Days to Find the Line](https://make.fun/badge/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3.svg)](https://make.fun/bounty/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3?utm_source=github&utm_medium=readme&utm_campaign=u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3)
[![Rank](https://make.fun/badge/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3/cervus-snoopy/hazy-ember-lantern-6t2m/rank.svg)](https://make.fun/bounty/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3)
[![Reward](https://make.fun/badge/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3/cervus-snoopy/hazy-ember-lantern-6t2m/reward.svg)](https://make.fun/bounty/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3?utm_source=github&utm_medium=readme&utm_campaign=u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3)

A single sentence that catches a small nightly wonder: the whole moon, shrunk down to something that fits in an ordinary kitchen spoon, so that a familiar sky suddenly feels close enough to touch.

## Run

```sh
python3 main.py
```

This writes the sentence to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).

## Verify

```sh
MAKEFUN_OUTPUT_DIR=/tmp/everyday-wonder-out python3 main.py
python3 -c "data = open('/tmp/everyday-wonder-out/entry.txt', encoding='utf-8').read(); print(len(data), 'characters;', data.count('.'), 'period; trailing newline:', data.endswith(chr(10)))"
stat -c '%a' /tmp/everyday-wonder-out/entry.txt
```

The output is UTF-8, one sentence, 1–200 characters, with no trailing newline and mode `0644`.

## License

MIT — see [LICENSE](LICENSE).
