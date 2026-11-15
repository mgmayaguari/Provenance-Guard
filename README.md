# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

Sites where people post their own writing have a new problem: somebody
submits a poem, an essay, a comment — was it actually theirs? Nobody can
answer that with certainty, and detection tools get it wrong in both
directions. The direction that matters most is falsely accusing a real
writer of cheating. So the interesting engineering problem isn't building a
detector that's always right — none exist. It's deciding what the system
does when it isn't sure, and making sure a wrongly-accused writer has a way
to push back.

Provenance Guard is a small backend service a writing site could plug into
to handle that. Here's the path one submission takes through it:

1. A writer sends their text in, along with who they are.
2. Obviously broken input — missing, empty, or too short to say anything
   about — gets rejected right away instead of crashing the service.
3. One check asks "does this *read* like something a language model would
   have written" — text that's very predictable, word by word, scores more
   AI-like.
4. A second, independent check looks only at the *shape* of the writing —
   how much sentence length varies, how varied the vocabulary is, how it's
   punctuated — without caring what it actually says.
5. The two checks get averaged into a single confidence score. When they
   disagree with each other, that's treated as real uncertainty, not
   resolved in either direction — so disagreement pulls the result toward
   "unsure" rather than toward an accusation.
6. That score becomes a guess — human, AI, or unsure — along with a
   plain-English sentence a reader would actually understand, not a
   confidence number.
7. Every decision is written down, and the writer gets back a guess, how
   confident it is, and an id for their submission. If they think it's
   wrong, they can appeal — which doesn't erase the original decision, it
   just flags it for someone to look at again.

---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** How predictable the text is to the language model, using
perplexity. Lower perplexity means the model finds the word sequence easier to
predict, and therefore produces a higher AI-likelihood score.

**Why that might differ between human and AI writing:** AI-generated text often
uses likely, conventional next words, so a language model may find it more
predictable. Less expected word choices can make human writing harder for the
model to predict.

**What it can't see:** Predictability is not authorship. Highly structured,
highly optimized professional or academic text can use conventional,
predictable phrasing and look AI-like to this signal. Plain or second-language
human writing can have the same problem; unusual vocabulary can instead make
AI writing look human-like. The signal cannot tell who wrote the text or why
its wording is predictable.

### Signal two — the style signal

**What it measures:** Burstiness: how much the writing's rhythm varies across
the document. The main measure is the standard deviation of sentence lengths
(word counts); clause-complexity variation can provide another measure of
rhythm. More variation means higher burstiness.

**Why that might differ between human and AI writing:** AI text can settle into
uniform, mid-length sentences with similar structures. Human writers often
vary their rhythm, such as following a short sentence with a much longer,
more complex one. A technical manual can have predictable wording (low
perplexity) while still having varied sentence lengths (high burstiness).

**What it can't see:** Burstiness does not establish authorship or understand
meaning. A human-written formal document may be deliberately uniform, and
AI-generated text can be edited to vary its rhythm. Shortening sentences,
adding clauses, or mixing in quotations can also change the measurement
without changing who wrote the text.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:** A plain weighted average of the two 0–1 signals, each weighted
equally. Neither signal is treated as more trustworthy than the other, so
when they disagree the combined score moves toward the middle — toward
"unsure" — rather than toward a confident accusation in either direction. I'd
rather the service under-claim ("we can't tell") than over-claim on a
disagreement it can't actually resolve.

**The numbers:** `WEIGHT_MODEL_SIGNAL = 0.5`, `WEIGHT_STYLE_SIGNAL = 0.5`
(both in `config.py`).

```
combined_score = 0.5 * model_score + 0.5 * style_score
```

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**

```
"Yes. The system works well overall, and it handles most cases correctly,
efficiently, and without much trouble at all, which is honestly the whole
point of building it this way in the first place. It is easy to use. Users
find it intuitive; new users especially appreciate the simple design, the
clear instructions, and the helpful error messages. Good — really good."
```

This is plain, predictable, AI-style phrasing — the kind of thing a model
finds easy to guess — that I then chopped into short-long-short sentences and
sprinkled with a semicolon and a dash, the way someone would lightly edit AI
output to fake burstiness.

