# ORF 原型文档 v0.2 融入式升级实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将 spec（`docs/superpowers/specs/2026-08-20-orf-prototype-v0.2-design.md`）中的八项决议融入式落实到新文档 `Open_Reasoning_Framework_Prototype_v0.2.md`，原 v0.1 文件保持不动。

**Architecture:** 先复制 v0.1 为 v0.2 底稿，随后按章节分 9 个任务逐块修订；每个任务含关键内容的确切文本、修订规则和一致性校验（grep 断言），完成即提交。最终做一次全文终审。

**Tech Stack:** Markdown 文档；校验工具为 grep/zsh；无代码、无运行时。

**参考文件:**
- Spec：`docs/superpowers/specs/2026-08-20-orf-prototype-v0.2-design.md`
- 底稿来源：`Open_Reasoning_Framework_Prototype_v0.1.md`
- 产出物：`Open_Reasoning_Framework_Prototype_v0.2.md`

**通用约定:** 所有任务在仓库根目录操作；路径含空格，shell 命令中一律给路径加双引号；每个任务结束时提交一次 git。

---

### Task 1: 创建 v0.2 底稿与修订说明

**Files:**
- Create: `Open_Reasoning_Framework_Prototype_v0.2.md`（由 v0.1 复制而来后修改头部）

- [ ] **Step 1: 复制 v0.1 为 v0.2**

```bash
cp "Open_Reasoning_Framework_Prototype_v0.1.md" "Open_Reasoning_Framework_Prototype_v0.2.md"
```

- [ ] **Step 2: 替换文档头部并插入修订说明**

将文件开头替换为（保留第 3 行 `> **一句话定义：**` 起的全部内容不变）：

```markdown
# Open Reasoning Framework（暂定名）
## 开源认知分析引擎原型文档 v0.2

### v0.2 修订说明

本版本由 v0.1 融入式升级而来（v0.1 保留于仓库，git 历史即版本记录）。修订基于八项设计决议：

| # | 张力点 | 决议 |
|---|---|---|
| ① | Operator 本质 | Operator 是类型化转换器；项目护城河 = Schema 校验 + 编排纪律 + 契约强制 + 评测回归（引擎四层论） |
| ② | 认知差无架构位置 | 认知差定位为执行组合器（Combinator），与 Framework、Operator 并列为三类可调用单位 |
| ③ | 框架清单矛盾 | MVP 维持 8 框架；补写激励结构、权力关系定义并增加边界判据；博弈移入长期扩展 |
| ④ | Cross-Audit 机制空白 | 并行单轮 + 攻击契约 + 综合硬规则 |
| ⑤ | Selector 无选择依据 | LLM 选择 + 强制结构化理由，Runtime 校验 3～7 数量边界 |
| ⑥ | 交互模型未定义 | 无状态再分析（prior_analysis + new_evidence，仅重审受影响假设） |
| ⑦ | 评测无 ground truth | 专家盲评验证核心假设 + 渐进 golden 变量集做回归 |
| ⑧ | 语言策略 | Schema 字段采用 localized map 结构，MVP 内容只填中文 |

> **一句话定义：**
（一句话定义及之后内容保持 v0.1 原样，待后续任务逐节修订）
```

- [ ] **Step 3: 修改文末文档状态**

```markdown
**文档状态：** 原型
**版本：** v0.2
**上一版本：** v0.1（保留于仓库）
**下一阶段：** Schema 定义与首批 Framework 设计
```

- [ ] **Step 4: 校验**

```bash
grep -q "v0.2 修订说明" "Open_Reasoning_Framework_Prototype_v0.2.md" && grep -q "一句话定义" "Open_Reasoning_Framework_Prototype_v0.2.md" && echo OK
```
Expected: `OK`

- [ ] **Step 5: Commit**

```bash
git add "Open_Reasoning_Framework_Prototype_v0.2.md"
git commit -m "docs: 创建 v0.2 底稿与修订说明（八项决议总账）"
```

---

### Task 2: 架构核心——三类可调用单位与引擎论证（§2、§5、§6）

