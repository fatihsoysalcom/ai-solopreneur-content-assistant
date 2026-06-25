import sys

def generate_ai_content(prompt):
    """
    Simulates an AI assistant generating content based on a prompt.
    In a real scenario, this would involve an actual AI model (e.g., LLM API call).
    Here, we use simple logic to illustrate the concept of AI-powered content generation
    for a solopreneur, helping them overcome resource limitations.
    """
    prompt_lower = prompt.lower()
    response_parts = []

    response_parts.append(f"AI Asistanı: Harika bir fikir! İşte '{prompt}' için bir taslak:")

    if "blog post" in prompt_lower or "makale" in prompt_lower:
        response_parts.append("\n--- Blog Yazısı Taslağı ---")
        response_parts.append("Başlık Fikirleri:")
        response_parts.append(f"- {prompt.replace('yaz', '').strip()} Hakkında Kapsamlı Rehber")
        response_parts.append(f"- {prompt.replace('yaz', '').strip()} ile Başarıya Ulaşmak")
        response_parts.append("\nGiriş:")
        response_parts.append("  - Konuya genel bakış ve okuyucunun ilgisini çekme.")
        response_parts.append("  - Makalenin ana hedefini belirtme.")
        response_parts.append("\nAna Bölümler:")
        response_parts.append("  1. Konunun Tanımı ve Önemi")
        response_parts.append("  2. Temel Adımlar/Yöntemler")
        response_parts.append("  3. Yaygın Zorluklar ve Çözümleri")
        response_parts.append("\nSonuç:")
        response_parts.append("  - Ana noktaların özeti.")
        response_parts.append("  - Okuyucuya eylem çağrısı veya ilham verici bir mesaj.")
    elif "social media" in prompt_lower or "sosyal medya" in prompt_lower or "tweet" in prompt_lower:
        response_parts.append("\n--- Sosyal Medya Gönderisi Taslağı ---")
        response_parts.append(f"Harika bir {prompt_lower.split('hakkında')[0].strip()} gönderisi için fikirler:")
        response_parts.append(f"- Heyecan verici haber! Yeni {prompt.replace('sosyal medya gönderisi yaz', '').strip()} ile tanışın! ✨ #Yenilik #Girişimcilik")
        response_parts.append(f"- Tek kişilik girişimci olarak {prompt.replace('sosyal medya gönderisi yaz', '').strip()} konusunda ipuçları mı arıyorsunuz? İşte size özel bir gönderi! 👇 #Solopreneur #AI")
        response_parts.append(f"- {prompt.replace('sosyal medya gönderisi yaz', '').strip()} hakkında düşündükleriniz neler? Yorumlarda bize katılın! 💬")
    elif "product description" in prompt_lower or "ürün açıklaması" in prompt_lower:
        response_parts.append("\n--- Ürün Açıklaması Taslağı ---")
        response_parts.append("Ürün Adı: [Ürün Adını Buraya Girin]")
        response_parts.append("Kısa Açıklama: [Ürünün en çekici özelliğini 1-2 cümlede özetleyin]")
        response_parts.append("\nÖzellikler:")
        response_parts.append("  - Özellik 1: Faydası 1")
        response_parts.append("  - Özellik 2: Faydası 2")
        response_parts.append("  - Özellik 3: Faydası 3")
        response_parts.append("\nNeden Bu Ürünü Seçmelisiniz?")
        response_parts.append("  - Sorun Çözümü: [Ürünün hangi sorunu çözdüğünü belirtin]")
        response_parts.append("  - Değer Teklifi: [Ürünün benzersiz değerini vurgulayın]")
        response_parts.append("\nŞimdi Satın Alın ve [Fayda] deneyimleyin!")
    else:
        response_parts.append("\n--- Genel İçerik Taslağı ---")
        response_parts.append(f"Konu: {prompt}")
        response_parts.append("Ana Fikirler:")
        response_parts.append("  - Giriş: Konuya genel bir bakış.")
        response_parts.append("  - Gelişme: Ana noktaları detaylandırın.")
        response_parts.append("  - Sonuç: Özet ve kapanış.")
        response_parts.append("\nBu taslağı kendi yaratıcılığınızla zenginleştirebilirsiniz!")

    return "\n".join(response_parts)

def main():
    print("AI Solopreneur Asistanına Hoş Geldiniz!")
    print("Tek kişilik girişimcilik yolculuğunuzda size yardımcı olmak için buradayım.")
    print("Örnek: 'Yapay zeka ile girişimcilik hakkında blog yazısı taslağı yaz'")
    print("Örnek: 'Yeni bir ürün lansmanı için sosyal medya gönderisi fikirleri ver'")
    print("Çıkmak için 'çıkış' yazın.")

    while True:
        try:
            user_prompt = input("\nSenin için ne yapabilirim? (Prompt girin): ")
            if user_prompt.lower() in ["çıkış", "exit"]:
                print("Görüşmek üzere! Başarılar dilerim.")
                break

            if not user_prompt.strip():
                print("Lütfen geçerli bir prompt girin.")
                continue

            # This is where the AI's "saving role" is demonstrated:
            # A solopreneur can quickly get content drafts without needing a team or extensive manual effort.
            ai_response = generate_ai_content(user_prompt)
            print(ai_response)

        except EOFError:
            print("\nÇıkış yapılıyor...")
            break
        except KeyboardInterrupt:
            print("\nÇıkış yapılıyor...")
            break
        except Exception as e:
            print(f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    main()
