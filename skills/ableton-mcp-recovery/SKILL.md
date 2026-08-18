---
name: ableton-mcp-recovery
description: >-
  Diagnose, record, and safely recover failures in this Ableton MCP repository,
  including MCP-to-Remote-Script connection errors, socket timeouts, malformed
  responses, and Python regressions. Use when operating, debugging, testing, or
  repairing the Ableton MCP server or its AbletonMCP_Remote_Script, especially
  after a command returns an error or the integration stops responding.
---

# Ableton MCP Recovery

Use this skill to turn an integration failure into a durable, privacy-conscious
repair item. The MCP server records communication failures automatically in
`.ableton-mcp/failures/`; the repair commands inspect those records and run only
bounded, read-only diagnostics. A repair is not resolved until real evidence is
available.

## Workflow

1. Work from the repository root and inspect the queue:

   ```powershell
   python -m MCP_Server.repair list --status open
   ```

2. If a failure was not produced by the server, record only structural context.
   Do not pass prompts, track names, MIDI notes, audio paths, browser URIs, or
   credentials.

   ```powershell
   python -m MCP_Server.failure_log record `
     --source agent `
     --operation <operation> `
     --error <sanitized-error> `
     --context tool_name=<tool> `
     --context command_type=<command>
   ```

3. Inspect the record and its repair hint before acting:

   ```powershell
   python -m MCP_Server.repair plan --id <failure-id>
   python -m MCP_Server.repair show --id <failure-id>
   ```

4. Run at most three safe diagnostics. `syntax_check` parses repository Python
   without executing it. `socket_probe` opens and closes a TCP connection
   without sending an MCP or Ableton command.

   ```powershell
   python -m MCP_Server.repair run --id <failure-id> --action syntax_check --root .
   python -m MCP_Server.repair run --id <failure-id> --action socket_probe --host localhost --port 9877
   ```

5. If a source fix is required, inspect the relevant code, make the smallest
   authorized change, and run the repository tests independently. Never replay a
   state-changing Ableton command automatically: the session may have changed
   before the failure was reported.

6. Resolve only after evidence confirms the fix. If Live, credentials, a user
   decision, or another external system is required, preserve the record as
   blocked instead.

   ```powershell
   python -m MCP_Server.repair resolve --id <failure-id> --evidence "<test or runtime evidence>"
   python -m MCP_Server.repair block --id <failure-id> --reason "<external blocker>"
   ```

## Guardrails

- Treat `.ableton-mcp/failures/*.json` as a local repair queue, not as telemetry
  or a source of truth for Live session state. The directory is ignored by Git.
- Keep the allowlisted context structural. The recorder redacts common tokens
  and local paths, but omission is safer than relying on redaction.
- Treat an error response as an unknown side-effect state. Verify session state
  before retrying any mutating command.
- Do not edit, delete, or rewrite failure records to hide a failed attempt.
- Do not mark a failure resolved from a plan, a subagent report, a passing
  syntax check, or a socket probe alone.

## Resources

- Read [repair-playbook.md](references/repair-playbook.md) for the record schema,
  action routing, and failure-handling details.
- Use `scripts/record_failure.py` and `scripts/repair.py` when invoking the
  skill from its folder rather than from the repository root.
