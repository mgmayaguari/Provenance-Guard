"""
Signal two: the style signal. ← YOU BUILD THIS IN MILESTONE 4

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures are stubbed below because the brief names those three. They are
stubs, not implementations: what they compute is yours, and so is how you
combine them.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
    punctuation_density      how much punctuation, and how varied?

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── The three measures — YOU BUILD THESE ─────────────────────────────────────

def sentence_length_spread(text: str) -> float:
    """
    How much sentence length varies. ← TODO

    Returns:
        A float. Decide yourself what scale it's on and which direction means
        "more human" — then write that down, because your combining rule
        depends on knowing it.

    A hint on what you're reaching for: the standard deviation of sentence
    lengths, probably divided by the mean so a long text and a short one are
    comparable. `statistics.stdev` is imported for you.

    Watch the edge case: a one-sentence submission has no spread at all, and
    `stdev` raises on fewer than two values. Decide what that should return
    before the attack set decides for you.
    """
    lengths = [len(words(s)) for s in sentences(text)]
    lengths = [n for n in lengths if n > 0]

    if len(lengths) < 2:
        return 0.0

    mean_length = statistics.mean(lengths)
    if mean_length == 0:
        return 0.0

    return statistics.stdev(lengths) / mean_length


def type_token_ratio(text: str) -> float:
    """
    Unique words over total words. ← TODO

    Returns:
        A float between 0 and 1. Higher means more varied vocabulary.

    Worth knowing before you rely on it: this measure falls as text gets
    longer, because common words repeat. Two texts of different lengths aren't
    directly comparable on it, and if your test inputs vary a lot in length,
    that alone can look like a signal.
    """
    all_words = words(text)
    if not all_words:
        return 0.0

    return len(set(all_words)) / len(all_words)


def punctuation_density(text: str) -> float:
    """
    How much punctuation, relative to length. ← TODO

    Returns:
        A float. Whether you count all punctuation or only some kinds — commas,
        semicolons, dashes — is a real choice. Semicolons and em dashes are
        more interesting than full stops, because they vary more between
        writers.
    """
    all_words = words(text)
    if not all_words:
        return 0.0

    interesting = len(re.findall(r"[;:—–()\"]", text))
    return interesting / len(all_words)


# ── Combining them ───────────────────────────────────────────────────────────

def style_signal(text: str) -> float:
    """
    The style signal as a 0–1 score. **Higher means more likely AI.** ← TODO

    Combine your three measures into one number. Same direction as
    `detector.model_signal`, so that `scoring.combine_signals` can treat them
    the same way — if one of your signals runs backwards, everything above it
    is wrong in a way that's hard to see.

    Two things to decide and write down:

      1. Which direction each measure points. Low spread means more AI-ish, so
         it needs flipping. Work out which of your three need that.
      2. How to get each onto a comparable scale. A raw type-token ratio sits
         between 0 and 1; a raw punctuation count doesn't. Adding them
         unscaled means whichever has the bigger numbers wins by default.

    Test it on the four calibration inputs from Milestone 4 — clearly AI,
    clearly human, plain conventional human writing, lightly-edited AI — before
    you trust it. Plain and ordinary, not formal: formal prose reads as *human*
    to signal one, and it is plain writing that gets accused.
    """
    # All three raw measures point toward "more human" when higher — low
    # sentence-length spread, low vocabulary variety, and sparse "interesting"
    # punctuation all read as more machine-like. So each gets scaled to 0-1
    # and then flipped (1 - x) before averaging.
    #
    # The caps below turn unbounded raw numbers into 0-1 scales. They're
    # calibration decisions, not universal constants — chosen so that
    # ordinary human prose lands comfortably under the cap while very
    # uniform, very repetitive, or very unpunctuated text saturates at 1.0.
    spread_cap = 1.0          # coefficient of variation of sentence length
    punctuation_cap = 0.15    # "interesting" punctuation marks per word

    # sentence_length_spread returns 0.0 both when a text is perfectly
    # uniform (real evidence of AI-like rhythm) AND when there's only one
    # sentence to measure (no evidence either way). Those aren't the same
    # thing, so a single-sentence submission gets a neutral 0.5 here instead
    # of being flipped into "maximally AI" — otherwise any short, punchy,
    # perfectly ordinary one-liner reads as AI-like on this measure alone.
    if len(sentences(text)) < 2:
        ai_from_spread = 0.5
    else:
        spread = min(sentence_length_spread(text) / spread_cap, 1.0)
        ai_from_spread = 1.0 - spread

    ttr = min(max(type_token_ratio(text), 0.0), 1.0)
    punctuation = min(punctuation_density(text) / punctuation_cap, 1.0)

    ai_from_ttr = 1.0 - ttr
    ai_from_punctuation = 1.0 - punctuation

    score = (ai_from_spread + ai_from_ttr + ai_from_punctuation) / 3.0
    return round(min(max(score, 0.0), 1.0), 4)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")
