# Data Model: Physical-AI Book Content Structure

**Date**: 2025-12-09
**Purpose**: Define the core entities, relationships, and validation rules for book content

## Core Entities

### 1. Lesson

**Description**: A self-contained learning unit representing a single, focused topic. Lessons are the atomic units of the book; users can complete any lesson independently (given prerequisites).

**Fields**:

| Field | Type | Required | Constraints | Description |
|-------|------|----------|-------------|-------------|
| `id` | string | ✅ | Unique; format: `chapter-{N}-lesson-{N}` | Unique identifier (e.g., `chapter-1-lesson-1`) |
| `title` | string | ✅ | Length: 5-80 chars | Lesson title (concise, descriptive) |
| `description` | string | ✅ | Length: 20-200 chars | One-liner for search previews |
| `chapter_id` | string | ✅ | Must reference existing Chapter | Parent chapter |
| `position` | integer | ✅ | >= 1 | Display order within chapter |
| `difficulty` | enum | ✅ | `beginner` \| `intermediate` | Target skill level |
| `estimated_time_minutes` | integer | ✅ | 15-180 range | Time to complete lesson + examples |
| `prerequisites` | array[string] | ✅ | Array of lesson IDs or external knowledge | Must-complete lessons before this one |
| `learning_outcomes` | array[string] | ✅ | Exactly 3-5 items; each 10-150 chars | What learner can do after completing |
| `content` | object | ✅ | See sections below | Main lesson content |
| `runnable_examples` | array[RunableExample] | ✅ | At least 1; up to 5 per lesson | Code examples users can execute |
| `metadata` | object | ✅ | See metadata schema | Author, last_updated, tags |
| `status` | enum | ✅ | `draft` \| `review` \| `published` | Publication status |

**Content Structure**:

```json
{
  "content": {
    "overview": {
      "type": "markdown",
      "description": "1-2 paragraph intro; why this matters; real-world relevance",
      "max_length": 500
    },
    "explanation": {
      "type": "markdown_with_code",
      "description": "2-4 core concepts, each with explanation + runnable example + variation",
      "min_sections": 2,
      "max_sections": 4
    },
    "hands_on_task": {
      "type": "markdown_with_code",
      "description": "Guided practice section; step-by-step instructions; includes verification",
      "required": true
    },
    "key_takeaways": {
      "type": "array[string]",
      "description": "3-5 summary bullets; reinforce core learning",
      "min_items": 3,
      "max_items": 5
    },
    "next_steps": {
      "type": "markdown",
      "description": "Pointer to follow-up lessons or advanced topics",
      "required": true
    }
  }
}
```

**Validation Rules**:

- Learning outcomes must be specific and measurable (use action verbs: create, build, explain, deploy)
- Prerequisites must be either: (a) lesson IDs from the same chapter, (b) lesson IDs from prior chapters, or (c) external knowledge marked as [TBD]
- All runnable examples must pass CI/CD tests
- Estimated time must match actual completion time (±10%)
- No links (internal or external) can be broken

**Relationships**:
- Belongs to: **Chapter** (many-to-one)
- Contains: **RunableExample** (one-to-many)
- References: **Lesson** (prerequisites; many-to-many)
- Has: **ContentQualityCheckpoint** (one-to-many)

---

### 2. Chapter

**Description**: A container for related lessons. Chapters organize lessons into coherent learning paths. Each chapter has 3-5 lessons covering a theme or skill area.

**Fields**:

| Field | Type | Required | Constraints | Description |
|-------|------|----------|-------------|-------------|
| `id` | string | ✅ | Unique; format: `chapter-{N}` | Unique identifier (e.g., `chapter-1`) |
| `title` | string | ✅ | Length: 5-100 chars | Chapter title |
| `description` | markdown | ✅ | Length: 50-500 chars | Chapter overview; why this chapter matters |
| `position` | integer | ✅ | >= 1 | Display order in book |
| `lessons` | array[Lesson] | ✅ | 3-5 lessons per MVP; expandable | Child lessons |
| `learning_goals` | array[string] | ✅ | 3-5 high-level goals | What users will learn from full chapter |
| `status` | enum | ✅ | `draft` \| `review` \| `published` | Publication status |
| `metadata` | object | ✅ | Author, last_updated, tags | Metadata |

