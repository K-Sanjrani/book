# Research: Docusaurus Book Setup & Example Testing

**Date**: 2025-12-09
**Purpose**: Resolve technical unknowns and establish best practices for building the Physical-AI book

## 1. Docusaurus 3.x Setup Best Practices

### Decision: Use Docusaurus 3.x with default "classic" preset

**Rationale**:
- Latest stable version (3.x released 2024) with React 18+ support
- MDX support built-in for interactive code examples
- Built-in dark mode, multi-language, versioning capabilities
- Large community; extensive third-party plugin ecosystem
- Static generation: easy deployment to GitHub Pages, Netlify, Vercel

**Alternatives Considered**:
- **Gatsby + Remark**: More flexible but overkill for documentation; steeper learning curve
- **Next.js + Contentlayer**: Full-featured but requires Node.js backend for deployment
- **VitePress**: Simpler but less mature; smaller ecosystem; UI customization harder

**Setup Command**:
```bash
npx create-docusaurus@latest book classic --typescript false --git false
```

**Key Dependencies**:
- Node.js: 18 LTS (18.17.0+) or 20 LTS
- npm or yarn (recommend npm 9+)
- React 18+
- MDX 2+

---

## 2. Example Code Testing & CI/CD

### Decision: Use GitHub Actions + Language-Specific Test Runners

**Rationale**:
- GitHub Actions is free for public repos; no additional infrastructure cost
- Native integration with GitHub; no third-party service needed
- Supports matrix builds (multiple OS, Node versions, Python versions)
- Can run weekly scheduled tests to catch breaking changes

**Python Example Testing** (pytest):
```yaml
- name: Test Python Examples
  run: |
    cd examples/chapter-1/lesson-1
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    python example-1.py > /tmp/output.txt 2>&1
    # Compare output to expected
    diff /tmp/output.txt expected-output.txt
```

**JavaScript Example Testing** (Node.js):
```yaml
- name: Test JavaScript Examples
  run: |
    cd examples/chapter-1/lesson-1
    npm ci  # Use package-lock.json
    node example-1.js > /tmp/output.txt 2>&1
    # Compare output
    diff /tmp/output.txt expected-output.txt
```

**Link Validation** (docusaurus broken-links detection):
```bash
npm run build  # Generates static site; Docusaurus warns about broken links
```

**Frequency**: Weekly schedule + on every pull request (for new/modified examples)

---

## 3. Content Version Management

### Decision: Pin All Example Versions; Test Weekly; Use Lockfiles

**Rationale**:
- Runnable examples are canonical truth (Constitution Principle III); they MUST work
- Unpinned versions cause "works in my environment" failures
- Weekly CI/CD runs catch breaking changes early
- Lockfiles (package-lock.json, poetry.lock) ensure reproducibility

**Python Strategy**:
- **requirements.txt**: Pin major.minor versions
  ```
  numpy==1.24.0
  tensorflow==2.13.0
  ```
- **Runtime**: Test against pinned versions in CI/CD
- **Breaking Changes**: When a new major version releases, create a variant example (e.g., `example-1-tf2.14.md`) and link from original

**JavaScript Strategy**:
- **package.json**: Use caret ranges (^) for patch updates; lock major.minor
  ```json
  {
    "dependencies": {
      "express": "^4.18.2",
      "axios": "^1.6.0"
    }
  }
  ```
- **package-lock.json**: Commit to repo; use in CI (`npm ci` not `npm install`)
- **Node.js Version**: Specify in `.nvmrc` (e.g., `18.17.0`)

**Versioning Examples in Documentation**:
```markdown
## Example Code

Prerequisites: Python 3.11+, numpy==1.24.0

\`\`\`python
# This example was tested with numpy 1.24.0
import numpy as np
...
\`\`\`

**Note**: If you're using a different version (e.g., numpy 2.0), you may need to
adjust import statements. See [Version Guide](../version-migration.md).
```

---

## 4. Lesson Template & Style Guide

### Decision: Prescriptive Template + Author Checklist

**Rationale**:
- Beginners and intermediate authors need clear structure
- Constitution Principles I-V must be enforced in every lesson
- Consistent template = consistent user experience = builds trust
- Checklist prevents publication of non-compliant lessons

**Lesson Template Structure** (enforced by _templates/lesson-template.md):

```markdown
---
title: "[Lesson Title]"
description: "[1-line summary for search/preview]"
sidebar_position: 1
---

# [Lesson Title]

## Before this chapter

**Prerequisites**:
- [ ] Have you completed [Prerequisite Lesson 1]? ([Link])
- [ ] Do you understand [Concept X]? ([Link to glossary])
- [ ] Have you installed [Tool Y]? ([Setup guide])

**Estimated time**: 30 minutes

---

## You will learn

By the end of this lesson, you will be able to:

1. [Specific, measurable outcome 1]
2. [Specific, measurable outcome 2]
3. [Specific, measurable outcome 3]
4. [Specific, measurable outcome 4]
5. [Specific, measurable outcome 5]

---

## Overview

[1-2 paragraphs: What is this about? Why does it matter? Connect to real-world use cases.]

---

## Explanation with Examples

### Core Concept 1: [Title]

[Explanation: What is this concept? When do you use it? Why is it important?]

**Example Code**:

\`\`\`python title="example-1.py" showLineNumbers
# [Description: What this code does and what it demonstrates]
# Prerequisites: pip install [packages]

[FULL WORKING CODE - NOT PSEUDOCODE]
\`\`\`

**Expected output**:
\`\`\`
[What the user should see when they run this code]
\`\`\`

**Variation 1: [How to modify the example]**

\`\`\`python
[Modified code]
\`\`\`

---

### Core Concept 2: [Title]

[Repeat structure for second concept]

---

## Hands-On Task

**Goal**: [What you'll build or accomplish in this section]

**Instructions**:

1. [Step 1: specific action with code if needed]
2. [Step 2]
3. [Step 3]

**Verification**: Run this command to verify your work:
\`\`\`bash
[Command or code snippet showing how to verify success]
\`\`\`

Expected output:
\`\`\`
[What should appear if successful]
\`\`\`

---

## Key Takeaways

- [Key point 1: Summarize a core concept or skill]
- [Key point 2]
- [Key point 3]

---

## Next Steps

[Brief summary of what comes next. Link to follow-up lessons or advanced topics.]

---

## Glossary (inline for this lesson)

- **Term 1**: [Definition]
- **Term 2**: [Definition]
```