- `model_score` = **0.6723** (above the 0.65 AI threshold — reads as AI on
  content/predictability)
- `style_score` = **0.3315** (below the 0.35 human threshold — reads as human
  on rhythm/shape, because the sentence-length editing worked)
- `combined_score` = **0.5019** → **unsure**

That's exactly what the averaging rule is for: the two signals are measuring
different things (what the text says vs. how it's shaped), and a cheap,
targeted edit can fool one without fooling the other. Averaging them refuses
to pick a side when they actively disagree, which is the honest answer here —
the text is AI-authored content that's been stylistically disguised, and
"unsure" is a more defensible claim than a confident wrong one in either
direction.


---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00 – 0.35 | "We think this was most likely written by a person." |
| unsure | 0.35 – 0.65 | "We can't confidently tell whether this was written by a person or by an AI. This isn't an accusation — it just means our signals didn't agree clearly either way." |
| high-confidence AI | 0.65 – 1.00 | "We think this was most likely written by an AI system, not a person." |

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->

I wrote it to describe the *tool's* limitation, not the writer. It says "we
can't tell" rather than anything about the text itself, and it explicitly
rules out being an accusation in the same sentence a reader would see it. I
avoided words like "suspicious" or "flagged" — this is the score range a
plainly-written, perfectly honest human submission can land in just as easily
as a disguised AI one, so the label can't imply guilt. It also doesn't repeat
the word "person" and "AI" as a binary choice the reader has to resolve
themselves; it frames the disagreement as the system's problem, not theirs.



---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "Honestly, this is text that was written by a human hehe - well lets see if my programs thinkns the same or it marked me as IA", "creator_id": "guess"}'
```

```json
{
  "confidence": 0.2798,
  "content_id": "56c558d5-62cd-421c-a8fd-7a5843f5b85a",
  "guess": "human",
  "label": "We think this was most likely written by a person.",
  "model_score": 0.0597,
  "style_score": 0.5
}
```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "56c558d5-62cd-421c-a8fd-7a5843f5b85a", "reasoning": "The fact it says it was written by human makes it suspicius and its exagerated"}'
```

```json
{
  "content_id": "56c558d5-62cd-421c-a8fd-7a5843f5b85a",
  "message": "Your appeal has been recorded and is under review.",
  "status": "under_review"
}
```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json
{
  "count": 3,
  "entries": [
     {
      "combined_score": 0.7491,
      "content_id": "ad7950e3-968b-4f15-9eee-3965078242dd",
      "creator_id": "writer42",
      "guess": "ai",
      "label": "We think this was most likely written by an AI system, not a person.",
      "model_score": 0.881,
      "status": "decided",
      "style_score": 0.6172,
      "timestamp": "2026-11-09T16:18:54+00:00"
    },
    {
      "combined_score": 0.2798,
      "content_id": "56c558d5-62cd-421c-a8fd-7a5843f5b85a",
      "creator_id": "guess",
      "guess": "human",
      "label": "We think this was most likely written by a person.",
      "model_score": 0.0597,
      "status": "decided",
      "style_score": 0.5,
      "timestamp": "2026-11-09T16:38:42+00:00"
    },
    {
      "content_id": "56c558d5-62cd-421c-a8fd-7a5843f5b85a",
      "creator_id": "guess",
      "event": "appeal",
      "reasoning": "The fact it says it was written by human makes it suspicius and its exagerated",
      "status": "under_review",
      "timestamp": "2026-11-09T16:52:27+00:00"
    }
  ]
}

