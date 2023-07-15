#!/usr/bin/env sh

ROOTS=$(pants roots --roots-sep=' ')
python3 -c "print('PYTHONPATH=\"./' + ':./'.join(\"${ROOTS}\".split()) + ':\$PYTHONPATH\"')" > .env
python3 -c "print('((nil . ((eval . (setenv \"PYTHONPATH\" \"./' + ':./'.join(\"${ROOTS}\".split()) + '\" )))))')" > .dir-locals.el
