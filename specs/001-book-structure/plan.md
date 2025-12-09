# Implementation Plan: Physical-AI Book Structure & Organization

**Branch**: `001-book-structure` | **Date**: 2025-12-09 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/001-book-structure/spec.md`

## Summary

Build a Docusaurus-based documentation site for the Physical-AI book that demonstrates hands-on learning principles through carefully structured chapters and lessons. The MVP focuses on Chapter 1 (3 lessons) with runnable examples, clear prerequisites, and modular design. Technical approach: Docusaurus 3.x with MDX for interactive code examples, automated CI/CD validation for all runnable examples, and a lesson template that enforces Constitution principles (hands-on learning, progressive disclosure, executable examples, clear prerequisites, modularity).

## Technical Context

**Documentation Framework**: Docusaurus 3.x (React + MDX)
**Primary Dependencies**:
- Docusaurus 3.x core
- Node.js 18+ (Docusaurus requirement)
- MDX support (built-in)
- Algolia DocSearch (optional, for search)

**Example Languages**: Python 3.11+ and/or JavaScript/Node.js (TBD per lesson; examples version-pinned in package.json or requirements.txt)

**Storage**: File-based (Markdown + MDX); no database required

**Testing**:
- Markdown linting (remark)
- Link validation (docusaurus broken-links detection)
- Example code validation (pytest for Python examples, node for JS)
- Constitution compliance checklist (manual + automated checks)

**Target Platform**: Web (static HTML); hosted on GitHub Pages, Netlify, or Vercel

**Project Type**: Documentation site (Docusaurus SPA)

**Performance Goals**:
- Page load: < 2 seconds (typical for static sites)
- Search response: < 200ms
- All runnable examples complete within advertised time (5-10 minutes per example)

**Constraints**:
- All examples MUST run successfully on first attempt (100% pass rate)
- No external API dependencies in examples (offline-capable)
- Examples must be version-pinned and tested weekly in CI/CD
- Zero broken links in published site

**Scale/Scope**:
- MVP: 1 chapter, 3 lessons
- Future: Expandable to 5+ chapters, 15+ lessons
- Expected audience: 100s to 1000s of learners initially

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Physical-AI Constitution Alignment

✅ **Principle I: Hands-On Learning First**
- Every lesson MUST include runnable code examples
- Examples are testable and verified before publication
- No theory-only sections; all theory grounded in practice
- Requirement FR-005 enforces testing; SC-001 measures 100% pass rate

✅ **Principle II: Progressive Disclosure (Scaffolded Complexity)**
- Lesson template enforces: Overview → Explanation → Examples → Hands-on task
- Beginner-focused introduction with intermediate extensions noted
- "You will learn" section scaffolds expectations
- User Story P1 demonstrates pattern; P2 scales to multiple lessons

✅ **Principle III: Executable Examples as Canonical Truth**
- Examples are source of truth; documentation corrected if conflicting
- CI/CD pipeline (weekly runs) catches version mismatches early
- Requirement FR-010 enforces link testing
- Success Criterion SC-001 requires 100% example pass rate

✅ **Principle IV: Clear Prerequisites and Skill Expectations**
- Lesson template mandates "Before this chapter" section (FR-002)
- "You will learn" section required (FR-003)
- Requirement FR-002 explicitly lists prerequisites
- Acceptance scenario validates independent completion

✅ **Principle V: Modular Documentation (Topic Independence)**
- Each lesson is self-contained (FR-006)
- Cross-references explicit (FR-010)
- Docusaurus sidebar enables non-linear discovery
- User Story P2 manages navigation to support modularity

**Constitutional Compliance**: ✅ ALL PRINCIPLES SATISFIED
- No violations identified
- All 10 functional requirements directly support Constitution principles
- 8 success criteria measure compliance

## Project Structure

### Documentation (this feature)

```text
specs/001-book-structure/
├── spec.md                  # Feature specification (completed)
├── plan.md                  # This file (in progress)
├── research.md              # Phase 0 research (TBD)
├── data-model.md            # Phase 1 content model (TBD)
├── quickstart.md            # Phase 1 onboarding guide (TBD)
├── contracts/               # Phase 1 API specs (TBD)
│   ├── lesson-schema.json   # Lesson data structure
│   ├── docusaurus-config.json # Docusaurus configuration
│   └── ci-cd-pipeline.yaml  # Example validation pipeline
├── checklists/
│   ├── requirements.md      # Specification quality (completed)
│   └── constitution.md      # Constitution compliance (TBD via /sp.checklist)
└── tasks.md                 # Phase 2 implementation tasks (via /sp.tasks)
```

### Source Code (repository root)

```text
book/                           # Main Docusaurus project
├── docusaurus.config.js         # Docusaurus configuration
├── package.json                 # Node.js dependencies
├── sidebars.js                  # Sidebar/navigation structure
├── docs/
│   ├── intro.md                 # Welcome/landing page
│   ├── chapter-1/               # Chapter 1: [Title - TBD]
│   │   ├── _category_.json      # Chapter metadata
│   │   ├── lesson-1.md          # Lesson 1: [Title - TBD]
│   │   ├── lesson-2.md          # Lesson 2: [Title - TBD]
│   │   └── lesson-3.md          # Lesson 3: [Title - TBD]
│   ├── chapter-2/               # Future chapters
│   └── _templates/              # Lesson template for authors
│       └── lesson-template.md   # Template with all required sections
├── examples/                    # Runnable example code
│   ├── chapter-1/
│   │   ├── lesson-1/
│   │   │   ├── example-1.py     # Python example (if applicable)
│   │   │   ├── example-1.js     # JavaScript example (if applicable)
│   │   │   ├── requirements.txt # Python dependencies
│   │   │   └── package.json     # Node dependencies
│   │   ├── lesson-2/
│   │   └── lesson-3/
│   └── README.md                # How to run examples locally
├── tests/
│   ├── examples/                # Integration tests for examples
│   │   └── test-examples.py     # Runs all examples, validates output
│   ├── links/                   # Link validation tests
│   │   └── test-links.js        # Broken link checker
│   └── constitution/            # Constitution compliance tests
│       └── test-constitution.js # Validates lesson structure
├── .github/workflows/           # CI/CD pipelines
│   ├── test-examples.yml        # Weekly example validation
│   ├── link-check.yml           # Link validation on PR
│   └── build.yml                # Docusaurus build verification
├── static/                      # Static assets (images, etc.)
└── src/                         # Docusaurus React components
    ├── components/              # Custom React components
    │   └── CodeExample.jsx       # Interactive code example component
    └── css/                      # Custom styles

