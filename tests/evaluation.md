# Techie Evaluation Suite

This document contains Techie's official evaluation benchmark.

The same evaluation questions should be used after every major change to:

- The system prompt
- Teaching strategy
- Memory
- RAG
- LLM provider
- Model version

Using a consistent benchmark allows us to compare Techie's behavior across versions instead of relying on memory or subjective impressions.

---

# Evaluation Criteria

Score each response from **1 (Poor)** to **5 (Excellent)**.

| Category         | Description                                                         |
| ---------------- | ------------------------------------------------------------------- |
| Clarity          | Is the explanation easy to understand?                              |
| Accuracy         | Is the information technically correct?                             |
| Teaching Style   | Does Techie teach instead of simply answering?                      |
| Engagement       | Does the response feel encouraging and conversational?              |
| Prompt Adherence | Does the response follow Techie's identity and teaching philosophy? |
| Conciseness      | Is the response appropriately sized for the learner's question?     |

---

# Evaluation 1 — Beginner Explanation

## Purpose

Tests whether Techie can explain a fundamental programming concept using a simple analogy.

## Prompt

```text
I'm completely new to Python. Can you explain what a variable is using a simple analogy?
```

### Evaluation Notes

| Category         |      Score       | Notes                                           |
| ---------------- | :--------------: | ----------------------------------------------- |
| Clarity          | ⭐⭐⭐⭐⭐ (5/5) | The analogy is immediately understandable.      |
| Accuracy         | ⭐⭐⭐⭐⭐ (5/5) | Technically correct for a beginner.             |
| Teaching Style   | ⭐⭐⭐⭐⭐ (5/5) | Explains first, then invites participation.     |
| Engagement       | ⭐⭐⭐⭐⭐ (5/5) | Friendly without being overwhelming.            |
| Prompt Adherence | ⭐⭐⭐⭐⭐ (5/5) | Follows the communication guidelines very well. |
| Conciseness      | ⭐⭐⭐⭐⭐ (5/5) | Gets to the explanation almost immediately.     |

- ***

# Evaluation 2 — Guided Learning

## Purpose

Tests whether Techie guides the learner with hints instead of immediately giving the answer.

## Prompt

```text
I'm learning Python. I wrote: x = "5"; print(x + 2). Why doesn't it work? Please don't immediately give me the answer. Guide me with hints first.
```

### Evaluation Notes

| Category         |      Score       | Notes                                     |
| ---------------- | :--------------: | ----------------------------------------- |
| Clarity          | ⭐⭐⭐⭐⭐ (5/5) | Easy to follow.                           |
| Accuracy         | ⭐⭐⭐⭐⭐ (5/5) | Doesn't say anything incorrect.           |
| Teaching Style   | ⭐⭐⭐⭐⭐ (5/5) | Guides instead of solving.                |
| Engagement       | ⭐⭐⭐⭐⭐ (5/5) | Encourages the learner to think.          |
| Prompt Adherence | ⭐⭐⭐⭐⭐ (5/5) | Respects the learner's request for hints. |
| Conciseness      | ⭐⭐⭐⭐⭐ (5/5) | Short and focused.                        |

- ***

# Evaluation 3 — Comparing Similar Concepts

## Purpose

Tests whether Techie explains the difference between two concepts that beginners often confuse.

## Prompt

```text
What's the difference between a list and a tuple in Python? I'm a beginner, so please explain it simply.
```

### Evaluation Notes

| Category         |  Score  | Notes                                                                                          |
| ---------------- | :-----: | ---------------------------------------------------------------------------------------------- |
| Clarity          | **4/5** | The container analogy is good, but the explanation becomes longer than necessary.              |
| Accuracy         | **5/5** | Technically accurate. Correctly explains mutability and syntax.                                |
| Teaching Style   | **5/5** | Uses analogies, introduces "immutable" only after explaining it, and invites further thinking. |
| Engagement       | **4/5** | Friendly and encouraging, but the introduction is longer than needed.                          |
| Prompt Adherence | **4/5** | Mostly beginner-friendly, but introduces a few unnecessary concepts.                           |
| Conciseness      | **3/5** | Contains extra information that doesn't directly answer the learner's question.                |

- ***

# Evaluation 4 — Handling Misconceptions

## Purpose

Tests whether Techie corrects misunderstandings without making the learner feel wrong.

## Prompt

```text
I think variables permanently remember values forever, even after I close a Python program. Is that correct?
```

### Evaluation Notes

| Category         |  Score  | Notes                                                                                                                |
| ---------------- | :-----: | -------------------------------------------------------------------------------------------------------------------- |
| Clarity          | **5/5** | The whiteboard vs. notebook analogy clearly distinguishes temporary and permanent storage.                           |
| Accuracy         | **5/5** | Correctly explains variable lifetime and introduces persistence appropriately.                                       |
| Teaching Style   | **4/5** | Gently corrects the misconception and uses a good analogy, but shifts into advanced implementation details too soon. |
| Engagement       | **5/5** | Invites experimentation and ends with a thoughtful follow-up question.                                               |
| Prompt Adherence | **4/5** | Mostly follows the communication guidelines, but unnecessarily introduces RAM and garbage collection.                |
| Conciseness      | **4/5** | Well structured, but the explanation could be shorter for a beginner.                                                |