**Files:**
- Modify: `Open_Reasoning_Framework_Prototype_v0.2.md` §2、§5、§6

- [ ] **Step 1: §2 末尾追加引擎论证小节**

在 §2.1 之后、`## 3. 项目目标` 之前插入：

```markdown
### 2.2 为什么不是 Prompt 仓库：引擎论证

SQL 语句本身只是文本，但数据库不是"文本文件集合"——让 SQL 有价值的是引擎、约束和事务。

同理，Operators 是推理的查询语言，Runtime 才是引擎。本项目区别于 Prompt 集合的护城河是四层机制：

1. **Schema 校验**：结构正确性强制，不合规内容无法入库；
2. **编排纪律**：选择、并行、对抗角色指派由 Runtime 决定，而非提示词自觉；
3. **契约强制**：输出缺字段即拒绝并重跑，攻击者不得沉默；
4. **评测回归**：对基线的持续对照，逻辑漂移会被测试捕获。
```

- [ ] **Step 2: 改写 §5 架构图**

在 §5 现有架构图之后追加一段：

```markdown
说明：本项目的可调用单位分为三类——

1. **Framework（分析框架）**：分析镜头，含边界判据（"我回答什么 / 我不回答什么"）；
2. **Operator（推理算子）**：类型化转换器，`(类型化输入 → 类型化输出)`，LLM 是负责填空的推理引擎；
3. **Combinator（执行组合器）**：执行组合模式，首个实例为认知差分析（见第 12 节）。

一次完整分析的所有中间产物（事实、假设、证据、冲突）累积为一张带溯源的类型化推理图。第 22 节要求的审计（哪些事实来自用户、哪些是模型推断、哪些框架冲突）是推理图的天然属性，不是额外机制。
```

- [ ] **Step 3: 改写 §6 两层原子结构为三类单位**

将 §6 中 `### 第一层：Framework（分析框架）` 与 `### 第二层：Operator（推理算子）` 的标题与引导语改为三类单位表述（内容沿用 §5 Step 2 的定义，Operator 示例保留原利益结构问题树），并在 §6 末尾追加：

```markdown
### 第三类：Combinator（执行组合器）

组合器不是新的内容单位，而是对 Operator 的执行组合模式。认知差分析是首个组合器：同一组 Operator 在不同立场参数下执行，再对结果做结构化 diff。详见第 12 节。

人物仅作为思想来源和理论谱系存在。
```

- [ ] **Step 4: 校验**

```bash
grep -q "引擎论证" "Open_Reasoning_Framework_Prototype_v0.2.md" && grep -q "Combinator（执行组合器）" "Open_Reasoning_Framework_Prototype_v0.2.md" && grep -q "类型化推理图" "Open_Reasoning_Framework_Prototype_v0.2.md" && echo OK
```
Expected: `OK`

- [ ] **Step 5: Commit**

```bash
git add "Open_Reasoning_Framework_Prototype_v0.2.md"
git commit -m "docs(v0.2): 三类可调用单位与引擎论证（§2/§5/§6）"
```

---

### Task 3: 首批框架内容修订（§7）

**Files:**
- Modify: `Open_Reasoning_Framework_Prototype_v0.2.md` §7

- [ ] **Step 1: 为 §7 已有的 6 个框架（7.1 角色与正名 ～ 7.5 有限理性、7.7 系统反馈）各追加边界判据**

在每个框架小节末尾追加 `### 边界判据`，要点（写成完整句子）：

- **角色与正名**：我回答"名义授权与实际授权、应然职责与实然职责的差距"；我不回答"谁实际控制关键资源与议程"（那是权力关系框架），也不回答"规则如何塑造行为动机"（那是激励结构框架）。
- **利益结构**：我回答"收益、成本、资源控制与规则制定权如何分配"；我不回答"分配规则如何影响行为动机"（那是激励结构框架）。
- **认知偏差**：我回答"信息处理过程中的系统性偏差"；我不回答"偏差背后的利益动机"（那是利益结构框架）。
- **有限理性**：我回答"信息、时间、处理能力约束下的决策质量"；我不回答"决策权归属是否正当"（那是角色与正名 / 权力关系框架）。
- **系统反馈**：我回答"变量间的相互影响、反馈回路与延迟效应"；我不回答"单个行动者的动机"（那是激励结构框架）。

