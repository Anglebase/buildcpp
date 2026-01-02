pdoc --html --output-dir dist src/buildcpp
mkdocs build --site-dir dist/site
git checkout site
Move-Item -Path dist/site -Destination ./ -Force
Move-Item -Path dist/buildcpp -Destination docs -Force
git stash save
git stash list
git commit -m "Update documentation"
git checkout master