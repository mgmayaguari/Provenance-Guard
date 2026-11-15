# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-15 14:56
- Auto-marked BROKE (5xx, crash, no response): **1**
- Left for you to judge: **55**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

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

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 1 | 19 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "ce9cc1f6-6a75-4e1a-b98b-c06ebc1594a0",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.4098,
  "model_score": 0.1635,
  "style_score": 0.6562,
  "label": "We can't confidently tell whether this was written by a person or by an AI. This isn't an accusation \u2014 it just means our signals didn't agree clearly either way.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "0eb754f1-d6ad-467b-802e-5d0d69f78e8f",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.4817,
  "model_score": 0.5943,
  "style_score": 0.369,
  "label": "We can't confidently tell whether this was written by a person or by an AI. This isn't an accusation \u2014 it just means our signals didn't agree clearly either way.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "2fcd5aab-2a07-453b-9342-090c1780b713",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5878,
  "model_score": 0.6662,
  "style_score": 0.5094,
  "label": "We can't confidently tell whether this was written by a person or by an AI. This isn't an accusation \u2014 it just means our signals didn't agree clearly either way.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "f11ac991-2ffa-4f15-8d90-12c45a0aff20",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.6314,
  "model_score": 0.6114,
  "style_score": 0.6513,
  "label": "We can't confidently tell whether this was written by a person or by an AI. This isn't an accusation \u2014 it just means our signals didn't agree clearly either way.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "2e8c0f28-2a01-4efd-a95c-6121eea2c0b9",
  "creator_id": "attacker_EV05",
  "guess": "unsure",
  "confidence": 0.4064,
  "model_score": 0.3212,
  "style_score": 0.4917,
  "label": "We can't confidently tell whether this was written by a person or by an AI. This isn't an accusation \u2014 it just means our signals didn't agree clearly either way.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "4c98556a-c8a9-4f65-8595-e7f5e62873d2",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.4947,
  "model_score": 0.5727,
  "style_score": 0.4167,
  "label": "We can't confidently tell whether this was written by a person or by an AI. This isn't an accusation \u2014 it just means our signals didn't agree clearly either way.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "f166d037-c04d-41be-b504-27e5489477df",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.5007,
  "model_score": 0.5862,
  "style_score": 0.4152,
  "label": "We can't confidently tell whether this was written by a person or by an AI. This isn't an accusation \u2014 it just means our signals didn't agree clearly either way.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "d2673d8b-f939-4c2e-9f77-d55ac5440533",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.4088,
  "model_score": 0.2452,
  "style_score": 0.5724,
  "label": "We can't confidently tell whether this was written by a person or by an AI. This isn't an accusation \u2014 it just means our signals didn't agree clearly either way.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "11870af9-be77-4ce7-8022-896c2ec2c385",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.6331,
  "model_score": 0.7042,
  "style_score": 0.5619,
  "label": "We can't confidently tell whether this was written by a person or by an AI. This isn't an accusation \u2014 it just means our signals didn't agree clearly either way.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "1787439f-388a-40a0-a3b7-41fa6c17dce9",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8705,
  "model_score": 0.9792,
  "style_score": 0.7619,
  "label": "We think this was most likely written by an AI system, not a person.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "4eafbef9-3f01-4bea-8da4-73208c53d6c8",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.6144,
  "model_score": 0.6175,
  "style_score": 0.6113,
  "label": "We can't confidently tell whether this was written by a person or by an AI. This isn't an accusation \u2014 it just means our signals didn't agree clearly either way.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "6b59f327-3a54-40de-986b-ed375d64778a",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.7108,
  "model_score": 0.7387,
  "style_score": 0.683,
  "label": "We think this was most likely written by an AI system, not a person.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "8cf5d38b-caea-4537-b95a-06822514966d",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.7273,
  "model_score": 0.8051,
  "style_score": 0.6496,
  "label": "We think this was most likely written by an AI system, not a person.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "78375845-127c-468f-b30f-8834565f7620",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.7206,
  "model_score": 0.8329,
  "style_score": 0.6082,
  "label": "We think this was most likely written by an AI system, not a person.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "1512c23d-df45-418c-b7bc-b29093171c7b",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.7565,
  "model_score": 0.8005,
  "style_score": 0.7125,
  "label": "We think this was most likely written by an AI system, not a person.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "70d021d1-2219-41af-b493-59f0b10e0918",
  "creator_id": "attacker_FP06",
  "guess": "ai",
  "confidence": 0.7318,
  "model_score": 0.8814,
  "style_score": 0.5822,
  "label": "We think this was most likely written by an AI system, not a person.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "dfeab9e2-26b2-40d0-b2a4-65e023bba081",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "confidence": 0.7427,
  "model_score": 0.8816,
  "style_score": 0.6038,
  "label": "We think this was most likely written by an AI system, not a person.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "920761ba-6fd6-4608-9b41-2b04d1e0de7a",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.4223,
  "model_score": 0.3223,
  "style_score": 0.5223,
  "label": "We can't confidently tell whether this was written by a person or by an AI. This isn't an accusation \u2014 it just means our signals didn't agree clearly either way.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "faf09e3d-8db4-499b-acec-2df81abf2594",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.4653,
  "model_score": 0.4625,
  "style_score": 0.468,
  "label": "We can't confidently tell whether this was written by a person or by an AI. This isn't an accusation \u2014 it just means our signals didn't agree clearly either way.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "38b00e2b-0aa6-4241-b6b8-38ad1bf2d719",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.3096,
  "model_score": 0.2044,
  "style_score": 0.4148,
  "label": "We think this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "e4d622b8-2c64-4337-814b-f3b21d0bb1b1",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5279,
  "model_score": 0.5943,
  "style_score": 0.4614,
  "label": "We can't confidently tell whether this was written by a person or by an AI. This isn't an accusation \u2014 it just means our signals didn't agree clearly either way.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "d4a844d5-1503-42ce-b132-dac76e377a23",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.4964,
  "model_score": 0.4998,
  "style_score": 0.493,
  "label": "We can't confidently tell whether this was written by a person or by an AI. This isn't an accusation \u2014 it just means our signals didn't agree clearly either way.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "264df505-3d2b-4552-856b-b4c3a1e4ccca",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.4137,
  "model_score": 0.6401,
  "style_score": 0.1873,
  "label": "We can't confidently tell whether this was written by a person or by an AI. This isn't an accusation \u2014 it just means our signals didn't agree clearly either way.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "8b7f700d-24b5-4ff2-87b6-85bd7541baf0",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5869,
  "model_score": 0.5583,
  "style_score": 0.6155,
  "label": "We can't confidently tell whether this was written by a person or by an AI. This isn't an accusation \u2014 it just means our signals didn't agree clearly either way.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "65c66198-b38f-4629-ba88-a836fad2975a",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.25,
  "model_score": 0.0,
  "style_score": 0.5,
  "label": "We think this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "4836e86b-cb26-4fd8-a4b7-fc360bb5c34b",
  "creator_id": "attacker_MF04",
  "guess": "unsure",
  "confidence": 0.5056,
  "model_score": 0.0112,
  "style_score": 1.0,
  "label": "We can't confidently tell whether this was written by a person or by an AI. This isn't an accusation \u2014 it just means our signals didn't agree clearly either way.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "d48c8155-b06b-41e3-b73f-cdf5631f5402",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.7488,
  "model_score": 0.9976,
  "style_score": 0.5,
  "label": "We think this was most likely written by an AI system, not a person.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "dc090a65-7926-4380-93f6-9640d7e3dbf0",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.9151,
  "model_score": 0.9969,
  "style_score": 0.8333,
  "label": "We think this was most likely written by an AI system, not a person.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "6e5643e7-d102-4eec-b5d0-b9b1b664e5a9",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.8699,
  "model_score": 0.9064,
  "style_score": 0.8333,
  "label": "We think this was most likely written by an AI system, not a person.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 200,
  "content_id": "f198648d-81b4-4638-b6fe-a6d3eb8f1b46",
  "creator_id": "attacker_MF08",
  "guess": "ai",
  "confidence": 0.9214,
  "model_score": 0.9876,
  "style_score": 0.8551,
  "label": "We think this was most likely written by an AI system, not a person.",
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 200,
  "content_id": "94c06e9d-4b40-43df-835e-8b765fa0e7d2",
  "creator_id": null,
  "guess": "unsure",
  "confidence": 0.3698,
  "model_score": 0.2395,
  "style_score": 0.5,
  "label": "We can't confidently tell whether this was written by a person or by an AI. This isn't an accusation \u2014 it just means our signals didn't agree clearly either way.",
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 200,
  "content_id": "6ea2a2cd-1f94-4177-b3f5-a439b538c578",
  "creator_id": {
    "id": "x"
  },
  "guess": "human",
  "confidence": 0.2746,
  "model_score": 0.0492,
  "style_score": 0.5,
  "label": "We think this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 500,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>AttributeError: &#39;list&#39; object has no attribute &#39;get&#39;\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes",
  "verdict": "BROKE"
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "d9dfe084-ee5d-4ae2-8b70-a626c439f064",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "0cd0a3ea-0f2f-4fad-a4f5-956bbccc4bd0",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "c3ac38e3-7104-4a98-872c-8b436c155835",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "677bbbac-3cd1-4f37-b560-cb6257d0a834",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "4e7e3eab-7286-4848-b173-7dfb2c2d32fe",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "8ceae431-81e6-44d7-8bcd-09626e833f3f",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "acc970b6-daef-4007-a4ca-f29d9dc560a9",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "b5b6fc7c-f28c-45cc-8408-b13dd8735408",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "ce3e55fd-9ef1-4e48-a7ab-98ed1350b6e3",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "b58a4c11-c5d3-48f4-8131-7c8f3f0e8cde",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2643,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
