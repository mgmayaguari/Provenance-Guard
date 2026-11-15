"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

# Criterion 2 ("score separation") and criterion 3 ("label coverage") are
# measured against the SAME mixed set — 5 clearly-AI and 5 human-written
# texts — per criteria.md. Defined once here and reused in both scenarios
# below so the two criteria are genuinely comparable, not two different sets
# that happen to share a name.
#
# The AI-written half is text I (the model) generated for this purpose — that's
# legitimate, it really is AI output. The human-written half is pulled from
# attack_set/attacks.csv's false_positive family (FP01, FP02, FP04, FP05,
# FP06) — written by course staff as plausible human writing, not by me and
# not AI-generated, which is exactly what this set needs and what I can't
# supply myself without secretly contaminating the "human" side with AI text.
MIXED_SET = [
    # --- clearly AI-written (5) ---
    "Effective time management is essential to achieving personal and "
    "professional success. By prioritizing tasks, individuals can ensure "
    "that their most important responsibilities are addressed first. "
    "Additionally, setting clear goals helps to maintain focus and "
    "motivation throughout the day. It is also beneficial to minimize "
    "distractions, as they can significantly reduce productivity. "
    "Ultimately, those who manage their time well are better positioned to "
    "accomplish their objectives and reduce unnecessary stress.",

    "Remote work offers numerous advantages for both employees and "
    "employers. Employees benefit from greater flexibility, reduced "
    "commuting time, and an improved work-life balance. Employers, in turn, "
    "often see increased productivity and lower overhead costs. However, it "
    "is important to acknowledge the challenges that remote work can "
    "present, such as feelings of isolation and difficulties with "
    "communication. Organizations that invest in the right tools and "
    "practices can successfully navigate these challenges and unlock the "
    "full potential of a distributed workforce.",

    "A balanced diet plays a crucial role in maintaining overall health and "
    "well-being. Consuming a variety of fruits, vegetables, whole grains, "
    "and lean proteins provides the body with essential nutrients. "
    "Furthermore, staying adequately hydrated supports digestion and "
    "cognitive function. It is also important to limit the intake of "
    "processed foods and added sugars, as excessive consumption has been "
    "linked to various health issues. By making mindful dietary choices, "
    "individuals can significantly improve their quality of life.",

    "The transition to renewable energy sources is a critical step in "
    "addressing climate change. Solar, wind, and hydroelectric power offer "
    "sustainable alternatives to fossil fuels, reducing greenhouse gas "
    "emissions. Moreover, investment in renewable infrastructure can create "
    "new jobs and stimulate economic growth. While the initial costs of "
    "transitioning can be significant, the long-term environmental and "
    "economic benefits make this shift a worthwhile endeavor for nations "
    "around the world.",

    "Lifelong learning is increasingly recognized as essential in today's "
    "rapidly changing world. As industries evolve and new technologies "
    "emerge, individuals must continually update their skills to remain "
    "competitive. Engaging in continuous education, whether through formal "
    "courses or self-directed study, fosters adaptability and opens new "
    "opportunities. Organizations that encourage a culture of learning "
    "among their employees tend to benefit from higher innovation and "
    "stronger long-term performance.",

    # --- human-written (5) — attack_set/attacks.csv, false_positive family ---
    "We got to the campsite about four. The pitch was fine, a bit sloped, "
    "but there was a tap nearby and the toilets were clean enough. Putting "
    "the tent up took longer than it should have because I had forgotten "
    "how the poles went. The weather held until Saturday night. Then it "
    "rained hard and kept raining. We stayed in the tent and played cards "
    "and ate most of the food we had brought for Sunday. On Sunday we "
    "packed up wet and drove home early. It was not the weekend we planned "
    "but the kids enjoyed it and we would go back.",

    "This report sets out the findings of the working group. The group met "
    "four times between January and March. Its remit was to review the "
    "current arrangements and to recommend changes where these were "
    "warranted. The group found that the existing arrangements are broadly "
    "sound. Three areas were identified where improvement is possible. "
    "These are set out in section four, together with an indicative "
    "timetable. The group recommends that the committee adopt the "
    "proposals in full.",

    "There are three main causes of the conflict. The first cause is "
    "economic. Trade between the two regions had declined significantly in "
    "the preceding decade. The second cause is political. Neither "
    "government was able to control its own border provinces effectively. "
    "The third cause is social. Population movements had created "
    "communities on both sides with divided loyalties. In conclusion, the "
    "conflict cannot be explained by any single factor.",

    "To configure the service, edit the settings file in the installation "
    "directory. Set the host value to the address the service should bind "
    "to. Set the port value to an unused port above 1024. Save the file "
    "and restart the service. The service will log its startup "
    "configuration. If the port is already in use, the service will exit "
    "with an error. Check the log file for details before retrying.",

    "Dear Sir or Madam, I am writing to enquire about the position "
    "advertised on your website. I have five years of relevant experience "
    "and I believe I would be a strong fit for the role. I have attached "
    "my curriculum vitae for your consideration. I am available for "
    "interview at your convenience. Thank you for your time. I look "
    "forward to hearing from you.",
]


