from typing import TypedDict, Annotated, List, Dict, Any
import operator
# from langchain_core.messages import AnyMessage, SystemMessage, HumanMessage # หากต้องการใช้ message history ใน state
# from langchain_core.prompts import ChatPromptTemplate # สำหรับสร้าง prompt
# from langchain_community.llms import HuggingFaceHub # ตัวอย่างการใช้ LLM จาก Hugging Face
# from langchain_openai import ChatOpenAI # หรือ LLM อื่นๆ
# from langgraph.graph import StateGraph, END # สำหรับสร้าง graph
# from langgraph.checkpoint.sqlite import SqliteSaver # ตัวอย่างสำหรับ persistence

# --- 1. Define Agent State ---
class AgentState(TypedDict):
    user_input: Dict[str, Any]  # Raw input from Streamlit
    processed_order: Dict[str, Any]  # Output from OrderTakerAgent
    cultural_insights: Dict[str, Any]  # Output from CulturalCulinaryScholarAgent
    fusion_ingredients: List[str]  # Output from ExtremeIngredientBrainstormerAgent
    recipe: Dict[str, Any]  # Output from AvantGardeRecipeArchitectAgent (includes rationale)
    image_prompt: str  # Derived from recipe for FoodVisualizerAgent
    image_url: str  # Output from FoodVisualizerAgent
    critique: str  # Output from AI Food Critic (optional)
    # messages: Annotated[List[AnyMessage], operator.add] # หากต้องการเก็บ history การสนทนา

# --- 2. Define Agent Nodes (Placeholder Functions) ---
# ในความเป็นจริง ฟังก์ชันเหล่านี้จะเรียกใช้ LLMs และ models อื่นๆ

def order_taker_agent(state: AgentState) -> Dict[str, Any]:
    print("--- Running Order Taker Agent ---")
    user_input = state["user_input"]
    # TODO: Implement NLU/NER to process user_input using a Hugging Face LLM
    # ตัวอย่างการประมวลผล (ควรใช้ LLM จริง)
    processed_order = {
        "main_ingredients": [ing.strip() for ing in user_input.get("ingredients", "").split(',')] if user_input.get("ingredients") else [],
        "target_cultures": user_input.get("cultures", []),
        "extreme_ingredient_user": user_input.get("extreme_ingredient", ""),
        "extremeness_level": user_input.get("extremeness_level", 3),
        "restrictions": user_input.get("restrictions", {}),
        "parsed_successfully": True
    }
    print(f"Processed Order: {processed_order}")
    return {"processed_order": processed_order}

def cultural_culinary_scholar_agent(state: AgentState) -> Dict[str, Any]:
    print("--- Running Cultural Culinary Scholar Agent ---")
    target_cultures = state.get("processed_order", {}).get("target_cultures", [])
    # TODO: Implement RAG or LLM call to get cultural insights from Hugging Face
    insights: Dict[str, Any] = {}
    for culture in target_cultures:
        insights[culture] = {
            "key_ingredients": [f"{culture}_ing1_demo", f"{culture}_ing2_demo"],
            "flavors": [f"{culture}_flavor_demo"],
            "techniques": [f"{culture}_tech_demo"],
            "philosophy": f"Philosophy of {culture} cuisine (demo)."
        }
    print(f"Cultural Insights: {insights}")
    return {"cultural_insights": insights}

def extreme_ingredient_brainstormer_agent(state: AgentState) -> Dict[str, Any]:
    print("--- Running Extreme Ingredient Brainstormer Agent ---")
    processed_order = state.get("processed_order", {})
    cultural_insights = state.get("cultural_insights", {})
    
    base_ingredients = processed_order.get("main_ingredients", [])
    cultural_ingredients: List[str] = []
    for culture_data in cultural_insights.values():
        cultural_ingredients.extend(culture_data.get("key_ingredients", []))
    
    fusion_ingredients = list(set(base_ingredients + cultural_ingredients)) # ใช้ set เพื่อลบรายการซ้ำ
    
    if processed_order.get("extreme_ingredient_user"):
        fusion_ingredients.append(processed_order["extreme_ingredient_user"])
    
    # TODO: ใช้ LLM ที่มีความสามารถในการคิดเชิงสร้างสรรค์สูง
    print(f"Fusion Ingredients (pre-LLM): {fusion_ingredients}")
    # สมมติว่า LLM อาจจะเพิ่มหรือปรับเปลี่ยนรายการนี้
    # fusion_ingredients.append("AI_suggested_surprise_ingredient")
    print(f"Fusion Ingredients (post-LLM placeholder): {fusion_ingredients}")
    return {"fusion_ingredients": list(set(fusion_ingredients))}


def avant_garde_recipe_architect_agent(state: AgentState) -> Dict[str, Any]:
    print("--- Running Avant-Garde Recipe Architect Agent ---")
    fusion_ingredients = state.get("fusion_ingredients", [])
    target_cultures = state.get("processed_order", {}).get("target_cultures", [])
    # TODO: Generate full recipe and rationale using a storytelling LLM
    menu_name_demo = f"AI Fusion: {', '.join(target_cultures)} Delight with {fusion_ingredients[0] if fusion_ingredients else 'Mystery'}"
    recipe = {
        "menu_name": menu_name_demo,
        "ingredients_list_detailed": [{ing: "1 unit (demo)"} for ing in fusion_ingredients],
        "cooking_steps": "1. Demo Step: Mix everything with passion.\n2. Demo Step: Cook until awesome.\n3. Demo Step: Plate like an artist.",
        "chef_rationale": f"This dish (demo) explores the exciting intersection of {', '.join(target_cultures)} cuisines, highlighting the unique potential of combining {', '.join(fusion_ingredients[:2])}..."
    }
    image_prompt = f"Photorealistic, michelin star plating, fusion cuisine: {recipe['menu_name']}, main ingredients {', '.join(fusion_ingredients[:3]) if fusion_ingredients else 'various ingredients'}, vibrant colors, dramatic lighting, inspired by {', '.join(target_cultures)}."
    print(f"Recipe: {recipe['menu_name']}")
    print(f"Image Prompt: {image_prompt}")
    return {"recipe": recipe, "image_prompt": image_prompt}

