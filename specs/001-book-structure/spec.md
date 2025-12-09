# Feature Specification: Physical-AI Book Structure & Organization

**Feature Branch**: `001-book-structure`
**Created**: 2025-12-09
**Status**: Draft
**Input**: User description: "Based on the constitution, create a detailed specification for a physical AI book including: 1. Book structure with 1 chapter and 3 lessons each (title and descriptions) 2. Content guidelines and lesson format 3. Docusaurus specific: requirements for organisation"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Content Author Writes First Lesson (Priority: P1)

A technical author needs to write the first lesson in Chapter 1 following the book's structure and content guidelines. The author should be able to understand the lesson format, structure their content according to the Physical-AI Constitution principles, and ensure their runnable examples are testable.

**Why this priority**: This is the MVP—establishing the pattern for all future content. A single well-structured, hands-on lesson demonstrates the book's viability and can be immediately deployed to validate the approach.

**Independent Test**: A content author can write a complete lesson (prerequisites, learning outcomes, explanation, runnable example, key takeaways) in one sitting (under 2 hours) following the provided template and guidelines. The lesson adheres to all 5 Constitution principles and includes working code examples.

**Acceptance Scenarios**:

1. **Given** a blank lesson template in Docusaurus, **When** an author follows the structure and guidelines, **Then** the lesson renders correctly with all sections visible and formatted properly
2. **Given** a runnable example in the lesson, **When** a reader runs the code snippet, **Then** the example executes without errors and produces expected output within 5 minutes
3. **Given** a lesson with prerequisites stated, **When** a reader completes the prerequisite lessons, **Then** they can follow the current lesson independently without external research

---

### User Story 2 - Organization Manages Chapter and Lesson Navigation (Priority: P2)

An information architect or documentation lead needs to organize multiple lessons into a coherent chapter structure within Docusaurus. They should be able to group lessons, manage navigation, and ensure readers can discover and navigate content intuitively.

**Why this priority**: P2 because it depends on P1 lessons existing. Once lessons are created, the navigation structure makes the book navigable and professional. This enables users to explore the full curriculum.

**Independent Test**: The Docusaurus site generates a working sidebar/navigation that displays all chapters and lessons in correct order, with proper hierarchies. Readers can navigate between related lessons and chapters using breadcrumbs or sidebar without getting lost.

**Acceptance Scenarios**:

1. **Given** a Docusaurus project with multiple lessons in Chapter 1, **When** the documentation builds, **Then** the sidebar automatically displays Chapter 1 with all 3 lessons nested correctly
2. **Given** a reader on any lesson page, **When** they click "Next" or use breadcrumb navigation, **Then** they move to the next logical lesson or section
3. **Given** a lesson with prerequisites, **When** a reader views that lesson, **Then** clear links to prerequisite lessons are visible at the top

---

### User Story 3 - Editor Validates Content Quality Against Constitution (Priority: P3)

An editor or QA reviewer needs to ensure that all lessons adhere to the Physical-AI Constitution principles before publication. They should have clear guidelines to validate executable examples, progressive disclosure, prerequisites clarity, and hands-on learning elements.

**Why this priority**: P3 because it builds on existing content from P1/P2. Quality gates ensure long-term consistency; they're important but not blocking initial book launch.

**Independent Test**: Using a provided checklist based on the Constitution, an editor can audit a lesson in under 30 minutes and determine if it meets all 5 principles. The checklist produces a clear pass/fail result with specific feedback for any failures.

**Acceptance Scenarios**:

1. **Given** a completed lesson, **When** an editor runs the Constitution compliance checklist, **Then** they receive a clear report: all 5 principles either PASS or list specific issues
2. **Given** a lesson with a non-functional example, **When** the editor tests the example, **Then** the issue is flagged and a clear remediation path is suggested
3. **Given** a lesson lacking clear prerequisites, **When** the editor reviews the "Before this chapter" section, **Then** missing prerequisites are highlighted for the author to address

---

### Edge Cases

- What happens when a lesson depends on prerequisites from multiple previous chapters? (e.g., Lesson 3 requires both Chapter 1, Lesson 2 AND Chapter 2, Lesson 1)
- How should the book handle breaking changes in framework/library versions used in examples? (examples tested against v1.0, but v2.0 released)
- What if a reader completes lessons out of order? Should the book allow this or enforce prerequisite order?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Book MUST contain at least 1 chapter with 3 lessons each (initial structure)
- **FR-002**: Each lesson MUST include a "Before this chapter" section listing all prerequisite knowledge
- **FR-003**: Each lesson MUST include a "You will learn" section with 3-5 concrete, measurable outcomes
- **FR-004**: Each lesson MUST include at least one runnable code example with full working code (not pseudocode)
- **FR-005**: All runnable examples MUST be tested and verified to execute end-to-end without errors
- **FR-006**: Lesson structure MUST follow a consistent template: Title → Prerequisites → Overview → Explanation with examples → Hands-on task → Key takeaways
- **FR-007**: Docusaurus site MUST auto-generate sidebar navigation displaying chapter/lesson hierarchy
- **FR-008**: Documentation MUST provide a style guide and lesson template for future authors
- **FR-009**: Documentation MUST include a Content Quality Checklist for editors to validate lessons against the Constitution
- **FR-010**: All external links (cross-references, example repos, API docs) MUST be tested and verified to work

### Key Entities

