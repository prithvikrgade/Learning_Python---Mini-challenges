## Program to remember git basic concepts in case i forget!
Help = {
    "Gitinit" : {
        "Concept" : " when you use git init in a folder on your local PC, you're turning that folder into a Git repository. It doesn't change your files directly, but it creates a hidden .git directory inside the folder.",
        "Command" : "Git init"
     },

     "Role of .git" : {
         "Concept" : "The .git folder keeps track of all the commits, branches, and other Git-related metadata. It does not store the actual content of the files themselves but keeps a reference to them (like a log) so Git can reconstruct your project history."
     },

     "Commit and Push" : {
         "Concept" : "When you commit in Git, you're saving your changes locally in the .git folder. These changes aren't pushed to GitHub (or any remote repo) until you run git push. The commit is like saying, I’m saving a version of my work at this point.",
         "Concept2" : "The files you commit are the ones stored in the repositorys history, and those are the ones that will be pushed to GitHub when you run git push. Any file that is not committed (i.e., files that are untracked or staged for commit) will not be pushed to GitHub."
     },

     "One GitHub Repo per Local Repo:" : {
         "Concept" : "typically, one local folder can only be connected to one remote GitHub repository at a time (though there are advanced techniques for working with multiple remotes).",
         "Concept2" : "When you set up a remote repository on GitHub and link it to your local repo (via the git remote add command), you're telling Git where to push your commits. You can only push changes to the GitHub repository that is linked as the remote."
     },
     
     "Gitadd" : {
         "Concept" : "When you run git add, you're staging files, i.e., preparing them to be included in the next commit.",
         "Command" : "git add file1.py",
     },

     "Gitcommit" : {
         "Concept" : "Always done after git add",
         "Concept2" : "you run git commit to save the changes locally.",
         "Command" : "git commit -m Commit message describing the changes in file.py"
     },
     
     "Link local git to github repo" : {
         "Command" : "git remote add origin https://github.com/yourusername/my-project.git",
         "what is origin?" : "In Git, origin is the default name given to the remote repository when you connect your local repo to a remote (like GitHub, GitLab, etc.).",
         "Explanation" : "By running the command we are telling git, Hey, I want to connect my local project to that GitHub repo, and I will  call that remote repository origin.",
         "Clarity" : "Its not an easy task to remember the url address of the remote repo so we give it an alias to remember it easily."
## we can call it anything there's no rule saying that we have to call it origin, 
## But by convention, origin is the default name everyone uses for the main remote — it’s not a rule, just a habit across most Git workflows
     }

}

print("Here's a list of all the topics that are accessible", list(Help.keys()))

while True: ## The while true condition creates an infinite loop to run the code inside infinite times until we break out of it using break

    User = input ("Hello, please select one of the topics mentioned above. (Type Quit to Exit)")

    if User == "Quit":
        print("Thank you, please come back again!!")
        break

    if User in Help: 
        for key, value in Help[User].items(): ## students[name]: Accesses the inner dictionary for the specific student.
            print("Here are the details for", User) ## students: Refers to the entire dictionary containing all students' records.
            print(f"{key}: {value}")
    else:
        print("Im sorry there's no information available!")
    


