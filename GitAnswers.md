
1. Answer: Git is a version control system that allows you to track changes in your code, while Gitlab is a web-based Git repository manager that provides a graphical interface for managing your Git repositories. Gitlab also provides additional features such as issue tracking, continuous integration, and code review tools.

2. Answer: GitLab, GitHub, and Bitbucket are all web-based Git repository managers that provide a graphical interface for managing your Git repositories. The main differences between them are the features they offer and the pricing models they use. GitLab is open-source and offers a self-hosted option, GitHub is more focused on social coding and collaboration, and Bitbucket is more focused on integration with other Atlassian products.

3. Git is a version control system that allows you to track changes in your code, while Gitlab is a web-based Git repository manager that provides a graphical interface for managing your Git repositories. You may want to use Git without Gitlab if you prefer to manage your repositories locally or if you are working on a project that does not require the additional features provided by Gitlab.

4. To update the GitLab server with local changes, first, stage and commit the modifications using git add and git commit. Then, push the committed changes to the remote repository with git push origin <branch-name>

5. What is a branch and why would I use one?
A branch is a separate version of the main repo which can thus be modified without interferring with the changes in the main branch / other branches until one is ready to save the changes back into the main branch. 
=> Safe development environment since other branches are unaffected
=> Easy to abolish if e.g. an experiment failed
=> Easier organisation of the workflow since the main branch can only contain tested and approved changes / new versions
Applications could be testing/experiments, new features, new releases, alternative versions

6. How could you visualize a branch with 3 commits, and then another branch that breaks off after the second commit and has a single commit?
cf. image
Main branch: Three dots aranged vertically, connected to each other by a line
Second branch: One dot next to the last dot of the main branch, connected to the middle dot of the main branch by a line

7. Give an example of a set of git commands that would result in a merge conflict.

mkdir git-merge-conflict
cd git-merge-conflict
git init .
echo "Some text" > someTextFile.txt
git add someTextFile.txt
git commit -m "Initializing someTextFile"
git checkout -b second_branch
echo "Modifiying the text file in the second branch" > someTextFile.txt
git commit -am "someTextFile edited in second branch"
git checkout main
echo "Modifiying the text file in the main branch" > someTextFile.txt
git commit -am "someTextFile edited in main branch => main and second branch diverge now"
git merge second branch

8. Is Git suitable for latex documents?
Generally yes, however since Git has issues with tracking changes in binary files (e.g. images, pdfs), the repo either becomes quite large quickly or these files have to be ignored by git and tracked another way

9. Should I from now on version my word and powerpoint slides using git? why/whynot?
It might be okay to version small to medium sized documents but using git for binary files like word and powerpoint is not ideal because git cannot handle binary files efficently.

10. What could happen when I push my latest commit to the remote repository without pulling first?
Conflicts might arise because someone else might have made changes before me. Working with the file without pulling/updating first will possibly cause rejection when trying to push the latest commit.

11. What happens when I pull without commiting my local changes first?
Git will suggest to commit or stash my changes first as it will possibly create a merge conflict if the changes I made are on the same part with the remote changes.

12. What is the difference between branching and forking?
Branching is used to collaborate parallely while using the same repository among contributors.Forking is copying a repository to an indepenent location and contributing to make changes by creating a pull request to the original repository.

