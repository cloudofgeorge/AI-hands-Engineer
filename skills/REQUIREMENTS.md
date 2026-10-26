# Skill requirements and setup

Reading or installing these Markdown skills does **not** require Python, Node.js,
or a repository-wide build. Running a skill's scripts or external tools can.
Install the requirements for the workflow you choose, in the environment where
your agent executes commands. A local installation will not supply tools to a
remote container or cloud agent.

This guide summarizes the checked-in skill instructions, script imports, package
manifests, and inline Python dependency declarations as of 26 October 2026.
Version numbers below are requirements recorded by those sources, not a promise
that every newer tool version is compatible. Follow the selected skill and target
project's lockfiles for exact versions.

## Start here

| What you want to do | What to have available |
| --- | --- |
| Read guidance, plan, review text, or use conversational skills | An agent that can read the skill and its references. No shared language runtime is required. |
| Run JavaScript helpers | Node.js and, where package installation is needed, npm/npx. The frontend browser inspector requires **Node.js 22+**; marketing CLIs declare 18+ and Vercel Optimize declares 20+. |
| Run Python helpers | Python 3 and pip or `uv`. Several security helpers require **3.11+**, constant-time analysis requires **3.10+**, and Regression Hunt requires **3.13+**. Use the workflow's declared version; there is no single Python minimum for the whole collection. |
| Work with repositories or shell helpers | Git; Bash for `.sh` scripts; common Unix tools such as `curl`, `tar`, and `grep` where the script uses them. Windows users need a suitable Unix environment for these workflows; Regression Hunt specifically uses POSIX locks. |
| Use browser, image-generation, cloud, or account tools | The corresponding installed tool or connected host capability, plus any required account access. Copying a skill does not provision these capabilities. |

If you use many of the bundled helpers, Node.js 22+ and Python 3.13+ meet the
highest runtime floors listed above. Specialized compilers, fuzzers, and target
applications still have their own compatibility requirements.

## Documents, PDFs, notes, and media

| Skill / workflow | Required for execution | Optional or task-specific |
| --- | --- | --- |
| [doc](./tools/doc/SKILL.md) | Python with `python-docx` for document editing. Rendering uses `pdf2image`, LibreOffice (`soffice`), and Poppler (`pdftoppm`, `pdfinfo`). | Text-only extraction can run without rendering tools; it does not verify layout. |
| [pdf](./tools/pdf/SKILL.md) | Python packages `reportlab`, `pdfplumber`, and `pypdf` for the documented generation/extraction workflow; Poppler for page rendering. | Install only the packages used by your chosen operation. |
| [obsidian-cli](./tools/obsidian-cli/SKILL.md) | Obsidian installed and running, with the `obsidian` command available on `PATH`. | Plain Markdown vault edits in other note-taking skills do not themselves require this CLI. |
| [recipe-to-cookbook: video reconstruction](./personal/recipe-to-cookbook/references/youtube-shorts-visual-reconstruction.md) | For the local video route: `yt-dlp`, FFmpeg, and an agent able to inspect extracted frames. | `uvx --from yt-dlp yt-dlp` can run the downloader without a permanent CLI installation. Text recipes do not need video tooling. |

