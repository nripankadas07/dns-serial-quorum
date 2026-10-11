# Runnable demo

```bash
python demo.py
python dns_serial_quorum.py example.json
```

`demo.py` checks a synthetic success and malformed-input rejection. The installed command uses the same arguments.

## Input contract

```text
{
  "expected": 0,
  "required": 2,
  "observations": [
    {
      "server": "ns1",
      "serial": 0
    },
    {
      "server": "ns2",
      "serial": 4294967295
    },
    {
      "server": "ns3",
      "serial": 0
    },
    {
      "server": "ns4",
      "serial": null
    }
  ]
}
```

Inspect `test_contract.py` for independently specified expected outcomes, including boundary failures. No live DNS queries, DNSSEC verification, TTL or propagation-time inference. Input is a single manually supplied authoritative-server snapshot. Server labels are asserted unique, not verified identities. RFC 1982 half-range ordering is undefined; ahead does not count as expected equality.
