import os
import sh

PATHS_TO_CHECK = ['../css', '../js', '../scss', '../site/snippets', '../site/templates', '../content']
IGNORE_2X = True
DRY_RUN = True

for (dirpath, dirnames, filenames) in os.walk('.'):
    for filename in filenames:
        if IGNORE_2X and '@2x' in filename:
            continue

        for cwd in PATHS_TO_CHECK:
            output = sh.grep('-F', '-m', 1, '-r', filename, cwd, _ok_code=[0,1])
            if output.exit_code == 0:
                break
        else:
            print filename, output.exit_code, 'deleting...'
            if not DRY_RUN:
                os.remove(os.path.join(dirpath, filename))

