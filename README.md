# Tuesday 24 November 2026 — The World in One Day

[![make.fun bounty](https://img.shields.io/badge/make.fun-news--image--20261124-blue)](https://make.fun/bounty/news-image-20261124)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

One image that sums up the world's news of Tuesday 24 November 2026 —
a newspaper front page with six stories that defined the day.

## The six stories

- **NO DEAL AT COP31** — climate talks in Antalya end in deadlock as a fossil-fuel deal stalls.
- **MOSCOW WARNS ESTONIA** — "open war" threat as Estonia plans to close its border with Russia.
- **25 SEAFARERS KILLED** — UN counts the dead after attacks near the Strait of Hormuz.
- **$1.6BN FOR NEPAL** — India pledges rebuild aid; a new Ayodhya–Janakpur train opens.
- **FACTORY FIRE IN BANTEN** — rescue under way in Indonesia after a deadly blaze.
- **LISBON PROTESTS** — thousands march against the rising cost of living.

Also today: Pant hits 128 in the Wellington Test, Verstappen wins the Las Vegas Grand Prix, Ferrari unveils two new 296 models.

## How it is built

`build_poster.py` draws the 1024×1024 poster with Pillow (flat pictograms,
masthead, six story cards, footer ticker) and writes `entry.png`.
`main.py` (standard library only) copies `entry.png` to `/output/entry.png`;
it is deterministic — two runs produce byte-identical output.

```sh
python3 build_poster.py   # regenerate entry.png
python3 main.py           # write /output/entry.png
```

Entry for the [make.fun bounty news-image-20261124](https://make.fun/bounty/news-image-20261124).
