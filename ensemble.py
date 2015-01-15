import os
import numpy as np

ensemble_files = os.listdir('ensemble_data')
print ensemble_files

ensemble_paths = [os.path.abspath('ensemble_data/') +'/'+ filename for filename in ensemble_files]

files = [open(filepath) for filepath in ensemble_paths]

weights = [0.55,0.45]
print weights

with open('output/submission.csv','w') as outfile:
    outfile.write('id,click\n')
    for f in files:
        print f.readline()
    while files[0]:
        probs = []
        for f in files:
            line = f.readline().strip()
            ID ,prob = line.split(',')
            probs.append(float(prob))
        click_prob = np.average(probs,weights=weights)
        outfile.write('%s,%s\n' % (ID,click_prob ))
