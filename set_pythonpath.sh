#!/usr/bin/env sh

ROOTS=$(pants roots --roots-sep=' ')
python3 -c "print('PYTHONPATH=\"./' + ':./'.join(\"${ROOTS}\".split()) + ':\$PYTHONPATH\"')" > .env
