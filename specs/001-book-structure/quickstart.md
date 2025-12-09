# Quickstart: Building & Contributing to the Physical-AI Book

**Purpose**: Get started with local development, adding lessons, and testing examples

## Prerequisites

- **Node.js**: 18 LTS (18.17.0+) or 20 LTS ([download](https://nodejs.org/))
- **npm**: 9+ (usually bundled with Node.js)
- **Git**: For version control ([download](https://git-scm.com/))
- **Code Editor**: VS Code, Sublime, or your favorite editor
- **Python** (optional): 3.11+ if writing Python examples

**Verify Installation**:

```bash
node --version      # Should be v18.x.x or v20.x.x
npm --version       # Should be 9.x.x or higher
git --version       # Should be 2.x.x or higher
```

---

## 1. Local Setup (First Time)

### Step 1: Clone the Repository

```bash
git clone https://github.com/[your-org]/physical-ai-book.git
cd physical-ai-book
```

### Step 2: Install Dependencies

```bash
npm install
```

This installs Docusaurus, React, and all required packages listed in `package.json`.

### Step 3: Start Local Server

```bash
npm start
```

**Output**:
```
[INFO] Starting the development server...
[SUCCESS] Docusaurus website is running at http://localhost:3000/
```

Open your browser to **http://localhost:3000/** to see the site locally.

### Step 4: Hot Reload (Auto-Refresh)

Edit any `.md` file and save. Your browser automatically reloads—no manual refresh needed!

---

## 2. Project Structure Overview

```
book/
├── docs/                      # Lesson content (Markdown + MDX)
│   ├── intro.md              # Landing page
│   └── chapter-1/            # Chapter 1
│       ├── _category_.json    # Chapter metadata
│       ├── lesson-1.md
│       ├── lesson-2.md
│       └── lesson-3.md
│
├── examples/                 # Runnable example code
│   └── chapter-1/
│       ├── lesson-1/
│       │   ├── example-1.py
│       │   ├── requirements.txt
│       │   └── expected-output.txt
│       └── ...
│
├── static/                   # Static assets (images, etc.)
├── src/                      # Custom React components
├── docusaurus.config.js      # Main configuration
├── sidebars.js              # Navigation structure
├── package.json             # Dependencies
└── README.md

```

---

## 3. Adding Your First Lesson

### Step 1: Copy Lesson Template

```bash
cp docs/_templates/lesson-template.md docs/chapter-1/lesson-4.md
```

### Step 2: Edit Lesson Template

Open `docs/chapter-1/lesson-4.md` and fill in:

```markdown
---
title: "Your Lesson Title"
description: "One-line description for search"
sidebar_position: 4
---

# Your Lesson Title

## Before this chapter

**Prerequisites**:
- [ ] Complete [Chapter 1, Lesson 3](lesson-3.md)
- [ ] Understand the concept of [X]
- [ ] Install [Tool Y]

---

## You will learn

By the end of this lesson, you will be able to:

1. [Outcome 1]
2. [Outcome 2]
3. [Outcome 3]

---

## Overview

[2 paragraphs: What is this about? Why does it matter?]

---

## Explanation with Examples

### Core Concept 1: [Title]

[Explanation text]

\`\`\`python title="example-1.py" showLineNumbers
# [Description]
# Prerequisites: pip install [packages]

[Your working code here]
\`\`\`

**Expected output**:
\`\`\`
[What user should see]
\`\`\`

---

## Hands-On Task

**Goal**: [What you'll build]

**Instructions**:

1. [Step 1]
2. [Step 2]
3. [Step 3]

---

## Key Takeaways

- [Point 1]
- [Point 2]
- [Point 3]

---

## Next Steps

[Point to follow-up content]
```

### Step 3: Save & View Locally

1. Save the file (Ctrl+S or Cmd+S)
2. Browser automatically reloads at http://localhost:3000/
3. Click "Chapter 1" in sidebar to see your new lesson!

---

## 4. Adding Runnable Examples

### Python Example

**Step 1**: Create example directory

```bash
mkdir -p examples/chapter-1/lesson-1
cd examples/chapter-1/lesson-1
```

**Step 2**: Create `example-1.py`

```python
# example-1.py: Calculate sum of squares
# Prerequisites: None (Python built-in only)

def sum_of_squares(n):
    """Return sum of squares from 1 to n."""
    return sum(i**2 for i in range(1, n+1))

# Test
result = sum_of_squares(5)
print(f"Sum of squares 1-5: {result}")
```

**Step 3**: Create `requirements.txt`

```
# requirements.txt (empty if no external dependencies)
# numpy==1.24.0
# tensorflow==2.13.0
```

**Step 4**: Create `expected-output.txt`

```
Sum of squares 1-5: 55
```

**Step 5**: Test locally

```bash
cd examples/chapter-1/lesson-1
python example-1.py
# Output should match expected-output.txt
```

### JavaScript Example

**Step 1**: Create `example-1.js`

```javascript
// example-1.js: Calculate sum of squares
// Prerequisites: Node.js 18+

function sumOfSquares(n) {
  let sum = 0;
  for (let i = 1; i <= n; i++) {
    sum += i * i;
  }
  return sum;
}

const result = sumOfSquares(5);
console.log(`Sum of squares 1-5: ${result}`);
```

**Step 2**: Create `package.json` (if using npm packages)

```json
{
  "name": "lesson-example",
  "version": "1.0.0",
  "description": "Physical AI lesson example",
  "main": "example-1.js",
  "engines": {
    "node": ">=18.0.0"
  }
}
```

**Step 3**: Create `expected-output.txt`

```
Sum of squares 1-5: 55
```

**Step 4**: Test locally

```bash
cd examples/chapter-1/lesson-1
node example-1.js
# Output should match expected-output.txt
```

---

## 5. Embedding Examples in Lessons

In your lesson Markdown, reference the example:

```markdown
## Explanation with Examples

### Core Concept: Sum of Squares

Calculating sums of sequences is a fundamental programming skill.

\`\`\`python title="examples/chapter-1/lesson-1/example-1.py" showLineNumbers
# This code demonstrates calculating the sum of squares.
# You can find and run the full example in our examples/ directory.

def sum_of_squares(n):
    return sum(i**2 for i in range(1, n+1))

result = sum_of_squares(5)
print(f"Sum of squares 1-5: {result}")
\`\`\`

**Expected output**:
\`\`\`
Sum of squares 1-5: 55
\`\`\`

**To run locally**:
\`\`\`bash
cd examples/chapter-1/lesson-1
python example-1.py
\`\`\`
```

---

## 6. Running Constitution Compliance Checklist

### Before Submitting a Lesson

1. Open `specs/001-book-structure/checklists/constitution.md`
2. Fill in the checklist for your lesson:

```markdown
# Constitution Compliance Checklist: [Your Lesson Name]

## Principle I: Hands-On Learning First
- [x] Every concept has at least one runnable code example
- [x] Examples are complete working code (not pseudocode)
- [x] Examples can be run within 5-10 minutes
- [x] All examples tested and verified
- [x] No "theory-only" sections

## Principle II: Progressive Disclosure
- [x] Overview is concise (1-2 pages)
- [x] Core concepts explained before advanced variations
- [x] Lesson builds on prerequisites
- ...
```

3. If all items pass ✅, your lesson is ready to submit!

---

## 7. Testing Examples (CI/CD)

### Run All Examples Locally (Python)

```bash
cd examples/chapter-1
for dir in lesson-*/; do
  cd "$dir"
  pip install -r requirements.txt
  python example-*.py > /tmp/output.txt 2>&1
  diff /tmp/output.txt expected-output.txt
  if [ $? -eq 0 ]; then
    echo "✅ $dir passed"
  else
    echo "❌ $dir failed"
  fi
  cd ..
done
```

### Run All Examples (JavaScript)

```bash
cd examples/chapter-1
for dir in lesson-*/; do
  cd "$dir"
  npm ci
  node example-*.js > /tmp/output.txt 2>&1
  diff /tmp/output.txt expected-output.txt
  if [ $? -eq 0 ]; then
    echo "✅ $dir passed"
  else
    echo "❌ $dir failed"
  fi
  cd ..
done
```

### GitHub Actions (Automatic)

Every pull request automatically:
- Runs all examples (Python + JavaScript)
- Validates links (internal + external)
- Lints Markdown
- Builds Docusaurus site

If any check fails, the PR shows a red ❌. Fix issues before merging!

---

## 8. Building for Production

### Generate Static Site

```bash
npm run build
```

**Output**:
```
[INFO] Generated static files in ./build
[SUCCESS] Docusaurus website built successfully!
```

This creates a `build/` directory with all HTML/CSS/JS ready for deployment.

### Deploy to GitHub Pages

```bash
npm run deploy
```

(Requires GitHub repo configuration; see `.github/workflows/deploy.yml`)

---

## 9. Creating a Pull Request

### Step 1: Create Feature Branch

```bash
git checkout -b chapter-1-lesson-4
```

### Step 2: Make Changes

Add/edit lessons and examples (see sections 3-5 above)

### Step 3: Commit Changes

```bash
git add docs/ examples/
git commit -m "feat: add chapter-1-lesson-4 with runnable examples

- Added hands-on lesson on [topic]
- Included Python and JavaScript examples
- Verified Constitution Principle compliance"
```

### Step 4: Push & Create PR

```bash
git push origin chapter-1-lesson-4
```

Go to GitHub and create a pull request. CI/CD runs automatically!

### Step 5: Address Review Comments

1. Reviewer suggests changes (e.g., "Example doesn't run")
2. Make edits locally
3. Commit: `git commit -m "fix: update example to use correct API"`
4. Push: `git push`
5. PR automatically updates

---

## 10. Troubleshooting

### Problem: `npm start` fails with "Cannot find module"

**Solution**:
```bash
rm -rf node_modules package-lock.json
npm install
npm start
```

### Problem: Python example fails with "ModuleNotFoundError"

**Solution**:
```bash
cd examples/chapter-1/lesson-1
pip install -r requirements.txt
python example-1.py
```

### Problem: JavaScript example fails silently

**Solution**:
```bash
cd examples/chapter-1/lesson-1
npm ci
node example-1.js
```

### Problem: Local site won't reload

**Solution**: Press Ctrl+C to stop `npm start`, then:
```bash
npm start
```

### Problem: How do I update external dependencies?

**For Python**:
```bash
pip install --upgrade numpy
pip freeze > requirements.txt
# Update lesson example version constraints
```

**For JavaScript**:
```bash
npm update
npm install  # Updates package-lock.json
# Update lesson example version constraints
```

---

## Quick Reference

| Task | Command |
|------|---------|
| Start local dev server | `npm start` |
| Build production site | `npm run build` |
| Test Python examples | `python example-1.py` |
| Test JavaScript examples | `node example-1.js` |
| Create new lesson | Copy `lesson-template.md` |
| Run all tests | `npm test` (via CI/CD) |
| Check links | `npm run check:links` |

---

## Next Steps

- ✅ Finish reading this Quickstart
- ✅ Set up local development (`npm install && npm start`)
- ✅ Copy and edit a lesson template (section 3)
- ✅ Create 1-2 runnable examples (section 4)
- ✅ Run Constitution checklist (section 6)
- ✅ Submit pull request (section 9)
- ✅ Celebrate! 🎉

**Questions?** Open an issue or ping the maintainers on GitHub.
