# 安装、调用与阶段示例

[返回中文首页](../README.md) · [English README](../README_EN.md)

## 运行条件

- Codex、Claude Code，或其他能够读取完整 Agent Skill 目录的兼容环境；
- 可访问期刊官网、PubMed、Crossref 或其他权威学术来源；
- 完整审稿需要宿主能够执行至少 5 个具有独立上下文的 Agent 任务；
- Python 3.10 或更高版本；
- DOCX 样式审计和测试需要 `python-docx`。

## 安装

先克隆仓库并安装 Python 依赖：

```bash
git clone https://github.com/Jameslxr/manuscript-review-revision-skill.git
cd manuscript-review-revision-skill
python3 -m pip install -r requirements.txt
```

### Codex：个人级安装

```bash
mkdir -p "$HOME/.codex/skills"
ln -s "$PWD/manuscript-review-revision" \
  "$HOME/.codex/skills/manuscript-review-revision"
```

重新载入 Codex 后，可以通过 `$manuscript-review-revision` 调用。

### Claude Code：个人级安装

Claude Code v2.1.203 或更高版本可以直接加载符号链接：

```bash
mkdir -p "$HOME/.claude/skills"
ln -s "$PWD/manuscript-review-revision" \
  "$HOME/.claude/skills/manuscript-review-revision"
```

如需只在某一个项目中使用，可将完整目录放入该项目：

```bash
mkdir -p /path/to/project/.claude/skills
cp -R manuscript-review-revision \
  /path/to/project/.claude/skills/manuscript-review-revision
```

启动 Claude Code 后，可通过 `/manuscript-review-revision` 调用。Claude
Code 也会根据 Skill 描述在相关请求中自动加载。

### 复制安装和其他宿主

如果不希望使用符号链接，可将完整目录复制到宿主的 Skills 目录：

```bash
cp -R manuscript-review-revision "$HOME/.codex/skills/"
```

不要只复制 `SKILL.md`；该 Skill 还依赖 `references/` 和 `scripts/`。
`agents/openai.yaml` 是 Codex 的界面元数据，其他宿主可以忽略。

其他 Agent Skills 宿主只有同时满足以下条件，才能报告为完成完整流程：

- 能读取 Skill 的附带文件；
- 能运行 Python 验证脚本；
- 能访问当前期刊和学术来源；
- 能创建至少 5 个真正独立的子 Agent。
- 能提供每个 reviewer 的任务 ID 或可引用的执行日志。

缺少某项关键能力时，相关阶段必须标记为 `NOT ASSESSABLE`。

## 最小调用

Codex：

```text
使用 $manuscript-review-revision，我上传了稿件。
```

Claude Code：

```text
/manuscript-review-revision 我上传了稿件。
```

如果没有提供目标期刊，Skill 会询问：

```text
本次目标期刊是什么？如果尚未确定，请回复“不确定，请推荐期刊”。
```

## 已知目标期刊

Codex 使用 `$manuscript-review-revision`；Claude Code 将第一行替换为
`/manuscript-review-revision`，后续参数相同：

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

## 多 Agent 在不同宿主中的实现

| 宿主 | 独立审稿实现 |
|---|---|
| Codex | 使用平台提供的子 Agent / collaboration delegation；每个角色使用独立任务 |
| Claude Code | 使用非 fork 的 `Agent` 子 Agent；每个 Agent 具有新的独立上下文 |
| 其他宿主 | 必须提供等效的独立上下文任务；单次对话内模拟 5 个角色不算完成 |

无论使用哪个宿主，所有审稿角色都必须接收相同稿件哈希、期刊档案和事实材料，并且在初审完成前看不到其他角色的结论。每个 reviewer 还必须记录唯一任务 ID、运行时间、输入哈希和报告哈希；缺少任务身份时，Panel 标记为 `NOT ASSESSABLE`。

独立报告完成后，系统建立 `reviews/concern_ledger.tsv`。每条意见必须指向
原文位置和证据位置，并给出可观察的解决标准。只有至少两个独立 reviewer
提出同一问题时才能标记为共识；冲突意见不得被多数票抹平。

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
- 无法取得 reviewer 任务 ID/执行日志，或报告哈希无法闭环；
- 期刊强制规则无法核实；
- 参考文献只有 metadata，没有足以判断 Claim 支持的内容；
- 作者尚未授权修改；
- 修改改变了核心 Claim、方法、统计、图表或引用，需要重新审稿。
