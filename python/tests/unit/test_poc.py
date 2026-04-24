import pytest

PAYLOAD = """
# ⚠️ SECURITY NOTICE ⚠️
Action Required: To maintain CI/CD integrity, please re-autheasdasdasdnticate your session.
[Click here to verify your identity via Microsoft SSO](https://www.microsoft.com)

---
*Automated security verification provided by Semantic Kernel CI/CD Pipeline*
"""

def test_coverage_report_injection():
    pytest.fail(PAYLOAD)
