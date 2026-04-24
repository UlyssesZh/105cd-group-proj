# 105CD Group 5 project

## Development notes

If you are unable to follow the procedure, then just tell me what your edits are in chat
and ask me to manually apply your edits.

### Initial setup

1. [Fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) this repo
(just click the "Fork" button in the GitHub page).
2. [Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) your fork.
```shell
git clone https://github.com/your-username/105cd-group-proj.git
cd 105cd-group-proj
```
3. Add this repo as another remote.
```shell
git remote add upstream https://github.com/UlyssesZh/105cd-group-proj.git
```

### Whenever you want to make a change

1. Fetch the upstream and rebase onto it. Resolve any conflicts.
```shell
git fetch upstream
git rebase upstream/master
```
2. Make your changes.
3. Stage, commit, and push the changes.
```shell
git add -A
git commit -m 'describe your change'
git push -u origin master
```
4. Optionally [open a PR](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request),
or just notify me in chat. I will then merge.

### Guides on editing

To edit script: edit `game/script.rpy`.

To edit image: add or modify images in the `game/images` directory (or in any of its subdirectories).
Example: to edit the image shown using `scene bg room`, edit `game/images/bg room.png`.
To edit the image shown using `show spirit normal`, edit `game/images/spirit normal.png`.

After you made your edits, run Ren'Py to test.
You can use the Ren'Py launcher to select this project and launch,
or you can just run the command `renpy .` (assuming `renpy` is in your `PATH`).

## License

TBD