**Validation Rules**:

- Each chapter must have at least 3 lessons (MVP requirement)
- Chapter learning goals must summarize all lesson outcomes
- All lessons in chapter must be tested and published before chapter is published
- Chapter position must be unique

**Relationships**:
- Contains: **Lesson** (one-to-many)

---

### 3. RunableExample

**Description**: A code snippet that users can copy and execute. Examples are the canonical source of truth; they must always work (Constitution Principle III).

**Fields**:

| Field | Type | Required | Constraints | Description |
|-------|------|----------|-------------|-------------|
| `id` | string | ✅ | Format: `{lesson_id}-example-{N}` | Unique identifier |
| `title` | string | ✅ | Length: 5-60 chars | Example name/description |
| `language` | enum | ✅ | `python` \| `javascript` \| `bash` | Programming language |
| `code` | string | ✅ | Length: 50-5000 chars | Full working code (NOT pseudocode) |
| `setup_instructions` | markdown | ✅ | Length: 20-500 chars | Prerequisites (install, import, config) |
| `expected_output` | string | ✅ | Length: 10-1000 chars | What code should produce when run |
| `estimated_time_seconds` | integer | ✅ | 5-600 range | How long to run (e.g., 30 for 30 seconds) |
| `version_constraints` | array[string] | ✅ | e.g., ["python>=3.11", "tensorflow==2.13.0"] | Framework/library versions tested |
| `test_status` | enum | ✅ | `pass` \| `fail` \| `pending` | Last CI/CD test result |
| `last_tested` | timestamp | ✅ | ISO 8601 format | When example was last validated |

**Validation Rules**:

- Code must be complete and executable (no ellipses "..."; no pseudocode)
- `expected_output` must exactly match actual output (or be a regex pattern for variable output)
- `version_constraints` must match what's in requirements.txt / package-lock.json
- Examples must pass CI/CD tests before publication
- Examples must be tested at least weekly (automated)

**Test Failure Handling**:

When `test_status` becomes `fail`:
1. Author is notified (via GitHub issue or email)
2. Example is marked as pending publication
3. Author must either:
   - Fix the code
   - Update version constraints if breaking change detected
   - Create a variant example (e.g., `example-1-tf2.14.md`)
4. Example must pass CI/CD before re-publication

**Relationships**:
- Belongs to: **Lesson** (many-to-one)

---

### 4. ContentQualityCheckpoint

**Description**: Tracks quality reviews and Constitution compliance for each lesson. Editors use this to validate lessons before publication.

**Fields**:

| Field | Type | Required | Constraints | Description |
|-------|------|----------|-------------|-------------|
| `id` | string | ✅ | UUID format | Unique checkpoint ID |
| `lesson_id` | string | ✅ | Must reference existing Lesson | Lesson being reviewed |
| `principle` | enum | ✅ | `I` \| `II` \| `III` \| `IV` \| `V` | Which Constitution Principle |
| `status` | enum | ✅ | `pass` \| `fail` \| `needs_revision` | Compliance status |
| `feedback` | markdown | ✅ | Length: 20-1000 chars | Specific issues or praise |
| `checked_by` | string | ✅ | GitHub username or email | Reviewer identity |
| `checked_at` | timestamp | ✅ | ISO 8601 format | When review occurred |
| `examples_tested` | boolean | ✅ | true \| false | Were all examples tested? |

**Validation Rules**:

- All 5 principles must be reviewed before lesson publication
- All principles must show `status: pass` for publication
- Feedback should be actionable and specific (not generic praise/criticism)
- If any principle fails, lesson cannot be published until revised

**Relationships**:
- References: **Lesson** (many-to-one)

---

## Relationships & Navigation

