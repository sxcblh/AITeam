import argparse
import os
import re
import subprocess
import sys
import tempfile


def _run_codex(prompt, repo_root, codex_home, unsafe):
    env = os.environ.copy()
    env["CODEX_HOME"] = codex_home

    output_file = tempfile.NamedTemporaryFile(delete=False, suffix=".txt")
    output_file.close()

    cmd = ["codex", "exec", "-C", repo_root, "-o", output_file.name]
    if unsafe:
        cmd.append("--dangerously-bypass-approvals-and-sandbox")
    cmd.append(prompt)

    subprocess.run(cmd, check=True, env=env)

    with open(output_file.name, "r", encoding="utf-8", errors="replace") as fh:
        text = fh.read()
    os.unlink(output_file.name)
    return text


def _extract_next_commands(text):
    lines = text.splitlines()

    # Prefer explicit marker if present.
    start_index = 0
    for i, line in enumerate(lines):
        if line.strip().upper().startswith("NEXT_COMMANDS"):
            start_index = i + 1

    tail = lines[start_index:] if start_index else lines[-80:]

    pattern = re.compile(r"^\s*[-*]?\s*/prompts:[^\s]+.*$")
    cmds = []
    in_code = False
    for line in tail:
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        if pattern.match(line):
            cmd = line.strip()
            if cmd.startswith("-"):
                cmd = cmd[1:].strip()
            cmds.append(cmd)

    # Deduplicate while preserving order.
    seen = set()
    ordered = []
    for cmd in cmds:
        if cmd not in seen:
            ordered.append(cmd)
            seen.add(cmd)
    return ordered


def main():
    parser = argparse.ArgumentParser(description="Auto-run Codex prompt chains.")
    parser.add_argument("--prompt", required=True, help="Initial /prompts:... command")
    parser.add_argument("--max-steps", type=int, default=25, help="Max chain steps")
    parser.add_argument("--unsafe", action="store_true", help="Bypass approvals and sandbox")
    parser.add_argument("--repo", default=os.getcwd(), help="Repo root")
    args = parser.parse_args()

    repo_root = os.path.abspath(args.repo)
    codex_home = os.path.join(repo_root, ".codex")

    executed = []
    queue = [args.prompt]

    while queue and len(executed) < args.max_steps:
        current = queue.pop(0)
        if current in executed:
            continue
        print(f"[auto-flow] running: {current}")
        output = _run_codex(current, repo_root, codex_home, args.unsafe)
        executed.append(current)

        next_cmds = _extract_next_commands(output)
        for cmd in next_cmds:
            if cmd not in executed and cmd not in queue:
                queue.append(cmd)

    if queue:
        print("[auto-flow] stopped: max steps reached", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
