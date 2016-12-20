#! /bin/bash
source ~/virtualenvs/pelican/bin/activate
make html && make publish
cd output
git add --all
git commit -m 'content update'
git push origin HEAD:master
