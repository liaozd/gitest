
`git merge -X patience another_branch`

`git diff --patience another_branch`

###### git cherry-pick

> `git cherry-pick cherry-pick-br`

> `git cherry-pick --edit another-br`

> `git cherry-pick -x another-br`

> `git cherry-pick --edit -x anther-br`

> `git cherry-pick --signoff anther-br`

> `git cherry --verbose another-br`

##### Chapter6 Rewriting history and disaster recovery

> `git reflog` equal to `git log --walk-reflogs --abbrev-commit --pretty=oneline`

> `git fsck`

> `git reset HEAD^ -- git-cheatsheet.md` The -- is optinal but makes more explicit the separation bwtween the ref and paths.

> `git reset --soft HEAD^` --soft reset neither the staging area nor the working tree but just changes the HEAD pointer to point to the previous commit.
