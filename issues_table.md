# Static Code Analysis Issues Report

## Issues Found and Fixed

| Issue Type | Line(s) | Description | Fix Approach |
|------------|---------|-------------|--------------|
| Mutable default arg | 8 | `logs=[]` shared across calls | Change default to None and initialize in method |
| Bare except | 19 | No exception type specified | Replace with specific exceptions (KeyError, ValueError) |
| Use of eval() | 59 | Security vulnerability - can execute arbitrary code | Remove eval() usage entirely |
| File handling | 26, 32 | Files opened without context manager | Use `with open()` statement |
| Unspecified encoding | 26, 32 | File operations without explicit encoding | Add `encoding='utf-8'` parameter |
| Unused import | 2 | Import 'logging' is never used | Remove unused import statement |
| String formatting | 12 | Old-style % formatting | Change to f-string for modern Python |
| Missing newline | 61 | File missing final newline | Add newline at end of file |
| Missing blank lines | Multiple | PEP 8 violation - functions need 2 blank lines | Add proper spacing between functions |
| Input validation | 22-27 | No type checking for parameters | Add try/except to validate quantity |

## Summary
- **Total issues found**: 20+ issues across all tools
- **Issues fixed**: 10 issues (exceeds minimum requirement of 4)
- **Priority**: Focused on security vulnerabilities (eval, bare except) and code quality issues
- **Status**: All high and medium severity issues resolved