def ai_food_visualizer_agent(state: AgentState) -> Dict[str, Any]:
    print("--- Running AI Food Visualizer Agent ---")
    image_prompt = state.get("image_prompt", "A delicious dish")
    menu_name = state.get("recipe", {}).get("menu_name", "Fusion Dish")
    # TODO: Call Text-to-Image model (e.g., Stable Diffusion via Hugging Face diffusers)
    # from diffusers import StableDiffusionPipeline
    # pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5") # Example
    # image = pipe(image_prompt).images[0]
    # image_url = save_image_and_get_url(image) # Placeholder
    image_url = f"https://via.placeholder.com/500x300.png?text={menu_name.replace(' ', '+')[:50]}" # Placeholder
    print(f"Generated Image URL: {image_url}")
    return {"image_url": image_url}

# (Optional) AI Food Critic Agent
def ai_food_critic_agent(state: AgentState) -> Dict[str, Any]:
    print("--- Running AI Food Critic Agent ---")
    recipe_name = state.get("recipe", {}).get("menu_name", "the dish")
    # TODO: LLM evaluates the recipe
    critique = f"Critique (demo): '{recipe_name}' is a bold concept! Consider the textural interplay. Overall, very promising."
    print(f"Critique: {critique}")
    return {"critique": critique}

# --- 3. Define Graph (Conceptual - Actual LangGraph code needed here) ---
# def create_graph():
#     workflow = StateGraph(AgentState)
#     workflow.add_node("order_taker", order_taker_agent)
#     workflow.add_node("cultural_scholar", cultural_culinary_scholar_agent)
#     workflow.add_node("ingredient_brainstormer", extreme_ingredient_brainstormer_agent)
#     workflow.add_node("recipe_architect", avant_garde_recipe_architect_agent)
#     workflow.add_node("food_visualizer", ai_food_visualizer_agent)
#     # workflow.add_node("food_critic", ai_food_critic_agent) # Optional

#     workflow.set_entry_point("order_taker")
#     workflow.add_edge("order_taker", "cultural_scholar")
#     workflow.add_edge("cultural_scholar", "ingredient_brainstormer")
#     workflow.add_edge("ingredient_brainstormer", "recipe_architect")
#     workflow.add_edge("recipe_architect", "food_visualizer")
#     workflow.add_edge("food_visualizer", END) # Or to critic then END
    
#     # Example for critic loop (simplified)
#     # workflow.add_conditional_edges(
#     # "food_visualizer",
#     # lambda x: "food_critic" if x.get("extremeness_level", 0) > 3 else END, # Example condition
#     # {"food_critic": "food_critic", END: END}
#     # )
#     # workflow.add_edge("food_critic", END)
#     # app = workflow.compile()
#     # return app

# # app = create_graph() # This would be your compiled LangGraph application

# --- 4. Main Invocation Function (Placeholder for actual graph execution) ---
def run_ai_chef_graph(user_input_dict: Dict[str, Any]) -> Dict[str, Any]:
    """
    Simulates running the LangGraph graph by calling agents sequentially.
    Replace this with `app.invoke()` or `app.stream()` when LangGraph is fully set up.
    """
    current_state: AgentState = { # type: ignore
        "user_input": user_input_dict,
        "processed_order": {}, "cultural_insights": {}, "fusion_ingredients": [],
        "recipe": {}, "image_prompt": "", "image_url": "", "critique": ""
    }

    current_state.update(order_taker_agent(current_state))
    current_state.update(cultural_culinary_scholar_agent(current_state))
    current_state.update(extreme_ingredient_brainstormer_agent(current_state))
    current_state.update(avant_garde_recipe_architect_agent(current_state))
    current_state.update(ai_food_visualizer_agent(current_state))
    # current_state.update(ai_food_critic_agent(current_state)) # Uncomment if using critic

    # Prepare output for Streamlit
    recipe_details = current_state.get("recipe", {})
    final_output = {
        "menu_name": recipe_details.get("menu_name", "AI Chef's Special (Demo)"),
        "image_url": current_state.get("image_url", "https://via.placeholder.com/300"),
        "ingredients_list": [ing for ing_dict in recipe_details.get("ingredients_list_detailed", []) for ing in ing_dict.keys()],
        "cooking_steps": recipe_details.get("cooking_steps", "No steps provided (demo)."),
        "chef_rationale": recipe_details.get("chef_rationale", "No rationale provided (demo)."),
        "drink_pairing": "AI Suggested Drink (to be implemented, demo)", # Future enhancement
        "critique": current_state.get("critique", "") # Include critique if available
    }
    return final_output

if __name__ == '__main__':
    # Example usage (for testing this file directly)
    sample_input_data = {
        "ingredients": "ไก่, ข้าว, พริก",
        "cultures": ["ไทย", "เม็กซิกัน"],
        "extreme_ingredient": "จิ้งหรีด",
        "extremeness_level": 4,
        "restrictions": {"vegetarian": False, "vegan": False, "nut_allergy": False, "not_spicy": False}
    }
    result = run_ai_chef_graph(sample_input_data)
    print("\n--- Final Result (Demo) ---")
    import json
    print(json.dumps(result, indent=2, ensure_ascii=False))