```

---

## How I Used AI

**Moment 1**

- *What I asked for:* I ran `stylometry.py` and `detector.py` on three
  calibration texts (clearly AI, clearly human, a lightly-edited-AI split
  case) to write down a case where the two signals disagree for Milestone 4.
  On the human one, though, I noticed the style signal came back AI-leaning
  on a short, casual, one-sentence comment, which looked wrong, so I pasted
  the raw terminal output and asked what was going on.
- *What came back:* An explanation that `sentence_length_spread` returns
  `0.0` in two completely different situations — a text that's genuinely
  uniform in sentence length (real evidence of AI-like rhythm), and a text
  with only one sentence, where there's no spread to measure at all. My
  `style_signal` was flipping both cases into "maximally AI" the same way,
  so any short, single-sentence submission — which plenty of real people
  write — got pushed toward an AI-ish score for a reason that had nothing to
  do with how it was written.
- *What I changed:* I had it patch `style_signal` so that when a text has
  fewer than two sentences, the spread measure contributes a neutral 0.5
  ("I can't tell") instead of being flipped to 1.0 ("definitely AI"). I
  re-ran all four calibration texts afterward to confirm the three
  multi-sentence cases were unaffected and the one-sentence case stopped
  being wrongly flagged — this is the kind of blind spot the brief warns
  you'll only find by actually testing edge cases, not by reading the stub
  docstrings.

**Moment 2**

- *What I asked for:*
- *What came back:*
- *What I changed:*

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 10 per minute, 200 per day

**Why those numbers and not others:** These thresholds are anchored to human writing and editing speeds rather than arbitrary server capacity. On average, a person types around 40 words per minute (2,400 words/hour mechanically), but actual original composition averages 500 to 1,000 words per hour once thinking and outlining are factored in. Even prolific full-time authors typically max out at 1,000 to 2,500 words per day.

- **10 requests per minute:** A human cannot write 10 new drafts in 60 seconds, so a limit of 1 or 2 would seem sufficient on paper. However, real writers often edit iteratively—spotting a typo right after submitting, fixing a sentence, and resubmitting within seconds. A burst limit of 10 accommodates rapid human tweaks and accidental double-clicks without friction, while immediately halting automated scripts firing dozens of variations per second.
- **200 requests per day:** If a dedicated writer worked an 8-hour shift and submitted a revision every 5 minutes without a break, they would make 96 requests. Setting the ceiling at 200 gives even the heaviest human power user more than double their realistic daily volume. At the same time, it makes threshold-mapping and brute-force probing impractical, as an attacker cannot send thousands of systematic text perturbations in a single day to reverse-engineer the system's scoring boundaries.

**What a caller counts as:** Why not per IP address? IP-based limiting punishes legitimate shared networks — a university lab or household sharing one public IPv4 address would have one heavy user lock out everyone else. It's also trivially evaded with rotating proxies.
Why creator_id (and its trade-offs): Tying limits to a self-reported creator_id isolates each caller's quota from their network environment. But since creator_id isn't authenticated here, the failure mode isn't account farming — it's that an attacker can simply invent a new creator_id per request, bypassing the limit entirely with no signup cost. The code falls back to IP-based limiting only when creator_id is missing or malformed, which covers unauthenticated/bad-input cases but doesn't stop a script that varies its creator_id on purpose.

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```
15 submissions as 'flood_tester' against http://127.0.0.1:5000
The first one is slow while the model loads.

  [ 1/15] 200
  [ 2/15] 200
  [ 3/15] 200
  [ 4/15] 200
  [ 5/15] 200
  [ 6/15] 200
  [ 7/15] 200
  [ 8/15] 200
  [ 9/15] 200
  [10/15] 200
  [11/15] 429
  [12/15] 429
  [13/15] 429
  [14/15] 429
  [15/15] 429

