#!/usr/bin/env python3
"""Static, dependency-free checks for design-expert prototype deliverables."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


STACK_RULES = {
    "semi": {
        "allowed": ("@douyinfe/semi-ui", "@douyinfe/semi-icons"),
        "forbidden": ("from 'antd'", 'from "antd"', "@ant-design/", "tdesign", "@oplus/nubes-ui"),
    },
    "antd": {
        "allowed": ("from 'antd'", 'from "antd"', "@ant-design/"),
        "forbidden": ("@douyinfe/semi-", "tdesign", "@oplus/nubes-ui"),
    },
    "tdesign": {
        "allowed": ("tdesign",),
        "forbidden": ("@douyinfe/semi-", "from 'antd'", 'from "antd"', "@oplus/nubes-ui"),
    },
    "nubes": {
        "allowed": ("@oplus/nubes-ui", "nb-"),
        "forbidden": ("@douyinfe/semi-", "from 'antd'", 'from "antd"', "tdesign"),
    },
}

SOURCE_EXTENSIONS = {".js", ".jsx", ".ts", ".tsx", ".vue", ".css", ".html"}
IGNORE_DIRS = {"node_modules", "dist", ".git", ".vite", "coverage"}


def source_files(project: Path) -> list[Path]:
    return [
        path
        for path in project.rglob("*")
        if path.is_file()
        and path.suffix in SOURCE_EXTENSIONS
        and not any(part in IGNORE_DIRS for part in path.parts)
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a design-expert prototype.")
    parser.add_argument("--project", required=True, help="Prototype project directory")
    parser.add_argument("--stack", required=True, choices=STACK_RULES, help="Selected UI stack")
    parser.add_argument("--evidence", help="Path to evidence.json; defaults to <project>/evidence.json")
    args = parser.parse_args()

    project = Path(args.project).resolve()
    evidence_path = Path(args.evidence).resolve() if args.evidence else project / "evidence.json"
    report: dict[str, list[dict[str, str]]] = {"errors": [], "warnings": [], "passed": []}

    if not project.is_dir():
        report["errors"].append({"rule": "project", "message": "原型目录不存在"})
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 1

    files = source_files(project)
    if not files:
        report["errors"].append({"rule": "sources", "message": "未找到可检查的源码文件"})

    evidence = None
    if not evidence_path.is_file():
        report["errors"].append({"rule": "evidence", "message": f"缺少证据记录：{evidence_path}"})
    else:
        try:
            evidence = json.loads(evidence_path.read_text(encoding="utf-8"))
            if evidence.get("stack", {}).get("name") != args.stack:
                report["errors"].append(
                    {"rule": "evidence-stack", "message": "evidence.json 的 stack.name 与 --stack 不一致"}
                )
            elif not evidence.get("components"):
                report["errors"].append({"rule": "evidence-components", "message": "evidence.json 未记录组件证据"})
            else:
                report["passed"].append({"rule": "evidence", "message": "证据记录完整"})
        except json.JSONDecodeError as exc:
            report["errors"].append({"rule": "evidence-json", "message": f"evidence.json 不是有效 JSON：{exc.msg}"})

    content = "\n".join(path.read_text(encoding="utf-8", errors="ignore") for path in files)
    rules = STACK_RULES[args.stack]
    forbidden_hits = [token for token in rules["forbidden"] if token.lower() in content.lower()]
    if forbidden_hits:
        report["errors"].append(
            {"rule": "single-stack", "message": f"发现非选定栈标识：{', '.join(forbidden_hits)}"}
        )
    else:
        report["passed"].append({"rule": "single-stack", "message": "未发现已知跨栈导入"})

    if not any(token.lower() in content.lower() for token in rules["allowed"]):
        report["warnings"].append({"rule": "stack-usage", "message": "未识别到选定栈标识，请人工确认"})
    else:
        report["passed"].append({"rule": "stack-usage", "message": "检测到选定栈标识"})

    visual_patterns = {
        "gradient": r"linear-gradient|radial-gradient|conic-gradient",
        "glass": r"backdrop-filter|background:\s*rgba\([^)]*,\s*0\.[0-9]",
        "neon": r"box-shadow:[^;]*(0\s+0\s+(?:1[6-9]|[2-9]\d)px|#[a-f0-9]{3,8})",
    }
    for rule, pattern in visual_patterns.items():
        if re.search(pattern, content, re.IGNORECASE):
            report["warnings"].append({"rule": f"visual-{rule}", "message": "发现需人工复核的视觉反模式"})

    state_terms = {
        "loading": r"loading|加载中",
        "empty": r"empty|暂无|无结果",
        "error": r"error|失败|异常",
        "permission": r"permission|无权限|权限不足",
    }
    absent_states = [name for name, pattern in state_terms.items() if not re.search(pattern, content, re.IGNORECASE)]
    if absent_states:
        report["warnings"].append(
            {"rule": "states", "message": f"未在静态源码中识别状态关键词：{', '.join(absent_states)}"}
        )
    else:
        report["passed"].append({"rule": "states", "message": "检测到基础状态关键词"})

    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if report["errors"] else 0


if __name__ == "__main__":
    sys.exit(main())
