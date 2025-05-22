import streamlit as st

# --- Helper Functions (Placeholder) ---
# ในอนาคต ฟังก์ชันเหล่านี้จะเรียก LangGraph agents
def generate_fusion_cuisine(ingredients, cultures, extreme_ingredient, extremeness_level, restrictions):
    # Placeholder: นี่คือส่วนที่จะเชื่อมต่อกับ LangGraph และ AI agents
    # ในตอนนี้จะ return ค่าจำลองไปก่อน
    print(f"Inputs: {ingredients}, {cultures}, {extreme_ingredient}, {extremeness_level}, {restrictions}")
    return {
        "menu_name": "ต้มยำทาโก้ลาวา (ตัวอย่าง)",
        "image_url": "https://via.placeholder.com/500x300.png?text=ต้มยำทาโก้ลาวา", # URL รูปภาพตัวอย่าง
        "ingredients_list": ["กุ้งแม่น้ำ", "แป้งทาโก้", "พริกขี้หนู", "มะนาว", "ตะไคร้", "ใบมะกรูด", "ซอสโมเล่ (ตัวอย่าง)"],
        "cooking_steps": "1. เตรียมวัตถุดิบ...\n2. ผัดเครื่องต้มยำ...\n3. ประกอบร่างกับทาโก้...",
        "chef_rationale": "เป็นการผสมผสานความจัดจ้านของต้มยำไทยเข้ากับความสนุกของทาโก้เม็กซิกัน เพิ่มความซับซ้อนด้วยซอสโมเล่",
        "drink_pairing": "น้ำมะพร้าวปั่น หรือ Michelada"
    }

# --- UI Setup ---
st.set_page_config(page_title="Extreme Fusion Cuisine AI Chef", layout="wide")

st.title("Extreme Fusion Cuisine AI Chef 🧑‍🍳🌶️🌏")
st.markdown("### กล้าฉีกทุกกฎเกณฑ์ด้านอาหาร สร้างสรรค์เมนูฟิวชั่นที่เหนือจินตนาการ!")

# --- Input Section ---
st.sidebar.header("ห้องครัวของคุณ (Your Kitchen Lab)")

with st.sidebar.form(key="chef_input_form"):
    st.subheader("วัตถุดิบในตู้เย็น (Your Fridge)")
    ingredients_input = st.text_area("ระบุวัตถุดิบที่มี (คั่นด้วยจุลภาค)", "กุ้ง, มะม่วง, พริกหยวก, ข้าวสวย")

    st.subheader("แรงบันดาลใจจากต่างแดน (Cultural Inspiration)")
    available_cultures = ["ไทย", "ญี่ปุ่น", "เม็กซิกัน", "อิตาเลียน", "อินเดีย", "ฝรั่งเศส", "เกาหลี", "เปรู", "ไวกิ้งโบราณ", "อาหารจากหนัง Sci-Fi"]
    selected_cultures = st.multiselect("เลือกวัฒนธรรมอาหารที่อยากผสม (เลือกได้มากกว่า 1)", available_cultures, default=["ไทย", "เม็กซิกัน"])
    custom_culture = st.text_input("หรือเพิ่มวัฒนธรรมอื่นๆ (ถ้ามี)")
    if custom_culture and custom_culture not in selected_cultures:
        selected_cultures.append(custom_culture)

    st.subheader("โจทย์สุดท้าทาย! (Extreme Challenge!)")
    extreme_ingredient_input = st.text_input("(Optional) ใส่วัตถุดิบ 'สุดแปลก' ที่อยากให้ AI นำมาใช้", "ทุเรียน")

    st.subheader("ระดับความสุดขั้ว (Extremeness Level)")
    extremeness_level_input = st.slider("เลือกความสุดขั้ว (1=ฟิวชั่นเบาๆ, 5=หลุดโลกไปเลย!)", 1, 5, 3)

    st.subheader("ข้อจำกัดพิเศษ (Special Restrictions)")
    is_vegetarian = st.checkbox("มังสวิรัติ (Vegetarian)")
    is_vegan = st.checkbox("วีแกน (Vegan)")
    has_nut_allergy = st.checkbox("แพ้ถั่ว (Nut Allergy)")
    not_spicy = st.checkbox("ไม่เผ็ด (Not Spicy)")

    restrictions_input = {
        "vegetarian": is_vegetarian,
        "vegan": is_vegan,
        "nut_allergy": has_nut_allergy,
        "not_spicy": not_spicy
    }

    submit_button = st.form_submit_button(label="รังสรรค์เมนู! (Generate Menu!)")

# --- Output Section ---
if submit_button:
    st.header("เมนูสุดจี๊ดจากเชฟ AI (AI Chef's Creation)")

    # Simulate calling the AI backend
    with st.spinner("เชฟ AI กำลังปรุงอาหารสุดขั้ว... โปรดรอสักครู่..."):
        # นี่คือส่วนที่จะเรียก AI agents จริงๆ
        # recipe_details = generate_fusion_cuisine(
        #     ingredients_input.split(','),
        #     selected_cultures,
        #     extreme_ingredient_input,
        #     extremeness_level_input,
        #     restrictions_input
        # )
        # For now, using placeholder function
        recipe_details = generate_fusion_cuisine(
            [ing.strip() for ing in ingredients_input.split(',')],
            selected_cultures,
            extreme_ingredient_input,
            extremeness_level_input,
            restrictions_input
        )


    if recipe_details:
        st.subheader(f"🍽️ {recipe_details['menu_name']}")

        if recipe_details.get("image_url"):
            st.image(recipe_details["image_url"], caption="ภาพจำลองเมนู (AI Generated Image)", use_column_width=True)

        st.markdown("### 📖 ตำราลับเชฟ AI (AI Chef's Secret Cookbook)")

        with st.expander("รายการวัตถุดิบ (Ingredients)"):
            for item in recipe_details["ingredients_list"]:
                st.markdown(f"- {item}")

        with st.expander("ขั้นตอนการปรุงอย่างละเอียด (Cooking Steps)"):
            st.markdown(recipe_details["cooking_steps"])

        with st.expander("ปรัชญาจานนี้ (Chef's Rationale)"):
            st.markdown(recipe_details["chef_rationale"])

        if recipe_details.get("drink_pairing"):
            st.markdown("---")
            st.markdown(f"🥂 **จับคู่เครื่องดื่ม (Suggested Pairing):** {recipe_details['drink_pairing']}")

        st.markdown("---")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("ขอสูตรอื่น! (Request Another Recipe!)"):
                st.info("ฟังก์ชันนี้จะพัฒนาในอนาคต (Coming soon!)") # Placeholder
        with col2:
            if st.button("ให้คะแนนความว้าว! (Rate Wow Factor!)"):
                st.info("ขอบคุณสำหรับ Feedback! (Coming soon!)") # Placeholder

    else:
        st.error("ขออภัย เชฟ AI ไม่สามารถสร้างสรรค์เมนูได้ในขณะนี้ ลองปรับเปลี่ยนข้อมูลดูนะครับ")

else:
    st.info("กรอกข้อมูลในแถบด้านข้างแล้วกด 'รังสรรค์เมนู!' เพื่อให้เชฟ AI เริ่มทำงาน")