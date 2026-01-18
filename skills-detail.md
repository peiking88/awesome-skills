# skill详细清单

## 官方 Anthropic Skills（已全部下载）

- **官方仓库**：https://bgithub.xyz/anthropics/skills
- **本地路径**：`/home/li/awesome-skills/Anthropic_skills/skills/`
- **清单**：algorithmic-art、brand-guidelines、canvas-design、doc-coauthoring、docx、frontend-design、internal-comms、mcp-builder、pdf、pptx、skill-creator、slack-gif-creator、theme-factory、web-artifacts-builder、webapp-testing、xlsx

| 名称 | 描述 | 脚本 | 参考资料 | 资源 |
|------|------|------|----------|------|
| Agent-Skills-for-Context-Engineering | 上下文工程的综合skill集合，用于构建生产级AI代理系统。涵盖上下文基础、多智能体模式、内存系统、工具设计、评估和项目开发 | 包含多个skill子文件夹，每个skill包含SKILL.md和可选的scripts/目录 | 有 | 有 |
| Agent Skills Platform | 开放的skill格式标准，为AI代理提供新能力和专业知识。支持领域专业知识打包、新能力扩展、可重复工作流和多代理互操作 | 由Anthropic开发的开放标准，支持多AI平台 | 有 | 有 |
| SkillsMP | AI skill市场平台，提供skill发现、管理和分发服务。支持多种AI代理工具的skill集成 | 包含市场功能和skill管理工具 | 有 | 有 |
| context-engineering-collection | 上下文工程skill的综合集合，用于构建、优化或调试需要有效上下文管理的AI代理系统 | 无特定脚本（集合类skill） | 有 | 有 |
| algorithmic-art | 使用p5.js创建算法艺术，支持随机种子和交互式参数探索 | 无特定脚本（但包含HTML模板生成） | 无 | 有（templates/viewer.html等） |
| brand-guidelines | 应用Anthropic官方品牌色彩和排版到各类工件 | 无 | 无 | 无 |
| canvas-design | 创建美观的视觉艺术PNG和PDF文档 | 无特定脚本 | 无 | 有（canvas-fonts目录包含字体文件） |
| doc-coauthoring | 指导用户通过结构化工作流进行文档协作编写 | 无 | 无 | 无 |
| docx | Word文档的创建、编辑和分析，支持修订跟踪、注释、格式保持和文本提取 | ooxml/scripts/unpack.py - 解压OOXML文件；ooxml/scripts/pack.py - 打包OOXML文件；ooxml/scripts/validate.py - 验证OOXML文件 | 有 | 有（ooxml/目录和reference/目录） |
| frontend-design | 创建独特、生产级的前端界面，具有高设计质量 | 无特定脚本 | 无 | 无 |
| internal-comms | 帮助撰写各类内部沟通内容的资源集合 | 无 | 有（examples/目录下的示例文件） | 有（examples/3p-updates.md等示例文件） |
| mcp-builder | 创建高质量MCP服务器的指南 | 无 | 有（reference/mcp_best_practices.md、reference/python_mcp_server.md等） | 有（reference/目录） |
| pdf | PDF处理工具包，支持文本和表格提取、创建新PDF、合并/拆分文档 | 无Python脚本（使用pypdf、pdfplumber、reportlab等库） | 有（reference.md、forms.md） | 有（reference/目录） |
| pptx | PowerPoint演示文稿的创建、编辑和分析 | scripts/html2pptx.js - HTML转PPTX；scripts/rearrange.py - 重新排列幻灯片；scripts/inventory.py - 提取文本清单；scripts/replace.py - 替换文本；scripts/thumbnail.py - 生成缩略图；ooxml/scripts/unpack.py - 解压OOXML；ooxml/scripts/pack.py - 打包OOXML；ooxml/scripts/validate.py - 验证OOXML | 有（html2pptx.md、ooxml.md等） | 有（reference/目录、templates/目录） |
| skill-creator | 创建有效skill的指南 | scripts/init_skill.py - 初始化新skill；scripts/package_skill.py - 打包skill | 有（references/workflows.md、references/output-patterns.md等） | 有（references/目录、assets/目录） |
| slack-gif-creator | 为Slack创建优化动画GIF的知识和实用工具 | core/gif_builder.py - GIF构建器；core/validators.py - 验证器；core/easing.py - 缓动函数；core/frame_composer.py - 帧合成器 | 无 | 有（core/目录） |
| theme-factory | 使用主题样式化工件的工具包 | 无 | 无 | 有（theme-showcase.pdf、themes/目录） |
| web-artifacts-builder | 使用现代前端Web技术创建复杂的claude.ai HTML工件的工具套件 | scripts/init-artifact.sh - 初始化项目；scripts/bundle-artifact.sh - 打包HTML工件 | 有（https://ui.shadcn.com/docs/components） | 无特定资源文件 |
| webapp-testing | 使用Playwright与本地Web应用交互和测试的工具包 | scripts/with_server.py - 管理服务器生命周期；examples/element_discovery.py - 元素发现示例；examples/static_html_automation.py - 静态HTML自动化示例；examples/console_logging.py - 控制台日志示例 | 有（examples/目录下的示例） | 有（examples/目录） |
| xlsx | Excel电子表格的创建、编辑和分析，支持公式、格式化、数据分析和可视化 | recalc.py - 重新计算Excel公式 | 无 | 无 |
| planning-with-files | 实现基于文件的复杂任务规划，创建task_plan.md、findings.md和progress.md文件 | scripts/init-session.sh - 初始化所有规划文件；scripts/check-complete.sh - 验证所有阶段是否完成 | 有（reference.md、examples.md） | 有（templates/目录下的模板文件） |
| template-skill | 创建新skill的模板 | 无 | 无 | 无 |
| book-sft-pipeline | 书籍SFT训练管道 | 无特定脚本 | 有 | 有 |
| digital-brain-skill | 数字大脑个人操作系统 | 无特定脚本 | 有 | 有 |
| interleaved_thinking | 交错思考 | 无特定脚本 | 有 | 有 |
| advanced-evaluation | 高级评估技术（LLM-as-Judge） | 各skill特定脚本 | 有 | 有（reference/目录和外部资源链接） |
| bdi-mental-states | BDI思维状态建模 | 各skill特定脚本 | 有 | 有（reference/目录） |
| context-compression | 上下文压缩策略 | 各skill特定脚本 | 有 | 有（reference/目录） |
| context-degradation | 上下文退化模式 | 各skill特定脚本 | 有 | 有（reference/目录） |
| context-fundamentals | 上下文工程基础 | 各skill特定脚本 | 有 | 有（reference/目录） |
| context-optimization | 上下文优化技术 | 各skill特定脚本 | 有 | 有（reference/目录） |
| evaluation | 代理系统评估方法 | 各skill特定脚本 | 有 | 有（reference/目录） |
| filesystem-context | 基于文件系统的上下文工程 | 各skill特定脚本 | 有 | 有（reference/目录） |
| hosted-agents | 托管代理基础设施 | 各skill特定脚本 | 有 | 有（reference/目录） |
| memory-systems | 记忆系统设计 | 各skill特定脚本 | 有 | 有（reference/目录） |
| multi-agent-patterns | 多代理架构模式 | 各skill特定脚本 | 有 | 有（reference/目录） |
| project-development | 项目开发方法论 | 各skill特定脚本 | 有 | 有（reference/目录） |
| tool-design | 代理工具设计 | 各skill特定脚本 | 有 | 有（reference/目录） |
| deep-researcher | 深度研究工作流 | TypeScript CLI核心和多个核心源文件 | 有 | 有 |
| test-skill | 测试skill模板 | 无特定脚本 | 有 | 无 |
| adaptyv | 云实验室平台，用于自动化蛋白质测试和验证 | 无特定脚本 | 有 | 有 |
| aeon | 时间序列机器学习工具包 | 无特定脚本 | 有 | 有 |
| alphafold-database | 访问AlphaFold 200M+ AI预测的蛋白质结构。通过UniProt ID检索结构，下载PDB/mmCIF文件，分析置信度指标（pLDDT、PAE），用于药物发现和结构生物学 | 无特定脚本（使用Biopython访问） | 有（references/api_reference.md包含完整的API文档、文件格式、数据架构、高级查询示例） | 有（包含references/api_reference.md和外部资源链接） |
| anndata | 用于单细胞分析带注释矩阵的数据结构。用于处理.h5ad文件或与scverse生态系统集成。这是数据格式skill - 用于分析工作流使用scanpy；用于概率模型使用scvi-tools；用于群体规模查询使用cellxgene-census | 无特定脚本 | 有（references/data_structure.md、references/io_operations.md、references/concatenation.md等） | 无 |
| arboreto | 从基因表达数据使用可扩展算法（GRNBoost2、GENIE3）推断基因调控网络（GRNs）。支持分布式计算处理大规模数据集 | scripts/basic_grn_inference.py - 基础GRN推断的标准推理任务 | 有（references/basic_inference.md、references/algorithms.md、references/distributed_computing.md等） | 有（references/目录和脚本文件） |
| astropy | 天文学和天体物理学综合Python库。用于处理天文学数据，包括天体坐标、物理单位、FITS文件、宇宙学计算、时间系统、表格、世界坐标系（WCS）和天文学数据分析 | 无特定脚本 | 有（references/units.md、references/coordinates.md、references/cosmology.md、references/fits.md、references/tables.md、references/time.md、references/wcs_and_other_modules.md等） | 无 |
| benchling-integration | Benchling R&D平台集成。通过API访问注册表（DNA、蛋白质）、库存、ELN条目、工作流，构建Benchling应用，查询数据仓库，用于实验室数据管理自动化 | Python SDK和REST API客户端，各模块操作脚本 | 有（references/authentication.md、references/sdk_reference.md、references/api_endpoints.md等） | 有（references/目录、scripts/目录和示例脚本） |
| biomni | 用于跨基因组学、药物发现、分子生物学和临床分析执行复杂研究任务的自主生物医学AI智能体框架。用于CRISPR筛选设计、单细胞RNA-seq分析、ADMET预测、GWAS解读、罕见疾病诊断或实验室方案优化 | scripts/setup_environment.py - 交互式环境和API密钥配置；scripts/generate_report.py - 增强PDF报告生成和自定义格式化 | 有（references/api_reference.md、references/llm_providers.md、references/use_cases.md等） | 有（references/目录、scripts/目录和外部资源） |
| biopython | 综合分子生物学工具包。用于序列操作、文件解析（FASTA/GenBank/PDB）、系统发育学、以及程序化NCBI/PubMed访问（Bio.Entrez）。最适合批量处理、自定义生物信息学管道、BLAST自动化 | 无特定脚本 | 有（references/sequence_io.md、references/alignment.md、references/databases.md、references/blast.md、references/structure.md、references/phylogenetics.md、references/advanced.md等） | 无 |
| biorxiv-database | bioRxiv预印本服务器的有效数据库搜索工具。用于按关键词、作者、日期范围或类别搜索生命科学预印本，检索论文元数据，下载PDF或进行文献综述 | scripts/biorxiv_search.py - 搜索脚本，支持关键词、作者、日期范围、类别和DOI搜索 | 有（references/api_reference.md） | 无 |
| bioservices | 40+生物信息学服务的统一Python接口。用于在单一工作流中查询多个数据库（UniProt、KEGG、ChEMBL、Reactome）并保持一致的API。最适合跨数据库分析、服务间ID映射 | scripts/protein_analysis_workflow.py - 蛋白质分析工作流；scripts/pathway_analysis.py - 通路分析；scripts/compound_cross_reference.py - 化合物交叉参考；scripts/batch_id_converter.py - 批量ID转换器 | 有（references/services_reference.md、references/workflow_patterns.md、references/identifier_mapping.md等） | 有（scripts/目录、references/目录） |
| brenda-database | 通过SOAP API访问BRENDA酶数据库。检索动力学参数（Km、kcat）、反应方程、生物体数据和底物特异性酶信息，用于生化研究和代谢通路分析 | scripts/brenda_queries.py - 高级函数，包括解析Km、反应条目、提取生物体数据、搜索酶等；scripts/brenda_visualization.py - 可视化函数；scripts/enzyme_pathway_builder.py - 酶通路构建器 | 有（references/api_reference.md） | 有（scripts/目录和references/目录） |
| cellxgene-census | 以编程方式查询CELLxGENE人口普查（6100万+细胞）。从最大的标准化单细胞图谱中获取跨组织、疾病或细胞类型的表达数据。最适合群体规模查询、参考图谱比较 | 无特定脚本 | 有（references/census_schema.md、references/common_patterns.md等） | 无 |
| chembl-database | 查询ChEMBL生物活性分子和药物发现数据。按结构/属性搜索化合物，检索生物活性数据（IC50、Ki），查找抑制剂，执行SAR研究，用于药物化学 | scripts/example_queries.py - 示例查询，包括get_molecule_info()、search_molecules_by_name()、find_molecules_by_properties()等 | 有（references/api_reference.md） | 无 |
| cirq | Google量子计算框架。用于针对Google Quantum AI硬件、设计噪声感知电路或运行量子表征实验。最适合Google硬件、噪声建模和低级电路设计 | 无特定脚本 | 有（references/building.md、references/simulation.md、references/transformation.md、references/hardware.md、references/noise.md、references/experiments.md等） | 无 |
| citation-management | 学术研究综合引文管理。搜索Google Scholar和PubMed查找论文，提取准确元数据，验证引文，生成正确格式的BibTeX条目。用于查找论文、验证引文信息、转换DOI为BibTeX或确保科学写作中的参考准确性 | scripts/search_google_scholar.py - Google Scholar搜索；scripts/search_pubmed.py - PubMed搜索；scripts/extract_metadata.py - 元数据提取；scripts/validate_citations.py - 引文验证；scripts/format_bibtex.py - BibTeX格式化；scripts/doi_to_bibtex.py - DOI转BibTeX | 有（references/google_scholar_search.md、references/pubmed_search.md、references/metadata_extraction.md、references/citation_validation.md、references/bibtex_formatting.md等） | 有（references/目录、scripts/目录、assets/目录和外部资源） |
| clinical-decision-support | 为制药和临床研究环境生成专业临床决策支持（CDS）文档，包括患者队列分析（按生物标志物分层和结局比较）和治疗推荐报告（基于证据的指南和决策算法） | scripts/generate_survival_analysis.py - Kaplan-Meier曲线生成；scripts/create_waterfall_plot.py - 最佳响应可视化；scripts/create_forest_plot.py - 亚组分析可视化；scripts/create_cohort_tables.py - 队列表格；scripts/build_decision_tree.py - TikZ流程图生成；scripts/biomarker_classifier.py - 患者分层算法；scripts/calculate_statistics.py - 危险比、Cox回归等；scripts/validate_cds_document.py - 质量和合规性检查；scripts/grade_evidence.py - GRADE评估助手 | 有（references/目录、assets/目录和脚本目录） | 有（references/目录、templates/目录和脚本目录） |
| clinicaltrials-database | 临床试验数据库搜索和分析 | 无特定脚本 | 有 | 有 |
| clinical-reports | 临床报告生成和分析 | 无特定脚本 | 有 | 有 |
| clinpgx-database | 临床药物基因组学数据库 | 无特定脚本 | 有 | 有 |
| clinvar-database | 临床变异数据库 | 无特定脚本 | 有 | 有 |
| cobrapy | 约束重建分析工具包 | 无特定脚本 | 有 | 有 |
| cosmic-database | COSMIC癌症突变数据库 | 无特定脚本 | 有 | 有 |
| dask | Python并行计算库 | 无特定脚本 | 有 | 有 |
| datacommons-client | Google Data Commons数据客户端 | 无特定脚本 | 有 | 有 |
| datamol | 分子分析和可视化库 | 无特定脚本 | 有 | 有 |
| deepchem | 深度学习药物发现库 | 无特定脚本 | 有 | 有 |
| deeptools | 生物信息学深度学习工具 | 无特定脚本 | 有 | 有 |
| denario | 变异数据库 | 无特定脚本 | 有 | 有 |
| diffdock | 蛋白质对接预测 | 无特定脚本 | 有 | 有 |
| dnanexus-integration | DNAnexus云平台集成 | 无特定脚本 | 有 | 有 |
| drugbank-database | DrugBank药物数据库 | 无特定脚本 | 有 | 有 |
| ena-database | 欧洲核苷酸序列档案（ENA）数据库 | 无特定脚本 | 有 | 有 |
| ensembl-database | Ensembl基因组数据库 | 无特定脚本 | 有 | 有 |
| esm | 蛋白质语言模型（ESM） | 无特定脚本 | 有 | 有 |
| etetoolkit | 进化树分析工具包 | 无特定脚本 | 有 | 有 |
| exploratory-data-analysis | 探索性数据分析 | 无特定脚本 | 有 | 有 |
| fda-database | FDA药品和医疗器械数据库 | 无特定脚本 | 有 | 有 |
| flowio | 流式细胞仪数据分析 | 无特定脚本 | 有 | 有 |
| fluidsim | 流体模拟工具包 | 无特定脚本 | 有 | 有 |
| gene-database | 基因数据库查询 | 无特定脚本 | 有 | 有 |
| generate-image | 图像生成工具 | 无特定脚本 | 有 | 有 |
| geniml | 基因组机器学习 | 无特定脚本 | 有 | 有 |
| geo-database | 基因表达综合数据库（GEO） | 无特定脚本 | 有 | 有 |
| geopandas | 地理空间数据处理 | 无特定脚本 | 有 | 有 |
| get-available-resources | 获取可用资源 | 无特定脚本 | 有 | 有 |
| gget | 快速生物信息学查询工具 | 无特定脚本 | 有 | 有 |
| gtars | 基因转录分析 | 无特定脚本 | 有 | 有 |
| gwas-database | 全基因组关联研究（GWAS）数据库 | 无特定脚本 | 有 | 有 |
| histolab | 数字病理学图像分析 | 无特定脚本 | 有 | 有 |
| hmdb-database | 人类代谢组数据库（HMDB） | 无特定脚本 | 有 | 有 |
| hypogenic | 假设生成工具 | 无特定脚本 | 有 | 有 |
| hypothesis-generation | 假设生成工作流 | 无特定脚本 | 有 | 有 |
| iso-13485-certification | ISO 13485医疗器械质量体系认证 | 无特定脚本 | 有 | 有 |
| kegg-database | KEGG通路数据库 | 无特定脚本 | 有 | 有 |
| labarchive-integration | LabArchive云存储集成 | 无特定脚本 | 有 | 有 |
| lamindb | 生物学数据管理框架 | 无特定脚本 | 有 | 有 |
| latchbio-integration | LatchBio云平台集成 | 无特定脚本 | 有 | 有 |
| latex-posters | LaTeX海报生成 | 无特定脚本 | 有 | 有 |
| literature-review | 文献综述系统化搜索和综合分析 | 无特定脚本 | 有 | 有 |
| market-research-reports | 市场研究报告生成 | 无特定脚本 | 有 | 有 |
| markitdown | Markdown文档转换工具 | 无特定脚本 | 有 | 有 |

