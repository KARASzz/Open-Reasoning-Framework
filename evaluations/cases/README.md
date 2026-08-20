# 测试案例集（evaluations/cases）

真实世界脏问题测试集，服务两阶段评测（见原型文档 §18.2 与 §19）：

- **阶段一（专家盲评）**：`problem` + `context` 作为输入，四基线输出混合后由专家成对比较；
- **阶段二（golden 变量集）**：`golden_variables` 由 2～3 位专家独立标注后填充，覆盖率 = 召回率。

## 种子案例格式（暂定，正式 case.schema.json 待评测阶段定义）

```yaml
id: case_<类别>_<序号>        # 全局唯一
category: 类别                 # 企业管理 / AI 转型 / 产品决策 / 项目管理 / 公共治理 / 个人决策
status: seed                   # seed=种子；annotated=已完成 golden 标注
problem: 一句话问题            # 必须是真实世界脏问题，不得用哲学教科书问题
context: 背景事实              # 供分析输入，标注哪些是用户事实
expected_dimensions: []        # 预期应命中的框架 id（提示用，不作评分硬约束）
golden_variables: []           # 阶段二专家标注区，种子阶段为空
combinator_hint: （可选）      # 建议使用的组合器，如 cognitive_gap
```

## 当前状态

10 个种子案例，覆盖六类场景。目标规模 30～50 个（§19）。
