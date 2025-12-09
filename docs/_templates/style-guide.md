# Physical AI Book: Style Guide & Writing Standards

**Purpose**: Ensure consistent, high-quality content across all lessons

---

## Writing Standards

### Readability

- **Target**: 8th-grade reading level (ages 13-14)
- **Sentence length**: Average 15-20 words; max 25 words per sentence
- **Paragraph length**: 3-5 sentences; max 10 lines
- **Jargon**: Minimize; define on first use or link to glossary

### Voice & Tone

- **Address readers as "you"**: "You will create..." not "The user creates..."
- **Active voice**: "You implement the function" not "The function is implemented"
- **Inclusive language**: Use "we," "let's," "together" to build community
- **Encouraging**: Celebrate progress; acknowledge challenges
- **Concrete, not abstract**: Show examples before explanations

### Formatting

- **Headers**: Use markdown hierarchy (`#`, `##`, `###`)
  - H1 (`#`): Lesson title only
  - H2 (`##`): Major sections (Before this chapter, Overview, Explanation, etc.)
  - H3 (`###`): Subsections (Core Concept 1, Variation 1, etc.)

- **Lists**: Use for steps, outcomes, and takeaways
  - Ordered lists for steps (`1.`, `2.`, `3.`)
  - Unordered lists for options or collections (`-` or `*`)

- **Emphasis**:
  - **Bold** for critical concepts: `**Important concept**`
  - *Italic* for emphasis: `*especially important*`
  - `` `code` `` for technical terms and commands

- **Code blocks**:
  ```markdown
  \`\`\`python title="example.py" showLineNumbers
  # Full working code with comments
  \`\`\`
  ```

---

## Lesson Structure (Required for every lesson)

### 1. Front Matter (YAML)

```yaml
---
title: "Lesson Title (5-80 chars)"
description: "One-liner for search (20-200 chars)"
sidebar_position: 1
id: "chapter-X-lesson-Y"
---
```

### 2. Title (H1)

```markdown
# Lesson Title
```

### 3. Before This Chapter (H2)

**Purpose**: Set expectations and prerequisites

```markdown
## Before this chapter

**Prerequisites**:
- [ ] Have you completed [Lesson](../link)?
- [ ] Do you understand [Concept]?
- [ ] Have you installed [Tool]?

**Estimated time**: 45 minutes
```

**Rules**:
- List ALL prerequisites (lessons or external knowledge)
- Link to prerequisite lessons
- Be specific: "Python 3.11+" not just "Python"
- Include setup steps if needed

### 4. You Will Learn (H2)

**Purpose**: Set clear, measurable outcomes

```markdown
## You will learn

By the end of this lesson, you will be able to:

1. [Action verb] [specific outcome]
2. [Action verb] [specific outcome]
3. [Action verb] [specific outcome]
4. [Action verb] [specific outcome]
5. [Action verb] [specific outcome]
```

**Rules**:
- 3-5 outcomes (exactly)
- Start with action verbs: create, build, explain, deploy, understand, apply
- Be specific and measurable
- No vague outcomes like "Learn about X"