- **Chapter**: Container for related lessons; has title, description, and 1-3 lessons
- **Lesson**: Individual learning unit; has prerequisites, learning outcomes, explanation, runnable example, key takeaways
- **Runnable Example**: Code snippet that users can copy and execute; includes setup instructions, code, expected output
- **Prerequisite**: Prior lesson, chapter, or external knowledge required before starting a lesson
- **Learning Outcome**: Specific, measurable skill or knowledge the learner gains from the lesson

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 100% of lessons include runnable examples that execute successfully on first attempt (verified by automated testing)
- **SC-002**: A beginner reader can complete any single lesson (including running examples and hands-on task) in 30-60 minutes without external research
- **SC-003**: An intermediate reader can skim a lesson (read overview + outcomes + example) and determine if it's relevant in under 3 minutes
- **SC-004**: Navigation works flawlessly: readers can move between lessons, chapters, and prerequisites with 1-2 clicks
- **SC-005**: Documentation for authors (style guide + template) enables a new author to write a lesson without clarification questions
- **SC-006**: Content Quality Checklist can be applied to any lesson in under 30 minutes and produces clear pass/fail feedback
- **SC-007**: Zero broken links (all cross-references, external repos, API docs resolve correctly)
- **SC-008**: First chapter with 3 lessons is fully written, tested, and ready for publication within the sprint

## Content Guidelines & Lesson Format

### Lesson Structure Template

Every lesson MUST follow this structure:

```
# Lesson Title

## Before this chapter

**Prerequisites**: [List specific prior lessons/chapters or external knowledge required]
- Have you completed [Prerequisite Lesson 1]?
- Do you understand [Concept X]?
- Have you installed [Tool Y]?

## You will learn

By the end of this lesson, you will be able to:
1. [Specific outcome 1 - measurable verb + object]
2. [Specific outcome 2]
3. [Specific outcome 3]
4. [Specific outcome 4]
5. [Specific outcome 5]

## Overview

[1-2 paragraphs] Plain-language explanation of what this lesson covers and why it matters.
Avoid jargon; if needed, define inline.

## Explanation with Examples

### Core Concept 1
[Explanation] → [Runnable example] → [Variation/extension]

### Core Concept 2
[Explanation] → [Runnable example] → [Variation/extension]

## Hands-On Task

**Goal**: [What the learner will build/accomplish]

**Instructions**:
1. [Step 1 with clear action]
2. [Step 2]
...

**Verification**: How the learner can confirm they've succeeded (expected output, working code, deployed app)

## Key Takeaways

- [Takeaway 1]
- [Takeaway 2]
- [Takeaway 3]

## Next Steps

[Point to follow-up lessons, advanced topics, or related resources]

---

## Code Examples

All code examples follow this format:

\`\`\`[language]
# [Description of what this code does]
# Prerequisites: [What must be installed/configured]

[Full working code - NOT pseudocode]
\`\`\`

Expected output:
\`\`\`
[What the code prints/returns when run successfully]
\`\`\`

Time to run: [5 minutes / 10 minutes / etc.]
```

### Content Guidelines

1. **Hands-On Learning First**: Every concept MUST include a working example. No theory-only sections.
2. **Progressive Disclosure**: Start simple (core concept in 1-2 pages), then extend with variations and advanced patterns.
3. **Executable Examples as Truth**: If documentation conflicts with examples, correct the documentation. Examples are tested before publication.
4. **Clear Prerequisites**: Always state what users need to know/install upfront. No hidden assumptions.
5. **Modular**: Each lesson is self-contained; readers can skip to any lesson and still succeed (given prerequisites).

### Writing Standards

- **Readability**: 8th-grade reading level; short sentences (< 20 words); active voice; address readers as "you"
- **Accuracy**: All examples tested; error handling documented; framework versions pinned
- **Engagement**: Open each lesson with "Why this matters"; include success celebrations; prompt users to share results

### Docusaurus-Specific Requirements

1. **File Structure**:
   ```
   docs/
   ├── intro.md                    (Welcome page)
   ├── chapter-1/
   │   ├── _category_.json         (Chapter metadata: title, description, position)
   │   ├── lesson-1.md
   │   ├── lesson-2.md
   │   └── lesson-3.md
   └── chapter-2/
       ├── _category_.json
       ├── lesson-1.md
       ├── lesson-2.md
       └── lesson-3.md
   ```

2. **Front Matter (YAML)**: Every `.md` file starts with:
   ```yaml
   ---
   title: "Lesson Title"
   description: "One-line description shown in search and previews"
   sidebar_position: 1
   ---
   ```

3. **Navigation**: Use `_category_.json` to define chapter grouping:
   ```json
   {
     "label": "Chapter 1: [Title]",
     "position": 1,
     "link": {
       "type": "generated-index",
       "description": "Chapter description shown to readers"
     }
   }
   ```

4. **Code Blocks**: Use MDX syntax for interactive examples:
   ````markdown
   ```python title="example.py" showLineNumbers
   # Your code here
   ```
   ````

5. **Cross-References**: Use relative paths for internal links:
   ```markdown
   See [Prerequisite Lesson](../chapter-1/lesson-1.md) for details
   ```

6. **Search & Metadata**: All lessons have front matter with:
   - Clear, searchable title
   - Description (shown in search results)
   - `sidebar_position` (controls order in sidebar)

## Assumptions

- The book will start with **exactly 1 chapter containing 3 lessons** (as specified); future chapters/lessons will follow the same pattern
- **Examples will use Python or JavaScript** (most common for physical AI projects); specific language to be determined per lesson
- **Initial target audience**: Beginners and early-intermediate learners; advanced topics will be cross-referenced but not primary focus
- **Deployment**: Static site hosted on GitHub Pages or Netlify; no backend required
- **Version management**: Example code is pinned to specific framework versions (e.g., Python 3.11, TensorFlow 2.13) and tested weekly in CI/CD
