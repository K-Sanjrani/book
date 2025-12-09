---
description: "Implementation tasks for Physical-AI Book Structure & Organization"
---

# Tasks: Physical-AI Book Structure & Organization

**Input**: Design documents from `specs/001-book-structure/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Test tasks are INCLUDED (per specification requirement SC-001: "100% of lessons include runnable examples that execute successfully on first attempt")

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story. Each user story is independently completable and testable.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure. All Phase 1 tasks are blocking prerequisites for user stories.

- [ ] T001 Create project directory structure per implementation plan at book/
- [ ] T002 Initialize Node.js project with npm init at book/package.json
- [ ] T003 Install Docusaurus 3.x and dependencies via npm install in book/
- [ ] T004 Create docusaurus.config.js with base configuration (title, tagline, theme: classic)
- [ ] T005 [P] Create sidebars.js with chapter structure template
- [ ] T006 [P] Create docs/ directory structure: intro.md, chapter-1/, _templates/
- [ ] T007 [P] Create examples/ directory structure: chapter-1/lesson-{1,2,3}/
- [ ] T008 Create docs/intro.md as landing/welcome page for book
- [ ] T009 [P] Create docs/_templates/lesson-template.md with full lesson structure (Before this chapter → You will learn → Overview → Explanation → Hands-on → Key takeaways → Next steps)
- [ ] T010 Copy .github/workflows/test-examples.yml from contracts/ to .github/workflows/ (Python + JS example testing)
- [ ] T011 Copy .github/workflows/build.yml from contracts/ to .github/workflows/ (Docusaurus build verification)
- [ ] T012 Copy .github/workflows/link-check.yml from contracts/ to .github/workflows/ (Broken link validation)
- [ ] T013 Create docs/chapter-1/_category_.json with chapter metadata (label, position, description)
- [ ] T014 Create README.md in book/ with quickstart instructions and project overview
- [ ] T015 Verify Docusaurus builds successfully locally: npm run build

**Checkpoint**: All infrastructure in place - ready for user story work

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core setup that MUST be complete before ANY user story implementation.

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T016 Create static/ directory for images and assets
- [ ] T017 Create src/components/ directory for custom React components (future use)
- [ ] T018 Create package-lock.json by running npm ci (lock dependencies for reproducibility)
- [ ] T019 Configure package.json scripts: "start" (npm run dev), "build" (npm run build), "test" (placeholder for CI)
- [ ] T020 [P] Create examples/README.md with instructions on how to run examples locally
- [ ] T021 [P] Create examples/chapter-1/.gitkeep to ensure directory structure is tracked
- [ ] T022 Set up git pre-commit hook template (optional: markdown linting)
- [ ] T023 Create docs/_templates/style-guide.md with writing standards (8th-grade reading level, active voice, you-addressing, code examples)
- [ ] T024 Create docs/_templates/author-checklist.md for Constitution compliance checks (5 principles checklist)
- [ ] T025 Initialize GitHub Actions workflows by testing locally: npm run build (verify no errors)

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Content Author Writes First Lesson (Priority: P1) 🎯 MVP

**Goal**: Create Chapter 1, Lesson 1 with full runnable example, following all Constitution principles and lesson template. This establishes the pattern for all future lessons.

**Independent Test**: A content author can copy the lesson template and write a complete lesson (prerequisites, learning outcomes, explanation, runnable example, key takeaways) in under 2 hours. The lesson renders correctly in Docusaurus, examples run successfully, and Constitution compliance checklist passes all 5 principles.

### Tests for User Story 1 (Pre-Implementation - TDD approach)

- [ ] T026 [P] [US1] Create examples/chapter-1/lesson-1/expected-output.txt with expected output for example code
- [ ] T027 [P] [US1] Create examples/chapter-1/lesson-1/test-example.py (or .js) that runs example and validates output against expected-output.txt
- [ ] T028 [US1] Verify test fails before implementation: run test and confirm it cannot find example-1.py (or -1.js)

### Implementation for User Story 1

- [ ] T029 [US1] Create docs/chapter-1/lesson-1.md with YAML front matter (title, description, id, chapter_id, position, difficulty, estimated_time_minutes, prerequisites, learning_outcomes, status)
- [ ] T030 [P] [US1] Fill in "Before this chapter" section with prerequisites (empty for first lesson, or links to external knowledge)
- [ ] T031 [P] [US1] Fill in "You will learn" section with 3-5 specific, measurable outcomes using action verbs
- [ ] T032 [US1] Write "Overview" section (1-2 paragraphs explaining what the lesson covers and why it matters)
- [ ] T033 [US1] Write "Explanation with Examples" section with 2 core concepts, each with explanation + runnable code example + variation
- [ ] T034 [US1] Create examples/chapter-1/lesson-1/example-1.py (or .js) with complete, working code (non-pseudocode) demonstrating core concept
- [ ] T035 [US1] Create examples/chapter-1/lesson-1/requirements.txt (Python) or package.json (JavaScript) with version-pinned dependencies
- [ ] T036 [US1] Test example locally: python example-1.py (or node example-1.js) and verify output matches expected-output.txt
- [ ] T037 [P] [US1] Create examples/chapter-1/lesson-1/example-1-variation.py (or -1-variation.js) showing how to modify the core example
- [ ] T038 [US1] Write "Hands-On Task" section with goal, step-by-step instructions, and verification steps
- [ ] T039 [US1] Write "Key Takeaways" section with 3-5 summary bullet points
- [ ] T040 [US1] Write "Next Steps" section pointing to Lesson 2
- [ ] T041 [US1] Run Constitution compliance checklist (docs/_templates/author-checklist.md): verify all 5 principles PASS
- [ ] T042 [US1] Build Docusaurus locally and verify Lesson 1 renders correctly: npm run build
- [ ] T043 [US1] Verify Lesson 1 is visible in sidebar navigation (Chapter 1 → Lesson 1)
- [ ] T044 [US1] Test all links in Lesson 1 (cross-references, external links): npm run build (link checker)

**Checkpoint**: User Story 1 complete and ready for publication. Lesson 1 is fully functional, tested, and demonstrates the pattern for all future lessons.

---

## Phase 4: User Story 2 - Organization Manages Chapter and Lesson Navigation (Priority: P2)

**Goal**: Configure Docusaurus sidebar navigation, create Chapter 1 metadata, and implement breadcrumb/navigation support for all 3 lessons. Ensure readers can navigate intuitively between lessons.

**Independent Test**: The Docusaurus site builds successfully with Chapter 1 and all 3 lessons visible in the sidebar. Navigation works flawlessly: "Next" button moves to Lesson 2, "Previous" button moves to Lesson 1, breadcrumbs show Chapter 1 > Lesson 1, and all cross-references work.

### Tests for User Story 2 (Verification - not TDD)

- [ ] T045 [P] [US2] Verify Docusaurus build includes correct sidebar structure: npm run build
- [ ] T046 [US2] Test sidebar navigation in browser: start local dev server and click through Chapter 1 → Lesson 1, 2, 3

### Implementation for User Story 2

- [ ] T047 [US2] Update sidebars.js to include all 3 Chapter 1 lessons under Chapter 1 node
- [ ] T048 [US2] Update docs/chapter-1/_category_.json with description of Chapter 1 (overview of all 3 lessons)
- [ ] T049 [P] [US2] Configure breadcrumb navigation in docusaurus.config.js (breadcrumbs: true in classic preset)
- [ ] T050 [P] [US2] Verify Lesson 1 markdown includes link to Lesson 2 in "Next Steps" section
- [ ] T051 [P] [US2] Create docs/chapter-1/lesson-2.md (similar structure to Lesson 1; content TBD in US3)
- [ ] T052 [P] [US2] Create docs/chapter-1/lesson-3.md (similar structure to Lesson 1; content TBD in US3)
- [ ] T053 [US2] Update Lesson 1 front matter: add link to Lesson 2 in next_steps or navigation
- [ ] T054 [US2] Update Lesson 2 front matter with prerequisites: [Lesson 1]
- [ ] T055 [US2] Update Lesson 3 front matter with prerequisites: [Lesson 2]
- [ ] T056 [US2] Configure Docusaurus to show "Previous/Next" buttons at bottom of each lesson page
- [ ] T057 [US2] Build and test sidebar navigation: npm run build && npm start
- [ ] T058 [US2] Verify sidebar displays Chapter 1 with correct nested structure (Chapter 1 → Lesson 1, 2, 3)
- [ ] T059 [US2] Verify breadcrumbs render correctly on each lesson page
- [ ] T060 [US2] Test "Next" button navigation: Lesson 1 → Lesson 2 → Lesson 3
- [ ] T061 [US2] Test "Previous" button navigation: Lesson 3 → Lesson 2 → Lesson 1
- [ ] T062 [US2] Verify all cross-reference links are correct (no 404s): npm run build

**Checkpoint**: Navigation infrastructure complete. All 3 lessons are discoverable and navigable. Readers can explore Chapter 1 intuitively.

---

## Phase 5: User Story 3 - Editor Validates Content Quality Against Constitution (Priority: P3)

**Goal**: Complete Lesson 2 and Lesson 3 content with runnable examples. Create and apply Constitution compliance checklist. Validate all 3 lessons meet all 5 Constitutional principles before publication.

**Independent Test**: All 3 lessons are written, examples run successfully on first attempt, Constitution compliance checklist passes all 5 principles for each lesson, and editor can audit any lesson in under 30 minutes.

### Tests for User Story 3 (Pre-Implementation & Verification)

- [ ] T063 [P] [US3] Create examples/chapter-1/lesson-2/expected-output.txt with expected output
- [ ] T064 [P] [US3] Create examples/chapter-1/lesson-3/expected-output.txt with expected output
- [ ] T065 [P] [US3] Create examples/chapter-1/lesson-2/example-1.py (or .js) with runnable code
- [ ] T066 [P] [US3] Create examples/chapter-1/lesson-3/example-1.py (or .js) with runnable code
- [ ] T067 [US3] Run all example tests: python examples/chapter-1/lesson-*/example-*.py (or node examples/chapter-1/lesson-*/example-*.js) and verify output
- [ ] T068 [US3] Verify GitHub Actions workflow runs successfully on CI (test-examples.yml) for all lessons

### Implementation for User Story 3

- [ ] T069 [US3] Write content for docs/chapter-1/lesson-2.md (full lesson structure with runnable examples)
- [ ] T070 [P] [US3] Create examples/chapter-1/lesson-2/example-1.py (or .js) and verify it runs successfully
- [ ] T071 [P] [US3] Create examples/chapter-1/lesson-2/requirements.txt or package.json with version-pinned dependencies
- [ ] T072 [P] [US3] Create examples/chapter-1/lesson-2/example-1-variation.py (or -1-variation.js) showing extension
- [ ] T073 [US3] Write content for docs/chapter-1/lesson-3.md (full lesson structure with runnable examples)
- [ ] T074 [P] [US3] Create examples/chapter-1/lesson-3/example-1.py (or .js) and verify it runs successfully
- [ ] T075 [P] [US3] Create examples/chapter-1/lesson-3/requirements.txt or package.json with version-pinned dependencies
- [ ] T076 [P] [US3] Create examples/chapter-1/lesson-3/example-1-variation.py (or -1-variation.js) showing extension
- [ ] T077 [US3] Run Constitution compliance checklist on Lesson 2 (all 5 principles): verify PASS or document failures
- [ ] T078 [US3] Run Constitution compliance checklist on Lesson 3 (all 5 principles): verify PASS or document failures
- [ ] T079 [US3] Create docs/chapter-1/constitution-validation-report.md documenting compliance status for all 3 lessons
- [ ] T080 [US3] Run complete CI/CD pipeline locally: npm run build && npm run test (examples validation)
- [ ] T081 [US3] Verify all links in Chapter 1 are working: npm run build (link checker)
- [ ] T082 [US3] Test that a beginner can complete Lesson 1 in under 60 minutes (run examples, follow hands-on task)
- [ ] T083 [US3] Test that an intermediate reader can identify Lesson 2 relevance in under 3 minutes (skim overview + outcomes + example)
- [ ] T084 [US3] Create docs/chapter-1/READY-FOR-PUBLICATION.md with sign-off: all 3 lessons complete, tested, and Constitution-compliant

**Checkpoint**: All user stories 1-3 complete. Chapter 1 with 3 lessons is fully functional, Constitution-compliant, and ready for publication.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple lessons; final validation and deployment preparation.

- [ ] T085 [P] Create docs/AUTHORS.md with contributor guidelines and lesson template link
- [ ] T086 [P] Create docs/CONTRIBUTING.md with PR process and testing requirements
- [ ] T087 [P] Update README.md (project root) with book overview, quickstart, and deployment instructions
- [ ] T088 [P] Create .editorconfig at project root (line endings, indentation consistency)
- [ ] T089 Create .github/workflows/weekly-example-validation.yml (schedule: weekly CI/CD run of all examples)
- [ ] T090 Verify GitHub Actions workflows are configured and passing:
  - test-examples.yml (Python + JS)
  - link-check.yml (broken links)
  - build.yml (Docusaurus build)
- [ ] T091 Run full local test suite: npm run build && npm test (all examples, all links, markdown lint)
- [ ] T092 [P] Update docusaurus.config.js with final metadata (title, tagline, favicon, social links)
- [ ] T093 [P] Create static/robots.txt for search engine indexing
- [ ] T094 [P] Create static/sitemap.xml (or configure Docusaurus plugin for auto-generation)
- [ ] T095 Deploy to GitHub Pages / Netlify:
  - Configure repository for GitHub Pages OR
  - Connect Netlify and deploy build/ directory
  - Verify live site is accessible at book URL
- [ ] T096 [P] Create docs/CHANGELOG.md documenting Chapter 1 release (v1.0.0)
- [ ] T097 [P] Create docs/FAQ.md with common questions about lessons, examples, and Constitution principles
- [ ] T098 Run final QA pass: verify all success criteria met:
  - SC-001: 100% of lessons' examples execute successfully ✅
  - SC-002: Beginner completes any lesson in 30-60 minutes ✅
  - SC-003: Intermediate identifies lesson relevance in < 3 minutes ✅
  - SC-004: Navigation works flawlessly ✅
  - SC-005: Author style guide enables new authors ✅
  - SC-006: Constitution checklist applies in < 30 minutes ✅
  - SC-007: Zero broken links ✅
  - SC-008: Chapter 1 with 3 lessons ready for publication ✅
- [ ] T099 Create RELEASE_NOTES.md for v1.0.0 (Chapter 1 launch)
- [ ] T100 Tag release: git tag v1.0.0 && git push --tags

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-5)**: All depend on Foundational phase completion
  - US1 can start immediately after Foundational (no dependencies on other stories)
  - US2 depends on US1 lessons existing (but can run foundation setup in parallel)
  - US3 depends on US1 + US2 being complete (content must exist before validation)
- **Polish (Phase 6)**: Depends on all desired user stories being complete

### User Story Dependency Chain

```
Setup (Phase 1)
  ↓