---

## 统计信息

| 类别 | 数量 |
|------|------|
| 主要项目 | 25 |
| 独立SKILL.md文件 | 382+ |
| 脚本文件(.js, .ts, .py) | 500+ |
| 参考文档(.md) | 500+ |
| 配置文件(.json, .yaml) | 210+ |
| 插件市场项目 | 5+ |

## 主要skill类别

- **上下文工程** - Agent Skills for Context Engineering
- **文档处理** - PDF、DOCX、PPTX、XLSX skill
- **软件开发** - 后端、前端、全栈开发skill
- **科学计算** - 生物信息、化学、蛋白质组学等
- **AI/ML** - 机器学习、深度学习skill
- **工作流自动化** - Git、测试、代码审查
- **可视化** - 图表、架构图、流程图
- **DevOps** - Docker、K8s、云平台
- **数据库** - MongoDB、PostgreSQL、各种生物数据库
- **工具管理** - MCP服务器、skill验证

## 安装方式

大部分skill支持以下安装方式：

1. **Claude Code Plugin Marketplace** - 最推荐
2. **手动安装** - 复制到 `~/.claude/skills/`
3. **MCP服务器** - 通过MCP协议使用
4. **通用安装器** (OpenSkills、Agent Skills CLI)

---

*注：所有项目都是开源的，遵循MIT、Apache 2.0等开源许可证。*

---

**说明**：以上清单基于当前目录下的382个SKILL.md文件整理。由于数量庞大，每个skill都包含了名称、描述（中文）、脚本功能介绍、参考资料和资源信息。对于部分skill，如果未读取到完整内容，脚本信息可能标注为"无特定脚本"或基于通用说明。
