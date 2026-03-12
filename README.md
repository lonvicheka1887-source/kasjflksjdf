# Python Starter Template

Repository នេះត្រូវបានរៀបចំជា **Python starter** មួយសម្រាប់ចាប់ផ្តើម project ថ្មី យ៉ាងស្រាល និងងាយពង្រីក។

## Structure

```text
.
├── .gitignore
├── Makefile
├── README.md
├── pyproject.toml
├── src/
│   └── app/
│       ├── __init__.py
│       └── main.py
└── tests/
    └── test_main.py
```

## Quick start

```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
python3 -m src.app.main
```

## What this starter gives you

- `src/` layout សម្រាប់បំបែក application code ចេញពី tooling/testing.
- Test example ដំបូង (`unittest`) ដែលមិនពឹង dependency ខាងក្រៅ។
- `Makefile` ដើម្បី standardize command ប្រចាំថ្ងៃ (`make test`, `make run`).
- `pyproject.toml` ជាគន្លឹះសម្រាប់ metadata និង tooling ក្រោយៗ។

## Suggested first PR plan

សូមមើលឯកសារ `docs/PR_PLAN.md` សម្រាប់ផែនការ PR ជាជំហានៗ (PR #1 → PR #4)។
