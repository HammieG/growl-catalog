# GROWL Task Force: individual data projects

Each GROWL Task Force member works on **one published population-synthesis dataset**. Your work
lives in your own folder here, and you share it with the team by opening a **pull request (PR)**.
A GROWL mentor reviews it and merges it into the repository.

Questions go to the GROWL Discord (your dataset channel or the shared "individual projects"
channel), not to GitHub issues.

```
GROWL_TF_individual_data_projects/
├── README.md                          <- this file
├── instructions_task_force/           <- instruction notebooks, one per step (read only, don't edit)
│   └── step1_download_and_investigate_data.ipynb
└── individual_project_folders/
    └── <dataset>_<n>__<YourName>/     <- YOUR folder, e.g. Broekgaarden22_1__Joseph
        ├── README.md                  <- your notes: the main file of your project
        ├── step1_<dataset>_<YourName>.ipynb
        ├── download_instructions.txt  <- deliverable of step 1 (Task C)
        ├── metadata_<dataset>.csv     <- deliverable of step 1 (Task E)
        └── figures/                   <- optional: small PNGs you refer to in README.md
```

---

## The three rules

1. **Only change files inside your own folder.** If you think something outside it should change
   (an instruction notebook, this README), ask on Discord.
2. **Never upload data.** No `.h5` / `.hdf5` files, no `.zip` / `.tar.gz` archives, no large
   tables. The data stays on the GROWL server and on your own machine; your notebook points at it
   through the `PATH` dictionary from Task B. An automatic check rejects data files and any file
   larger than 10 MB.
3. **Every change goes through a pull request.** Nobody pushes directly to `main`. That is not
   because we don't trust you: it gives a mentor a chance to see your work and comment on it.

---

## What goes in your folder

| File | What it is | When |
|---|---|---|
| `README.md` | **Your notes.** This is the main file of your project. Write down what you did, what you found, what was unclear, and questions for the team. Keep adding to it; dated entries work well (`### 2026-11-20`). | Always |
| `step1_<dataset>_<YourName>.ipynb` | Your copy of the instruction notebook, with the tasks filled in. | Step 1 |
| `download_instructions.txt` | The exact recipe to download your data (Task C): links, the commands you typed, checksums, difficulties. Someone else must be able to follow it literally. | Step 1 |
| `metadata_<dataset>.csv` | The filled-in metadata table (Task E). | Step 1 |
| `figures/*.png` | Small plots you want to show in your `README.md`. | Optional |

More deliverables will be added as the next steps are released.

**Notebooks:** before committing, make sure your notebook isn't huge (a few MB at most). If it has
many large plots, clear those outputs (*Edit → Clear Outputs of All Cells* in Jupyter, or for one cell)
and save the plots you want to keep as PNGs in `figures/`.

---

## How to submit your work

You have write access to this repository, so you can make a **branch**, push it, and open a pull
request. Choose whichever route you're comfortable with.

### Route A: in the browser (no git needed)

1. Go to your folder on GitHub:
   `https://github.com/growl-lab/growl-catalog/tree/main/GROWL_TF_individual_data_projects/individual_project_folders/`
2. **To upload files:** click **Add file → Upload files**, drag your files in.
   **To edit your README:** open `README.md`, click the pencil icon.
3. At the bottom, choose **"Create a new branch for this commit and start a pull request"**. Give
   the branch a name like `Joseph/step1-download`, then click **Propose changes**.
4. On the next page, write a short description and click **Create pull request**.

### Route B: on the command line

One-time setup:

```bash
git clone https://github.com/growl-lab/growl-catalog.git
cd growl-catalog
```

Each time you want to submit something:

```bash
git switch main
git pull                                      # get everyone else's latest work
git switch -c <YourName>/<what>               # e.g. Joseph/step1-download
# ... work in your folder ...
git add GROWL_TF_individual_data_projects/individual_project_folders/<your folder>
git status                                    # check: only your folder, no data files
git commit -m "<dataset>: <what you did>"
git push -u origin <YourName>/<what>
```

Then open the link that `git push` prints (or go to the repository page and click **Compare & pull
request**), write a short description, and click **Create pull request**.

### After you open the pull request

- The automatic checks run (you'll see a green ✓ or a red ✗). If one fails, the details tell you
  why; usually it is a file that is too large or a data file.
- A GROWL mentor reviews it. They may approve it straight away or leave comments.
- To respond to comments, **keep working on the same branch** and push again (or, in the browser,
  edit the file on that branch). The pull request updates automatically.
- Once approved, a mentor merges it. Then start your next piece of work from a fresh `main`
  (`git switch main && git pull`).

**Small and often beats big and rare.** Open a pull request after each task or two; don't wait
until the whole step is done. We'd love to see intermediate results.

---

## Need help?

- Git or GitHub problems: ask on Discord, and paste the error message.
- Stuck on a task, or found something odd in the data: write it in your `README.md` and ask on
  Discord. "This isn't in the file" or "the paper doesn't say" is a useful result.
