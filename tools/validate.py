#!/usr/bin/env python3
"""ORF 内容校验工具。

校验仓库中所有 Framework / Operator / Combinator 定义文件：
1. 对照 schemas/ 下的 JSON Schema（结构、必填字段、反例数量等）；
2. 交叉引用检查：
   - operator.framework 必须指向已存在的框架目录；
   - framework.related_frameworks 必须指向已存在的框架；
   - 同一 unit 的 id 全局唯一。

用法：
    python3 tools/validate.py          # 校验全部
    python3 tools/validate.py --strict # 失败时以非零码退出（CI 用）

依赖：pyyaml、jsonschema。
"""

from __future__ import annotations

import argparse
import glob
import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent.parent

# 校验目标：(schema 文件名, 文件 glob 模式, 单元名称)
TARGETS = [
    ("framework.schema.json", "frameworks/*/framework.yaml", "framework"),
    ("operator.schema.json", "frameworks/*/operators/*.yaml", "operator"),
    ("combinator.schema.json", "combinators/*/combinator.yaml", "combinator"),
]


def load_schema(name: str) -> dict:
    with open(ROOT / "schemas" / name, encoding="utf-8") as f:
        return json.load(f)


def load_yaml(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def main() -> int:
    parser = argparse.ArgumentParser(description="ORF 内容校验工具")
    parser.add_argument("--strict", action="store_true", help="存在失败时以退出码 1 结束")
    args = parser.parse_args()

    total, failed = 0, 0
    seen_ids: dict[str, str] = {}
    framework_ids: set[str] = set()
    errors: list[str] = []

    # 第一轮：schema 校验 + id 唯一性 + 收集框架集合
    for schema_name, pattern, unit in TARGETS:
        validator = Draft202012Validator(load_schema(schema_name))
        for path in sorted(glob.glob(str(ROOT / pattern))):
            total += 1
            rel = str(Path(path).relative_to(ROOT))
            try:
                data = load_yaml(path)
            except yaml.YAMLError as e:
                failed += 1
                errors.append(f"{rel}: YAML 解析失败 → {e}")
                continue
            if not isinstance(data, dict):
                failed += 1
                errors.append(f"{rel}: YAML 未解析为映射（空文件或文件损坏）")
                continue

            errs = sorted(validator.iter_errors(data), key=str)
            if errs:
                failed += 1
                for e in errs[:3]:
                    errors.append(f"{rel}: {e.message}")
                continue

            uid = data["id"]
            if uid in seen_ids:
                failed += 1
                errors.append(f"{rel}: id '{uid}' 与 {seen_ids[uid]} 重复")
            else:
                seen_ids[uid] = rel
            if unit == "framework":
                framework_ids.add(uid)
            print(f"✔ {rel}")

    # 第二轮：交叉引用检查
    for path in sorted(glob.glob(str(ROOT / "frameworks/*/operators/*.yaml"))):
        rel = str(Path(path).relative_to(ROOT))
        data = load_yaml(path)
        if not isinstance(data, dict):
            failed += 1
            errors.append(f"{rel}: YAML 未解析为映射，跳过交叉引用检查")
            continue
        fw = data.get("framework")
        if fw not in framework_ids:
            failed += 1
            errors.append(f"{rel}: 引用了不存在的框架 '{fw}'")
        prefix = data.get("id", "").split(".")[0]
        fw_dir = Path(path).parent.parent.name
        if not _dir_matches_framework(fw_dir, fw):
            errors_warning = f"{rel}: 所在目录 '{fw_dir}' 与 framework 字段 '{fw}' 不一致"
            failed += 1
            errors.append(errors_warning)
        if prefix and prefix not in _short_prefixes(fw):
            failed += 1
            errors.append(f"{rel}: id 前缀 '{prefix}' 与框架 '{fw}' 约定不符")

    for path in sorted(glob.glob(str(ROOT / "frameworks/*/framework.yaml"))):
        rel = str(Path(path).relative_to(ROOT))
        data = load_yaml(path)
        if not isinstance(data, dict):
            continue
        for related in data.get("related_frameworks", []):
            if related not in framework_ids:
                failed += 1
                errors.append(f"{rel}: related_frameworks 引用了不存在的框架 '{related}'")

    print(f"\n共 {total} 个定义文件，失败 {failed}")
    if errors:
        print("\n问题清单：")
        for e in errors:
            print("  ✘", e)
    if failed and args.strict:
        return 1
    return 0


def _dir_matches_framework(dir_name: str, framework_id: str) -> bool:
    """算子目录名应与所属框架目录一致。"""
    return dir_name == framework_id


def _short_prefixes(framework_id: str) -> set[str]:
    """算子 id 前缀约定：框架名本身或其常用缩写。"""
    aliases = {
        "role_and_naming": {"role"},
        "interest_structure": {"interest"},
        "incentive_structure": {"incentive"},
        "power_structure": {"power"},
        "cognitive_bias": {"cognition", "bias"},
        "bounded_rationality": {"bounded"},
        "system_feedback": {"system"},
        "falsification": {"falsification"},
    }
    return {framework_id} | aliases.get(framework_id, set())


if __name__ == "__main__":
    sys.exit(main())
