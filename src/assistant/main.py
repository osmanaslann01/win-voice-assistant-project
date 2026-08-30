from src.assistant.assistant import Assistant


def main() -> None:
    assistant = Assistant()

    print("Win Voice Assistant")
    print("Çıkmak için 'çıkış' yazın.")

    while True:
        text = input("Komut > ").strip()

        if text.lower() in {"çıkış", "exit", "quit"}:
            print("Asistan kapatılıyor...")
            break

        assistant.process(text)


if __name__ == "__main__":
    main()
    