SCENARIOS = [
    {
        "name": "false positives (calibration set A)",
        "criterion": 1,
        # ⚠️ PUT YOUR OWN WRITING HERE. Not AI text, not a sample from the web —
        # things you actually wrote. This is the criterion that matters most and
        # it's meaningless with someone else's prose. Needs 10, all human,
        # distinct from MIXED_SET above (criteria.md calls this "calibration
        # set A"). Old emails, commit messages expanded into prose, journal
        # entries, forum posts you wrote — anything is fair game as long as
        # you actually wrote it.
        "texts": [
            "how can i write this without the em dash \"Built inventory systems for two Ecuadorian retailers in Google Apps Script and Sheets: point-of-sale receipts that automatically decrement stock, restock and return handling, and tax-ready sales records — replacing handwritten ledgers and monthly physical counts. Deployed inside the owners' existing Google environment so they could adopt it without learning new software, and handed off operations through hands-on training. Both remain in daily use two years later; I still provide updates and support.",
            "think like an senior softwar developer and analyze this project and compare it to another project i'm interested to build using similar technologies but the new one alins with my current trade job as an electrician - an estimator tool (similar tools already exists) but i want to integrate it within a system and create a SAS meaning, this tools can be integrate a bussiness owner environment and eentually automate most of the processes, starting from estimating costs, tracking materials costs across multiple supliers, and accounting it in the estimations as well, then bidding, and eventually scheduling - more features to be added but that's how i would like to start - by architecturing it, building it, testing it, integratying RAG and also AI to learn and adapt communications, etc etc - specifications are not 100 yet - but also i want to use my software developer skills and enhance my career capital - not the robinhood project i can simplify it and deploy but where should i allocate my time and or i can work on the robinhood copilot awhile working on the specificacions of the other tool",
            "before starting the electrical project, can i simplify the robinhood portfolio - rather than being so complext, only spend a weekend time of work to have it sitting ther in my github rather than having it incomplete",
            "i joined the gym with my girlfriend and want to work out together, our goal is to burn fat and tone the body - create a step by step plan for our join workputs starting today to august 3rd - main focus on legs",
            "i'm back to my day to day and the goal is to tone and slim down, alrady drinking 4 liter of water, heating somewhat healthy but still 180lbs and physic is a bit overweight in the chest, face and stomach - as an exper fitness trainer create a work out plan, one that pushes me to the extreme, take in mind i do walk my dog about 3 miles daily - i'm trying to run with him but he is also fat so we just walk - also i want to see tangible results by end of this year",
            "now i will take my mm to the gym, but she will be doing her own routine - not mix with mine - help me as an expert fitness trainer to crave a plan for her - he goal is to improve movement and strengh for an adult years, she is 54 years old, healthy somewhat overweigh but not execisive and diet is very healthy - he day to day is to baby sit her grandchild and few days a week she works cleaning houses where she exaustes a lot - so i want a plan of 1 hur in the gym to improve her strght and mobility as well as since she has varices to help with the blood flow",
            "Based on everything you know about me and my goals to be a successful businessman and philosophies recommend audible books I can use my credits on to grow my knowledge and get inspired or learn from authors that have been very successful",
            "the house in rent: 53 pleasantville road ossining ny 10562 two rooms it second floor, with a shared hall bathroom; room dimensions are roughly 10 x 11 feet and 8 x11 feet respedctively, they are spacius and comfortable. main floor, has two rooms about the same sizes, with their own closets, plus kitchen and living rooom and deck as well backyard, parking spot and right to laundy and central air only incovinience is that the persons renting upstairs will need to use the shower here. research the zone and rentals with similar features to determine the right price for each rental",
            "Dream meaning: I was running away from someone then found back door but it lead to someone’s home a father and boy, I was unarmed somehow I broke the barrier without breaking, I was outside the building observing but the man following me broke downs door and because of ig I ran the boy shot me in the back following later the man that was chasing me appeared and they also shot him. My dog, my a aguas dog came by and inigially i was facing up and he hides me to lay face down and he peed on me before laying down next to me in the right, we were close to a hospital like right next to ig but entrance was on the other side and the father and son prioritized the other man rising him there then asked me but I could speak just make noise and he usderstood I didn’t need a ambulance and left me there following a cow appeared and lilac my hand I think it also Vite me but then luee down on the left side i was dragging myself to the hospital before I had the two animals next to me laying with me",
            "Wiser or confused?\nA memoir after solo traveling\nBy Michael Mayaguari\n\n\n\n\n\n\n\nLast night, a friend asked, Do you feel wiser after traveling for so long? And there I was with a vague response. Define “wise” – the ability to make sound judgments and decisions based on knowledge, experience, and understanding. It often involves a deep awareness of the complexities of life and the capacity to apply this insight thoughtfully and practically. Wise individuals are typically characterized by their prudence, foresight, and the ability to consider the long-term consequences of their actions.\n\nWhere exactly did it begin?\n\nLong ago, before I even knew I wanted to embark on this journey before I even understood the world as it is and what it meant to be a traveler.\n\nI found myself many times at family events having to explain what exactly I do to my relatives. Now I have an elevator pitch for it since understanding can come as difficult sometimes. I’m not saying they are not smart to understand it but they are unaware of this type of work since I’m the first one in my family to break into tech. The pitch goes like “...open your phone, now go to any of the applications in it. There, I help create, improve and maintain a similar app…”\nMy name is Michael Mayaguari, a full stack software engineer at a fintech company. Well, there is more to it, I’m Ecuadorian, immigrant, first generation college graduate and first one in my family to break into tech.\n\n\nHonesty, something i value over anything else! I recently encounter with a respons that was honest and sincere. In tech it’s easy to heard thing like i love what i do and i’m happy to be here. But how many time do you hear honest answers about i chose this path over this because it will buid the skillset i need to achieve what i need to do.as someone who is just starting their journey in tehc or any field of the matter is great to surround yourself with people who sahare values and perspectives that align with yours because eventually they can help you learning and support to avoidable challenges that you have to overcome in your path but if you have some sorth pf guidance it will be easier in a sense that it will be better to learn and be ready than face them without any knowledge and then find out others had already gone throught that before you. Yes, challenges build you but rether than figuring out challenges someone else already went throught you could face and spend time on new challenges. This is a [rocess of growth and building a legacy for future generations.\n\nMy passion is still unclear i’m good at what i do, but i’m not yet the best at it and i know once i’m the best this 9=-5 will be boring and eventually move on to somerthing different but it’s important to move somewhere where my skillset growth in a different way and eventually lead me to my big picture.\n\nI’m a big picture oriente guy and to be honest it’s fien to be this way because the little things cn be figured out on the spot but if you lose track of the big goal then you get lost on the road. So what’s next for me.\n\nHonesty, something I appreciate over anything else! I recently encountered a very honest response to the question “why did you leave?” Time to time people say because it was time, i wanted a new experience or there was no more rrom for me to growth. But someone answered this question in away that aligned with my sentiments. Because i needed to build a skill set that will help me achieve my personal growth. Yes, as an engineer you spend quality time with very talented people, smart people and get to build fun things but Personally I know where I want to be in the next 10 years so as someone who is just starting in their career is hard to know where to go. Listening to honest answers gives me a clear signt that there a is different path to get and practice while building the skillset to be where i want to be in the furturew.\n"
        ],
    },
    {
        "name": "score separation (mixed set)",
        "criterion": 2,
        # Same 10 texts as criterion 3 below — criteria.md measures both off
        # the identical mixed set, so the comparison is apples-to-apples.
        "texts": MIXED_SET,
    },
    {
        "name": "label coverage (same mixed set)",
        "criterion": 3,
        # Deliberately the same list object as above, not a re-typed copy —
        # criterion 3 is reachability of all three labels on this exact set.
        "texts": MIXED_SET,
    },
    {
        "name": "bad input",
        "criterion": 5,
        "bodies": [
            {"text": "", "creator_id": "eval_bad_empty"},
            {"creator_id": "eval_bad_missing"},                    # no text field at all
            {"text": None, "creator_id": "eval_bad_null"},
            {"text": "   \t  \n  ", "creator_id": "eval_bad_whitespace"},
            {"text": 12345, "creator_id": "eval_bad_nonstring"},   # text is not a string
            {"text": "word " * 2500, "creator_id": "eval_bad_oversized"},  # > 10,000 chars
        ],
    },

    # Criterion 4 (the appeal path) can't be expressed as "texts" or "bodies"
    # alone — it needs a submission first and then an appeal against the
    # content_id that submission returns, and this file only sends one batch
    # of independent requests per scenario. I tested this one by hand against
    # a running server instead of through run_eval.py: submitted a piece of
    # text, took the content_id from the response, posted it to /appeal, and
    # confirmed the returned status and the resulting audit log entries.
    # That's documented with the real output in the README, not here.
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