**Action Verbs** (Bloom's Taxonomy):
- Remember: list, identify, name, define
- Understand: explain, describe, summarize, classify
- Apply: use, implement, solve, demonstrate
- Analyze: compare, contrast, distinguish, examine
- Evaluate: assess, judge, critique, justify
- Create: design, build, construct, develop

### 5. Overview (H2)

**Purpose**: Hook the reader and explain relevance

```markdown
## Overview

[1-2 paragraphs]

- What is this about?
- Why does it matter?
- What real-world problems does it solve?
- How does it connect to previous lessons?

[NO CODE IN THIS SECTION - conceptual only]
```

**Rules**:
- Written for beginners
- Avoid framework internals
- Connect to learner motivation
- Set context before diving into details

### 6. Explanation with Examples (H2)

**Purpose**: Teach core concepts with working examples

```markdown
## Explanation with Examples

### Core Concept 1: [Title]

[Explanation paragraph]

**Example Code**:

\`\`\`python title="example-1.py" showLineNumbers
# [Description of what this code does]
# Prerequisites: pip install [packages]

[COMPLETE, WORKING CODE - NOT PSEUDOCODE]
\`\`\`

**Expected output**:
\`\`\`
[Exact output when running the code]
\`\`\`

**Variation 1: [How to extend or modify]**

\`\`\`python
[Modified code showing variation]
\`\`\`
```

**Rules**:
- 2-4 core concepts per lesson
- Explanation before code (explain what, then show how)
- Code MUST be complete and runnable
- No pseudocode or ellipses (`...`)
- Include comments in code explaining key lines
- Show expected output exactly as it appears
- Include 1-2 variations showing how to extend

### 7. Hands-On Task (H2)

**Purpose**: Let learners apply what they learned

```markdown
## Hands-On Task

**Goal**: [What they'll build or accomplish]

**Instructions**:

1. [Step 1: specific action]
2. [Step 2]
3. [Step 3]

**Verification**: Run this command:
\`\`\`bash
[Command to verify success]
\`\`\`

Expected output:
\`\`\`
[What success looks like]
\`\`\`
```

**Rules**:
- Can be completed in 15-30 minutes
- Builds on the lesson examples
- Include specific, step-by-step instructions
- Provide verification (how to know they succeeded)
- Celebrate success: "Congratulations! You've..."

### 8. Key Takeaways (H2)

**Purpose**: Summarize and reinforce learning

```markdown
## Key Takeaways

- [Takeaway 1: Core concept or skill]
- [Takeaway 2: Why it matters]
- [Takeaway 3: How to use it]
```

**Rules**:
- 3-5 takeaways (bullets)
- Concise and memorable
- Reinforce learning outcomes
- Include practical application

### 9. Next Steps (H2)

**Purpose**: Guide to further learning

```markdown
## Next Steps

[Brief summary of what comes next or related topics]

- [Link to next lesson](../lesson-X.md)
- [Link to advanced topic](../lesson-Y.md)
- [Suggested challenge project]
```

**Rules**:
- Point to next logical lesson
- Suggest related/advanced topics
- Inspire further exploration

---

## Code Example Standards

### Complete, Working Code

- ✅ `def calculate_sum(n): return sum(range(1, n+1))`
- ❌ `def calculate_sum(n): ... # implementation`
- ❌ Pseudocode or incomplete snippets

### Version Pinning

Always specify exact versions:

```python
# Python: requirements.txt
numpy==1.24.0
tensorflow==2.13.0
```

```json
{
  "dependencies": {
    "express": "4.18.2",
    "axios": "1.6.0"
  }
}
```

### Comments in Code

```python
# Explain WHY, not WHAT
# Calculate sum of squares using efficient method
result = sum(i**2 for i in range(1, n+1))

# Avoid: result = sum(...) # sum of squares
```

### Expected Output

Show EXACT output:

```
Sum of squares 1-5: 55
Processing complete!
```

Not: `[some output]` or `Output varies`

---

## Links & References

### Internal Links

Always use relative paths:

```markdown
[Lesson 1](./lesson-1.md)
[Chapter 2](../chapter-2/lesson-1.md)
```

### External Links

```markdown
[NumPy Docs](https://numpy.org/doc/)
```

### Links to Code Examples

```markdown
See [examples/chapter-1/lesson-1/](../../../examples/chapter-1/lesson-1/)
```

---

## Constitutional Principles Checklist

Before publishing, verify:

- ✅ **I. Hands-On Learning**: Every concept has a runnable example
- ✅ **II. Progressive Disclosure**: Simple → complex; no jumps
- ✅ **III. Executable Examples**: Examples tested and working
- ✅ **IV. Clear Prerequisites**: No hidden assumptions
- ✅ **V. Modular Design**: Lesson works independently (given prerequisites)

---

## Common Mistakes to Avoid

| ❌ Don't | ✅ Do |
|---------|-------|
| "The reader will learn" | "You will learn" |
| Theory-only sections | Every concept has an example |
| "See the code below..." | Explain, then show code |
| Vague outcomes: "Learn X" | Specific: "Build a classifier" |
| Untested examples | Run and verify all examples |
| Broken links | Test all links before publishing |
| Long paragraphs (>10 lines) | Split into 2-3 paragraphs |
| Jargon without definition | Define or link on first use |

---

## Resources

- [Bloom's Taxonomy](https://en.wikipedia.org/wiki/Bloom%27s_taxonomy)
- [Markdown Guide](https://www.markdownguide.org/)
- [8th-Grade Reading Level](https://www.wguniversity.com/reading_level_guide.html)
- [Plain Language Writing](https://www.plainlanguage.gov/)

---

Questions? Open an issue on GitHub: https://github.com/physical-ai/book/issues
