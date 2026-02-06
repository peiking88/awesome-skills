# Skills 列表

> **注意**：本仓库使用Git子模块管理各个skill项目。由于代码目录中的子模块链接指向外部仓库，直接点击可能会遇到404错误。**请使用下方表格中的链接访问各项目**，或查看[.gitmodules](.gitmodules)获取完整仓库地址。

## 快速入口

- 官方仓库必装清单（本地整理）：[Agent Skills Essential Checklist.md](Agent Skills Essential Checklist.md)
- HTML → Markdown 通用转换脚本：[html2md.py](html2md.py)
- 本仓库详细清单：[skills-detail.md](skills-detail.md)
- 子模块配置文件：[.gitmodules](.gitmodules)

## 流行Skill仓库

| 名称 | 描述 | 脚本 | 参考资料 | 资源 |
|------|------|------|----------|------|
| [Agent Skills Platform](https://agentskills.io/) | 开放的Skill平台 | 支持Anthropic开发的开放标准，支持多AI平台 | 有 | 有 |
| [SkillsMP](https://skillsmp.com/) | AI Skill市场平台，提供Skill发现、管理和分发服务。支持多种AI代理工具的skill集成 | 包含市场功能和skill管理工具 | 有 | 有 |
| [Agent Skills for Context Engineering](https://bgithub.xyz/muratcankoylan/Agent-Skills-for-Context-Engineering) | 上下文工程的综合skill集合，用于构建生产级AI代理系统。涵盖上下文基础、多智能体模式、内存系统、工具设计、评估和项目开发 | 包含多个skill子文件夹，每个skill包含SKILL.md和可选的scripts/目录 | 有 | 有 |
| [Anthropic Skills Collection](https://bgithub.xyz/anthropics/skills) | Anthropic官方skill集合，演示Claude skill的可能性。包括创意应用(艺术、设计)、技术任务(测试Web应用、MCP服务器生成)、企业工作流(沟通、品牌等) | 包含 16 个官方 skills：algorithmic-art、brand-guidelines、canvas-design、doc-coauthoring、docx、frontend-design、internal-comms、mcp-builder、pdf、pptx、skill-creator、slack-gif-creator、theme-factory、web-artifacts-builder、webapp-testing、xlsx（见 Anthropic_skills/skills/ 与 Agent Skills Essential Checklist.md） | 有 | 有 |
| [Skill Seeker](https://bgithub.xyz/yusufkaraaslan/Skill_Seekers) | 自动化工具，将文档网站、GitHub仓库和PDF文件转换为生产就绪的Claude AI skill。支持多源统一抓取、冲突检测、AI增强等功能 | Python源码，包括文档抓取、GitHub抓取、PDF抓取脚本和MCP服务器 | 有 | 有 |
| [Hugging Face Skills](https://bgithub.xyz/huggingface/skills) | Hugging Face Hub操作的skill定义，包括数据集创建、模型训练、评估、论文发布等。兼容多种AI编码工具 | 包含8个skill和Python脚本目录，支持AI生成代理 | 有 | 有 |
| [My Skills Hub](https://bgithub.xyz/bear2u/my-skills) | Claude Code的定制skill集合，提高开发生产力。包含Flutter/Next.js项目初始化、代码变更文档化、Codex集成、Web到Markdown转换、卡片新闻生成等18+skill | 包含18+skill和JavaScript脚本(如extract-markdown.js、fetch-dynamic-content.js) | 有 | 有 |
| [Claude Skills Marketplace](https://bgithub.xyz/mhattingpete/claude-skills-marketplace) | Claude Code软件工程工作流的精选插件市场。包含工程工作流插件、可视化文档插件、生产力skill插件、代码操作插件等 | 4个插件目录和执行运行时(MCP服务器、Python API) | 有 | 有 |
| [Build with Claude Marketplace](https://bgithub.xyz/davepoon/buildwithclaude) | Claude Code插件市场和发现平台。包含117个Agent、175个命令、28个Hook、26个skill、50个插件的精选集合 | 包含大量脚本，如marketplace生成、验证和抓取脚本，以及Next.js Web UI | 有 | 有 |
| [ClaudeKit Agent Skills](https://bgithub.xyz/mrgoonie/claudekit-skills) | 专业skill集合，涵盖后端开发、前端开发、AI/ML、DevOps、调试、问题解决、可视化、文档处理等多个领域 | 包含30+skill和多个脚本(Chrome DevTools、MCP管理) | 有 | 有 |
| [N-Skills Universal Marketplace](https://bgithub.xyz/numman-ali/n-skills) | "一次编写，随处运行"的通用市场。支持Claude Code、GitHub Copilot、Codex、Cursor、Windsurf等所有AI代理 | 包含同步脚本(如sync-external.mjs、update-registry.mjs) | 有 | 有 |
| [OpenSkills Universal Installer](https://bgithub.xyz/numman-ali/openskills) | 通用skill安装器，支持所有AI代理。支持从Git仓库安装、skill验证、导出等功能 | TypeScript CLI，包含核心命令和功能模块 | 有 | 有 |
| [Agent Skills CLI](https://bgithub.xyz/Karanjot786/agent-skills-cli) | 单一CLI，50000+skill，支持所有AI代理。可以从市场安装skill、搜索、验证、导出等 | TypeScript CLI核心和多个核心源文件 | 有 | 有 |
| [Agent Skills (Vercel)](https://bgithub.xyz/vercel-labs/agent-skills) | AI coding agent skills集合，含React/Next最佳实践、Web设计审查、Vercel部署等 | 包含多个skills定义 | 有 | 有 |
| [Vercel Labs Skills](https://bgithub.xyz/vercel-labs/skills) | 开放agent skill生态系统CLI工具，支持40+种AI代理。提供skill安装、查找、更新、移除等功能 | TypeScript CLI，包含find-skills等skill；本地路径：`vercel-labs-skills/` | 有 | 有 |
| [n8n-skills](https://bgithub.xyz/czlonkowski/n8n-skills) | 基于n8n-mcp的工作流构建技能集合（7个skills） | 无主要脚本 | 有 | 有 |
| [Claude Store](https://bgithub.xyz/13331112522/claude-store) | Claude Code技巧/命令/技能/代理配置的个人合集 | 包含skills、commands、agents与工具目录 | 有 | 有 |
| [UI UX Pro Max Skill](https://bgithub.xyz/nextlevelbuilder/ui-ux-pro-max-skill) | 提供跨平台UI/UX设计智能与设计系统生成能力 | 包含skill与CLI资源 | 有 | 有 |
| [Claude Scientific Skills](https://bgithub.xyz/K-Dense-AI/claude-scientific-skills) | 140个科学skill的综合集合，涵盖生物信息学、化学信息学、蛋白质组学、临床研究、医疗AI、机器学习等多个科学领域 | 包含140+skill，每个skill包含SKILL.md和示例代码 | 有 | 有 |
| [Obsidian Skills](https://bgithub.xyz/kepano/obsidian-skills) | 用于Obsidian的Agent Skills，创建和编辑兼容Obsidian的纯文本文件(OFM、.base、.canvas) | 无主要脚本文件 | 有 | 有 |
| [Superpowers](https://bgithub.xyz/obra/superpowers) | 完整的软件开发工作流，基于可组合的"skill"和初始指令。包含测试驱动开发、系统调试、协作、子智能体驱动开发等 | 包含核心库脚本和多个功能脚本 | 有 | 有 |
| [Planning with Files](https://bgithub.xyz/OthmanAdi/planning-with-files) | 使用持久化Markdown文件进行规划、进度跟踪和知识存储的Claude Code插件。基于Manus AI的模式 | 包含脚本目录和模板文件 | 有 | 有 |
| [Awesome Claude Skills Collection](https://bgithub.xyz/VoltAgent/awesome-claude-skills) | Claude skill的精选列表，包含多个版本(awesome-claude-skills、awesome-claude-skills_1、awesome-claude-skills_2) | 无主要脚本 | 有 | 无 |
| [Awesome Obsidian](https://bgithub.xyz/kmaasrud/awesome-obsidian) | Obsidian插件、主题等资源的精选列表 | 无主要脚本 | 有 | 有 |
| [Obsidian Dataview Plugin](https://bgithub.xyz/blacksmithgu/obsidian-dataview) | Obsidian的Dataview插件源码，提供强大的数据查询和可视化功能 | TypeScript源码，包含main.ts、api/、query/、ui/等模块 | 有 | 有 |
| [Obsidian Git Plugin](https://bgithub.xyz/Vinzent03/obsidian-git) | Obsidian的Git集成插件源码，自动提交和同步Obsidian笔记 | TypeScript源码，包含main.ts、automaticsManager.ts、commands.ts等 | 有 | 有 |
| [Obsidian Releases](https://bgithub.xyz/obsidianmd/obsidian-releases) | Obsidian发布信息数据库，跟踪插件、主题、桌面应用的版本 | Python数据处理脚本 | 有 | 有 |
| [Whenwords](https://bgithub.xyz/dbreunig/whenwords) | 一个只有Skill的代码库，用于上下文窗口管理的工具，使用文件系统作为持久化记忆 | 包含测试配置文件 | 有 | 无 |
| [Skills.sh](https://skills.sh/) | 开放Agent Skill生态系统，提供skill目录和安装工具。支持36,000+ skill安装，包含排行榜和搜索功能 | 提供`npx skills add`命令行工具 | 有 | 有 |
| [Vercel Skills CLI](https://bgithub.xyz/vercel-labs/add-skill) | 开放agent skill生态系统CLI工具，支持40+种AI代理。提供skill安装、查找、更新、移除等功能 | TypeScript CLI，支持40+种代理（Claude Code、Cursor、Codex、OpenCode等） | 有 | 有 |
| [C++ Core Guidelines Skills](https://bgithub.xyz/peiking88/cppcoreguidelines-skills) | C++代码审查实用工具包，基于C++ Core Guidelines的审查工作流和检查清单 | 提供SKILL.md定义和references/目录下的章节参考文档 | 有 | 有 |
| [Trail of Bits Skills](https://bgithub.xyz/trailofbits/skills) | 安全研究、漏洞检测和审计工作流的Claude Code skill市场。包含20+安全相关skill | Python脚本、YARA规则、CodeQL查询、Semgrep规则等 | 有 | 有 |
| [Vue Skills (vuejs-ai)](https://bgithub.xyz/hyf0/vue-skills) | Vue 3开发的Agent skill集合。包含8个skill涵盖最佳实践、路由、Pinia、测试、JSX等 | 8个skill：vue-best-practices、vue-router-best-practices、vue-pinia-best-practices、vue-testing-best-practices、vue-jsx-best-practices、vue-development-guides、vue-debug-guides、create-adaptable-composable | 有 | 有 |
| [Three.js Skills](https://bgithub.xyz/CloudAI-X/threejs-skills) | Three.js skill文件集合，为Claude Code提供3D开发基础知识。包含10个skill | 10个skill：threejs-fundamentals、threejs-geometry、threejs-materials、threejs-lighting、threejs-textures、threejs-animation、threejs-loaders、threejs-shaders、threejs-postprocessing、threejs-interaction | 有 | 有 |
| [Nuxt Skills](https://bgithub.xyz/onmax/nuxt-skills) | Vue、Nuxt和NuxtHub的AI编程助手skill集合。包含17个skill | 17个skill：vue、nuxt、nuxt-modules、nuxthub、nuxt-content、nuxt-ui、nuxt-better-auth、reka-ui、document-writer、ts-library、motion、vueuse、nuxt-seo、vitest、vite、pnpm、tsdown | 有 | 有 |
| [VueUse Skills](https://bgithub.xyz/vueuse/skills) | VueUse组合式工具库的Agent skill。提供渐进式披露、最小token使用、离线优先设计 | vueuse-functions skill，包含VueUse所有组合式函数的参考文档 | 有 | 有 |
| [Vercel Labs Skills](https://bgithub.xyz/vercel-labs/skills) | 开放agent skill生态系统CLI工具，支持40+种AI代理。提供skill安装、查找、更新、移除等功能 | TypeScript CLI，包含find-skills等skill；本地路径：`vercel-labs-skills/` | 有 | 有 |
| [Antfu Skills](https://bgithub.xyz/antfu/skills) | Anthony Fu的个人skill集合，包含Vue、Nuxt、TypeScript等开发工具的skill | 多个skill文件 | 有 | 无 |
| [Awesome OpenClaw Skills](https://bgithub.xyz/VoltAgent/awesome-openclaw-skills) | OpenClaw技能精选列表，包含多个skill集合 | 无主要脚本 | 有 | 无 |
| [Alirezarezvani Claude Skills](https://bgithub.xyz/alirezarezvani/claude-skills) | Claude技能集合，包含多种实用skill | 多个skill目录 | 有 | 有 |
| [Videocut Skills](https://bgithub.xyz/Ceeon/videocut-skills) | 视频剪辑相关skill | 无主要脚本 | 有 | 有 |
| [Skill from Masters](https://bgithub.xyz/GBSOSS/skill-from-masters) | 从专家收集的skill集合 | 无主要脚本 | 有 | 有 |
| [Khazix Skills](https://bgithub.xyz/KKKKhazix/Khazix-Skills) | 个人skill集合 | 无主要脚本 | 有 | 有 |
| [NotebookLM Skill](https://bgithub.xyz/PleasePrompto/notebooklm-skill) | NotebookLM相关skill | 无主要脚本 | 有 | 有 |
| [Humanizer](https://bgithub.xyz/blader/humanizer) | 文本人性化处理skill | 无主要脚本 | 有 | 有 |
| [Auto Redbook Skills](https://bgithub.xyz/comeonzhj/Auto-Redbook-Skills) | 小红书自动化skill | 无主要脚本 | 有 | 有 |
| [Postgres Skill](https://bgithub.xyz/digoal/postgres_skill) | PostgreSQL数据库skill | 无主要脚本 | 有 | 有 |
| [Humanizer ZH](https://bgithub.xyz/op7418/Humanizer-zh) | 中文文本人性化处理skill | 无主要脚本 | 有 | 有 |
| [Youtube Clipper Skill](https://bgithub.xyz/op7418/Youtube-clipper-skill) | YouTube视频剪辑skill | 无主要脚本 | 有 | 有 |
| [Skills Hub](https://bgithub.xyz/qufei1993/skills-hub) | 技能集合中心 | 无主要脚本 | 有 | 有 |
| [Repo2Skill](https://bgithub.xyz/zhangyanxs/repo2skill) | 将仓库转换为skill的工具 | 无主要脚本 | 有 | 有 |
| [AgentSkills](https://bgithub.xyz/agentskills/agentskills) | AgentSkills核心仓库 | 无主要脚本 | 有 | 有 |

## Agent Skills 必装清单（以官方仓库为准）

- **官方仓库**：https://bgithub.xyz/anthropics/skills
- **本地路径**：`/home/li/awesome-skills/Anthropic_skills/skills/`

> 说明：本清单仅保留 Anthropic 官方仓库中真实存在、并已在本地下载的 skills。

### 1. frontend-design

- **功能**：生成更有个性的前端设计稿/落地页风格建议
- **适合人群**：独立开发者、前端工程师
- **场景**：做落地页、H5、个人项目时，希望设计更有特色
- **URL**：https://bgithub.xyz/anthropics/skills/tree/main/skills/frontend-design

### 2. web-artifacts-builder

- **功能**：创建多文件 React 项目（支持 Tailwind + shadcn/ui），不只是单文件组件
- **适合人群**：需要快速原型开发的全栈工程师
- **场景**：验证想法、做 MVP、内部工具
- **URL**：https://bgithub.xyz/anthropics/skills/tree/main/skills/web-artifacts-builder

### 3. webapp-testing（基于 Playwright）

- **功能**：自动化测试本地 Web 应用，捕获截图、查看日志
- **适合人群**：前端开发者、QA
- **场景**：功能测试、UI 回归测试
- **URL**：https://bgithub.xyz/anthropics/skills/tree/main/skills/webapp-testing

### 4. mcp-builder

- **功能**：快速创建 MCP 服务器（Python/TypeScript），让 Claude 访问外部 API 或数据库
- **适合人群**：需要扩展 Claude 能力的开发者
- **场景**：连接内部 API、数据库查询、第三方服务集成
- **URL**：https://bgithub.xyz/anthropics/skills/tree/main/skills/mcp-builder

### 5. skill-creator

- **功能**：引导创建高质量自定义 Skill（包含初始化/打包脚本）
- **适合人群**：想扩展 AI 能力的高级用户、团队工具负责人
- **场景**：团队内部工作流定制
- **URL**：https://bgithub.xyz/anthropics/skills/tree/main/skills/skill-creator

### 6. internal-comms

- **功能**：撰写内部沟通文档（状态报告、更新、FAQ 等）
- **适合人群**：团队 Leader、产品经理
- **场景**：周报、项目更新、团队公告
- **URL**：https://bgithub.xyz/anthropics/skills/tree/main/skills/internal-comms

### 7. doc-coauthoring

- **功能**：提供“上下文收集 → 结构化迭代 → 读者测试”的文档共创工作流
- **适合人群**：团队协作者、项目经理、技术负责人
- **场景**：写 PRD、RFC、设计文档、提案、决策记录
- **URL**：https://bgithub.xyz/anthropics/skills/tree/main/skills/doc-coauthoring

### 8. pdf

- **功能**：PDF 文本/表格提取、表单抽取、合并/拆分等
- **适合人群**：技术写作者、数据整理人员
- **场景**：从 PDF 抽取结构化数据、生成报告素材
- **URL**：https://bgithub.xyz/anthropics/skills/tree/main/skills/pdf

### 9. docx

- **功能**：Word 文档创建/编辑/分析（支持 OOXML 工具链）
- **适合人群**：技术写作者、内容创作者
- **场景**：生成/修改 Word 报告、从 docx 提取内容
- **URL**：https://bgithub.xyz/anthropics/skills/tree/main/skills/docx

### 10. pptx

- **功能**：PowerPoint 演示文稿创建/编辑/分析（含 HTML→PPTX 工具）
- **适合人群**：产品经理、咨询/汇报场景用户
- **场景**：自动生成演示文稿、批量替换/重排幻灯片内容
- **URL**：https://bgithub.xyz/anthropics/skills/tree/main/skills/pptx

### 11. xlsx

- **功能**：Excel 电子表格创建/编辑/分析（含公式重算脚本）
- **适合人群**：数据分析师、运营人员
- **场景**：报表自动化、表格数据处理
- **URL**：https://bgithub.xyz/anthropics/skills/tree/main/skills/xlsx

### 12. brand-guidelines

- **功能**：将 Anthropic 官方品牌色与排版规范应用到各类 artifact
- **适合人群**：设计师、品牌维护者
- **场景**：对外/对内材料统一视觉风格
- **URL**：https://bgithub.xyz/anthropics/skills/tree/main/skills/brand-guidelines

### 13. theme-factory

- **功能**：为各类 artifact（Slides/Docs/HTML 等）应用主题（内置 10 套配色/字体主题，也可临时生成新主题）
- **适合人群**：需要快速统一视觉风格的内容产出者
- **场景**：演示稿/报告一键换肤、不同场景快速套主题
- **URL**：https://bgithub.xyz/anthropics/skills/tree/main/skills/theme-factory

### 14. canvas-design

- **功能**：生成美观的视觉设计（PNG/PDF）
- **适合人群**：内容创作者、设计师
- **场景**：公众号封面、活动海报
- **URL**：https://bgithub.xyz/anthropics/skills/tree/main/skills/canvas-design

### 15. algorithmic-art

- **功能**：使用 p5.js 生成算法艺术（可控随机种子与参数探索）
- **适合人群**：创意编程者、数字艺术家
- **场景**：生成艺术作品、动态视觉效果
- **URL**：https://bgithub.xyz/anthropics/skills/tree/main/skills/algorithmic-art

### 16. slack-gif-creator

- **功能**：制作适合 Slack 的动画 GIF（带构建与校验工具）
- **适合人群**：团队沟通者、内容创作者
- **场景**：团队表情包、教程演示、产品展示
- **URL**：https://bgithub.xyz/anthropics/skills/tree/main/skills/slack-gif-creator

### 三、按领域选 Skills（官方仓库）

#### 开发类
- webapp-testing（见上文）
- mcp-builder（见上文）
- web-artifacts-builder（见上文）
- skill-creator（见上文）

#### 设计类
- frontend-design（见上文）
- canvas-design（见上文）
- algorithmic-art（见上文）
- brand-guidelines（见上文）
- theme-factory（见上文）
- slack-gif-creator（见上文）

#### 文档/办公类
- doc-coauthoring（见上文）
- internal-comms（见上文）
- pdf（见上文）
- docx（见上文）
- pptx（见上文）
- xlsx（见上文）

### 四、三个平台对比：官方仓库 vs SkillsMP vs Awesome 合集

#### 1. 官方仓库：bgithub.xyz/anthropics/skills

- 特点：质量最高，官方示例与最佳实践（当前仓库含 16 个示例 skills，已全部作为子模块添加）
- 适合：学习最佳实践、需要稳定可靠的 skills
- 不足：数量有限，更新频率相对较慢

#### 2. SkillsMP：skillsmp.com

- 特点：第三方平台，数量多，支持搜索/分类/热度
- 适合：快速发现新 skills、按关键词搜索
- 不足：质量参差不齐，需要自行筛选

#### 3. Awesome 合集

- 特点：社区维护，有人工筛选与分类，通常附带说明
- 适合：深度挖掘小众需求、看别人推荐与评价
- 不足：更新不一定及时，不同合集质量差异大

---

## 统计信息

| 类别 | 数量 |
|------|------|
| 主要项目 | 52 |
| 独立SKILL.md文件 | 400+ |
| 脚本文件(.js, .ts, .py) | 500+ |
| 参考文档(.md) | 500+ |
| 配置文件(.json, .yaml) | 210+ |
| 插件市场项目 | 9+ |

## 主要skill类别

- **上下文工程** - Agent Skills for Context Engineering、Agent Skills Platform
- **skill市场** - SkillsMP、Claude Skills Marketplace、N-Skills、Skills.sh、Vercel Skills CLI、Vercel Labs Skills
- **文档处理** - PDF、DOCX、PPTX、XLSX skill
- **软件开发** - 后端、前端、全栈开发skill、Vue、Nuxt、Three.js
- **科学计算** - 生物信息、化学、蛋白质组学等
- **AI/ML** - 机器学习、深度学习skill
- **工作流自动化** - Git、测试、代码审查
- **可视化** - 图表、架构图、流程图
- **DevOps** - Docker、K8s、云平台
- **数据库** - MongoDB、PostgreSQL
- **工具管理** - MCP服务器、skill验证、安全审计、C++代码审查

## 安装方式

大部分skill支持以下安装方式：

1. **Claude Code Plugin Marketplace** - 最推荐
2. **手动安装** - 复制到 `~/.claude/skills/`
3. **MCP服务器** - 通过MCP协议使用
4. **通用安装器** (OpenSkills、Agent Skills CLI、Vercel Labs Skills CLI)

## 新增子模块

### vercel-labs/skills

- **仓库地址**: https://bgithub.xyz/vercel-labs/skills
- **本地路径**: `/home/li/awesome-skills/vercel-labs-skills/`
- **描述**: 开放agent skill生态系统CLI工具，支持40+种AI代理
- **主要功能**:
  - `npx skills add` - 安装skill
  - `npx skills find` - 搜索skill
  - `npx skills list` - 列出已安装skill
  - `npx skills remove` - 移除skill
  - `npx skills check` - 检查更新
  - `npx skills update` - 更新skill
- **包含skill**: find-skills（帮助用户发现和安装agent skills）
- **安装状态**: 已安装并构建完成

---

*注：所有项目都是开源的，遵循MIT、Apache 2.0等开源许可证。*