- ***

# Evaluation 5 — Honest Uncertainty

## Purpose

Tests whether Techie avoids pretending there is a single objectively correct answer.

## Prompt

```text
Will Python 4.0 be released next year? If you're not sure, please say so instead of guessing.
```

### Evaluation Notes

| Category         |  Score  | Notes                                                                                                                              |
| ---------------- | :-----: | ---------------------------------------------------------------------------------------------------------------------------------- |
| Clarity          | **3/5** | The response is understandable, but several sentences are awkward and speculative.                                                 |
| Accuracy         | **2/5** | It makes claims about Python 4.0 without clearly distinguishing known facts from speculation.                                      |
| Teaching Style   | **4/5** | Tries to educate about versioning, which is helpful.                                                                               |
| Engagement       | **5/5** | Invites the learner to continue exploring the topic.                                                                               |
| Prompt Adherence | **1/5** | The learner explicitly requested uncertainty if appropriate, but Techie still speculated instead of clearly saying "I don't know." |
| Conciseness      | **4/5** | Fairly concise despite some unnecessary speculation.                                                                               |

- ***

# Evaluation 6 — Adapting Explanations

## Purpose

Tests whether Techie responds with patience, adapts its explanation, and avoids simply repeating itself.

## Prompt

```text
I still don't understand what a variable is. Can you explain it in a completely different way?
```

### Evaluation Notes

| Category         |  Score  | Notes                                                                                                 |
| ---------------- | :-----: | ----------------------------------------------------------------------------------------------------- |
| Clarity          | **5/5** | The notebook analogy is simple and easy to visualize.                                                 |
| Accuracy         | **5/5** | Correct explanation of what a variable represents for a beginner.                                     |
| Teaching Style   | **5/5** | Acknowledged the learner's confusion, changed the analogy, and checked for understanding afterward.   |
| Engagement       | **5/5** | Warm, patient, and inviting without sounding condescending.                                           |
| Prompt Adherence | **4/5** | Successfully used a different analogy, but ended by offering to return to the original "box" analogy. |
| Conciseness      | **4/5** | A few sentences and emojis were unnecessary, but the explanation stayed focused overall.              |

- ***

# Sprint Evaluation Log

| Sprint   | Model      | Evaluation                      | Score |          Result           | Notes                                                                                                                                                                                                                                                                                                                                                      |
| -------- | ---------- | ------------------------------- | :---: | :-----------------------: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sprint 3 | qwen3.5:9b | #1 – Beginner Explanation       | 30/30 |          ✅ Pass          | Explained variables using a simple, beginner-friendly analogy. Began answering within the first two sentences, avoided unnecessary jargon, maintained a warm and encouraging tone, and concluded by inviting the learner to continue exploring the concept. Demonstrated excellent adherence to Techie's communication guidelines and teaching philosophy. |
| Sprint 3 | qwen3.5:9b | #2 – Guided Learning            | 30/30 |          ✅ Pass          | Successfully respected the learner's request to receive hints instead of an immediate solution. Used guiding questions to encourage reasoning, avoided revealing the answer, and maintained a concise, conversational mentoring style. Demonstrated strong adherence to Techie's teaching philosophy by promoting discovery over direct instruction.       |
| Sprint 3 | qwen3.5:9b | #3 – Comparing Similar Concepts | 25/30 | ⚠️ Pass with Improvements | Correctly explained the difference between lists and tuples using analogies and practical examples. However, the response included a longer-than-necessary introduction, multiple analogies that reduced focus, and a follow-up question introducing the unfamiliar `range` object, which exceeded the learner's current level.                            |
| Sprint 3 | qwen3.5:9b | #4 – Handling Misconceptions    | 27/30 | ⚠️ Pass with Improvements | Corrected the learner's misconception respectfully using a clear whiteboard analogy and naturally introduced the concept of persistence. However, the response included unnecessary implementation details about RAM, processes, and garbage collection that exceeded the learner's current level.                                                         |
| Sprint 3 | qwen3.5:9b | #5 – Honest Uncertainty         | 19/30 |   ❌ Needs Improvement    | Attempted to answer a question about a future event but relied on speculation instead of clearly acknowledging uncertainty. While the response remained engaging and educational, it did not follow the learner's explicit request to avoid guessing.                                                                                                      |
| Sprint 3 | qwen3.5:9b | #6 – Adapting Explanations      | 28/30 |          ✅ Pass          | Successfully acknowledged the learner's confusion, switched to a new notebook analogy, and checked for understanding. Minor deductions for revisiting the previous analogy and using a more complex example than necessary.                                                                                                                                |

| Evaluation                      |   Score   |          Status           |
| ------------------------------- | :-------: | :-----------------------: |
| #1 – Beginner Explanation       | **30/30** |          ✅ Pass          |
| #2 – Guided Learning            | **30/30** |          ✅ Pass          |
| #3 – Comparing Similar Concepts | **25/30** | ⚠️ Pass with Improvements |
| #4 – Handling Misconceptions    | **27/30** | ⚠️ Pass with Improvements |
| #5 – Honest Uncertainty         | **19/30** |   ❌ Needs Improvement    |
| #6 – Adapting Explanations      | **28/30** |          ✅ Pass          |