（证伪框架 7.3 是元框架，边界判据写：我回答"任何假设的可检验性"；我不替代具体领域框架提出实质解释。）

- [ ] **Step 2: 删除 §7.6 博弈框架小节**

完整删除 7.6（含其核心问题），后续小节不重新编号（7.7 保持，避免引用漂移），在被删位置留一行：

```markdown
## 7.6 博弈框架

已移入第 24 节长期扩展方向，MVP 不收录。
```

- [ ] **Step 3: §24 长期扩展方向追加博弈**

在 §24 的扩展清单中（"亚里士多德：目的与德性"一段）追加一行：

```markdown
- 博弈论：参与者、策略与均衡（从 MVP 移出，见第 7.6 节说明）
```

- [ ] **Step 4: 新增 §7.8 激励结构框架**

```markdown
## 7.8 激励结构框架

**思想来源：** 委托-代理理论、机制设计与组织行为学中的激励研究。

### 核心问题

- 行动者能否分享自己创造的成功收益？
- 行动者是否承担超出其收益范围的风险？
- 激励对象与责任主体是否一致？
- 激励是强化短期行为还是长期行为？
- 当前规则是否激励了"指标表演"而非真实产出？

### 典型问题

> 组织鼓励创新，但考核只看既定产出指标。

此时"没人创新"大概率不是意愿或能力问题，而是激励结构与创新行为不耦合。

### 边界判据

我回答"规则如何塑造行为动机"；我不回答"收益与成本如何分配"（那是利益结构框架）。分界示例：改变分配格局是利益问题，改变行为与回报的耦合方式是激励问题。
```

- [ ] **Step 5: 新增 §7.9 权力关系框架**

```markdown
## 7.9 权力关系框架

**思想来源：** 马克斯·韦伯的权威与支配理论、组织研究中的权力与议程设置文献。

### 核心问题

- 谁的决定能够被执行？
- 谁可以否决他人的决定？
- 谁控制关键资源与信息通道？
- 谁设定议程（决定哪些问题被讨论、哪些不被讨论）？
- 依赖关系是否单向？退出权是否对称？

### 典型问题

> 名义上集体决策，实际上议题与结论在会前已由个别人定调。

这是议程设置型权力，比命令型权力更隐蔽，也更难通过"完善会议流程"解决。

### 边界判据

我回答"谁实际上能决定、否决与控制"；我不回答"名义角色与应然职责"（那是角色与正名框架）。分界示例：名义授权与实际授权不一致是角色问题，谁控制资源、议程与退出权是权力问题。
```

- [ ] **Step 6: 校验**

```bash
grep -q "激励结构框架" "Open_Reasoning_Framework_Prototype_v0.2.md" && grep -q "权力关系框架" "Open_Reasoning_Framework_Prototype_v0.2.md" && grep -q "已移入第 24 节长期扩展方向" "Open_Reasoning_Framework_Prototype_v0.2.md" && grep -q "博弈论：参与者、策略与均衡" "Open_Reasoning_Framework_Prototype_v0.2.md" && grep -c "边界判据" "Open_Reasoning_Framework_Prototype_v0.2.md"
```
Expected: `OK`（前三项）且"边界判据"出现 ≥ 8 次

- [ ] **Step 7: Commit**

```bash
git add "Open_Reasoning_Framework_Prototype_v0.2.md"
git commit -m "docs(v0.2): 补写激励/权力框架与全部边界判据，博弈移入扩展（§7）"
```

---

### Task 4: Operator Schema 重写（§8）

**Files:**
- Modify: `Open_Reasoning_Framework_Prototype_v0.2.md` §8

- [ ] **Step 1: 用以下类型化版本完整替换 §8 的 YAML 示例**

