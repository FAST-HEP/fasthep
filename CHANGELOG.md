# Changelog

All notable changes to this project are documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). This project uses
calendar versioning (`YYYY.MM.N`) rather than semantic versioning.

Release sections are assembled from the packages' own changelogs when a release is prepared
(`release-aggregate-changelog` in `fasthep-dev`). Do not edit them by hand, and do not add entries
under `## [Unreleased]`: it stays empty.

## [Unreleased]

## [2026.11.1] - 2026-11-02

### fasthep-toolbench

#### Added

- A dataset line in a DAS list can end in `# allow-invalid`: `fasthep tools das-discover` then queries that dataset
  and its files with `status=*`, for a dataset that is INVALID in DAS but whose files are still available.

#### Fixed

- `read_dataset_list` (`fasthep tools das-discover`) takes the group only from section headers such as
  `##### QCD_Zjet #####`. Commented-out datasets (`##/Z/.../NANOAODSIM`) and free-text comments no longer become the
  group of the datasets below them.

### fasthep-flow

#### Added

- `execution.file_access` maps dataset file names to the URLs a site reads them from: a list of
  `{match, prefix}` rules, the first matching rule puts its prefix in front of the name (for
  example `/store/` with `root://cms-xrd-global.cern.ch/`). Dataset files keep logical names and
  no redirector; the plan lists the URLs in `context.datasets.<name>.files` and the partitions,
  and the declared names in `logical_files`. The normalized `execution` block now always has
  `file_access` (empty by default).
- Compile hook registry entries accept `enabled: false` to skip the hook. A workflow's `registry:`
  section can switch off a hook that a profile registers (for example the D2 graph render, which
  takes minutes on large graphs) without repeating its `spec` and `impl`.
- Datasets accept `file_nevents`, one event count per file in the order of `files`. Event chunking
  (`chunk_size`) uses each file's own count.

#### Fixed

- Chunking a multi-file dataset no longer applies the dataset-level `nevents` total to every file,
  which planned hundreds of out-of-range chunks per file. Compiling with `chunk_size` now fails
  with a message asking for `file_nevents` when only the total is known.

### fasthep-distributed

#### Added

- `execution.config.batch_name` names the HTCondor workers of a run, so their batch names in
  `condor_q` differ between concurrent runs (`<batch_name>-default-0`, ...). It defaults to the
  basename of the output directory.

### fasthep-carpenter

#### Added

- The `root_tree` writer accepts `shared_counters: true` (TTree only). The jagged branches
  `<collection>_<attribute>` with the same lengths then share one counter `n<collection>`, as the
  legacy skims do, instead of every branch getting its own `n<branch>`.

### fasthep-curator

Unchanged: stays at 2026.10.1.

### fasthep-render

#### Added

- The `fasthep.render.graph_d2` compile hook skips graphs larger than `max_d2_bytes` (hook parameter,
  default 50 kB; typical graphs are below 10 kB) with a warning that names the command to render them (`fasthep render graph
  <build dir>`); rendering a large graph took minutes of every compile. `render_compile_graph` renders
  the graph of a compile output directory regardless of size.

### fasthep-cli

#### Added

- `fasthep render graph <build dir>` renders `graph/graph.d2` of a compile output directory to
  `graph/graph.svg`. The compile step skips this for large graphs (fasthep-render), and its warning
  names this command.

### fasthep-workshop

#### Changed

- `examples/CMS/Zmumu` selects its hook profiles explicitly (`registry`, each package's `registry`, and
  curator's `default_context` and `runtime_diagnostics`) instead of the `hep_debug` profile.
- FAST-HEP dependencies are pinned to the 2026.11.1 release set: exactly (`==`) in `pixi.toml`, the released
  environment, and as floors (`>=`) in `pyproject.toml`, so an editable development checkout keeps resolving
  after a dependency's next commit. `fasthep-curator` stays at 2026.10.1 (no changes since).
- The pixi environments cap Python below 3.15: `xrootd` has no wheel for it and failed to build from source.

#### Fixed

- `examples/LZ/mssi` no longer lists `SS_skim_U238-late_AnodeGridWires.root`, which is not in its download
  manifest (`remote_data.json`).

## [2026.08.2] - 2026-08-25

### Changed

- Updated the pinned `fasthep-flow`, `fasthep-cli`, `fasthep-carpenter`, and `fasthep-workshop`
  versions to their latest releases.
