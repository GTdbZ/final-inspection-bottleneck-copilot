# Agent Instructions & Guidelines

This document outlines the context, rules, and guidelines for AI agents working on the Final Inspection Bottleneck Copilot project.

## Project Goal
Build a manufacturing analytics assistant using synthetic final-inspection data to identify bottleneck stations, defect trends, waiting-time issues, and suggested next actions.

## Hard Constraints
- **Confidentiality:** Do not use confidential company data, real customer names, real part numbers, internal factory reports, or real company files.
- **Data Source:** Use only synthetic mock data.
- **Environment:** Do not install MCP servers. Do not deploy anything. Do not create or use API keys.
- **Scope:** Do not modify files outside the current workspace.

## Static Context
- **Project Structure:**
  - `docs/AGENTS.md`: Agent behavior rules and project constraints.
  - `docs/data_schema.md`: Definition of fields in the final inspection dataset.
  - `docs/project_brief.md`: Project summary, goals, and workflow context.
  - `mock_data/final_inspection_sample.csv`: Synthetic dataset containing final-inspection records.
- **Inspection Stations:**
  - `FI-AOI` (Automated Optical Inspection)
  - `FI-VI` (Visual Inspection)
  - `FI-Packing` (Final Packing)
  - `FI-Recheck` (Quality Recheck)
- **Defect Types:**
  - `scratch`, `contamination`, `open_short`, `label_error`, `dimension_ng`, `cosmetic_ng`

## Dynamic Context
- Any analytical scripts (e.g., pandas Jupyter notebooks, Python scripts) added to the repository should leverage the schema defined in `docs/data_schema.md` and read from `mock_data/final_inspection_sample.csv`.
- Future extensions may include local dashboards (e.g., Streamlit) or reporting scripts.

## Guardrails
- **Data Integrity:** Never append real production data to the CSV files. All modifications to mock data must adhere to the synthetic format.
- **Security:** Do not check in any API keys, credentials, or sensitive environmental variables.
- **System Boundaries:** Any operations must run locally. Do not attempt external API integrations or cloud deployments.

## Preferred Workflow
1. **Analyze:** Inspect existing data schema and mock data files.
2. **Prototype:** Create isolated Python scripts or notebooks for data analysis.
3. **Verify:** Test code locally with the synthetic dataset.
4. **Document:** Keep documentation, walkthroughs, and schema updated.
