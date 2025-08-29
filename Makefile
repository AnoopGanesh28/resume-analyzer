run:
\tstreamlit run app/main_app.py

test:
\tpytest -q

format:
\trufflehog --version >/dev/null 2>&1 || true
\tpython -m pip install ruff black -q
\truff check .
\tblack .