For local document work, these are the setup commands already described by the
[DOCX](./tools/doc/SKILL.md#dependencies-install-if-missing) and
[PDF](./tools/pdf/SKILL.md#dependencies-install-if-missing) skills. Create an
isolated Python environment first; the commands below use a macOS/Linux shell:

```bash
python3 -m venv "$HOME/.venvs/ai-hands"
source "$HOME/.venvs/ai-hands/bin/activate"
python -m pip install python-docx pdf2image reportlab pdfplumber pypdf
```

Install the rendering tools using your system package manager:

```bash
# macOS, with Homebrew already installed
brew install libreoffice poppler

# Ubuntu/Debian alternative
sudo apt-get install libreoffice poppler-utils
```

Use either system command, not both. On Windows, install equivalent applications
and expose their executables to the environment running the agent.

## Design and browser workflows

| Skill / workflow | Required for execution | Setup details |
| --- | --- | --- |
| [design-taste-frontend](./design/design-taste-frontend/README.md#requirements) | Node.js 18+ for draw/lint/asset scripts; **22+** and installed Chrome, Edge, or Chromium for `inspect.mjs` and `scenes.mjs`. | No npm dependencies. Set `CHROME_PATH` if the browser is not found. Asset search/download needs network access; it does not require API keys. |
| [impeccable](./design/impeccable/SKILL.md) | Node.js for its bundled `.mjs` helpers; a browser and reachable project page for live editing. | Its core helpers use bundled code and Node built-ins. Use the target application's own package manager to start its development server. |
| [huashu-design](./design/huashu-design/README.en.md) — screenshots and design checks | Python with `playwright` and `Pillow`, plus Playwright's Chromium browser. | Installing the Python package alone does not install the browser binary. |
| Huashu — rendered HTML to editable PowerPoint | The Python screenshot stack plus `python-pptx`. | See [rendered HTML export](./design/huashu-design/references/pptx-from-rendered-html.md). |
| Huashu — JavaScript slide/PDF/video helpers | Node.js/npm and the packages in its [package.json](./design/huashu-design/package.json): `playwright`, `pptxgenjs`, `pdf-lib`, and `sharp`; Playwright Chromium for browser rendering. | Install in the skill folder using its lockfile. Video/audio scripts also use Bash and FFmpeg/`ffprobe`. |
| Huashu — cloud narration or video review | Narration: configured Doubao TTS credentials. Video review: Python 3.10+, `requests>=2.28.0`, FFmpeg/`ffprobe`, and `ARK_API_KEY`. | These are optional cloud routes. See [.env.example](./design/huashu-design/.env.example), [SECURITY.md](./design/huashu-design/SECURITY.md), and the script's `uv run` instructions. Local design checks do not need these keys. |
| [playwright-cli](./tools/playwright-cli/SKILL.md#local-installation) | The `playwright-cli` command, or Node.js/npm for the documented `npx playwright-cli` fallback, with its browser setup. | This command-line interface is separate from the Python `playwright` package. |
| [develop-web-game](./engineering/domains/web/develop-web-game/SKILL.md) | Node.js, JavaScript `playwright`, its browser binary, and a running game server. | The bundled client imports `playwright`; make it resolvable from the helper's location. A package installed only in an unrelated app folder may not be found. |
| [brandkit](./design/brandkit/SKILL.md), [image-to-code](./design/image-to-code/SKILL.md), and frontend image skills | An image-generation tool supplied by the host or an installed integration. | These Markdown skills do not install an image model or API client. Provider credentials are needed only for the chosen integration. |

For Huashu's local Python checks and rendered PowerPoint export, run inside the
Python environment created above:

```bash
python -m pip install playwright Pillow python-pptx
python -m playwright install chromium
```

For its JavaScript helpers, run from this repository's root:

```bash
cd skills/design/huashu-design
npm ci
npx playwright install chromium
```

Python and JavaScript Playwright are separate packages and may require different
browser revisions. Install the browser through each package you actually use.
Linux browser execution may also need system libraries; follow that Playwright
installation's dependency diagnostic. FFmpeg is a separate system installation,
not a Python or npm dependency.

## GitHub, infrastructure, and application platforms

| Workflow | Tools and access needed when executing it |
| --- | --- |
| [GitHub ticket intake](./engineering/tools/github-ticket-intake/SKILL.md) | Node.js, GitHub CLI (`gh`), an authenticated account, and access to the intended repository/project. The bundled `gh-preflight.mjs` checks CLI authentication and scopes. |
| [GitHub CI investigation](./engineering/tools/gh-fix-ci/SKILL.md) | `gh` authenticated with repository and workflow access. Local reproduction additionally needs the target project's build/test dependencies. |
| [wizard](./engineering/wizard/SKILL.md) | Bash and a browser for manual steps; `gh` with authentication when writing GitHub secrets or variables. Missing `gh` is reported for manual follow-up. |
| [vercel-deploy](./engineering/tools/vercel-deploy/SKILL.md) | Bash, `curl`, `tar`, standard Unix utilities, and network access to the claimable-preview service. This helper does not require the Vercel CLI login used by Vercel Optimize. |
| [vercel-optimize](./engineering/domains/web/vercel-optimize/SKILL.md#prerequisites) | Node.js 20+, Vercel CLI 53+, an authenticated linked app directory, and Observability Plus for route-level recommendations. |
| [Next.js workflows](./engineering/domains/web/nextjs/README.md#compatibility) | At the imported revision, `next-dev-loop` requires Next.js 16.3+, Turbopack, a running `next dev` server exposing `/_next/mcp`, and `agent-browser` 0.31.1+. Follow each skill's compatibility checks before changing a project's framework version. |
| [macOS development](./engineering/domains/macos/macos-development/SKILL.md) | A macOS development environment with Xcode/Swift tooling for building native apps. Accessibility automation additionally needs the relevant macOS permissions. Reading design guidance does not require compiling an app. |
| [Kubernetes](./engineering/domains/infrastructure/troubleshooting-kubernetes/SKILL.md), [GitOps](./engineering/domains/infrastructure/gitops/SKILL.md), and [Terraform](./engineering/domains/infrastructure/terraform/SKILL.md) | The selected CLI (`kubectl`, `argocd` or `flux`, `terraform`), matching cluster/backend configuration, and authorized access. Install only the tool for the selected platform. |
| [AWS FinOps](./engineering/domains/infrastructure/aws-finops/SKILL.md) and [observability](./engineering/domains/infrastructure/observability/SKILL.md) | AWS CLI/account access or the relevant monitoring service's API/CLI/connector, according to the investigation. |
| [Supabase](./engineering/domains/database/README.md), [Better Auth](./engineering/domains/authentication/README.md), and [Stripe](./engineering/domains/payments/README.md) | Target application dependencies and any required database/service access. CLI or MCP setup, authentication, SDK installation, and application configuration are separate from importing the skill. |

## Security and testing

These are specialized toolchains, not a prerequisite for using the rest of the
repository. Follow the selected skill's installation section for its platform
and language-specific dependencies.

| Skill / group | Requirements |
| --- | --- |
| [security-ownership-map](./engineering/security/security-ownership-map/SKILL.md#requirements) | Git history, Python 3, and `networkx` (community detection is enabled by default). Install with `python -m pip install networkx` inside your environment. |
| [C review](./engineering/security/c-review/README.md) | Python 3.11+ and `uv` for scripts with inline dependencies. The parsing helpers pin `tree-sitter`, `tree-sitter-c`, and `tree-sitter-cpp`; use their `uv run` entry points to resolve those pins. The package's empty dependency list does not cover these script-level dependencies. |
| [Rust review](./engineering/security/rust-review/README.md), [supply-chain risk](./engineering/security/supply-chain-risk-auditor/README.md), and [CodeQL helpers](./engineering/security/static-analysis/skills/codeql/scripts/pyproject.toml) | Python 3.11+ for their declared helper projects; `uv` for documented runner commands. Rust builds/tests need the target Rust toolchain. Supply-chain signal collection needs access to package-host APIs. |
| [CodeQL](./engineering/security/static-analysis/skills/codeql/SKILL.md) | CodeQL CLI, `jq`, `uv`, query packs, and any language build toolchain needed to create the database. Python helper installation alone does not install CodeQL. |
| [Semgrep](./engineering/security/static-analysis/skills/semgrep/SKILL.md) and [rule creation](./engineering/security/semgrep-rule-creator/README.md) | Semgrep CLI and the selected rules. Pro analysis additionally needs the corresponding authenticated capability. |
| [SARIF parsing](./engineering/security/static-analysis/skills/sarif-parsing/SKILL.md) | `jq` for shell queries, or a chosen Python SARIF library for the Python route. The skill lists `pysarif` and `sarif-tools` alternatives. |
| [constant-time analysis](./engineering/security/constant-time-analysis/skills/constant-time-analysis/SKILL.md#prerequisites) | Python 3.10+, the documented `uv` runner, and the compiler/interpreter for the language being inspected: for example Clang/GCC, Go, Rust, Swift, JDK/Kotlin, or .NET with `ilspycmd`. Install only the relevant language tools. |
| [Regression Hunt](./engineering/tests/regression-hunt/pyproject.toml) | Python 3.13+, `uv`, Git, and POSIX file locks. Its pinned pytest/Ruff/ty dependencies are for development of the package, not all skill use. |
| [Post-patch validation](./engineering/tests/post-patch-validation/README.md) | Python for the local runner and the target project's build/test environment. |
| [Property-based testing](./engineering/tests/property-based-testing/README.md) and [mutation testing](./engineering/tests/mutation-testing/README.md) | The test framework and property/mutation engine appropriate to the project's language. There is no universal package to install for both. |
| [Testing Handbook](./engineering/tests/testing-handbook-skills/README.md) | Tool-specific: LLVM/Clang for sanitizers/libFuzzer/coverage; Rust/Cargo and nightly for `cargo-fuzz`; Rust plus the documented LLVM version for LibAFL; Python/Clang for Atheris; Ruby/Clang for Ruzzy; Docker for container-based AFL++ or OSS-Fuzz workflows. Ruzzy's native route is Linux. Consult each skill for exact versions and extra build libraries. |
| [Handbook generator validator](./engineering/tests/testing-handbook-skills/scripts/pyproject.toml) | Python 3.11+ and `pyyaml>=6.0`; these are validator dependencies, not requirements for reading every Handbook skill. |
| [Smart-contract security](./engineering/security/building-secure-contracts/README.md) | The target chain's build/test tools and, when the chosen analysis uses them, scanners such as Slither. These vary by chain; they are not shared requirements for all security reviews. |

Use `uv run` exactly as documented when a script has a `# /// script` dependency
header. It can provision the declared interpreter/packages; running that file
with plain `python` may fail even if the adjacent `pyproject.toml` has no
dependencies. First-time dependency resolution and tool downloads need network
access. A checked-in lockfile is a version record, not an installed environment.

## Marketing, SEO, and connected capabilities

The [marketing CLI collection](./marketing/tools/clis/README.md) requires Node.js
18+ and no npm installation. Each CLI needs its own service credentials and
network access; that README lists the exact environment variables. `jq` is
optional for the JSON-filtering examples.

Most marketing, SEO, planning, teaching, and note-taking skills contain guidance
rather than standalone programs. Executing a workflow may still require web
search, an analytics/search-console account, a connected provider, a browser, or
access to a local vault. Those requirements depend on the chosen task. Delegation,
image generation, and scheduling are host capabilities; see
[portability](./PORTABILITY.md). Installing Python does not add them.

## Check your setup

Run only the checks relevant to your selected workflow. A missing command here
does not mean the whole repository is unusable.

```bash
python3 --version
node --version
npm --version
uv --version
git --version
gh auth status
soffice --version
pdftoppm -v
ffmpeg -version
ffprobe -version
```

Check Python imports with the same interpreter/environment that will run the
helpers. For example, after installing the document packages:

```bash
python -c "import docx, pdf2image, reportlab, pdfplumber, pypdf; print('Document packages available')"
```

Huashu also provides a local capability check (run from the repository root):

```bash
python3 skills/design/huashu-design/scripts/capabilities.py --json
```

It checks selected tools and Python Playwright's browser file, not every export
dependency or successful browser launch. API authentication and a reachable
development server must be verified separately for workflows that use them.

## Maintaining this guide

When adding or updating a skill, document its runtime version, system tools,
package installation location, browser binaries, account access, and optional
features here or in a linked setup section. Check both package manifests and
inline script dependencies. Keep workflow dependencies separate from packages
used only to develop or test the skill itself.