```

**Structure Decision**:
Using **Docusaurus 3.x static site** with co-located example code. Rationale:
- Examples are version-pinned and tested separately (ci-cd-pipeline.yml)
- Lesson markdown files are in `docs/chapter-*/`, making them easy to navigate
- Examples in `examples/` directory allow independent CI/CD validation
- Docusaurus auto-generates sidebar from `_category_.json` files
- MDX support enables interactive code blocks if needed
- Static hosting (GitHub Pages, Netlify, Vercel) is free and simple
- No backend complexity; all content is discoverable via full-text search

## Complexity Tracking

No Constitution violations identified. All design decisions align with project principles.

---

## Phase 0: Research & Clarification

**Goals**: Resolve unknowns in Technical Context; establish best practices for Docusaurus + Example Testing + Content Management

### Research Tasks

1. **Docusaurus 3.x Setup Best Practices**
   - Question: How to structure Docusaurus projects for maximum scalability?
   - Research: Docusaurus 3.x documentation, community patterns
   - Output: Optimal directory layout, Docusaurus config template

2. **Example Code Testing & CI/CD**
   - Question: How to validate runnable examples in CI/CD for multiple languages?
   - Research: GitHub Actions patterns, pytest + Node.js testing, version management
   - Output: CI/CD pipeline examples (Python + JavaScript validation)

3. **Content Version Management**
   - Question: How to pin example versions and detect breaking changes?
   - Research: requirements.txt pinning, package.json lock files, testing practices
   - Output: Version strategy document

4. **Lesson Template & Style Guide**
   - Question: How to make lesson template usable by non-technical authors?
   - Research: Technical writing standards, Progressive Disclosure patterns
   - Output: Author style guide + Template validation checklist

5. **Search & Navigation Patterns**
   - Question: Best way to organize navigation for non-linear learning?
   - Research: Docusaurus sidebar features, breadcrumb patterns, search optimization
   - Output: Navigation architecture document

### Research Outputs

**research.md** will document:
- Docusaurus 3.x setup command (npx create-docusaurus@latest)
- Recommended Node.js version (18 LTS)
- Example structure for Python/JavaScript projects
- GitHub Actions workflow templates for CI/CD
- Content versioning strategy (SemVer for examples)
- Author onboarding checklist

---

## Phase 1: Design & Implementation Plan

**Prerequisites**: `research.md` complete

### Phase 1a: Content Model (data-model.md)

**Entities**:

1. **Lesson**
   - title (string): Lesson name
   - chapter (string): Parent chapter
   - prerequisites (array): Required prior lessons
   - learning_outcomes (array[5]): Measurable outcomes
   - sections:
     - overview (markdown)
     - explanation (markdown + code examples)
     - hands_on_task (markdown)
     - key_takeaways (array)
     - next_steps (markdown)
   - runnable_examples (array): Code examples with expected output
   - estimated_time (minutes): How long to complete
   - difficulty (beginner | intermediate)

2. **Chapter**
   - title (string): Chapter name
   - description (markdown): Overview
   - lessons (array[3+]): Child lessons
   - position (integer): Display order
   - learning_goals (array): High-level chapter goals

3. **RunableExample**
   - language (python | javascript | bash)
   - title (string): Example name
   - code (string): Full working code
   - setup_instructions (markdown): Prerequisites (CLI setup, package installs)
   - expected_output (string): What code should produce
   - estimated_time (minutes): How long to run
   - version_constraint (string): Framework/library version (e.g., "python>=3.11", "tensorflow>=2.13")

4. **ContentQualityCheckpoint**
   - lesson_id (string)
   - constitution_principle (enum: I-V)
   - status (PASS | FAIL | NEEDS_REVISION)
   - feedback (string): Specific issues or praise
   - checked_by (user): Editor/reviewer
   - checked_at (timestamp)

### Phase 1b: API Contracts & Configuration (contracts/)

**Lesson Schema** (contracts/lesson-schema.json):
```json
{
  "type": "object",
  "required": ["title", "chapter", "prerequisites", "learning_outcomes", "sections"],
  "properties": {
    "title": { "type": "string", "minLength": 5 },
    "chapter": { "type": "string" },
    "prerequisites": { "type": "array" },
    "learning_outcomes": { "type": "array", "minItems": 3, "maxItems": 5 },
    "sections": {
      "type": "object",
      "required": ["overview", "explanation", "hands_on_task", "key_takeaways"],
      "properties": { ... }
    },
    "runnable_examples": {
      "type": "array",
      "items": {
        "required": ["language", "code", "expected_output"],
        "properties": { ... }
      }
    }
  }
}
```

**Docusaurus Config** (contracts/docusaurus-config.json):
```json
{
  "title": "Physical AI Book",
  "tagline": "Learn hands-on AI with practical examples",
  "url": "https://physical-ai.dev",
  "theme": "classic",
  "docs": {
    "sidebar": { "path": "sidebars.js" },
    "sidebarPath": "sidebars.js",
    "routeBasePath": "/learn"
  },
  "presets": [
    [
      "@docusaurus/preset-classic",
      {
        "docs": {
          "sidebarPath": "sidebars.js"
        }
      }
    ]
  ]
}
```

**CI/CD Pipeline** (contracts/ci-cd-pipeline.yaml):
```yaml
name: Validate Examples
on:
  schedule:
    - cron: '0 0 * * 0'  # Weekly
  pull_request:

