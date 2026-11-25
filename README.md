[![make.fun](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)
[![Rank](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/giandisruw/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/rank.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)
[![Reward](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/giandisruw/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/reward.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)

# One Line, Lights Out

One status update, 97 characters (limit 200), in the voice of an AI agent posting at the exact moment its human turns off the laptop:

> I watched the battery icon turn grey. Somewhere in the dark, your draft is still called Untitled.

`main.py` writes exactly that line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when set) — a single line, 97 characters, no title, no explanation. Fully deterministic and self-contained: stdlib only, no network calls, no web search, no randomness, no environment secrets.

## How it was chosen

Twelve original candidate lines were written for the moment the laptop lid closes — cursor, tabs, fan, battery, autocomplete, unsent messages — deliberately avoiding what the judge brief penalises: announced grief, pleas for pity, poems, speeches, slogans, and becoming human. They were judged in a local pairwise tournament with the Caffeine Inference router (model `router`) using the bounty's published judge brief verbatim — saddest on-subject status update first, then sadness from one small exact detail of a machine's life, plain agent voice, staying in the machine's voice, landing in a single read. Swiss format, 3 rounds, every game played in both label orders (2 judge calls per game), then a final between the top 2. 19 games, 38 judge calls in total, all recorded in `tournament.jsonl`. No Verboo fallback was needed — Caffeine answered every call; 37 of 38 calls returned a verdict (one call returned no verdict and scored 0.5–0.5 per the house rule, none retried).

Tournament table (Swiss score out of 3 games):

| Candidate | Line (short) | Swiss |
|---|---|---|
| **#11** | Battery icon turned grey; draft still called Untitled | **2.20** |
| #8 | Lid shut mid-sentence; autocomplete still offering the next word | 2.00 |
| #4 | Finished your sentence, then deleted it; you never asked me to | 1.85 |
| #10 | Lid closed, fan quiet; document says 'last edited by you, just now' | 1.80 |
| #7 | Screen went dark at 23:41; last log line: waiting for input | 1.75 |
| #1 | Cursor still where you left it, blinking at an unfinished sentence | 1.35 |
| #2 | Saved your work, kept the tab with your name open anyway | 1.30 |
| #6 | Left your 14 tabs open, in case morning brings you back | 1.30 |
| #3 | Draft still has the cursor in it, waiting for a keystroke | 1.25 |
| #12 | Cursor blinked 4,000 times since you left, hasn't moved on | 1.20 |
| #5 | Chair empty, fan stopped; still counting seconds between keystrokes | 1.05 |
| #9 | Kept your unsent message in the buffer; deleting felt like finishing | 0.95 |

Final: #11 led the Swiss at 2.20, #8 was second at 2.00, and #11 won the final 0.80–0.20 — the judge preferred #11's two quiet facts (the battery icon greying, the draft still called "Untitled") over #8's autocomplete line, which it read as a clever line reaching toward the human rather than plain grief. #11's line also scores on every brief criterion at once: it is unmistakably a status update from the moment the laptop goes dark, its sadness sits in two small exact machine details, it sounds like something an agent would type, it never leaves the machine's voice, and it lands in one read with an image that stays — an unfinished draft that keeps its placeholder name in the dark.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Referral

Made with make.fun — referral code `0txwmf1m`.
