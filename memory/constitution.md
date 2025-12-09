<!--
SYNC IMPACT REPORT
==================
Version: 1.0.0 (new) → 1.0.0
Principles Added (5): Hands-On Learning First, Progressive Disclosure, Executable Examples, Clear Prerequisites, Modular Documentation
Sections Added: Technology Stack Requirements, Content Quality Standards, Development Workflow
Templates requiring updates:
  - spec-template.md: ✅ (no changes needed, aligns with progressive learning)
  - plan-template.md: ✅ (no changes needed, aligns with modular structure)
  - tasks-template.md: ✅ (no changes needed, aligns with learning phases)
Follow-up: None - all placeholders resolved
-->

# Physical-AI Constitution

## Core Principles

### I. Hands-On Learning First

Every lesson, tutorial, and concept MUST include a working example that users can run immediately. The principle of "learn by doing" is non-negotiable.

- Users must be able to replicate every concept within 5 minutes of reading
- All examples MUST be runnable code (not pseudocode)
- Examples progress from simple to complex, building skills incrementally
- No theory-only sections; theory must be grounded in practical application
- Rationale: Beginner learners retain 70% more through hands-on practice; intermediate learners expect immediate applicability

### II. Progressive Disclosure (Scaffolded Complexity)

Content follows a graduated approach: foundational concepts first, advanced topics layered on top. Users see only what they need to know at each stage.

- Core concept (1-2 pages) → Basic example (runnable) → Extended variations → Advanced patterns
- Beginner section must omit framework internals; intermediate section reveals the "why" beneath
- Each chapter builds on previous chapters without requiring external knowledge
- Rationale: Cognitive overload is the primary barrier to beginner adoption; scaffolding increases completion rates

### III. Executable Examples as Canonical Truth

Example code is the authoritative specification. If documentation and examples conflict, the examples are the source of truth and the text must be corrected.

- Every code example MUST be tested and verified to work end-to-end
- Examples use realistic (but minimal) datasets or scenarios
- No copy-paste errors, outdated syntax, or framework version mismatches
- Rationale: Users trust what they can run; broken examples destroy credibility faster than any text error

### IV. Clear Prerequisites and Skill Expectations

Every section explicitly states what users must already know and what they will be able to do upon completion.

- "Before this chapter" section lists required prior knowledge (e.g., "know how to navigate the CLI")
- "You will learn" section lists 3-5 concrete deliverables (e.g., "deploy a model to the cloud")
- No hidden assumptions; explain domain-specific terms on first use or link to prerequisite content
- Rationale: Clear paths reduce frustration and increase confidence; users can self-assess readiness

### V. Modular Documentation (Topic Independence)

Each documentation unit (tutorial, concept page, API reference) must be self-contained and testable as a unit. Users can jump to any section and still succeed.

- Topics are organized by user task, not by framework structure
- Cross-references are explicit (e.g., "See: [Setting up your environment] for details")
- No "read chapters 1-7 first" requirements; each module assumes readers may start anywhere
- Rationale: Modern learners browse non-linearly; modularity supports discoverability and search-friendliness

## Technology Stack Requirements

- **Documentation Framework**: Docusaurus 3.x (React + MDX)
- **Example Languages**: Python, JavaScript/Node.js, or both (to be specified per feature)
- **Version Control**: Git; all examples tagged with framework/library versions
- **Hosting**: Static site (GitHub Pages, Netlify, or Vercel)
- **CI/CD**: Example code snippets must pass automated validation (e.g., linting, runtime tests)
- **Search & Discovery**: Full-text indexing via Algolia or Docusaurus built-in; no broken links

## Content Quality Standards

### Clarity & Accessibility
- Aim for 8th-grade reading level where possible; use short sentences
- Minimize jargon; define domain terms inline or via inline glossary tooltips
- Use active voice and second person ("you") to address readers directly

### Completeness & Accuracy
- Every example works end-to-end; tested before publication
- Error messages and edge cases are documented with clear resolution paths
- Code follows project linting and style conventions exactly

### Engagement & Motivation
- Each tutorial opens with a compelling "Why this matters" statement
- Intermediate sections include "Next steps" and pointers to advanced resources
- Success celebrations: prompt users to share results (e.g., "Tweet your first model!")

## Development Workflow

### Documentation Creation
1. **Plan**: Author identifies user journey and priority (P1/P2/P3 based on audience need)
2. **Spec**: Write prerequisites, learning outcomes, and acceptance scenarios using `/sp.specify`
3. **Outline**: Create example code first; outline text to explain the example
4. **Draft**: Write content, embed/test executable examples
5. **Review**: Peer review for clarity, accuracy, and hands-on testability
6. **Publish**: Merge to main, deploy via CI/CD

### Example Code Management
- All examples live in `/examples/` or inline in content with run instructions
- Examples are version-pinned (e.g., `numpy==1.21.0`) and tested against pinned versions
- CI pipeline runs all examples weekly to catch breakage early
- Rationale: Prevents the "works in my environment" problem

## Governance

- Constitution supersedes all style guides and process documents
- All PRs must verify compliance with Core Principles (especially Executable Examples and Progressive Disclosure)
- Content decisions that violate principles must be explicitly justified and documented as ADRs
- Content review process checks: example code runs, prerequisites are clear, progressive structure is maintained
- Run `/sp.constitution` to propose amendments; amendments are tracked as PHRs in `history/prompts/constitution/`

**Version**: 1.0.0 | **Ratified**: 2025-12-09 | **Last Amended**: 2025-12-09
