# Fix the mineapolis dataset by recomputing the cardinality parameters

import os

from preflibtools.instances.preflibinstance import OrdinalInstance


IN_DIR = "../datasets/"

for ds_dir in os.listdir(IN_DIR):
    if os.path.isdir(os.path.join(IN_DIR, ds_dir)):
        if ds_dir == "minneapolis":
            for file in os.listdir(os.path.join(IN_DIR, ds_dir)):
                if os.path.splitext(file)[1][1:] in ["soc", "toc", "soi", "toi"]:
                    file_path = os.path.join(IN_DIR, ds_dir, file)
                    instance = OrdinalInstance(file_path)
                    if len(set(instance.orders)) < len(instance.orders):
                        inst = OrdinalInstance()
                        inst.parse_file(file_path, autocorrect=True)
                        inst.recompute_cardinality_param()
                        inst.write(file_path)