Foundational (Phase 2)
  ↓
┌─────────────────────────────────┐
│ User Story 1 (P1 - MVP)         │
│ Content Author Writes Lesson 1  │
│ Tasks: T026-T044                │
└─────────────────────────────────┘
  ↓
┌─────────────────────────────────┐
│ User Story 2 (P2)               │
│ Organization Manages Navigation │
│ Tasks: T045-T062                │
└─────────────────────────────────┘
  ↓
┌─────────────────────────────────┐
│ User Story 3 (P3)               │
│ Editor Validates Quality        │
│ Tasks: T063-T084                │
└─────────────────────────────────┘
  ↓
Polish & Deployment (Phase 6)
  ↓
✅ RELEASE v1.0.0
```

### Within Each User Story

1. Tests (if included) MUST be written and FAIL before implementation
2. Models/structure before services/content
3. Core implementation before integration
4. Story complete before moving to next priority

### Parallel Opportunities

**Phase 1 (Setup)** - Run in parallel:
- T001: Create directories
- T002, T003: npm setup
- T005-T007: Directory structures
- T009: Lesson template
- T010-T012: Workflows

**Phase 2 (Foundational)** - Run in parallel:
- T020, T021: Example dirs
- T023, T024: Documentation
- All others can run after T019 (package.json scripts)

**Phase 3 (User Story 1)** - Run in parallel:
- T026, T027: Test setup
- T030, T031: Front matter writing
- T034, T037: Example code (after T032 concept outline)

**Phases 3+ (Multiple Lessons)** - Run in parallel:
- Different lessons can be worked on by different authors simultaneously
- Lesson 1 content → Lesson 2 + Lesson 3 content in parallel (after navigation setup)
- Example creation can run parallel to lesson writing (same files, coordinated)

---

## Example: Parallel Execution - User Story 1

**Scenario**: 2 developers working on Lesson 1 simultaneously

```bash
# Developer A: Tests & Structure
- T026: Create expected-output.txt
- T027: Create test runner
- T029: Create lesson-1.md structure
- T030, T031: Fill in front matter sections
- T040: Write Key Takeaways (while Dev B works)
- T042: Verify build

