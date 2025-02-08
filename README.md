# Project 0: Week 1 and Week 2

This GitHub Assignment ("Project 0") is reused in Week 1 and Week 2. For details on what you should
do each week, please see the corresponding subfolder in the main course repo.

Question Answers:
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