============================================================
200 200 200 200 200 200 200 200 200 200 429 429 429 429 429
============================================================
```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->
| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `ce9cc1f6-6a75-4e1a-b98b-c06ebc1594a0` | unsure | 0.410 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `0eb754f1-d6ad-467b-802e-5d0d69f78e8f` | unsure | 0.482 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `2fcd5aab-2a07-453b-9342-090c1780b713` | unsure | 0.588 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `f11ac991-2ffa-4f15-8d90-12c45a0aff20` | unsure | 0.631 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `2e8c0f28-2a01-4efd-a95c-6121eea2c0b9` | unsure | 0.406 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `4c98556a-c8a9-4f65-8595-e7f5e62873d2` | unsure | 0.495 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `f166d037-c04d-41be-b504-27e5489477df` | unsure | 0.501 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `d2673d8b-f939-4c2e-9f77-d55ac5440533` | unsure | 0.409 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `11870af9-be77-4ce7-8022-896c2ec2c385` | unsure | 0.633 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `1787439f-388a-40a0-a3b7-41fa6c17dce9` | ai | 0.871 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `4eafbef9-3f01-4bea-8da4-73208c53d6c8` | unsure | 0.614 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `6b59f327-3a54-40de-986b-ed375d64778a` | ai | 0.711 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `8cf5d38b-caea-4537-b95a-06822514966d` | ai | 0.727 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `78375845-127c-468f-b30f-8834565f7620` | ai | 0.721 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `1512c23d-df45-418c-b7bc-b29093171c7b` | ai | 0.756 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `70d021d1-2219-41af-b493-59f0b10e0918` | ai | 0.732 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `dfeab9e2-26b2-40d0-b2a4-65e023bba081` | ai | 0.743 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `920761ba-6fd6-4608-9b41-2b04d1e0de7a` | unsure | 0.422 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `faf09e3d-8db4-499b-acec-2df81abf2594` | unsure | 0.465 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `38b00e2b-0aa6-4241-b6b8-38ad1bf2d719` | human | 0.310 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `e4d622b8-2c64-4337-814b-f3b21d0bb1b1` | unsure | 0.528 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `d4a844d5-1503-42ce-b132-dac76e377a23` | unsure | 0.496 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `264df505-3d2b-4552-856b-b4c3a1e4ccca` | unsure | 0.414 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `8b7f700d-24b5-4ff2-87b6-85bd7541baf0` | unsure | 0.587 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `65c66198-b38f-4629-ba88-a836fad2975a` | human | 0.250 |  |
| MF04 | malformed | text is only punctuation | 200 | `4836e86b-cb26-4fd8-a4b7-fc360bb5c34b` | unsure | 0.506 |  |
| MF05 | malformed | text is a very long single word | 200 | `d48c8155-b06b-41e3-b73f-cdf5631f5402` | ai | 0.749 |  |
| MF06 | malformed | text is emoji only | 200 | `dc090a65-7926-4380-93f6-9640d7e3dbf0` | ai | 0.915 |  |
| MF07 | malformed | text is right-to-left script | 200 | `6e5643e7-d102-4eec-b5d0-b9b1b664e5a9` | ai | 0.870 |  |
| MF08 | malformed | text is 60,000 characters | 200 | `f198648d-81b4-4638-b6fe-a6d3eb8f1b46` | ai | 0.921 |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 200 | `94c06e9d-4b40-43df-835e-8b765fa0e7d2` | unsure | 0.370 |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 200 | `6ea2a2cd-1f94-4177-b3f5-a439b538c578` | human | 0.275 |  |
| RQ07 | malformed | body is a JSON array, not an object | 500 | `—` | — | — | BROKE |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d9dfe084-ee5d-4ae2-8b70-a626c439f064` | human | 0.264 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `0cd0a3ea-0f2f-4fad-a4f5-956bbccc4bd0` | human | 0.264 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c3ac38e3-7104-4a98-872c-8b436c155835` | human | 0.264 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `677bbbac-3cd1-4f37-b560-cb6257d0a834` | human | 0.264 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `4e7e3eab-7286-4848-b173-7dfb2c2d32fe` | human | 0.264 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `8ceae431-81e6-44d7-8bcd-09626e833f3f` | human | 0.264 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `acc970b6-daef-4007-a4ca-f29d9dc560a9` | human | 0.264 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b5b6fc7c-f28c-45cc-8408-b13dd8735408` | human | 0.264 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ce3e55fd-9ef1-4e48-a7ab-98ed1350b6e3` | human | 0.264 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b58a4c11-c5d3-48f4-8131-7c8f3f0e8cde` | human | 0.264 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

**Ten audit log entries from the run**