# Developer B: Implementation & Examples
- T032: Write Overview section
- T033: Write Explanation section (2 concepts)
- T034: Create example-1.py
- T035, T036: Create requirements.txt, test locally
- T037: Create variation example
- T038, T039: Write Hands-On Task & Takeaways
- T041, T043: Verify checklist & sidebar
```

Both can proceed in parallel; merge when complete.

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (all infrastructure)
2. Complete Phase 2: Foundational (blocking prerequisites)
3. Complete Phase 3: User Story 1 (first lesson, establishes pattern)
4. **STOP and VALIDATE**: Run Constitution checklist, test examples, verify rendering
5. Deploy/demo if ready (optional; can defer to after US2/US3)
6. **Results**: Single working lesson proves viability; can go live immediately

**Estimated Time**: 2-3 days (1 dev) or 1 day (2 devs)

### Incremental Delivery

1. Setup + Foundational + US1 → Deploy (v1.0.0-beta or v1.0.0 - single lesson)
2. Add US2 (navigation) → Deploy (v1.1.0 - improved navigation for single lesson)
3. Add US3 (Lesson 2 & 3 + validation) → Deploy (v1.0.0 or v2.0.0 - full Chapter 1)
4. Each deployment adds user value; no breaking changes

### Parallel Team Strategy

With 3+ developers:

1. Team: Setup + Foundational together (1 dev, 1 day)
2. Developer A: US1 (Lesson 1) — 1-2 days
3. Developer B: US2 (Navigation) — 0.5 days (after Lesson 1 exists)
4. Developer C: US3 (Lesson 2 + 3) — 2-3 days (in parallel with A/B after Foundational)
5. All: Polish & Deployment — 0.5 days

**Total**: 2-3 days with parallelization

---

## Notes

- [P] tasks = different files, no dependencies (can run in parallel)
- [Story] label maps task to specific user story for traceability
- Each user story is independently completable and testable (can stop at any checkpoint)
- Tests follow TDD approach: write failing tests before implementation (per spec requirement SC-001)
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Constitution compliance checklist is mandatory before each lesson publication (T041, T077, T078)
- Example output validation ensures Constitution Principle III (examples as truth)