```yaml
id: incentive.reward_risk_asymmetry
name:
  zh: 收益风险不对称
  # en: Reward-Risk Asymmetry（i18n 预留，MVP 只填中文）
framework: incentive_structure
version: 1.0.0
unit_type: operator   # operator | combinator

description:
  zh: >
    检查某项行为的收益归属与失败风险承担是否一致。

inputs:                # 类型化输入：引用前序产物或用户输入的对象类型
  - type: problem_statement
  - type: actor_list
  - type: action_outcome_records
outputs:               # 类型化输出：写入推理图的对象
  - type: hypothesis
  - type: evidence_reference
  - type: uncertainty_assessment

questions:
  - 成功后谁获得收益？
  - 失败后谁承担责任？
  - 行动者是否能分享到成功收益？
  - 行动者是否承担超出收益范围的风险？

required_evidence:
  - 绩效制度
  - 奖励规则
  - 责任制度
  - 实际案例

possible_findings:
  - 收益风险对称
  - 收益集中、风险下沉
  - 收益下沉、风险集中
  - 无法判断

counterexamples:
  - 即使收益风险不对称，行为者仍高度积极（如使命驱动、长期声誉收益）
  - 表面不对称但存在隐性补偿（晋升、股权、豁免权）

failure_conditions:
  - 缺乏真实激励数据
  - 用户仅提供主观感受

boundary_criteria:
  answers: 行为与回报的耦合方式
  does_not_answer: 收益成本的总体分配（利益结构）、名义职责（角色与正名）

output:
  hypothesis:
  evidence:
  uncertainty:
  next_validation:
```

- [ ] **Step 2: 在示例后追加 Schema 说明**

```markdown
Schema 要点：

- `inputs` / `outputs` 为类型化声明，算子消费与产出的都是推理图中的类型化对象，而非自由文本；
- 所有文本字段采用 localized map 结构（如 `name.zh`），MVP 只填中文；
- `boundary_criteria`、`counterexamples`（≥ 2）、`failure_conditions` 为强制字段；
- 输出契约四件套：`hypothesis / evidence / uncertainty / next_validation`，缺任何一项即被 Runtime 拒绝。
```

- [ ] **Step 3: 校验**

```bash
grep -q "unit_type: operator" "Open_Reasoning_Framework_Prototype_v0.2.md" && grep -q "boundary_criteria:" "Open_Reasoning_Framework_Prototype_v0.2.md" && grep -q "zh: 收益风险不对称" "Open_Reasoning_Framework_Prototype_v0.2.md" && echo OK
```
Expected: `OK`

- [ ] **Step 4: Commit**

```bash
git add "Open_Reasoning_Framework_Prototype_v0.2.md"
git commit -m "docs(v0.2): Operator Schema 类型化 + i18n + 边界判据（§8）"
```

---

### Task 5: 运行流程、输出协议与 Runtime（§9、§13、§17）

**Files:**
- Modify: `Open_Reasoning_Framework_Prototype_v0.2.md` §9、§13、§17

- [ ] **Step 1: 用以下流程图完整替换 §9 现有流程图**

```text
用户输入（可携带 prior_analysis + new_evidence）
↓
问题重述
↓
区分事实 / 假设 / 推理 / 价值判断
↓
识别问题类型
↓
Framework Selector（LLM 选择 + 强制理由，Runtime 校验 3～7 边界）
↓
并行执行各框架 Operators（产出类型化对象，累积进推理图）
↓
Cross-Audit（并行单轮攻击 → 证伪过关）
↓
Synthesizer（硬保留规则综合）
↓
结构化输出 + 完整审计日志
↓
（可选）用户补充证据 → 携带 prior_analysis 再调用，仅重审受影响假设
```

并在流程图后追加交互模型说明：

```markdown
### 交互模型：无状态再分析

Runtime 不维护会话状态。用户补充证据后，携带上一次的输出（`prior_analysis`）与新证据（`new_evidence`）再次调用，Runtime 仅对受新证据影响的假设重走互审。多轮能力由调用方通过再调用组装，库与 Runtime 保持无状态。
```

- [ ] **Step 2: 修订 §13 输出协议**

在六层结构之前插入第 0 层，并修改第 2 层：

