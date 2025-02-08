# Project 0: Week 1 and Week 2

This GitHub Assignment ("Project 0") is reused in Week 1 and Week 2. For details on what you should
do each week, please see the corresponding subfolder in the main course repo.
9. Should I from now on version my word and powerpoint slides using git? why/whynot?
It might be okay to version small to medium sized documents but using git for binary files like word and powerpoint is not ideal because git cannot handle binary files efficently.

10. What could happen when I push my latest commit to the remote repository without pulling first?
Conflicts might arise because someone else might have made changes before me. Working with the file without pulling/updating first will possibly cause rejection when trying to push the latest commit.

11. What happens when I pull without commiting my local changes first?
Git will suggest to commit or stash my changes first as it will possibly create a merge conflict if the changes I made are on the same part with the remote changes.

12. What is the difference between branching and forking?
Branching is used to collaborate parallely while using the same repository among contributors.Forking is copying a repository to an indepenent location and contributing to make changes by creating a pull request to the original repository.
Q1:Answer: Git is a version control system that allows you to track changes in your code, while Gitlab is a web-based Git repository manager that provides a graphical interface for managing your Git repositories. Gitlab also provides additional features such as issue tracking, continuous integration, and code review tools.
Q2:Answer: GitLab, GitHub, and Bitbucket are all web-based Git repository managers that provide a graphical interface for managing your Git repositories. The main differences between them are the features they offer and the pricing models they use. GitLab is open-source and offers a self-hosted option, GitHub is more focused on social coding and collaboration, and Bitbucket is more focused on integration with other Atlassian products.
Q3:Git is a version control system that allows you to track changes in your code, while Gitlab is a web-based Git repository manager that provides a graphical interface for managing your Git repositories. You may want to use Git without Gitlab if you prefer to manage your repositories locally or if you are working on a project that does not require the additional features provided by Gitlab.
Q4:To update the GitLab server with local changes, first, stage and commit the modifications using git add and git commit. Then, push the committed changes to the remote repository with git push origin <branch-name>