**Author Checklist** (checklists/constitution.md):

```markdown
# Constitution Compliance Checklist: [Lesson Name]

## Principle I: Hands-On Learning First
- [ ] Every concept has at least one runnable code example
- [ ] Examples are complete working code (not pseudocode)
- [ ] Examples can be run within 5-10 minutes (including setup)
- [ ] All examples tested and verified before submission
- [ ] No "theory-only" sections without supporting examples

## Principle II: Progressive Disclosure
- [ ] Overview section is concise (1-2 pages max)
- [ ] Core concepts explained before advanced variations
- [ ] Beginner section avoids framework internals
- [ ] Intermediate explanation reveals "why" beneath the code
- [ ] Lesson builds on prerequisites without requiring external research

## Principle III: Executable Examples as Canonical Truth
- [ ] All example code tested and produces expected output
- [ ] Version numbers explicitly stated (e.g., "numpy==1.24.0")
- [ ] No outdated syntax or deprecated APIs
- [ ] If documentation conflicts with example, documentation is wrong
- [ ] All external links in examples tested and working

## Principle IV: Clear Prerequisites and Skill Expectations
- [ ] "Before this chapter" section lists ALL required prior knowledge
- [ ] Prerequisites are either linked to previous lessons or marked [TBD]
- [ ] "You will learn" section has 3-5 specific, measurable outcomes
- [ ] No hidden assumptions about what readers know
- [ ] Difficult terms defined inline or linked to glossary

## Principle V: Modular Documentation
- [ ] This lesson can be completed independently (given prerequisites)
- [ ] Cross-references use explicit links
- [ ] No "read chapters 1-7 first" requirements
- [ ] Lesson is discoverable via search
- [ ] Related lessons are linked in "Next steps"

## Quality Checks
- [ ] Markdown lints without errors
- [ ] All links (internal and external) work
- [ ] Code blocks use syntax highlighting for language
- [ ] No spelling or grammar errors
- [ ] Estimated time is accurate (tested by timing yourself)

## Ready to Publish
- [ ] All checkboxes above are checked
- [ ] Code examples run without errors
- [ ] Another person can follow this lesson without issues
```

---

## 5. Search & Navigation Patterns

### Decision: Docusaurus Sidebar + Algolia DocSearch (Optional)

**Rationale**:
- Docusaurus sidebar auto-generates from `_category_.json`; minimal config required
- Algolia DocSearch is free for open-source docs; provides instant full-text search
- Breadcrumb navigation helps readers understand hierarchy
- "Previous/Next" buttons guide linear learners

**Sidebar Structure** (sidebars.js):
```javascript
module.exports = {
  docs: [
    'intro',
    {
      label: 'Chapter 1: Introduction to Physical AI',
      position: 1,
      items: [
        'chapter-1/lesson-1',
        'chapter-1/lesson-2',
        'chapter-1/lesson-3',
      ],
    },
    {
      label: 'Chapter 2: [TBD]',
      position: 2,
      items: [
        'chapter-2/lesson-1',
        // ...
      ],
    },
  ],
};
```

**Chapter Metadata** (_category_.json):
```json
{
  "label": "Chapter 1: Introduction to Physical AI",
  "position": 1,
  "link": {
    "type": "generated-index",
    "description": "Learn the fundamentals of hands-on AI development. This chapter covers core concepts with practical examples you can run immediately."
  }
}
```

**Navigation Pattern**:
```
Breadcrumb: Home > Chapter 1 > Lesson 1
[Previous] [Next] buttons at bottom
"Related lessons" sidebar
Full-text search at top
```

---

## Summary: Recommended Tech Stack

| Component | Choice | Version |
|-----------|--------|---------|
| **Documentation Framework** | Docusaurus | 3.x |
| **Runtime** | Node.js | 18 LTS or 20 LTS |
| **Example: Python** | Python | 3.11+ |
| **Example: JavaScript** | Node.js | 18 LTS |
| **Build Tool** | npm | 9+ |
| **CI/CD** | GitHub Actions | (built-in) |
| **Hosting** | GitHub Pages / Netlify | (free) |
| **Search (Optional)** | Algolia DocSearch | Free OSS tier |
| **Code Validation** | pytest (Python), Node.js (JS) | Latest |
| **Link Validation** | Docusaurus built-in | (automatic) |

---

## Implementation Readiness

✅ All unknowns resolved
✅ Best practices documented
✅ CI/CD pipeline template provided
✅ Example versioning strategy defined
✅ Lesson template enforces Constitution principles
✅ Author checklist prevents non-compliant lessons

**Ready to proceed to Phase 1** (Design & Implementation)
