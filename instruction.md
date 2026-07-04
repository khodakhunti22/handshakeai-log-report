Parse the Apache-style access log at `/app/access.log` and write a JSON report to `/app/report.json`.

Success criteria:

1. `/app/report.json` exists and contains a valid JSON object.
2. The JSON object has exactly these top-level keys: `total_requests`, `unique_ips`, and `top_path`.
3. `total_requests` is the number of nonblank log entries, and `unique_ips` is the number of distinct client IP addresses from the first field of each entry.
4. `top_path` is the request path that appears most often inside the quoted HTTP request line.
