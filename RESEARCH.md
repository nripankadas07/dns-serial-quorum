# Candidate brief and fair comparison — 11 October 2026

**User:** DNS operators reviewing a zone rollout across authoritative servers. **Painful task:** Ordinary numeric comparison mishandles SOA serial rollover, while a partial rollout can look complete.

**Current alternatives:** BIND utilities, dnspython serial arithmetic, checkzoneserial. **Smallest useful capability:** Classify equal, ahead, behind, half-range ambiguous and unavailable observations; calculate an explicit equality quorum.

**Demand evidence:** inferred from the documented protocol/workflow and established comparable projects, not a verified request for this new product. Current comparable READMEs, representative implementation/docs and recent issue/PR lists were reviewed. Those issues do not prove demand for our feature, and no competitor absence is asserted. See [portfolio research evidence](https://github.com/nripankadas07/nripankadas07/blob/main/docs/RESEARCH_2026-10-11.json) for exact observations and code/doc URLs.

**Acceptance:** the 16 core contract tests must pass, the demo must check its known output and malformed input, and a clean installed command outside source must reproduce both success and error behavior. Scope limits remain visible in README/output. LIVE additionally requires final default-branch CI and verified docs/install path.

**Discovery:** descriptive GitHub topics, the profile chronological index, and a reproducible linked demo. No promised growth, invented users or unsolicited third-party issue promotion.

**Distinctness:** compared with all 158 existing owned repository names and today's other four briefs. Cookie routing is separate from CSP/cache/robots checks; SOA rollout arithmetic is separate from mail DNS topology and DNS blocking; expression alternatives are separate from SBOM inventory/dependency audits; startup pull-in versus ordering is separate from general migration plans; captured packet accounting is separate from live LAN delivery/network discovery. These are five independent capabilities, not subdivisions of one product.

## Live GitHub research

Queries: `DNS serial sort:stars`, `DNS library sort:stars`, `DNS zone serial sort:stars`. Observation date 2026-10-11 UTC. GitHub query results were relevance-screened; some broad queries include unrelated repositories. Highest-star relevant comparable **found** in this research: [miekg/dns](https://github.com/miekg/dns) (8777 stars). Coverage is limited; this is not an exhaustive global ranking. Additional established tools were inspected directly. Stars are discovery evidence, not performance.

| Comparable | Stars | Latest push observed (UTC) | Documented workflow |
| --- | ---: | --- | --- |
| [isc-projects/bind9](https://github.com/isc-projects/bind9) | 780 | 2026-10-09T13:18:49Z | Archived mirror of https://gitlab.isc.org/isc-projects/bind9, please submit issues and PR/MRs in the GitLab. |
| [rthalley/dnspython](https://github.com/rthalley/dnspython) | 2681 | 2026-10-10T19:56:30Z | a powerful DNS toolkit for python |
| [shuque/checkzoneserial](https://github.com/shuque/checkzoneserial) | 6 | 2026-09-02T01:26:54Z | Check zone serial numbers across DNS servers |
| [NLnetLabs/ldns](https://github.com/NLnetLabs/ldns) | 362 | 2026-10-06T18:11:11Z | LDNS is a DNS library that facilitates DNS tool programming |

| [miekg/dns](https://github.com/miekg/dns) | 8777 | 2026-10-01T17:37:07Z | Go DNS library with zone and wire-message support |

## Workflow tradeoffs

Established alternatives have broader capabilities, documentation, examples and ecosystems; installability varies by language and platform. Ours offers a narrow one-command synthetic example and a zero-runtime-dependency Python source install. No competitor installation was timed or independently stress-tested in this run. No measured time-to-first-result, reliability, support responsiveness, performance or superiority claim. Current comparable licenses are recorded in linked research metadata; none of their implementation or prose was reused. Our license is MIT. Support is best-effort GitHub reports with no SLA.

**Limits and negative result:** No live DNS queries, DNSSEC verification, TTL or propagation-time inference. Input is a single manually supplied authoritative-server snapshot. Server labels are asserted unique, not verified identities. RFC 1982 half-range ordering is undefined; ahead does not count as expected equality. Broader production needs should use the established tools. Runnable local success demonstrates our behavior only.