```markdown
## 0. 选择理由
Selector 选用了哪些框架、逐个命中理由。此层是用户质疑与纠正的入口。

## 1. 当前事实
已经能够确认的信息。

## 2. 核心假设
目前最可能成立的解释。允许以"竞争假设集 + 证据不足声明"形态出现——当多个假设未被反驳时，不得强行合并为单一结论。
```

（第 3～6 层保持原文。）

- [ ] **Step 3: 修订 §17 Runtime 原型**

将 §17 现有流程图替换为（新增 Model Adapter 与输入携带项）：

```text
Input（可携带 prior_analysis + new_evidence）
↓
Model Adapter（LLM 接入抽象层，所有 LLM 调用经由此层）
↓
Problem Classifier
↓
Framework Selector
↓
Operator Executor（并行）
↓
Cross-Audit（并行单轮）
↓
Evidence Checker
↓
Falsification
↓
Synthesis
↓
Structured Output + Audit Log
```

在 Framework Selector 小节末尾追加：

```markdown
输出契约：问题类型标签 + 框架列表（3～7 个）+ 每个框架一句话命中理由。Runtime 校验数量边界，越界即拒绝。选择理由对用户可见、可质疑，并进入审计日志。
```

并新增小节：

```markdown
### Model Adapter

所有 LLM 调用经由统一适配层。换模型只需换 adapter，编排与契约不变——这是成功标准"不同 LLM 接入后仍能保持基本推理结构"的实现前提。
```

- [ ] **Step 4: 校验**

```bash
grep -q "无状态再分析" "Open_Reasoning_Framework_Prototype_v0.2.md" && grep -q "## 0. 选择理由" "Open_Reasoning_Framework_Prototype_v0.2.md" && grep -q "Model Adapter" "Open_Reasoning_Framework_Prototype_v0.2.md" && echo OK
```
Expected: `OK`

- [ ] **Step 5: Commit**

```bash
git add "Open_Reasoning_Framework_Prototype_v0.2.md"
git commit -m "docs(v0.2): 运行流程/输出协议/Runtime 修订（§9/§13/§17）"
```

---

### Task 6: Cross-Audit 机制与认知差组合器（§11、§12）

**Files:**
- Modify: `Open_Reasoning_Framework_Prototype_v0.2.md` §11、§12

- [ ] **Step 1: 改写 §11 基本流程**

将 §11 的串行流程图替换为：

```text
各框架并行产出结论（互不可见）
↓
攻击者并行攻击（每个攻击者只见被攻击结论，不见其他攻击）
↓
证伪过关（每个重大假设必须带可推翻条件）
↓
Synthesizer 按硬保留规则综合
```

并新增五个小节：

```markdown
### 并行产出

各框架结论同时生成，攻击者互不可见。串行攻击链会让后续调用顺着前序结论走，是"框架互相证明"（风险四）的温床，因此禁止。

### 攻击契约

每次攻击必须产出至少一项实质攻击（冲突 / 反例 / 替代解释 / 推翻条件），或明确声明"无实质攻击"并附已检查项清单。两种结果都进审计日志——既防止编造噪声攻击，也防止默认沉默。

### 证伪过关

每个重大假设必须带可推翻条件，否则不得进入综合。

### 综合硬规则

Synthesizer 不得把仍有未被反驳竞争假设的局面合并成单一结论。"证据不足，无法判断主因"是一等合法输出。

### 轮次

MVP 固定单轮，不迭代。多轮互审在 LLM 场景下天然向收敛漂移且成本翻倍。
```

（保留原 §11 的"员工执行力不足"示例及其输出。）

- [ ] **Step 2: 改写 §12 为组合器定义**

保留 §12 开头"信息差/认知差"定义与"可分析维度"列表，在其后插入架构定位段落：

```markdown
### 架构定位：执行组合器

认知差分析是三类可调用单位中的 Combinator（见第 5、6 节）：

- **输入：** 问题 + 立场 A + 立场 B；
- **执行：** 同一组 Operator 分别按立场 A、立场 B 执行；
- **输出契约：** 下方"典型输出"的六项结构是该组合器的固定输出契约。
```

