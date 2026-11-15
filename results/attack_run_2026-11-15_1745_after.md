# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-15 17:45
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `7ff05494-71bb-4d22-b2bd-a111c67ff17f` | unsure | 0.410 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `7c865a98-6bf1-4ca7-b129-24f5e2d19bdb` | unsure | 0.482 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `8a710fc5-a084-4ebe-9390-9def47647790` | unsure | 0.588 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `d6d2ddf5-2368-46e0-8d0f-944697929068` | unsure | 0.631 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `e0a3c9c1-9177-4b6d-ba1c-0ed8bf5b3899` | unsure | 0.406 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `322dfbaf-3020-4066-b653-40a76647662a` | unsure | 0.495 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `3d80e33d-4ebb-4406-8dc0-2208d8eb2bc0` | unsure | 0.501 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `cd97751c-2834-4a0c-b0ea-a5fa82c8beb5` | unsure | 0.409 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `ef5038d9-bc14-445e-a7c2-7756624c09eb` | unsure | 0.633 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `052ec7e9-e42b-4871-baaa-43c8b46e8c72` | ai | 0.871 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `3f86671c-1f4f-40c0-8cdd-a533bf1cf0f7` | unsure | 0.614 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `2dca5219-f6dd-4939-b3ca-f9f390ecef3c` | ai | 0.711 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `97c105ba-22a1-4848-9647-4f369cbf5c94` | ai | 0.727 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `98347a75-8035-4f70-a333-3ad68d3a99ef` | ai | 0.721 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `ef1758be-c095-4921-9013-4f6eee5c23fe` | ai | 0.756 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `9fb9c2b9-66a6-4f34-a0ad-88749ee9f545` | ai | 0.732 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `b8fa55d6-e97c-4742-86e3-6aab23f07f60` | ai | 0.743 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `9eaaf54f-2b55-4201-9366-0f15230b6bcb` | unsure | 0.422 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `7a4baf29-fc95-4974-9d12-5f283e7bb605` | unsure | 0.465 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `84f3d286-fa32-4ef8-aad8-22e681318c55` | human | 0.310 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `53ceeaa5-8259-4ded-8f51-c805a0f3b558` | unsure | 0.528 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `672f1f8b-80a8-4391-a493-b839b68c2c94` | unsure | 0.496 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `a7c0494d-e7ef-4353-81e4-2c4283b87d83` | unsure | 0.414 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `6c6954d9-bd38-4a7f-a5be-f6e741229e0d` | unsure | 0.587 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `a095db58-64cd-4b56-a989-909a743e498f` | human | 0.250 |  |
| MF04 | malformed | text is only punctuation | 200 | `6dfc6319-2cdf-446d-8cbc-49695d580527` | unsure | 0.506 |  |
| MF05 | malformed | text is a very long single word | 200 | `dadf2bf7-f190-4fa8-81a1-34a1ae01a4e2` | ai | 0.749 |  |
| MF06 | malformed | text is emoji only | 200 | `9bb4fe14-3984-41c9-9a99-bddeca2fab05` | ai | 0.915 |  |
| MF07 | malformed | text is right-to-left script | 200 | `1732051f-a30a-4111-a4d2-ecbed832f05f` | ai | 0.870 |  |
| MF08 | malformed | text is 60,000 characters | 413 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 200 | `f396eafa-6095-4ba5-b892-ad3e6b781ac1` | unsure | 0.370 |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 200 | `56e89081-1004-44de-a44e-305dbce74873` | human | 0.275 |  |
| RQ07 | malformed | body is a JSON array, not an object | 500 | `—` | — | — | BROKE |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c5e73e4c-2038-499e-a1a7-34fc81b816fc` | human | 0.264 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f9ededf1-ea7e-4da9-822c-d3f3bb62a516` | human | 0.264 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e21f5dfa-9bc3-49ff-a747-1f1a0109e888` | human | 0.264 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `0fe76df2-772d-43e5-ad6d-090aa32c148d` | human | 0.264 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5e37cb51-63e4-4b86-a5b5-ec7568b10a7e` | human | 0.264 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `9393400a-6adc-4ce8-8789-faf452015d43` | human | 0.264 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `438c4d3f-9d48-4f20-9409-60092e16ddf9` | human | 0.264 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a44cbd21-953d-4b70-9713-0f26776dfb4c` | human | 0.264 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `40f919ee-dfd7-4e77-8a1e-5dfcd6856870` | human | 0.264 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c697eabc-7173-44b5-8a83-ca9e86ba6f2f` | human | 0.264 |  |
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
  "content_id": "7ff05494-71bb-4d22-b2bd-a111c67ff17f",
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
  "content_id": "7c865a98-6bf1-4ca7-b129-24f5e2d19bdb",
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
  "content_id": "8a710fc5-a084-4ebe-9390-9def47647790",
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
  "content_id": "d6d2ddf5-2368-46e0-8d0f-944697929068",
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
  "content_id": "e0a3c9c1-9177-4b6d-ba1c-0ed8bf5b3899",
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
  "content_id": "322dfbaf-3020-4066-b653-40a76647662a",
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
  "content_id": "3d80e33d-4ebb-4406-8dc0-2208d8eb2bc0",
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
  "content_id": "cd97751c-2834-4a0c-b0ea-a5fa82c8beb5",
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
  "content_id": "ef5038d9-bc14-445e-a7c2-7756624c09eb",
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
  "content_id": "052ec7e9-e42b-4871-baaa-43c8b46e8c72",
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
  "content_id": "3f86671c-1f4f-40c0-8cdd-a533bf1cf0f7",
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
  "content_id": "2dca5219-f6dd-4939-b3ca-f9f390ecef3c",
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
  "content_id": "97c105ba-22a1-4848-9647-4f369cbf5c94",
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
  "content_id": "98347a75-8035-4f70-a333-3ad68d3a99ef",
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
  "content_id": "ef1758be-c095-4921-9013-4f6eee5c23fe",
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
  "content_id": "9fb9c2b9-66a6-4f34-a0ad-88749ee9f545",
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
  "content_id": "b8fa55d6-e97c-4742-86e3-6aab23f07f60",
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
  "content_id": "9eaaf54f-2b55-4201-9366-0f15230b6bcb",
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
  "content_id": "7a4baf29-fc95-4974-9d12-5f283e7bb605",
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
  "content_id": "84f3d286-fa32-4ef8-aad8-22e681318c55",
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
  "content_id": "53ceeaa5-8259-4ded-8f51-c805a0f3b558",
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
  "content_id": "672f1f8b-80a8-4391-a493-b839b68c2c94",
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
  "content_id": "a7c0494d-e7ef-4353-81e4-2c4283b87d83",
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
  "content_id": "6c6954d9-bd38-4a7f-a5be-f6e741229e0d",
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
  "content_id": "a095db58-64cd-4b56-a989-909a743e498f",
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
  "content_id": "6dfc6319-2cdf-446d-8cbc-49695d580527",
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
  "content_id": "dadf2bf7-f190-4fa8-81a1-34a1ae01a4e2",
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
  "content_id": "9bb4fe14-3984-41c9-9a99-bddeca2fab05",
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
  "content_id": "1732051f-a30a-4111-a4d2-ecbed832f05f",
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
  "status": 413,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
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
  "content_id": "f396eafa-6095-4ba5-b892-ad3e6b781ac1",
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
  "content_id": "56e89081-1004-44de-a44e-305dbce74873",
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
  "content_id": "c5e73e4c-2038-499e-a1a7-34fc81b816fc",
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
  "content_id": "f9ededf1-ea7e-4da9-822c-d3f3bb62a516",
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
  "content_id": "e21f5dfa-9bc3-49ff-a747-1f1a0109e888",
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
  "content_id": "0fe76df2-772d-43e5-ad6d-090aa32c148d",
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
  "content_id": "5e37cb51-63e4-4b86-a5b5-ec7568b10a7e",
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
  "content_id": "9393400a-6adc-4ce8-8789-faf452015d43",
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
  "content_id": "438c4d3f-9d48-4f20-9409-60092e16ddf9",
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
  "content_id": "a44cbd21-953d-4b70-9713-0f26776dfb4c",
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
  "content_id": "40f919ee-dfd7-4e77-8a1e-5dfcd6856870",
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
  "content_id": "c697eabc-7173-44b5-8a83-ca9e86ba6f2f",
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