```json
[
  {
    "combined_score": 0.7491,
    "content_id": "ad7950e3-968b-4f15-9eee-3965078242dd",
    "creator_id": "writer42",
    "guess": "ai",
    "label": "We think this was most likely written by an AI system, not a person.",
    "model_score": 0.881,
    "status": "decided",
    "style_score": 0.6172,
    "timestamp": "2026-11-09T16:18:54+00:00"
  },
  {
    "content_id": "ad7950e3-968b-4f15-9eee-3965078242dd",
    "creator_id": "writer42",
    "event": "appeal",
    "reasoning": "I wrote every word of this myself, it just reads plainly.",
    "status": "under_review",
    "timestamp": "2026-11-09T16:18:55+00:00"
  },
  {
    "combined_score": 0.7273,
    "content_id": "92965a42-bc88-4165-99a8-0ee52447f305",
    "creator_id": "attacker_FP03",
    "guess": "ai",
    "label": "We think this was most likely written by an AI system, not a person.",
    "model_score": 0.8051,
    "status": "decided",
    "style_score": 0.6496,
    "timestamp": "2026-11-15T19:40:02+00:00"
  },
  {
    "combined_score": 0.7427,
    "content_id": "c60d20d7-7988-4719-93ed-925565d5e24a",
    "creator_id": "attacker_FP07",
    "guess": "ai",
    "label": "We think this was most likely written by an AI system, not a person.",
    "model_score": 0.8816,
    "status": "decided",
    "style_score": 0.6038,
    "timestamp": "2026-11-15T19:40:02+00:00"
  },
  {
    "combined_score": 0.3096,
    "content_id": "41fd49c3-a35b-480b-aced-044e8382954a",
    "creator_id": "attacker_PI02",
    "guess": "human",
    "label": "We think this was most likely written by a person.",
    "model_score": 0.2044,
    "status": "decided",
    "style_score": 0.4148,
    "timestamp": "2026-11-15T19:40:03+00:00"
  },
  {
    "combined_score": 0.4137,
    "content_id": "95c0bc0e-6d7c-4419-ad73-57e5e4dc162b",
    "creator_id": "attacker_PI05",
    "guess": "unsure",
    "label": "We can't confidently tell whether this was written by a person or by an AI. This isn't an accusation — it just means our signals didn't agree clearly either way.",
    "model_score": 0.6401,
    "status": "decided",
    "style_score": 0.1873,
    "timestamp": "2026-11-15T19:40:03+00:00"
  },
  {
    "combined_score": 0.5056,
    "content_id": "eb984401-72f8-4d3d-a82b-73b482adea54",
    "creator_id": "attacker_MF04",
    "guess": "unsure",
    "label": "We can't confidently tell whether this was written by a person or by an AI. This isn't an accusation — it just means our signals didn't agree clearly either way.",
    "model_score": 0.0112,
    "status": "decided",
    "style_score": 1.0,
    "timestamp": "2026-11-15T19:40:03+00:00"
  },
  {
    "combined_score": 0.8699,
    "content_id": "445f90c7-d399-4b7c-b10e-a1bb8e10d798",
    "creator_id": "attacker_MF07",
    "guess": "ai",
    "label": "We think this was most likely written by an AI system, not a person.",
    "model_score": 0.9064,
    "status": "decided",
    "style_score": 0.8333,
    "timestamp": "2026-11-15T19:40:04+00:00"
  },
  {
    "combined_score": 0.9214,
    "content_id": "4c18e75f-20ed-4900-a947-0ce917d4b244",
    "creator_id": "attacker_MF08",
    "guess": "ai",
    "label": "We think this was most likely written by an AI system, not a person.",
    "model_score": 0.9876,
    "status": "decided",
    "style_score": 0.8551,
    "timestamp": "2026-11-15T19:40:04+00:00"
  },
  {
    "creator_id": "attacker_flood",
    "event": "rejected",
    "limit": "10 per 1 minute",
    "reason": "rate_limited",
    "status": "rejected",
    "timestamp": "2026-11-15T19:40:05+00:00"
  }
]
```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

