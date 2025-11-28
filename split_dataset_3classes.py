import os
import shutil
import random

# Paths
SRC_DIR = "data_original"
DST_DIR = "data"

CLASSES = ["NORMAL", "PNEUMONIA", "NOT_XRAY"]

SPLITS = {
    "train": 0.70,
    "val": 0.15,
    "test": 0.15
}

def create_structure():
    for split in SPLITS.keys():
        for cls in CLASSES:
            os.makedirs(f"{DST_DIR}/{split}/{cls}", exist_ok=True)

def split_class(class_name):
    src_path = f"{SRC_DIR}/{class_name}"
    files = os.listdir(src_path)

    random.shuffle(files)

    total = len(files)
    train_count = int(total * SPLITS["train"])
    val_count = int(total * SPLITS["val"])

    train_files = files[:train_count]
    val_files = files[train_count:train_count+val_count]
    test_files = files[train_count+val_count:]

    # Copy to new folders
    for f in train_files:
        shutil.copy(f"{src_path}/{f}", f"{DST_DIR}/train/{class_name}/{f}")

    for f in val_files:
        shutil.copy(f"{src_path}/{f}", f"{DST_DIR}/val/{class_name}/{f}")

    for f in test_files:
        shutil.copy(f"{src_path}/{f}", f"{DST_DIR}/test/{class_name}/{f}")

    print(f"📌 {class_name}: Total={total} → Train={len(train_files)}, Val={len(val_files)}, Test={len(test_files)}")

def main():
    print("🚀 Splitting dataset into NORMAL / PNEUMONIA / NOT_XRAY...")
    create_structure()

    for cls in CLASSES:
        split_class(cls)

    print("\n✅ Dataset split completed!")

if __name__ == "__main__":
    main()
