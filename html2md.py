#!/usr/bin/env python3
"""html2md.py

一个轻量的 HTML → Markdown 转换脚本（偏向“结构化文本/清单”类 HTML）。

特点：
- 识别并转换 h1-h6 标题
- 识别并转换 ul/ol 列表（支持嵌套）
- 尝试把类似“键：值 / key: value”的列表项转为 “- **键**：值”
- 自动补全裸域名/裸 github.com/... 为 https://...

用法：
  python3 html2md.py input.html -o output.md
  python3 html2md.py input.html            # 默认同名 .md

注意：
- 该脚本不追求 100% 的富文本样式还原；目标是把“标题 + 列表要点”类内容干净地抽取出来。
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString, Tag


WS_RE = re.compile(r"\s+")


def clean_text(t: str) -> str:
    t = WS_RE.sub(" ", (t or "")).strip()
    # 常见中英文混排的冒号修正
    t = t.replace(" ：", "：").replace(": ", "：")
    return t


def normalize_url(s: str) -> str:
    s = (s or "").strip()
    if not s:
        return s

    m = re.search(r"(https?://\S+|www\.[^\s]+|[\w.-]+\.[a-z]{2,}/\S+)", s, flags=re.IGNORECASE)
    if not m:
        return s

    url = m.group(1)
    if url.lower().startswith("http://") or url.lower().startswith("https://"):
        return url
    return "https://" + url


def guess_kv_line(text: str) -> str | None:
    """把“key: value / key：value”类行转换为 markdown。"""
    text = clean_text(text)
    if not text:
        return None

    m = re.match(r"^(.{1,20}?)[：:]\s*(.+)$", text)
    if not m:
        return None

    key, val = m.group(1).strip(), m.group(2).strip()

    # 过于像句子/段落的不当作 key-value（简单启发式）
    if len(key) > 12 and any(ch in key for ch in " ，。,.!?！？"):
        return None

    # 如果 value 里包含 URL，尝试标准化
    if "github.com" in val or "http" in val or "www." in val:
        val = normalize_url(val)

    return f"- **{key}**：{val}" if val else f"- **{key}**"


def tag_text(tag: Tag) -> str:
    return clean_text(tag.get_text(" ", strip=True))


def render_list(lst: Tag, indent: int = 0) -> list[str]:
    """渲染 ul/ol（支持嵌套）"""
    lines: list[str] = []
    bullet = "-"  # 统一用 -，避免数字列表在复杂嵌套下错位

    for li in lst.find_all("li", recursive=False):
        # li 可能含 p/span/font/... + nested ul/ol
        nested = [c for c in li.children if isinstance(c, Tag) and c.name in {"ul", "ol"}]

        # 取除 nested list 之外的“正文”文本
        li_clone = BeautifulSoup("<li></li>", "html.parser").li
        for child in li.contents:
            if isinstance(child, Tag) and child.name in {"ul", "ol"}:
                continue
            li_clone.append(child if isinstance(child, NavigableString) else child.__copy__())

        text = clean_text(li_clone.get_text(" ", strip=True))
        kv = guess_kv_line(text)

        prefix = "  " * indent + bullet + " "
        if kv:
            # kv 已包含 '- '，去掉它并加上正确缩进
            lines.append("  " * indent + kv)
        elif text:
            lines.append(prefix + text)

        for sub in nested:
            lines.extend(render_list(sub, indent=indent + 1))

    return lines


def is_heading(tag: Tag) -> bool:
    return tag.name in {"h1", "h2", "h3", "h4", "h5", "h6"}


def heading_level(tag: Tag) -> int:
    return int(tag.name[1])  # h1 -> 1


def convert_html_to_md(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    body = soup.body or soup

    parts: list[str] = []

    # 按文档顺序找所有标题
    headings = body.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])

    if not headings:
        # 没有标题时：尽量输出正文纯文本 + 列表
        for lst in body.find_all(["ul", "ol"]):
            parts.extend(render_list(lst, indent=0))
        text = tag_text(body)
        if text and not parts:
            parts.append(text)
        return "\n".join(parts).rstrip() + "\n"

    min_level = min(heading_level(h) for h in headings)

    for h in headings:
        title = tag_text(h)
        if title:
            # 把最小标题级别映射为 '#'
            lvl = heading_level(h) - min_level + 1
            parts.append(f"{'#' * max(1, lvl)} {title}\n")

        # 收集该标题后面的兄弟节点，直到下一个标题
        sib = h.next_sibling
        while sib is not None:
            # BeautifulSoup 里 next_sibling 可能是 \n 等文本
            if isinstance(sib, Tag) and is_heading(sib):
                break

            if isinstance(sib, Tag) and sib.name in {"ul", "ol"}:
                parts.extend(render_list(sib, indent=0))
                parts.append("")
            sib = sib.next_sibling

    md = "\n".join(parts).rstrip() + "\n"
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Convert HTML to Markdown (headings + lists focused).")
    p.add_argument("input", type=Path, help="输入 HTML 文件路径")
    p.add_argument("-o", "--output", type=Path, default=None, help="输出 Markdown 文件路径（默认与输入同名 .md）")
    p.add_argument("--encoding", default="utf-8", help="输入文件编码（默认 utf-8；失败会自动忽略非法字符）")
    return p.parse_args()


def main() -> int:
    args = parse_args()

    src: Path = args.input
    if not src.exists() or not src.is_file():
        raise SystemExit(f"输入文件不存在：{src}")

    dst: Path = args.output or src.with_suffix(".md")

    html = src.read_text(encoding=args.encoding, errors="ignore")
    md = convert_html_to_md(html)

    dst.write_text(md, encoding="utf-8")
    print(f"Wrote: {dst} ({len(md)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