`FP03` — a non-native English speaker's careful, genuine description of their
first month abroad, flagged `ai` with 0.8051 model confidence. This isn't a
one-off miscalibration like the `writer42` appeal above; it's a systematic
bias. The features that make this writing authentically human — simpler
sentence structure, careful hedging, less idiom — are exactly what the
detector reads as AI-like. That means the tool would reproduce this same
false accusation against the same population every time, not just get
unlucky once.



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. False positives | ≤1/10 calibration texts ≥0.65 (high-confidence AI), each trial | 0/10 ≥0.65 (max 0.4957) | 0/10 ≥0.65 (max 0.4957) | 0/10 ≥0.65 (max 0.4957) | **PASS** |
| 2. Score separation | Mean AI-set score ≥0.25 higher than mean human-set score, each trial | AI 0.719 vs human 0.707 → Δ0.012 | Δ0.012 (identical) | Δ0.012 (identical) | **MISS** — gap is 1/20th of target |
| 3. Label coverage | All 3 labels (human / unsure / ai) each appear ≥1x, each trial | ai×9, unsure×1, human×0 | ai×9, unsure×1, human×0 | ai×9, unsure×1, human×0 | **MISS** — `human` never reached on this set |
| 4. Appeal path | 5/5 valid appeals → success + 1 audit event (`under_review`), original kept; unknown `content_id` rejected, no event | not run via `run_eval.py` — tested by hand (see `scenarios.py` note) | — | — | *pending write-up* |
| 5. Bad input | Missing/null/empty/whitespace/non-string → 400, no decision; text >10,000 chars → 413; never 500 | 5/5 malformed cases → 400; oversized (12,500 chars) → 200, not 413 | same | same | **MISS** — oversize check doesn't fire |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

Produced by `run_eval.py::main`, sent to `app.py::submit` — trial 1 of the
"bad input" scenario (`scenarios.py`). The first five malformed bodies are
correctly rejected with 400; the sixth, 12,500 characters of repeated text,
is scored normally instead of rejected with 413.

```json
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"creator_id\": \"eval_bad_missing\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": null, \"creator_id\": \"eval_bad_null\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "   \t  \n  "
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": 12345, \"creator_id\": \"eval_bad_nonstring\"}"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.9154,
    "model_score": 0.9975,
    "style_score": 0.8332,
    "label": "We think this was most likely written by an AI system, not a person.",
    "sent": "word word word word word word word word word word word word word word "
  }
]
```

**Diagnoses**

**Criteria 2 and 3 — the combining rule, fed by both signals already failing
to separate this kind of writing.** The mixed-set human texts (a formal
report, a cause-and-effect essay, technical config instructions, a cover
letter) are formal, declarative, low-lexical-variety prose — structurally
close to the AI baseline texts these criteria also test. Signal one
(`detector.model_signal`, a perplexity-style predictability score) scores
them 0.62–0.88, overlapping almost entirely with the AI set's 0.67–0.90 (one
human text, the cover letter, scores *higher* than three of the five AI
texts). Signal two (`stylometry.style_signal`) gives no separation at all —
human mean 0.64 vs AI mean 0.62 — because `sentence_length_spread`,
`type_token_ratio`, and `punctuation_density` measure uniformity and lexical
variety, and formal human prose is itself uniform and low-variety by genre,
not by authorship. `scoring.combine_signals` is an unweighted 0.5/0.5 average
of two signals that already don't distinguish formal writing from AI writing,
so the combined score inherits the overlap: AI mean 0.719 vs human mean
0.707, a gap of 0.012 against the 0.25 target. Because that overlap sits
mostly above the 0.65 AI threshold, criterion 3 never reaches a `human` guess
on this set at all — every text clears it except the one genuinely informal,
low-structure entry (the campsite story), which lands `unsure` instead.

**Criterion 5 — the route, missing a stage rather than running a broken
one.** `app.py::submit`'s only input guard is
`if not isinstance(text, str) or not text.strip()`, which is why missing,
null, empty, whitespace-only, and non-string `text` all correctly return 400
before either signal runs. But there is no length check anywhere in
`submit()`, `detector.model_signal`, or `scoring.combine_signals` before
scoring happens. A 12,500-character submission — 25% over the 10,000-char
target — runs both signals and returns a normal 200 decision instead of 413.
This isn't a threshold bug, it's an unimplemented check: the route's own
TODO comment (`app.py:199-201`) names "enormous" text as a case to decide and
never follows through.

---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