```
Book
  ├─ Chapter 1
  │   ├─ Lesson 1.1 ──→ [prerequisites: Lesson 0.X (none for MVP)]
  │   │   ├─ RunableExample 1.1.1 ──→ (Python code)
  │   │   ├─ RunableExample 1.1.2 ──→ (JavaScript variant)
  │   │   └─ ContentQualityCheckpoint (5 principles)
  │   ├─ Lesson 1.2 ──→ [prerequisites: Lesson 1.1]
  │   │   ├─ RunableExample 1.2.1
  │   │   └─ ContentQualityCheckpoint
  │   └─ Lesson 1.3 ──→ [prerequisites: Lesson 1.2]
  │       ├─ RunableExample 1.3.1
  │       └─ ContentQualityCheckpoint
  │
  ├─ Chapter 2 (future)
  │   ├─ Lesson 2.1 ──→ [prerequisites: Lesson 1.3]
  │   └─ ...
  │
  └─ Chapter 3+ (future)
```

**Navigation Paths**:
- **Linear**: Lesson 1.1 → 1.2 → 1.3 → 2.1 → 2.2 (follow prerequisites)
- **Non-linear**: Jump to any lesson with prerequisites met
- **Exploratory**: Search/browse sidebar for topics of interest

---

## State Transitions

### Lesson Lifecycle

```
[DRAFT] ──→ [REVIEW] ──→ [PUBLISHED] ←→ [UPDATED]
   ↑          ↑              ↓
   └──────────┴──────────────┘
        (revision loop)
```

**Transition Rules**:
- Draft → Review: Author submits for review (all fields filled, examples pass CI/CD)
- Review → Published: Editor approves all 5 Constitutional principles (via ContentQualityCheckpoint)
- Published → Updated: Minor edits (typos, link fixes) don't require full review
- Any state → Draft: Author can revert for edits

### RunableExample Test Cycle

```
[PASSING] ──(weekly CI/CD)──→ [PASSING or FAILING]
   ↑                              ↓
   └──(author fixes code)─────────┘
         ↓
    [FAILING] ──(author investigates)──→ [version breaking change?]
                                            ├─ YES: Create variant example
                                            └─ NO: Fix code
```

---

## Metadata Schema

**Lesson Metadata**:
```json
{
  "metadata": {
    "author": "string (GitHub handle)",
    "created_at": "timestamp (ISO 8601)",
    "last_updated": "timestamp (ISO 8601)",
    "last_tested": "timestamp (ISO 8601) - auto-updated by CI/CD",
    "tags": ["array", "of", "searchable", "keywords"],
    "languages": ["python", "javascript"],
    "difficulty_stars": 2,
    "completion_rate": 0.85,
    "feedback_score": 4.8,
    "view_count": 1234
  }
}
```

**Example Metadata**:
```json
{
  "metadata": {
    "language": "python",
    "last_tested": "timestamp",
    "version_tested": {
      "python": "3.11.7",
      "tensorflow": "2.13.0",
      "numpy": "1.24.0"
    },
    "ci_run_url": "https://github.com/.../actions/runs/...",
    "test_duration_seconds": 8
  }
}
```

---

## Implementation Notes

### Markdown File Structure

Lessons are stored as Markdown files with YAML front matter:

```markdown
---
title: "Lesson Title"
description: "One-liner for search"
id: "chapter-1-lesson-1"
chapter_id: "chapter-1"
position: 1
difficulty: "beginner"
estimated_time_minutes: 45
prerequisites: []
learning_outcomes:
  - "Create a working [concept] from scratch"
  - "Explain how [mechanism] works"
  - "Deploy a [project] to production"
status: "published"
metadata:
  author: "your-github-handle"
  tags: ["hands-on", "beginner-friendly", "python"]
---

# Lesson Title

## Before this chapter
...
```

### Validation During Build

Docusaurus build process (via GitHub Actions):
1. Parse YAML front matter
2. Validate all required fields present
3. Test all runnable examples in `examples/` directory
4. Check all links (internal and external)
5. Lint Markdown (remark)
6. Generate table of contents (TOC)
7. Publish to static site

---

## Summary

The data model ensures:
- ✅ Lessons are independent, testable units (Principle V: Modular)
- ✅ Examples are always working (Principle III: Executable Examples as Truth)
- ✅ Quality is enforced (Principle I-V validation via ContentQualityCheckpoint)
- ✅ Prerequisites are clear (Principle IV: Clear Prerequisites)
- ✅ Content is progressive (Principle II: Progressive Disclosure enforced via lesson structure)