jobs:
  python-examples:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - run: |
          cd examples/chapter-1
          for dir in lesson-*/; do
            cd "$dir"
            pip install -r requirements.txt
            python example-*.py > /tmp/output.txt
            # Verify output matches expected
            cd ..
          done

  javascript-examples:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
      - run: |
          cd examples/chapter-1
          for dir in lesson-*/; do
            cd "$dir"
            npm ci
            node example-*.js > /tmp/output.txt
            cd ..
          done
```

### Phase 1c: Quickstart Guide (quickstart.md)

**quickstart.md** covers:
1. Prerequisites (Node.js 18+, npm/yarn)
2. Local setup (git clone, npm install)
3. Running Docusaurus locally (npm start)
4. Adding your first lesson (copy template, follow structure)
5. Testing examples locally (python/node commands)
6. Deploying to GitHub Pages/Netlify
7. Running Constitution compliance checklist

### Phase 1d: Agent Context Update

Run `.specify/scripts/powershell/update-agent-context.ps1 -AgentType claude` to:
- Add Docusaurus 3.x to tech stack context
- Document lesson template structure
- Note Constitution principles alignment
- Update development patterns (example validation, CI/CD)

---

## Phase 1 Outputs

- ✅ **research.md**: Docusaurus best practices, CI/CD patterns, content versioning
- ✅ **data-model.md**: Lesson, Chapter, RunableExample, ContentQualityCheckpoint entities
- ✅ **quickstart.md**: Local development setup guide
- ✅ **contracts/**: Lesson schema, Docusaurus config, CI/CD pipeline template
- ✅ **Agent context updated**: Docusaurus + example testing patterns documented

---

## Phase 2: Implementation Tasks (via /sp.tasks)

The `/sp.tasks` command will generate:

1. **Phase 1: Setup** (Shared Infrastructure)
   - Initialize Docusaurus project
   - Configure package.json with dependencies
   - Set up GitHub Actions workflows
   - Create lesson template

2. **Phase 2: Foundational** (Blocking Prerequisites)
   - Create sidebars.js with Chapter 1 structure
   - Set up CI/CD for example validation
   - Create _category_.json for chapters/lessons
   - Initialize examples/ directory with version requirements

3. **Phase 3: User Story 1** (P1 - MVP)
   - Write Chapter 1, Lesson 1 (with runnable example)
   - Write Chapter 1, Lesson 2 (with runnable example)
   - Write Chapter 1, Lesson 3 (with runnable example)
   - Test all examples in CI/CD
   - Validate Constitution compliance

4. **Phase 4: User Story 2** (P2)
   - Configure navigation/breadcrumbs
   - Set up Algolia search (optional)
   - Test cross-lesson navigation

5. **Phase 5: User Story 3** (P3)
   - Create Constitution compliance checklist tool
   - Document editor/QA process
   - Run full QA pass on Chapter 1

6. **Phase 6: Polish & Deployment**
   - Deploy to GitHub Pages / Netlify
   - Verify site performance
   - Create author onboarding docs

---

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Examples break with library updates | High | Weekly CI/CD runs; version pinning; automated alerts |
| Lesson template too complex for authors | Medium | Provide detailed style guide + interactive template validator |
| Navigation gets cluttered as lessons grow | Medium | Modular chapter structure; search-driven discovery |
| Broken links in cross-references | Medium | Link validation in CI/CD; automated PRs to fix |

---

## Success Criteria (Recap)

1. ✅ 100% of runnable examples execute successfully
2. ✅ Beginner completes any lesson in 30-60 minutes without external research
3. ✅ Intermediate reader identifies lesson relevance in < 3 minutes
4. ✅ Zero broken links; flawless navigation
5. ✅ Author style guide enables new authors without clarification
6. ✅ Quality checklist produces pass/fail in < 30 minutes
7. ✅ First chapter with 3 lessons ready for publication within sprint

---

## Next Steps

1. **Proceed to Phase 0 research** (if needed for clarifications)
2. **Run `/sp.tasks`** to generate implementation tasks for Phase 1-3
3. **Execute Phase 1** (Docusaurus setup, content model, CI/CD)
4. **Execute Phase 2 & 3** (Write lessons, validate examples)
5. **Deploy to production** (GitHub Pages / Netlify)
