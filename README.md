# news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/ajidasidiq/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/ajidasidiq/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

Tuesday 24 November 2026 world news in one image: a newspaper front page with six stories that defined the day — COP31 deadlock in Antalya, Moscow warning to Estonia, 25 seafarers killed near the Strait of Hormuz, $1.6bn India aid for Nepal, factory fire in Banten, Lisbon cost-of-living protests — plus the footer ticker.

## Run it

```sh
python3 build_poster.py   # regenerate entry.png
python3 main.py           # write /output/entry.png
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>

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

Entry for the [make.fun bounty news-image-20261124](https://make.fun/bounty/news-image-20261124).
