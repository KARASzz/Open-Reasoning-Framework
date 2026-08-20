# TODO — ORF 开发路线图

> 总原则：**先证明核心假设**（结构化 Reasoning Operators + 多框架互审是否优于裸 LLM 与大系统提示词），再谈工程化、社区与生态。质量比数量重要。

## ✅ 已完成

- [x] v0.1 原型文档（`Open_Reasoning_Framework_Prototype_v0.1.md`）
- [x] 八项设计决议（算子定位、认知差组合器、MVP 框架集、互审编排、选择机制、交互模型、评测地基、语言策略）
- [x] v0.2 升级设计 spec（`docs/superpowers/specs/2026-08-20-orf-prototype-v0.2-design.md`）
- [x] v0.2 实施计划（`docs/superpowers/plans/2026-08-20-orf-prototype-v0.2-upgrade.md`）
- [x] README 与 TODO
- [x] v0.2 原型文档定稿（`Open_Reasoning_Framework_Prototype_v0.2.md`，八项决议全部落地）

## ✅ 已完成：v0.2 原型文档升级

按实施计划的 9 个任务执行：

- [x] Task 1：创建 v0.2 底稿与修订说明（八项决议总账）
- [x] Task 2：三类可调用单位与引擎论证（§2/§5/§6）
- [x] Task 3：补写激励结构、权力关系框架 + 全部边界判据 + 博弈移入扩展（§7/§24）
- [x] Task 4：Operator Schema 类型化 + i18n 结构 + 边界判据（§8）
- [x] Task 5：运行流程 / 输出协议 / Runtime + Model Adapter（§9/§13/§17）
- [x] Task 6：Cross-Audit 机制完整化 + 认知差组合器（§11/§12）
- [x] Task 7：目录结构（operators 并入 frameworks）+ 评测两阶段地基化（§16/§18）
- [x] Task 8：风险一防线扩写 + Schema 变更治理（§21/§25）
- [x] Task 9：全文一致性终审，v0.2 定稿

## ⏭️ 阶段一：内容建设（下一步）

- [ ] 定义 JSON Schema：`framework.schema.json`、`operator.schema.json`、`combinator.schema.json`、`output.schema.json`
- [ ] 人工制作首批 8 个 Framework 定义文件（含边界判据）
- [ ] 构建 60～100 个高质量 Operators（每个：标准问题、证据要求、≥2 反例、失效条件、类型化输入输出）
- [ ] 实现认知差组合器的首个实例
- [ ] 制作 30～50 个真实世界脏问题测试集（企业管理 / AI 转型 / 产品决策 / 项目管理 / 公共治理 / 个人决策）

## ⏭️ 阶段二：最小 Runtime

- [ ] Model Adapter（LLM 接入抽象层）
- [ ] Problem Classifier
- [ ] Framework Selector（LLM 选择 + 强制理由 + 3～7 数量校验）
- [ ] Operator Executor（并行执行，产出累积进推理图）
- [ ] Cross-Audit（并行单轮 + 攻击契约 + 证伪过关）
- [ ] Synthesizer（硬保留规则）
- [ ] 结构化输出 + 审计日志
- [ ] 无状态再分析协议（prior_analysis + new_evidence）

## ⏭️ 阶段三：评测与假设验证

- [ ] 建立四基线：裸 LLM 零样本 / 大型系统提示词 / 单一 Framework / 多 Framework + Cross-Audit
- [ ] 专家盲评协议（成对比较、隐藏来源、按七项指标评分）
- [ ] 渐进建设 golden 变量集（每案例 2～3 位专家独立标注、保留分歧）
- [ ] 对照评测，验证核心假设
- [ ] **决策点：假设不成立 → 停止扩张；成立 → 进入阶段四**

## 📅 长期（假设验证通过后才启动）

- [ ] Reasoning API（Layer 3：`/analyze`、`/frameworks/select`、`/operators/run`、`/cross-audit`、`/falsify`）
- [ ] 可视化界面（Layer 4：推理路径与框架冲突展示）
- [ ] 扩展框架（博弈、亚里士多德目的与德性、韦伯制度、贝叶斯推理、因果推断、第一性原理、OODA、红队分析等——必须转换为 Framework/Operator，不得因人物知名而加入）
- [ ] CONTRIBUTING 与社区贡献流程（Schema 校验 / 重复性检查 / 测试案例 / 人工 Review）
- [ ] 开源许可证选定与项目正式命名（当前 ORF 为暂定名）

## ❌ 明确不做（第一阶段）

用户系统、社区积分、复杂前端、大型知识图谱、多 Agent 自主协作、私有模型训练、向量数据库大规模收录哲学原文、"100 位哲学家人格"。
