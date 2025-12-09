# Constitution Compliance Checklist: [Lesson Name]

**Purpose**: Validate that your lesson adheres to all 5 Constitutional principles before publishing

**Lesson**: [Lesson Title]
**Author**: [Your GitHub username]
**Date**: [Completion date]

---

## Principle I: Hands-On Learning First ✅

Every lesson, tutorial, and concept MUST include a working example that users can run immediately.

- [ ] Every concept has at least one runnable code example
- [ ] All examples are complete working code (NOT pseudocode or ellipses)
- [ ] Examples can be run within 5-10 minutes (including setup)
- [ ] All examples have been tested and verified locally before submission
- [ ] No "theory-only" sections exist; all theory is grounded in examples
- [ ] Examples include clear, helpful comments explaining key lines
- [ ] Expected output is shown for each example

**Issues Found**: (list any problems)
```
[None / describe issues]
```

---

## Principle II: Progressive Disclosure (Scaffolded Complexity) ✅

Content follows a graduated approach: foundational concepts first, advanced topics layered on top.

- [ ] Overview section is concise (1-2 pages max)
- [ ] Core concepts are explained before advanced variations
- [ ] Beginner section avoids framework internals and complexity
- [ ] Intermediate explanation reveals the "why" beneath the code
- [ ] Lesson builds naturally on prerequisites without requiring external research
- [ ] Complexity increases gradually within the lesson
- [ ] No sudden jumps from simple to complex concepts

**Issues Found**: (list any problems)
```
[None / describe issues]
```

---

## Principle III: Executable Examples as Canonical Truth ✅

Example code is the authoritative specification. If documentation conflicts with examples, fix the documentation.

- [ ] All example code has been tested and produces expected output
- [ ] Versions are explicitly stated (e.g., "python==3.11", "numpy==1.24.0")
- [ ] No outdated syntax or deprecated APIs are used
- [ ] No copy-paste errors in examples
- [ ] If documentation conflicts with examples, documentation has been corrected
- [ ] All external links in examples have been tested and work
- [ ] examples/ directory has matching code + requirements.txt + expected-output.txt

**Issues Found**: (list any problems)
```
[None / describe issues]
```

---

## Principle IV: Clear Prerequisites and Skill Expectations ✅

Every section explicitly states what users must already know and what they'll be able to do.

- [ ] "Before this chapter" section lists ALL required prior knowledge
- [ ] Prerequisites are either linked to previous lessons or explicitly marked [external]
- [ ] No hidden assumptions about what readers know
- [ ] Difficult terms are defined inline or linked to a glossary
- [ ] "You will learn" section has 3-5 specific, measurable outcomes
- [ ] Learning outcomes use action verbs (create, build, explain, deploy)
- [ ] Learning outcomes are testable (not vague like "understand")
- [ ] Estimated time to complete is realistic and accurate

**Issues Found**: (list any problems)
```
[None / describe issues]
```

---

## Principle V: Modular Documentation (Topic Independence) ✅

Each documentation unit must be self-contained and independently testable.

- [ ] This lesson can be completed independently (given prerequisites)
- [ ] Cross-references use explicit links (not "see the section above")
- [ ] No "read chapters 1-7 first" requirements
- [ ] Lesson is discoverable via search (title/description are clear)
- [ ] Related lessons are linked in "Next steps" section
- [ ] Lesson doesn't assume knowledge of future lessons
- [ ] Sidebar navigation shows this lesson in correct hierarchy

**Issues Found**: (list any problems)
```
[None / describe issues]
```

---

## Quality Checks 📋

### Content Quality

- [ ] No spelling or grammar errors
- [ ] Markdown lints without errors
- [ ] Writing is clear and concise (8th-grade reading level)
- [ ] Active voice used (not passive)
- [ ] Reader is addressed as "you"
- [ ] Tone is encouraging and inclusive

### Technical Quality

- [ ] All code is properly formatted with syntax highlighting
- [ ] Code blocks include `title` and `showLineNumbers` attributes
- [ ] All links (internal and external) work
- [ ] No 404 or broken link errors
- [ ] File paths in examples are correct
- [ ] Command-line examples are accurate and tested

### Lesson Structure

- [ ] Has YAML front matter (title, description, sidebar_position, id)
- [ ] Has "Before this chapter" section with prerequisites
- [ ] Has "You will learn" section with 3-5 outcomes
- [ ] Has "Overview" section (1-2 paragraphs)
- [ ] Has "Explanation with Examples" section (2+ concepts)
- [ ] Has "Hands-On Task" section with goal, instructions, verification
- [ ] Has "Key Takeaways" section (3-5 points)
- [ ] Has "Next Steps" section with links to follow-up content

---

## Final Verification 🎯

### Testing

- [ ] Ran all examples locally and verified output
- [ ] Examples complete in advertised time
- [ ] Hands-on task can be completed by target audience
- [ ] All links are working (internal and external)
- [ ] Docusaurus builds without errors: `npm run build`
- [ ] Lesson renders correctly in browser

### Constitutional Compliance

- [ ] Principle I: Hands-On Learning ✅
- [ ] Principle II: Progressive Disclosure ✅
- [ ] Principle III: Executable Examples ✅
- [ ] Principle IV: Clear Prerequisites ✅
- [ ] Principle V: Modular Design ✅

### Ready for Review

- [ ] All checklists above are complete
- [ ] No outstanding issues
- [ ] Lesson is ready for editor/QA review

---

## Sign-Off

- **Author**: [Your name]
- **Date Completed**: [Date]
- **Status**: ⬜ Draft / ⏳ Review / ✅ Approved
- **Reviewer**: [Editor/QA name] (leave blank until review)
- **Review Date**: (leave blank until review)

---

## Notes

```
[Add any additional notes or context for reviewers]

Example:
- Examples tested with Python 3.11.7 and 3.12.0
- External links verified on 2025-12-09
- Audience feedback: [feedback if available]
```

---

## Questions?

If any item above is unclear:
1. Review the [Style Guide](./style-guide.md)
2. Check the [Lesson Template](./lesson-template.md)
3. Open an issue: https://github.com/physical-ai/book/issues

---

**Remember**: Every checkbox must be ✅ before publication. If you check a box and then discover an issue, uncheck it and fix the issue.

**Quality over speed** — A lesson that passes this checklist will help thousands of learners. Thank you for your care and attention to detail!
