# Task: diagnose the retry policy

A production incident report says transient upstream failures are causing request retries to amplify load. Inspect the implementation and fix the retry delay policy so it uses capped exponential backoff: attempt 0 has base delay, each subsequent attempt doubles it, and no delay exceeds max_delay. Preserve the public API. Reject negative attempt values and non-positive base/max delay. Do not edit tests to conceal failures.
