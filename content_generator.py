import random
from scholarships import SCHOLARSHIPS_DB
from lifehacks import LIFEHACKS_DB
from config import RED_FLAGS

class ContentGenerator:
    def check_red_flags(self, text):
        text_lower = text.lower()
        for category, keywords in RED_FLAGS.items():
            for keyword in keywords:
                if keyword in text_lower:
                    return False, f"Найдено: {category}"
        return True, "OK"
    
    def generate_scholarship_post(self):
        scholarship = random.choice(SCHOLARSHIPS_DB)
        post = f"""
🎓 {scholarship['name']}

Страна: {scholarship['country']}
Описание: {scholarship['description']}

Выгода:
""" + "\n".join([f"• {b}" for b in scholarship['benefits']]) + f"""

Требования:
""" + "\n".join([f"• {r}" for r in scholarship['requirements']]) + f"""

Дедлайн: {scholarship['deadline']}
Результаты: {scholarship['results_date']}
Начало: {scholarship['start_date']}

{scholarship['engagement_question']}
        """
        is_safe, msg = self.check_red_flags(post)
        return post.strip() if is_safe else None
    
    def generate_lifehack_post(self):
        lifehack = random.choice(LIFEHACKS_DB)
        post = f"""
💡 {lifehack['title']}

Категория: {lifehack['category']}
Уровень: {lifehack['level']}

{lifehack['intro']}

{lifehack['content']}

Результат: {lifehack['result']}

{lifehack['engagement_question']}
        """
        is_safe, msg = self.check_red_flags(post)
        return post.strip() if is_safe else None
