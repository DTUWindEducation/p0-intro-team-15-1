9. Should I from now on version my word and powerpoint slides using git? why/whynot?
It might be okay to version small to medium sized documents but using git for binary files like word and powerpoint is not ideal because git cannot handle binary files efficently.

10. What could happen when I push my latest commit to the remote repository without pulling first?
Conflicts might arise because someone else might have made changes before me. Working with the file without pulling/updating first will possibly cause rejection when trying to push the latest commit.

11. What happens when I pull without commiting my local changes first?
Git will suggest to commit or stash my changes first as it will possibly create a merge conflict if the changes I made are on the same part with the remote changes.

12. What is the difference between branching and forking?
Branching is used to collaborate parallely while using the same repository among contributors.Forking is copying a repository to an indepenent location and contributing to make changes by creating a pull request to the original repository.