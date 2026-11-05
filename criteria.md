# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1. False positives stay rare across trials

In each of 3 trials, no more than 1 of 10 human-written calibration texts
(calibration set A, all human-written, distinct from the mixed set in
criterion 3) is labelled high-confidence AI (combined score at or above
0.65).

**Why this target:** A false accusation can seriously harm a real writer, so I
would rather let some AI-written text through than often label human writing
as AI. Checking each trial separately prevents a good average from hiding an
inconsistent detector.

---

## 2. Clearly AI and human scores separate

Using the same set of 5 clearly AI-written and 5 human-written texts, the mean
AI score is at least 0.25 higher for the AI set in each of 3 trials.

**Why this target:** The two sets should be separated enough to give the
labels useful evidence, but I do not expect perfect detection or a gap between
every individual text. Repeating the comparison accounts for the model
signal's variation.

---

## 3. All three labels are reachable

Using the same mixed set of 5 clearly-AI and 5 human-written texts from
criterion 2 (not calibration set A, which is all human-written), at least one
text receives each label in each of 3 trials: high-confidence human, unsure,
and high-confidence AI.

**Why this target:** A label that never appears is not useful, and its absence
could mean the score ranges are unreachable with the actual signals. This set
must contain real AI-written text, otherwise reaching "high-confidence AI"
would require the false positive that criterion 1 is designed to make rare.
Testing real submissions checks the full path, not just the threshold
definitions.

---

## 4. Valid appeals are recorded and put under review

For 5 out of 5 appeals with an existing `content_id`, the endpoint returns
success and appends exactly one matching audit event with status
`under_review`; the original decision remains in the log. An appeal for an
unknown `content_id` is rejected and creates no appeal event.

**Why this target:** An appeal is the writer's path to challenge a decision.
It must give clear confirmation and leave an audit trail without erasing the
original decision; rejecting unknown IDs avoids recording a review that
cannot be tied to a submission.

---

## 5. Invalid and oversized text gets a clear rejection

Missing, null, empty, whitespace-only, or non-string `text` returns HTTP 400
with a JSON error and creates no decision. Text longer than 10,000 characters
returns HTTP 413 and is not scored. None of these cases returns HTTP 500.

**Why this target:** These checks give clients a clear way to correct
malformed requests and keep oversized submissions from consuming unbounded
work. The 10,000-character limit is a concrete boundary that can be tested
reproducibly.



---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
