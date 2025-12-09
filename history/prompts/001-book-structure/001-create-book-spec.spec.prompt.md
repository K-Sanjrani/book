---
id: 001
title: Create Physical-AI Book Specification
stage: spec
date: 2025-12-09
surface: agent
model: claude-haiku-4-5-20251001
feature: 001-book-structure
branch: master
user: user
command: /sp.specify
labels: ["spec", "book-structure", "content-organization", "docusaurus", "requirements"]
links:
  spec: specs/001-book-structure/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-book-structure/spec.md
  - specs/001-book-structure/checklists/requirements.md
  - history/prompts/001-book-structure/001-create-book-spec.spec.prompt.md
tests: []
---

## Prompt

Based on the constitution, create a detailed specification for a physical AI book including:
1. Book structure with 1 chapter and 3 lessons each (title and descriptions)
2. Content guidelines and lesson format
3. Docusaurus specific: requirements for organisation

## Response snapshot

Created feature specification for "Physical-AI Book Structure & Organization" (feature 001) with:

**3 User Stories** (P1 → P3):
- P1 (MVP): Content Author writes first lesson following template + Constitution principles → single self-contained, deployable lesson
- P2: Organization manages chapter/lesson navigation in Docusaurus → complete, navigable book structure
- P3: Editor validates content quality against Constitution → quality gates for long-term consistency

**10 Functional Requirements** covering lesson structure, prerequisites, learning outcomes, runnable examples, Docusaurus navigation, and validation tools

**8 Success Criteria** (all measurable, technology-agnostic):
- 100% of examples execute successfully on first attempt
- Beginner completes any lesson in 30-60 minutes without external research
- Intermediate reader identifies lesson relevance in < 3 minutes
- Zero broken links; flawless navigation
- Author style guide enables new authors without clarification questions
- Content Quality Checklist produces pass/fail in < 30 minutes
- First chapter ready for publication within sprint

**Lesson Template** with strict structure: Before this chapter → You will learn → Overview → Explanation with examples → Hands-on task → Key takeaways → Next steps

**Docusaurus Requirements**: File structure (docs/ hierarchy with `_category_.json`), YAML front matter (title, description, sidebar_position), MDX code blocks, cross-references, search metadata

**Edge Cases** documented: multi-chapter prerequisites, framework version breaking changes, out-of-order lesson navigation

**Assumptions**: 1 chapter × 3 lessons MVP, Python/JavaScript examples, beginner-to-intermediate audience, static hosting, weekly example testing

## Outcome

- ✅ Impact: Specification establishes authoritative requirement for book structure, content guidelines, and Docusaurus organization. Aligns with Constitution principles (hands-on learning, progressive disclosure, executable examples, clear prerequisites, modularity). Enables authors and editors to work independently with clear templates and validation checklists.
- 🧪 Tests: Specification Quality Checklist (requirements.md) passes all items: no missing clarifications, all requirements testable/unambiguous, success criteria measurable and technology-agnostic, scope bounded, edge cases identified. Ready for planning phase.
- 📁 Files: 2 files created (spec.md, requirements.md); feature directory structure established at `specs/001-book-structure/`
- 🔁 Next prompts: `/sp.plan` (architecture/content organization), `/sp.tasks` (implementation tasks for Chapter 1 + 3 lessons), `/sp.clarify` (if detail needed before planning)
- 🧠 Reflection: Specification tightly couples to Constitution principles; lesson template and content guidelines enforce Principle I (hands-on), Principle II (progressive disclosure), and Principle V (modularity) at spec level. Docusaurus requirements provide implementation direction without leaking tech specifics into spec. Three user stories enable MVP-first delivery: P1 lesson demonstrates viability; P2 navigation makes it discoverable; P3 validation ensures quality.

## Evaluation notes (flywheel)

- Failure modes observed: None—all requirements clear and testable. Constitution principles successfully translated into spec requirements. Lesson template is prescriptive enough to guide authors while flexible enough for varied topics.
- Graders run and results: Specification Quality Checklist: ALL PASS (8/8 categories)
- Prompt variant: None
- Next experiment: Proceed to `/sp.plan` to design content architecture, example repository structure, and CI/CD validation pipeline for runnable examples
