# remove ignored files

# -d use directory
# -X remove ignored files
# -x remove ignored files and non ignored files (untracked)

# git clean -n -dX to see files that will be deleted

python setup.py clean
git clean -fdX