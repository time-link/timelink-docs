# Timelink and AI agents

Since version 1.2.0, Timelink ships an
[MCP](https://modelcontextprotocol.io) server: a standard way for AI
agents — Claude, ZCode, and any MCP-compatible client — to operate
Timelink directly: list projects and databases, search people and
attributes, follow relations, and run the translate/import pipeline.

Agents are good Timelink users because Timelink is agent-friendly by
design: everything is a string id, dates are lexical strings,
vocabularies can be listed before filtering, and every query result
carries provenance back to the source line.

## In this section

* [The Timelink MCP server](mcp_server.md) — installation,
  configuration, the tool set, and how an agent session looks.

## Related

* [Timelink projects and project discovery](../reference/timelink_projects.md)
  — what `list_projects` sees, and the structural rules behind it.
* [How Timelink works](../introduction/system_overview.md) — the
  pipeline the agent tools expose (translate → import → explore).
