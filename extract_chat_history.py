#!/usr/bin/env python3
import json
import os
from datetime import datetime
from pathlib import Path

# Directories to search
dirs = [
    "/Users/watsonchao/.claude/projects/-Users-watsonchao-CMU-Courses-fall25-AITools-P3-team-code-cruise",
    "/Users/watsonchao/.claude/projects/-Users-watsonchao-CMU-Courses-fall25-AITools-P3-team-code-cruise-ride-app"
]

# Files from Oct 22-23
oct_22_23_files = [
    "/Users/watsonchao/.claude/projects/-Users-watsonchao-CMU-Courses-fall25-AITools-P3-team-code-cruise/490b8c29-bd67-436e-ba74-af548bc38616.jsonl",
    "/Users/watsonchao/.claude/projects/-Users-watsonchao-CMU-Courses-fall25-AITools-P3-team-code-cruise/7c1d101f-a8d0-4c1b-a4e7-338bb7afbe51.jsonl",
    "/Users/watsonchao/.claude/projects/-Users-watsonchao-CMU-Courses-fall25-AITools-P3-team-code-cruise/87ed2b99-7436-48ef-969c-bd4ad248a159.jsonl",
    "/Users/watsonchao/.claude/projects/-Users-watsonchao-CMU-Courses-fall25-AITools-P3-team-code-cruise/c43ef406-68ff-498f-b3b7-9dcdb347494d.jsonl",
    "/Users/watsonchao/.claude/projects/-Users-watsonchao-CMU-Courses-fall25-AITools-P3-team-code-cruise/e1da2245-d899-4332-9af1-811fa39e72bd.jsonl",
    "/Users/watsonchao/.claude/projects/-Users-watsonchao-CMU-Courses-fall25-AITools-P3-team-code-cruise/96fbcee4-a15d-42f1-9151-839b8246ee5c.jsonl",
    "/Users/watsonchao/.claude/projects/-Users-watsonchao-CMU-Courses-fall25-AITools-P3-team-code-cruise/e51b3979-7b92-4b56-8cf4-0867da116f1e.jsonl",
    "/Users/watsonchao/.claude/projects/-Users-watsonchao-CMU-Courses-fall25-AITools-P3-team-code-cruise-ride-app/ce36f320-940f-41c2-b209-e0bcfb5c20f7.jsonl"
]

all_messages = []

for file_path in oct_22_23_files:
    if not os.path.exists(file_path):
        continue

    print(f"Processing: {file_path}")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue

                try:
                    data = json.loads(line)

                    # Extract message content and timestamp
                    # Messages have type 'user' or 'assistant' and contain a 'message' field
                    if data.get('type') in ['user', 'assistant']:
                        message_obj = data.get('message', {})
                        message_data = {
                            'timestamp': data.get('timestamp'),
                            'role': message_obj.get('role', data.get('type', 'unknown')),
                            'content': message_obj.get('content', []),
                            'file': os.path.basename(file_path),
                            'message_id': data.get('uuid', ''),
                            'cwd': data.get('cwd', ''),
                            'session_id': data.get('sessionId', '')
                        }
                        all_messages.append(message_data)

                except json.JSONDecodeError as e:
                    print(f"  Warning: Line {line_num} in {file_path} is not valid JSON: {e}")
                    continue

    except Exception as e:
        print(f"  Error reading {file_path}: {e}")

# Sort by timestamp
all_messages.sort(key=lambda x: x['timestamp'] if x['timestamp'] else '')

print(f"\nTotal messages extracted: {len(all_messages)}")

# Format as markdown
output = ["# Claude Code Chat History - October 22-23, 2025", ""]

current_conversation = None
message_count = 0

for msg in all_messages:
    # Parse timestamp
    ts = msg['timestamp']
    if ts:
        try:
            dt = datetime.fromisoformat(ts.replace('Z', '+00:00'))
            time_str = dt.strftime('%Y-%m-%d %H:%M:%S')
        except:
            time_str = ts
    else:
        time_str = "Unknown time"

    # Check if new conversation file
    if current_conversation != msg['file']:
        current_conversation = msg['file']
        output.append(f"\n---\n\n## Conversation: {msg['file']}\n")
        if msg.get('cwd'):
            output.append(f"**Working Directory:** `{msg['cwd']}`\n")
        if msg.get('session_id'):
            output.append(f"**Session ID:** `{msg['session_id']}`\n")

    # Format role
    role = msg['role'].upper()

    # Format message header
    output.append(f"### [{time_str}] {role}\n")

    # Format content
    content = msg['content']
    if isinstance(content, list):
        for item in content:
            if isinstance(item, dict):
                if item.get('type') == 'text':
                    text = item.get('text', '')
                    if text:
                        output.append(text)
                        output.append("")
                elif item.get('type') == 'tool_use':
                    tool_name = item.get('name', 'unknown')
                    tool_input = item.get('input', {})
                    output.append(f"**Tool Use:** `{tool_name}`")
                    output.append(f"```json")
                    output.append(json.dumps(tool_input, indent=2))
                    output.append(f"```")
                    output.append("")
                elif item.get('type') == 'tool_result':
                    tool_use_id = item.get('tool_use_id', 'unknown')
                    tool_content = item.get('content', '')
                    output.append(f"**Tool Result:** {tool_use_id}")
                    if isinstance(tool_content, str):
                        output.append(f"```")
                        output.append(tool_content[:1000] + ('...' if len(tool_content) > 1000 else ''))
                        output.append(f"```")
                    else:
                        output.append(f"```json")
                        output.append(json.dumps(tool_content, indent=2)[:1000])
                        output.append(f"```")
                    output.append("")
            elif isinstance(item, str):
                output.append(item)
                output.append("")
    elif isinstance(content, str):
        output.append(content)
        output.append("")

    message_count += 1

output.append(f"\n---\n\n*Total messages: {message_count}*")

# Write to output file
output_file = "/Users/watsonchao/CMU/Courses/fall25/AITools/P4ClaudeChatHistory.md"
os.makedirs(os.path.dirname(output_file), exist_ok=True)

with open(output_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(output))

print(f"\nChat history written to: {output_file}")
print(f"Total messages processed: {message_count}")