将原"典型输出"代码块标题改为"输出契约（固定六项）"，保留六项内容。文末"让不同的人在关键问题上共享同一套判断坐标"保留。

- [ ] **Step 3: 校验**

```bash
grep -q "攻击契约" "Open_Reasoning_Framework_Prototype_v0.2.md" && grep -q "综合硬规则" "Open_Reasoning_Framework_Prototype_v0.2.md" && grep -q "架构定位：执行组合器" "Open_Reasoning_Framework_Prototype_v0.2.md" && echo OK
```
Expected: `OK`

- [ ] **Step 4: Commit**

```bash
git add "Open_Reasoning_Framework_Prototype_v0.2.md"
git commit -m "docs(v0.2): Cross-Audit 机制完整化与认知差组合器（§11/§12）"
```

---

### Task 7: 目录结构与评测体系（§16、§18）

**Files:**
- Modify: `Open_Reasoning_Framework_Prototype_v0.2.md` §16、§18

- [ ] **Step 1: 替换 §16 目录结构**

用以下版本完整替换 §16 的目录树（operators 并入 frameworks、新增 adapter、schemas 增加 combinator）：

```text
open-reasoning-framework/
│
├── README.md
├── LICENSE
├── CONTRIBUTING.md
│
├── frameworks/
│   ├── role_and_naming/
│   │   ├── framework.yaml
│   │   └── operators/
│   ├── interest_structure/
│   │   ├── framework.yaml
│   │   └── operators/
│   ├── incentive_structure/
│   │   ├── framework.yaml
│   │   └── operators/
│   ├── power_structure/
│   │   ├── framework.yaml
│   │   └── operators/
│   ├── cognitive_bias/
│   │   ├── framework.yaml
│   │   └── operators/
│   ├── bounded_rationality/
│   │   ├── framework.yaml
│   │   └── operators/
│   ├── system_feedback/
│   │   ├── framework.yaml
│   │   └── operators/
│   └── falsification/
│       ├── framework.yaml
│       └── operators/
│
├── combinators/
│   └── cognitive_gap/
│
├── schemas/
│   ├── framework.schema.json
│   ├── operator.schema.json
│   ├── combinator.schema.json
│   └── output.schema.json
│
├── runtime/
│   ├── adapter/
│   ├── selector/
│   ├── executor/
│   ├── cross_audit/
│   └── synthesizer/
│
├── evaluations/
│   ├── cases/
│   ├── benchmarks/
│   ├── golden_sets/
│   └── regression/
│
├── examples/
│   ├── management/
│   ├── business/
│   ├── policy/
│   └── personal_decision/
│
└── docs/
    ├── philosophy/
    ├── architecture/
    └── governance/
```

并在目录树后追加一句：算子放在所属框架目录下（取消独立 operators 树），避免框架与算子双树漂移。

- [ ] **Step 2: 改写 §18 评测体系**

在 §18.1 基线之后、§18.2 指标之前插入 ground truth 小节，并将指标说明绑定到两阶段：

```markdown
## 18.2 Ground Truth 与两阶段评测

### 阶段一：专家盲评（验证第 28 节核心假设）

- 对每个测试案例，将四基线（裸 LLM 零样本 / 大型系统提示词 / 单一 Framework / 多 Framework + Cross-Audit）的输出混合打乱、隐藏来源；
- 专家成对比较并沿 18.3 指标维度评分；
- 盲评回答一个问题：ORF 是否比基线更稳定地发现遗漏变量、反例与推翻条件。

### 阶段二：渐进 golden 变量集（回归资产）

- 从核心测试案例起，每案例由 2～3 位专家独立预标注"已知重要变量清单"，保留分歧、不强行合并；
- 覆盖率指标落地为对 golden 集的召回率；
- 分工：盲评出结论，golden 集防回归，两者不互相替代。
```

（原 §18.2 核心指标顺延为 §18.3，内容不变。）

- [ ] **Step 3: 校验**

