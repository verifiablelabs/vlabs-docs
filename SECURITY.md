# Security Policy

## Reporting a vulnerability

Please report suspected vulnerabilities **privately** to
**sdi2200243@di.uoa.gr**. Do not open public issues for security
reports.

## Scope notes

Public contributions must exclude hidden evaluation content, gold answers,
anti-hack detection details, private verifier logic, customer data, and secrets.
This is a disclosure rule, not a guarantee that a leak is impossible. If you
believe such material has leaked here, report it through the existing private
reporting route above.

## Hardening recommendations (maintainers)

- Branch protection on `main`: require pull requests, at least one review,
  and passing status checks; no force pushes.
- Enable **CodeQL** default setup and **Dependabot** alerts + security updates.
- Pin GitHub Actions to specific versions.
