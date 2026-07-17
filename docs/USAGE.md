# 安装、调用与阶段示例

[返回中文首页](../README.md) · [English README](../README_EN.md)

## 运行条件

- 支持本地 Skills 的 Codex 环境；
- 可访问期刊官网、PubMed、Crossref 或其他权威学术来源；
- 完整审稿需要能够执行至少 5 个彼此独立的 Agent 任务；
- Python 3.10 或更高版本；
- DOCX 样式审计和测试需要 `python-docx`。

## 安装

```bash
git clone https://github.com/Jameslxr/manuscript-review-revision-skill.git
cd manuscript-review-revision-skill
python3 -m pip install -r requirements.txt
mkdir -p "$HOME/.codex/skills"
ln -s "$PWD/manuscript-review-revision" \
  "$HOME/.codex/skills/manuscript-review-revision"
```

如果不希望使用符号链接，也可以复制完整技能目录：

```bash
cp -R manuscript-review-revision "$HOME/.codex/skills/"
```

不要只复制 `SKILL.md`；该 Skill 还依赖 `references/`、`scripts/` 和 `agents/`。

## 最小调用

```text
使用 $manuscript-review-revision，我上传了 manuscript。
```

如果没有提供目标期刊，Skill 会询问：

```text
本次目标期刊是什么？如果尚未确定，请回复“不确定，请推荐期刊”。
```

## 已知目标期刊

```text
使用 $manuscript-review-revision。
目标期刊：Journal of Hepatology
文章类型：Original Article
阶段：Initial submission
先审稿，不修改原稿。
```

## 目标期刊不确定

```text
使用 $manuscript-review-revision。
目标期刊不确定，请根据稿件主题、创新性、研究质量、
证据强度和投稿可行性推荐 Top 5。
```

系统先返回经过核实的候选期刊，等待作者选定主目标后再开始完整审稿。

## 只审稿，不修改

```text
使用 $manuscript-review-revision。
目标期刊：Journal of Hepatology
阶段：Initial submission
只运行 scientific-review。
保持 manuscript 只读，完成综合结论后暂停。
```

## 参考文献专项审计

```text
使用 $manuscript-review-revision。
运行 reference-audit：
1. 核查 DOI、PMID、题目、作者、期刊和年份；
2. 检查目标期刊格式；
3. 将句子拆分为 atomic claims；
4. 判断每条引用是直接、部分、间接、矛盾或无法评估。
```

## 作者授权修改

审阅 `05_review_verdict.md` 后，使用明确授权：

```text
我已审阅 05_review_verdict.md，同意进入 revise-manuscript。
请保留原稿，并输出 tracked copy、clean copy 和 revision_log.tsv。
```

“继续”“帮我看看”或上传新文件不自动视为修改授权。

## 返修回复

```text
使用 $manuscript-review-revision。
模式：response-to-reviewers
目标期刊：[journal]
请读取 editor letter、reviewer comments、当前修订稿和作者说明。
先建立 comment-response tracker，再起草逐点回复。
无法证明已经完成的修改必须标记为 AUTHOR_INPUT_NEEDED。
```

## 可用模式

| Mode | 用途 |
|---|---|
| `journal-recommendation` | 目标不确定时推荐并核实 Top 5 |
| `scientific-review` | 默认只读科学审稿 |
| `reference-audit` | 文献真实性、格式、位置和 Claim 支持 |
| `response-to-reviewers` | 审稿意见分解、回复和修改映射 |
| `revise-manuscript` | 作者授权后的科学修改 |
| `format-manuscript` | 科学内容稳定后的期刊排版 |
| `release-gate` | 投稿前 fail-closed 审计 |
| `full-run` | 全流程，但仍会在审稿后暂停等待授权 |

## 重要停止条件

- 目标期刊未确定；
- 关键稿件版本冲突；
- 无法执行至少 5 个独立 Agent 任务；
- 期刊强制规则无法核实；
- 参考文献只有 metadata，没有足以判断 Claim 支持的内容；
- 作者尚未授权修改；
- 修改改变了核心 Claim、方法、统计、图表或引用，需要重新审稿。
