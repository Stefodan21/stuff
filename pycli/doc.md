# pycli documentation

## Purpose
This folder contains a small Python CLI task tracker prototype.

## Current decisions
- Tasks are stored in a local JSON file named `task.json`.
- The script should load or create task storage before any command logic runs.
- Task data is kept as a nested dictionary in memory, keyed by task id.
- The code uses only Python's standard library.

### Why these choices were chosen
- A local JSON file keeps the project simple, portable, and easy to inspect without extra dependencies.
- Initializing storage first prevents command code from failing when the file is missing.
- A nested dictionary gives faster search, update, and delete operations because task ids can be accessed directly.
- Using only the standard library keeps the script lightweight and easier to run on any machine with Python installed.

## Faster lookup option
If membership/search speed is the priority, use a nested dictionary keyed by task id instead of a plain list.

Example shape:

```python
tasks = {
	1: {
		"title": "Buy groceries",
		"description": "Milk, bread, eggs",
		"status": "Todo"
	},
	2: {
		"title": "Finish report",
		"description": "Prepare weekly summary",
		"status": "pending"
	}
}
```

### Why this is faster
- Looking up `tasks[1]` is direct, so membership checks are faster than scanning a list.
- It is a better fit when you need frequent search, update, or delete by task id.
- The tradeoff is that it is a little less natural than a JSON list if you want the file to stay human-readable.

## Startup flow
1. Start the script.
2. Run the storage initializer.
3. Create `task.json` if it does not exist.
4. Load existing tasks from disk.
5. Continue to command handling.

## Implementation notes
- Keep storage setup in a function so it is easy to call first.
- Keep file loading and recovery logic in one place.
- If the JSON file is invalid, reset to an empty task list and report the error.

## Open items
- Complete the command dispatcher for add, update, delete, and list actions.
- Decide on final status names and keep them consistent.
- Add examples for each command once the CLI behavior is finalized.
