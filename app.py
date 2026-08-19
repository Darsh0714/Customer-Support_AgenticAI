import streamlit as st
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate

# Page Configuration
st.set_page_config(page_title="Local AI Task Agent", layout="wide")
st.title("Local AI Task Routing Agent")
st.write("An autonomous agent system that selects and executes Python functions based on user requests.")

# Initialize Local LLM via Ollama
llm = OllamaLLM(model="llama3", temperature=0)

# --- Define Agent Tools (Python Functions) ---
def tool_check_balance(username):
    """Simulates looking up account balances from a database layer."""
    mock_database = {"darshini": "INR 12,500.00", "test_user": "INR 450.00"}
    balance = mock_database.get(username.lower().strip(), "INR 0.00 (Account not found)")
    return f"[TOOL EXECUTION] Successfully checked database. Balance for {username} is {balance}."

def tool_calculate_refund(amount):
    """Simulates calculating an enterprise tiered fractional refund."""
    try:
        base_amt = float(amount)
        refund_amt = base_amt * 0.8
        return f"[TOOL EXECUTION] Calculated 80% partial refund. Original: INR {base_amt}, Refund Due: INR {refund_amt}."
    except ValueError:
        return "[TOOL ERROR] Invalid numeric amount provided to the refund processing tool."

# --- Define Agent Prompts and Routing Logic ---
agent_template = """
You are an operational support agent. Analyze the user request and determine which action to take.
You must respond with exactly one of these choices:
- If they want to check an account balance, reply with: CHECK_BALANCE: <username>
- If they want to calculate a refund for a number amount, reply with: CALCULATE_REFUND: <amount>
- If it is anything else, reply with: GENERAL_REPLY

User Request: {user_input}
Agent Decision:"""

agent_prompt = PromptTemplate(template=agent_template, input_variables=["user_input"])
agent_chain = agent_prompt | llm

# --- User Interface ---
user_input = st.text_input("Enter a request for the agent:", placeholder="e.g., Check my account balance for darshini")

if st.button("Execute Agent Logic"):
    if user_input:
        with st.spinner("Agent routing logic executing..."):
            
            # Step 1: Decision Logic
            decision = agent_chain.invoke({"user_input": user_input}).strip()
            
            st.subheader("Agent Execution Log")
            st.text(f"Model Decision String: {decision}")
            
            # Step 2: Tool Execution Matrix
            st.subheader("Action Output")
            if "CHECK_BALANCE" in decision:
                username = decision.split(":")[-1].strip()
                tool_result = tool_check_balance(username)
                st.info(tool_result)
                
            elif "CALCULATE_REFUND" in decision:
                amount = decision.split(":")[-1].strip()
                tool_result = tool_calculate_refund(amount)
                st.info(tool_result)
                
            else:
                st.text("No matching tool identified. Executing default text response fallback.")
                fallback_template = "Answer this request professionally: {user_input}"
                fallback_prompt = PromptTemplate(template=fallback_template, input_variables=["user_input"])
                fallback_chain = fallback_prompt | llm
                st.write(fallback_chain.invoke({"user_input": user_input}))
    else:
        st.error("Input field cannot be empty.")