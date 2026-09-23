# flaky-demo

A small, deliberately imperfect test suite that exists to generate **real**
flaky-test data for [flaky-detector](../flaky-detector) — a tool that detects
flaky tests from CI history. Every push here runs the suite and uploads the
JUnit report to a flaky-detector project.

## What's flaky here, on purpose

| Test | Behavior |
|---|---|
| `test_search.py::test_results_load_in_time` | Fails ~25% of runs (simulated slow page load) |
| `test_payments.py::test_webhook_delivery` | Fails ~15% of runs (simulated flaky webhook) |
| `test_cart.py::test_checkout` | Fails ~6% of runs (simulated race condition) |
| `test_profile.py::test_avatar_upload` | Fails **every** run — broken, not flaky, and the dashboard should tell the two apart |
| everything else | Always passes |

No random seed is fixed, so real variance shows up across separate CI runs,
the same way it would in a real project's test suite.

## Setup

1. Create a project at your flaky-detector deployment and copy its token.
2. In this repo's Settings → Secrets and variables → Actions:
   - Secret `FLAKY_DETECTOR_TOKEN` = the project token
   - Variable `FLAKY_DETECTOR_URL` = the deployed backend's base URL (no trailing slash)
3. Push a commit. Check the Actions tab, then the flaky-detector dashboard for this project.