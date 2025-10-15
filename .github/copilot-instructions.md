# Copilot Instructions for AI Coding Agents

## Project Overview
This repository contains Python exercises and modules for studying computer science, AI, and ML at the master's level. The structure is organized by course modules and homework assignments.

## Directory Structure
- `My_Python_course/` — Main folder for course content
  - `goit-pycore-hw-03/` — Homework assignments (e.g., `01_get_days_from_today.py`)
  - `module1/`, `module3/`, `module4/` — Thematic modules with scripts and utilities
- Each module contains scripts for specific topics (e.g., date calculations, phone normalization, time zones).

## Key Patterns & Conventions
- Each script is self-contained and typically solves a single problem or demonstrates a concept.
- Naming: Filenames use a pattern like `NN_description.py` for clarity (e.g., `03_normalize_phone.py`).
- No central entrypoint; scripts are run individually.
- Minimal external dependencies; standard library is preferred.
- No formal test suite or build system is present.

## Developer Workflows
- **Run scripts:** Execute any script directly with `python <script.py>` from its directory.
- **Debugging:** Add print statements or use Python debuggers (e.g., `pdb`).
- **Adding new exercises:** Place new scripts in the relevant module or homework folder, following the existing naming convention.

## Integration & Data Flow
- Scripts are independent; there is no cross-module import or shared state.
- If you need to share code, create a utility file (e.g., `deffunc.py`) and import functions as needed within the same module.

## Examples
- See `My_Python_course/goit-pycore-hw-03/03_normalize_phone.py` for input normalization patterns.
- See `My_Python_course/module4/timezone_time.py` for time zone handling.

## AI Agent Guidance
- Prefer clear, concise, and well-commented code.
- Follow the established file naming and organization patterns.
- Do not introduce frameworks or complex dependencies unless required by the exercise.
- When in doubt, mimic the style and structure of existing scripts in the target folder.

---
For questions or unclear conventions, review the most similar script in the relevant folder and follow its approach.