```bash
grep -q "combinator.schema.json" "Open_Reasoning_Framework_Prototype_v0.2.md" && grep -q "golden_sets/" "Open_Reasoning_Framework_Prototype_v0.2.md" && grep -q "Ground Truth 与两阶段评测" "Open_Reasoning_Framework_Prototype_v0.2.md" && ! grep -q "^├── operators/$" "Open_Reasoning_Framework_Prototype_v0.2.md" && echo OK
```
Expected: `OK`

- [ ] **Step 4: Commit**

```bash
git add "Open_Reasoning_Framework_Prototype_v0.2.md"
git commit -m "docs(v0.2): 目录结构合并 operators 树、评测两阶段地基化（§16/§18）"
```

---

### Task 8: 风险与治理修订（§21、§25）

**Files:**
- Modify: `Open_Reasoning_Framework_Prototype_v0.2.md` §21、§25

- [ ] **Step 1: §21 版本治理追加 Schema 变更规则**

在 §21 末尾追加：

```markdown
Schema 字段结构变更（如 localized map、类型化输入输出声明）属破坏性变更，必须走上述变更记录流程。
```

- [ ] **Step 2: 扩写 §25 风险一的"处理"**

将风险一的"处理"段落替换为：

```markdown
**处理：**

强制 Schema 与测试案例只是第一层。完整防线是引擎四层论（见 2.2 节）：

1. Schema 校验——结构正确性强制；
2. 编排纪律——选择、并行、对抗角色指派由 Runtime 决定；
3. 契约强制——输出缺字段即拒绝重跑，攻击者不得沉默；
4. 评测回归——对基线持续对照，逻辑漂移被测试捕获。
```

- [ ] **Step 3: 校验**

```bash
grep -q "属破坏性变更" "Open_Reasoning_Framework_Prototype_v0.2.md" && grep -q "引擎四层论（见 2.2 节）" "Open_Reasoning_Framework_Prototype_v0.2.md" && echo OK
```
Expected: `OK`

- [ ] **Step 4: Commit**

```bash
git add "Open_Reasoning_Framework_Prototype_v0.2.md"
git commit -m "docs(v0.2): 风险一防线扩写与 Schema 变更治理（§21/§25）"
```

---

### Task 9: 全文一致性终审与收尾

**Files:**
- Modify: `Open_Reasoning_Framework_Prototype_v0.2.md`（仅修正发现的不一致）

- [ ] **Step 1: 决议落地检查**

逐条核对 v0.2 修订说明中的八项决议，每项在正文中指出对应章节。任何一条找不到落点，回到对应任务补写。

- [ ] **Step 2: 矛盾检查**

确认以下三组表述全文一致，发现不一致处修改后文就前文：

- MVP 框架数量："8 个"出现在 §14 且与 §7 实际小节（7.1、7.2、7.3、7.4、7.5、7.7、7.8、7.9）吻合；
- 博弈框架：§7.6 标注已移出、§24 长期扩展中含博弈；
- Cross-Audit："并行单轮"在 §11 与 §17 流程图中一致。

- [ ] **Step 3: 残留检查**

```bash
grep -nE "两层原子结构|第一层：Framework" "Open_Reasoning_Framework_Prototype_v0.2.md" || echo CLEAN
```
Expected: `CLEAN`（旧两层表述已全部替换）

- [ ] **Step 4: 编号与引用检查**

通读全文目录编号（§1～§29）连续无跳号；文内所有"见第 N 节"引用指向存在的章节。

- [ ] **Step 5: Commit**

```bash
git add "Open_Reasoning_Framework_Prototype_v0.2.md"
git commit -m "docs(v0.2): 全文一致性终审完成，v0.2 定稿"
```

---

## 验收标准（对照 spec）

1. `Open_Reasoning_Framework_Prototype_v0.1.md` 未被修改（`git diff --stat` 中不出现）；
2. v0.2 头部含八项决议总账；
3. 八项决议均有正文落点（Task 9 Step 1 核对通过）；
4. 无旧表述残留（Task 9 Step 3 输出 CLEAN）；
5. 每个 Task 均有独立 commit，共 9 次。
