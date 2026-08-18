# Ableton MCP repair playbook

## Record shape

Each failure is one JSON file named by its generated `id`:

```json
{
  "schema_version": 1,
  "id": "<uuid-hex>",
  "created_at": "<UTC timestamp>",
  "source": "mcp_server",
  "operation": "send_command",
  "error_type": "TimeoutError",
  "message": "<bounded and sanitized message>",
  "context": {
    "command_type": "get_session_info",
    "host": "localhost",
    "port": 9877,
    "timeout_seconds": 10.0
  },
  "status": "open",
  "attempts": 0,
  "repair": {
    "strategy": "connection",
    "safe_actions": ["socket_probe", "syntax_check"],
    "requires_user_action": true
  }
}
```

The recorder keeps an allowlist of structural context keys. It does not retain
the original user prompt, arbitrary parameters, MIDI notes, track or clip names,
audio file paths, browser URIs, or credentials. Runtime records are local and
best effort; a logging failure must never replace the original MCP error.

## Action routing

| Signal | First safe action | What it proves |
|---|---|---|
| connect, socket, timeout, broken pipe | `socket_probe` | The configured TCP endpoint accepts a connection; it does not prove Live state or command success. |
| JSON, response, protocol | `syntax_check` | Repository Python parses; inspect the wire path before retrying. |
| track, clip, browser, Live API | `syntax_check` | Repository Python parses; inspect the current Live session before replaying. |
| anything else | `syntax_check` | There is no automatic repair assumption. |

Each failure allows three repair attempts. An attempt records its action,
timestamp, result, and bounded details in the same JSON record. The diagnostics
are intentionally read-only. Fixing source code, restarting Live, or retrying a
state-changing command remains an explicit operator decision.

## Resolution rules

Use `resolve` only when evidence is concrete, such as a passing unit test plus a
real MCP smoke test. Use `block` when the next step depends on Ableton Live,
another machine, credentials, or human listening. Keep the original record and
its repair history in both cases.
