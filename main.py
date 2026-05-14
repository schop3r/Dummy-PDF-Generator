import random
from src.core import PDFGenerator
from src.constants import TOPIC_POOL


def main():
    print("--- PDF Dummy Data Generator ---")
    gen = PDFGenerator(output_dir="generated_pdfs")

    selected_topics = random.sample(TOPIC_POOL, 5)

    for topic in selected_topics:
        file_id = random.randint(1000, 9999)
        file_name = f"doc_{topic['tag']}_{file_id}.pdf"

        success = gen.create_pdf(file_name, topic['title'], topic['keys'])
        if success:
            print(f"Successfully generated: {file_name}")


if __name__ == "__main__":
    main()