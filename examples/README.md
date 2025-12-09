# Runnable Examples for Physical AI Book

All code examples from the book are located here, organized by chapter and lesson.

## Structure

```
examples/
├── chapter-1/
│   ├── lesson-1/
│   │   ├── example-1.py          # Python example
│   │   ├── example-1.js          # JavaScript variant
│   │   ├── requirements.txt      # Python dependencies
│   │   ├── package.json          # Node.js dependencies
│   │   ├── expected-output.txt   # Expected output when code runs
│   │   └── README.md             # Lesson-specific notes
│   ├── lesson-2/
│   └── lesson-3/
└── ...
```

## Running Examples Locally

### Python Examples

```bash
# Navigate to lesson directory
cd examples/chapter-1/lesson-1

# Install dependencies (if needed)
pip install -r requirements.txt

# Run the example
python example-1.py
```

### JavaScript Examples

```bash
# Navigate to lesson directory
cd examples/chapter-1/lesson-1

# Install dependencies
npm install

# Run the example
node example-1.js
```

## Testing All Examples

### Test Python Examples

```bash
#!/bin/bash
for chapter_dir in chapter-*/; do
  for lesson_dir in "$chapter_dir"lesson-*/; do
    cd "$lesson_dir"
    echo "Testing $lesson_dir..."

    if [ -f "requirements.txt" ]; then
      pip install -r requirements.txt
    fi

    python example-*.py > /tmp/output.txt 2>&1

    if diff -q /tmp/output.txt expected-output.txt; then
      echo "✅ PASS"
    else
      echo "❌ FAIL"
    fi

    cd - > /dev/null
  done
done
```

### Test JavaScript Examples

```bash
#!/bin/bash
for chapter_dir in chapter-*/; do
  for lesson_dir in "$chapter_dir"lesson-*/; do
    cd "$lesson_dir"
    echo "Testing $lesson_dir..."

    if [ -f "package.json" ]; then
      npm ci
    fi

    node example-*.js > /tmp/output.txt 2>&1

    if diff -q /tmp/output.txt expected-output.txt; then
      echo "✅ PASS"
    else
      echo "❌ FAIL"
    fi

    cd - > /dev/null
  done
done
```

## CI/CD Validation

All examples are automatically tested via GitHub Actions:

- **test-examples.yml**: Runs weekly + on every PR
- Tests Python 3.11 and 3.12
- Tests Node.js 18 and 20
- Validates output against expected-output.txt
- Enforces 30-second timeout per example

## Version Management

Examples are version-pinned to ensure reproducibility:

### Python

Lock specific package versions in `requirements.txt`:

```
numpy==1.24.0
tensorflow==2.13.0
pandas==2.0.0
```

Create/update via:

```bash
pip install numpy==1.24.0 tensorflow==2.13.0
pip freeze > requirements.txt
```

### JavaScript

Lock specific package versions in `package-lock.json`:

```bash
npm install express@4.18.2 axios@1.6.0
```

Commit `package-lock.json` to repo to lock versions.

## Reporting Issues

If an example doesn't work:

1. **Check the lesson**: Verify prerequisites are met
2. **Test locally**: Run the example and check output
3. **Report**: Open an issue with:
   - Lesson name
   - Example name
   - Python/Node.js version
   - Error message
   - Expected vs. actual output

## Contributing Examples

When adding a new example:

1. **Create a runnable example**:
   ```bash
   mkdir -p examples/chapter-X/lesson-Y
   cd examples/chapter-X/lesson-Y
   ```

2. **Write complete, working code**:
   ```bash
   cat > example-1.py << 'EOF'
   # Your code here
   EOF
   ```

3. **Add dependencies**:
   - Python: Create `requirements.txt`
   - Node.js: Create `package.json` and commit `package-lock.json`

4. **Record expected output**:
   ```bash
   python example-1.py > expected-output.txt
   ```

5. **Test locally**:
   ```bash
   python example-1.py
   # Verify output matches expected-output.txt
   ```

6. **Commit all files**:
   ```bash
   git add examples/chapter-X/lesson-Y/
   git commit -m "feat: add chapter-X lesson-Y examples"
   ```

## Questions?

- Review the [Lesson Template](../docs/_templates/lesson-template.md)
- Check the [Style Guide](../docs/_templates/style-guide.md)
- Open an issue: https://github.com/physical-ai/book/issues
