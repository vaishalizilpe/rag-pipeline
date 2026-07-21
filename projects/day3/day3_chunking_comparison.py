from pathlib import Path
from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter

DOC_PATH = Path(__file__).resolve().parents[2] / "README.md"
text = DOC_PATH.read_text()

CHUNK_SIZE = 500

# 1. Fixed-size, no overlap -- naive, cuts mid-sentence freely
fixed_no_overlap = CharacterTextSplitter(
    separator="", chunk_size=CHUNK_SIZE, chunk_overlap=0
).split_text(text)

# 2. Fixed-size, 20% overlap -- softens boundary loss, still ignores sentence structure
fixed_with_overlap = CharacterTextSplitter(
    separator="", chunk_size=CHUNK_SIZE, chunk_overlap=int(CHUNK_SIZE * 0.2)
).split_text(text)

# 3. Recursive, respects paragraph/sentence boundaries when possible
recursive = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE, chunk_overlap=int(CHUNK_SIZE * 0.2)
).split_text(text)


def show(name, chunks):
    print(f"\n{'=' * 70}\n{name}  ({len(chunks)} chunks)\n{'=' * 70}")
    for i, chunk in enumerate(chunks[:3], 1):
        preview = chunk.replace("\n", " ⏎ ")
        print(f"\n--- chunk {i} ---\n{preview[:300]}")


show("1. FIXED SIZE, NO OVERLAP", fixed_no_overlap)
show("2. FIXED SIZE, 20% OVERLAP", fixed_with_overlap)
show("3. RECURSIVE (paragraph/sentence aware)", recursive)

print(f"\n{'=' * 70}")
print("Look at chunk boundaries above: does chunk 1 or 2 cut a sentence")
print("or heading in half where chunk 3 doesn't?")
