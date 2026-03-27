# Project Report: AI-Assisted Development

## 1. Initial Approach
* **Understanding:** Briefly describe your strategy for tackling the requirements.
I used the strategy that was discussed in the course and that was asking CoPilot to explain the idea and then implement the stubs. Which was my first time using this strategy in particular and found it very helpful in terms of breaking down the main task into smaller chunks

* **Assumptions:** What did you assume about the project before starting?
I assumed it's going to be impossible to implement, to be honest. Probably because I hadn't really explored with Python visulization tools and only done visualization on the web with JS.

## 2. Prompting & AI Interaction
* **Successes:** What types of prompts or context worked best for you?
When I provided the context and asked specific details about a function or a feature I was trying to implement. I particularly like the socratic mode as it helps me learn how to tackle problems better each time.

* **Failures:** Describe specific instances where CoPilot failed (hallucinations, over-engineering, or logical errors).
I don't know why, might be because I used the free models, but AI failed to understand I wanted to implement the bar display at first and implemented the stubs for in-place visulization, showing the numbers and how they were swapped in one line. Also, at first, when I asked for stubs, it implemented them without me asking it to. There were a lot of hallucinations compared to the last time.
Update: Again, Copilot added some dead code and also deprecated code, like in the last project, that was unintended. And when I asked it to remove the redundant code it didn't(The model is GPT Codex, which I've seen suggest deprecated code and ignoring the user's prompt to remove them before)


* **Analysis:** Why do you think these failures happened, and how did they impact your progress?
I assume because I used a free, weaker model sometimes(to save my requests for more important tasks) and also maybe because I wasn't clear enough in my prompts

## 3. Key Learnings
* **Technical Skills:** What CS concepts or tools did you discover or master during this project?
I wouldn't say I mastered any tool, but the use of visualization tools was new and challenging and a valuable outcome.

* **AI Workflow:** How will you change your use of AI tools in your next project?
First of all, I'd try understand the project in depth before starting to code with the socratic mode until I have a semi-clear plan. Then suggest a few functions and ask for a review and then, most importantly, ask for stubs, which I found very helpful in terms of breaking down the tasks and have a clear view on what's to come next.