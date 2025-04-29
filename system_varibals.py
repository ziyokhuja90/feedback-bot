malumotlar = {
    "group":"",
    "teacher_name":"",
    "teacher_p":"",
    "teacher_n":"",
    "teacher_score":"",
    "valiteach":"",
    "why_valiteach":"",

}
from dotenv import load_dotenv
import os


# main vars
TOKEN = os.getenv("BOT_TOKEN")

BRAND_NAME = "IT-Line"
CHANNEL_ID = "-1002651153176"
CITY = "Qo'qon"
FEEDBACK_BTN_TEXT = "Fikr qoldirish"
# examples
EXAMPLE_TIME = "Dushanba, Chorshanba , Juma - 15:00"
EXAMPLE_TEACHER = "Abdullayev Ziyoxo'ja"

# responces
START_R = """Xush kelibsiz!

Assalomu alaykum, hurmatli foydalanuvchi! Ushbu bot sizdan qimmatli fikr-mulohazalarni olish uchun yaratilgan. Fikrlaringiz biz uchun juda muhim va ularni yaxshiroq xizmat ko'rsatish uchun ishlatamiz.

✅ Iltimos, bizga fikrlaringizni yuboring.

ℹ️ Eslatma: Ushbu bot orqali yuborilgan hech qanday shaxsiy ma'lumotlar saqlanmaydi va maxfiyligingizni himoya qilamiz.

Matn yuborish uchun "Fikr qoldirish" tugmasini bosing."""
FEEDBACK_BTN_R = F"""Guruhingizning vaqti va kunlarini kiriting

Hurmatli foydalanuvchi, iltimos, guruhingizning dars o'tkaziladigan vaqti va kunlarini kiriting. 

⏰ Misol: {EXAMPLE_TIME}"""
GROUP_R = f"""O'qituvchingizning ismini kiriting

Hurmatli foydalanuvchi, iltimos, dars o'tayotgan o'qituvchingizning ismini kiriting. Bu ma'lumot bizga sizning fikr-mulohazalaringizni to'g'ri odamga yo'naltirishda yordam beradi.

📋 Misol: {EXAMPLE_TEACHER}"""

TEACHERNAME_R = """Sizning o'qituvchingiz haqida fikringiz qanday?

Hurmatli foydalanuvchi, sizning fikringiz biz uchun juda muhim! Iltimos, o'qituvchingiz haqida ijobiy fikrlaringizni biz bilan baham ko'ring. O'qituvchingizning sizga qanday yordam bergani yoki qanday yaxshi xususiyatlari borligini yozib yuboring.

📜 Biz sizning fikrlaringizni qadrlaymiz va ularni o'qituvchilarimizni qo'llab-quvvatlash uchun ishlatamiz.
"""

TEACHER_P_R = """Sizning o'qituvchingiz haqida tanqidingiz bormi?

Hurmatli foydalanuvchi, biz barcha fikr-mulohazalaringizni eshitishni xohlaymiz. Iltimos, o'qituvchingiz haqida sizni qoniqtirmagan jihatlarni biz bilan baham ko'ring. O'qituvchining qaysi xatti-harakatlari yoki o'qitish usuli sizga yoqmaganini yozib yuboring.

⚠️ Sizning salbiy fikrlaringiz biz uchun juda muhim va o'qituvchilarimizni yaxshilashda yordam beradi.
"""

TEACHER_N_R = """O'qituvchingizga baho bering

Hurmatli foydalanuvchi, iltimos, o'qituvchingizga 0 dan 10 gacha baho bering. Sizning bahoingiz o'qituvchining darslarni qanday o'tayotgani va umumiy ish faoliyatini baholashga yordam beradi.

🔢 0 - umuman qoniqarli emas
🔢 10 - juda a'lo darajada

Iltimos, tanlovingizni biz bilan baham ko'ring."""

TEACHER_SCORE_R = """O'quv markazimizga takliflaringiz bormi?

Hurmatli foydalanuvchi, biz o'quv markazimizni yanada yaxshilash uchun sizning takliflaringizni eshitishni istaymiz. Iltimos, darslarimiz, o'qituvchilarimiz yoki umumiy muhitimizni yaxshilash bo'yicha har qanday takliflaringizni biz bilan baham ko'ring.

💡 Sizning takliflaringiz biz uchun juda muhim va o'quv markazimizni yanada samarali qilishga yordam beradi.
"""

LEARNING_CENTER_R = F"""{CITY} shahrida turli o‘quv markazlari bor, lekin siz aynan {BRAND_NAME}’ni tanladingiz! 🌟 Bu qaroringizga nima sabab bo‘ldi? Fikringiz biz uchun juda muhim! 📝😊
"""



WHY_R = f"""Fikr-mulohazangiz uchun rahmat!

Hurmatli foydalanuvchi, sizning fikrlaringiz uchun katta rahmat! Biz sizning taklif va mulohazalaringizni albatta inobatga olamiz va xizmatlarimizni yanada yaxshilash uchun ulardan foydalanamiz.

🌟 Sizning ishtirokingiz va qo'llab-quvvatlashingiz biz uchun juda qadrli!

Agar yana biror narsa haqida o'z fikringizni bildirmoqchi bo'lsangiz, istalgan vaqtda biz bilan bog'lanishingiz mumkin."""

ECHO_R = 'Fikr qoldirish uchun "Fikr qoldirish" tugmasini bosing'