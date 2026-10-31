import streamlit as st
from prediction_helper import predict

# =====================================================
# PAGE CONFIGURATION
# =====================================================
st.set_page_config(
    page_title="Health Insurance Predictor",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =====================================================
# CUSTOM CSS
# =====================================================
st.html("""
<style>
.stApp {
    background: linear-gradient(
        135deg, #eff8ff 0%, #f8fbff 50%, #e8f8f7 100%
    );
    color: #17365d;
}

.block-container {
    max-width: 1200px;
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.hero {
    background: linear-gradient(120deg, #075985, #0284c7, #06b6d4);
    padding: 38px 35px;
    border-radius: 25px;
    color: white;
    margin-bottom: 28px;
    box-shadow: 0 12px 30px rgba(2, 132, 199, 0.18);
}

.hero h1 {
    color: white !important;
    font-size: 38px;
    font-weight: 800;
    margin-bottom: 12px;
}

.hero p {
    color: #e0f7ff !important;
    font-size: 17px;
    line-height: 1.7;
}

.hero-badges {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-top: 20px;
}

.hero-badge {
    background: rgba(255, 255, 255, 0.15);
    border: 1px solid rgba(255, 255, 255, 0.3);
    padding: 9px 14px;
    border-radius: 30px;
    font-size: 13px;
    color: white;
}

.section-title {
    font-size: 24px;
    font-weight: 800;
    color: #075985;
    margin-top: 28px;
    margin-bottom: 5px;
}

.section-subtitle {
    color: #64748b;
    font-size: 14px;
    margin-bottom: 15px;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(255, 255, 255, 0.88);
    border: 1px solid #dbeafe;
    border-radius: 20px;
    padding: 20px;
    box-shadow: 0 5px 20px rgba(30, 64, 175, 0.04);
}

.stNumberInput label,
.stSelectbox label,
.stSlider label,
.stSelectSlider label {
    color: #334155 !important;
    font-weight: 650 !important;
    font-size: 14px !important;
}

div[data-testid="stNumberInput"] input {
    border-radius: 11px;
    border: 1px solid #cbdff3;
    min-height: 42px;
}

div[data-testid="stSelectbox"] > div > div {
    border-radius: 11px;
    border-color: #cbdff3;
    min-height: 42px;
}

.plan-card {
    padding: 18px 12px;
    border-radius: 16px;
    text-align: center;
    margin-bottom: 12px;
}

.bronze {
    background: linear-gradient(135deg, #fff7ed, #ffedd5);
    border: 1px solid #fed7aa;
}

.silver {
    background: linear-gradient(135deg, #eff6ff, #dbeafe);
    border: 1px solid #93c5fd;
}

.gold {
    background: linear-gradient(135deg, #fffbeb, #fef3c7);
    border: 1px solid #fcd34d;
}

.plan-icon {
    font-size: 32px;
    margin-bottom: 7px;
}

.plan-name {
    font-size: 19px;
    font-weight: 800;
    color: #1e3a5f;
    margin-bottom: 5px;
}

.plan-description {
    color: #64748b;
    font-size: 13px;
}

.stButton > button {
    background: linear-gradient(90deg, #0369a1, #0284c7, #06b6d4);
    color: white !important;
    font-size: 18px;
    font-weight: 750;
    border: none;
    border-radius: 14px;
    padding: 15px 22px;
    min-height: 55px;
    box-shadow: 0 7px 18px rgba(2, 132, 199, 0.22);
}

.stButton > button:hover {
    background: linear-gradient(90deg, #075985, #0369a1);
}

.result-card {
    background: linear-gradient(135deg, #ffffff, #ecfeff);
    border: 2px solid #67e8f9;
    border-radius: 24px;
    padding: 32px 20px;
    text-align: center;
    margin-top: 28px;
    box-shadow: 0 10px 30px rgba(8, 145, 178, 0.10);
}

.result-icon {
    font-size: 38px;
    margin-bottom: 8px;
}

.result-label {
    color: #475569;
    font-size: 18px;
    font-weight: 650;
}

.result-value {
    color: #0369a1;
    font-size: 42px;
    font-weight: 850;
    margin: 12px 0;
    overflow-wrap: anywhere;
}

.result-note {
    color: #64748b;
    font-size: 13px;
    line-height: 1.7;
}

.info-box {
    background: #eff6ff;
    border-left: 4px solid #0284c7;
    padding: 14px 17px;
    border-radius: 10px;
    color: #334155;
    font-size: 13px;
    line-height: 1.7;
    margin-top: 18px;
}

@media (max-width: 768px) {
    .hero {
        padding: 25px 20px;
    }

    .hero h1 {
        font-size: 29px;
    }

    .hero p {
        font-size: 15px;
    }

    .section-title {
        font-size: 21px;
    }

    .result-value {
        font-size: 32px;
    }
}

footer {
    visibility: hidden;
}
</style>
""")

# =====================================================
# HERO HEADER
# =====================================================
st.html("""
<div class="hero">
    <h1>🏥 Health Insurance Cost Predictor</h1>

    <p>
        Understand your estimated health insurance costs
        with the power of Machine Learning.<br>
        Enter your details below to get your personalized estimate.
    </p>

    <div class="hero-badges">
        <div class="hero-badge">🛡️ Smarter Planning</div>
        <div class="hero-badge">💚 Health Awareness</div>
        <div class="hero-badge">⚙️ Machine Learning</div>
    </div>
</div>
""")

# =====================================================
# CATEGORICAL OPTIONS
# =====================================================
categorical_options = {
    "Gender": ["Male", "Female"],
    "Marital Status": ["Unmarried", "Married"],
    "BMI Category": [
        "Normal", "Obesity", "Overweight", "Underweight"
    ],
    "Smoking Status": [
        "No Smoking", "Regular", "Occasional"
    ],
    "Employment Status": [
        "Salaried", "Self-Employed", "Freelancer", ""
    ],
    "Region": [
        "Northwest", "Southeast", "Northeast", "Southwest"
    ],
    "Medical History": [
        "No Disease",
        "Diabetes",
        "High blood pressure",
        "Diabetes & High blood pressure",
        "Thyroid",
        "Heart disease",
        "High blood pressure & Heart disease",
        "Diabetes & Thyroid",
        "Diabetes & Heart disease"
    ],
    "Insurance Plan": ["Bronze", "Silver", "Gold"]
}

# =====================================================
# PERSONAL INFORMATION
# =====================================================
st.html("""
<div class="section-title">👤 Personal Information</div>
<div class="section-subtitle">
    Tell us a little about yourself.
</div>
""")

with st.container(border=True):
    row1 = st.columns(3)

    with row1[0]:
        age = st.number_input(
            "🎂 Age (years)",
            min_value=18,
            max_value=100,
            value=25,
            step=1
        )

    with row1[1]:
        gender = st.selectbox(
            "👤 Gender", categorical_options["Gender"]
        )

    with row1[2]:
        marital_status = st.selectbox(
            "💍 Marital Status",
            categorical_options["Marital Status"]
        )

    row2 = st.columns(3)

    with row2[0]:
        number_of_dependants = st.number_input(
            "👨‍👩‍👧 Number of Dependants",
            min_value=0,
            max_value=20,
            value=0,
            step=1
        )

    with row2[1]:
        income_lakhs = st.number_input(
            "💰 Annual Income (Lakhs)",
            min_value=0.0,
            max_value=200.0,
            value=5.0,
            step=1.0
        )

    with row2[2]:
        employment_status = st.selectbox(
            "💼 Employment Status",
            categorical_options["Employment Status"],
            format_func=lambda x: "Not Specified" if x == "" else x
        )

# =====================================================
# HEALTH AND LIFESTYLE
# =====================================================
st.html("""
<div class="section-title">🩺 Health & Lifestyle</div>
<div class="section-subtitle">
    Share your health and lifestyle information.
</div>
""")

with st.container(border=True):
    row3 = st.columns(3)

    with row3[0]:
        bmi_category = st.selectbox(
            "⚖️ BMI Category",
            categorical_options["BMI Category"]
        )

    with row3[1]:
        smoking_status = st.selectbox(
            "🚭 Smoking Status",
            categorical_options["Smoking Status"]
        )

    with row3[2]:
        genetical_risk = st.number_input(
            "🧬 Genetical Risk",
            min_value=0,
            max_value=5,
            value=0,
            step=1
        )

    row4 = st.columns(2)

    with row4[0]:
        medical_history = st.selectbox(
            "🩻 Medical History",
            categorical_options["Medical History"]
        )

    with row4[1]:
        region = st.selectbox(
            "📍 Region", categorical_options["Region"]
        )

# =====================================================
# INSURANCE PLAN
# =====================================================
st.html("""
<div class="section-title">🛡️ Choose Your Insurance Plan</div>
<div class="section-subtitle">
    Select a plan to include it in your prediction.
</div>
""")

with st.container(border=True):
    plan_col1, plan_col2, plan_col3 = st.columns(3)

    with plan_col1:
        st.html("""
        <div class="plan-card bronze">
            <div class="plan-icon">🥉</div>
            <div class="plan-name">Bronze</div>
            <div class="plan-description">Basic coverage tier</div>
        </div>
        """)

    with plan_col2:
        st.html("""
        <div class="plan-card silver">
            <div class="plan-icon">🥈</div>
            <div class="plan-name">Silver</div>
            <div class="plan-description">Mid-level coverage tier</div>
        </div>
        """)

    with plan_col3:
        st.html("""
        <div class="plan-card gold">
            <div class="plan-icon">🥇</div>
            <div class="plan-name">Gold</div>
            <div class="plan-description">Higher coverage tier</div>
        </div>
        """)

    insurance_plan = st.select_slider(
        "Select Your Plan",
        options=categorical_options["Insurance Plan"],
        value="Silver",
        help="Choose Bronze, Silver or Gold."
    )

    if insurance_plan == "Bronze":
        st.info("🥉 Bronze selected — Basic coverage tier.")
    elif insurance_plan == "Silver":
        st.info("🥈 Silver selected — Mid-level coverage tier.")
    else:
        st.info("🥇 Gold selected — Higher coverage tier.")

# =====================================================
# PREPARE MODEL INPUT
# =====================================================
input_dict = {
    "Age": age,
    "Number of Dependants": number_of_dependants,
    "Income in Lakhs": income_lakhs,
    "Genetical Risk": genetical_risk,
    "Insurance Plan": insurance_plan,
    "Employment Status": employment_status,
    "Gender": gender,
    "Marital Status": marital_status,
    "BMI Category": bmi_category,
    "Smoking Status": smoking_status,
    "Region": region,
    "Medical History": medical_history
}

# =====================================================
# PREDICTION BUTTON
# =====================================================
st.html("<br>")

left, center, right = st.columns([1, 2, 1])

with center:
    predict_button = st.button(
        "✨ Predict Insurance Cost →",
        use_container_width=True
    )

# =====================================================
# DISPLAY PREDICTION
# =====================================================
if predict_button:
    try:
        with st.spinner(
            "🔍 Analyzing your information and calculating the estimate..."
        ):
            prediction = predict(input_dict)

        try:
            amount = float(prediction)

            if amount < 0:
                st.error(
                    "The model returned a negative cost. "
                    "Please check your prediction model."
                )
            else:
                formatted_amount = f"₹{amount:,.2f}"

                st.html(f"""
                <div class="result-card">
                    <div class="result-icon">💰</div>
                    <div class="result-label">
                        Estimated Health Insurance Cost
                    </div>
                    <div class="result-value">{formatted_amount}</div>
                    <div class="result-note">
                        Your estimate is based on the information provided
                        and the trained Machine Learning model.
                    </div>
                </div>
                """)

                st.success(
                    f"Prediction completed successfully for "
                    f"the {insurance_plan} insurance plan!"
                )

        except (ValueError, TypeError):
            st.html(f"""
            <div class="result-card">
                <div class="result-icon">💰</div>
                <div class="result-label">
                    Estimated Health Insurance Cost
                </div>
                <div class="result-value">{prediction}</div>
                <div class="result-note">
                    This estimate was generated by your prediction model.
                </div>
            </div>
            """)

    except Exception as e:
        st.error(f"Unable to calculate the prediction: {e}")
        st.info(
            "Please check prediction_helper.py, your trained model files, "
            "and the input feature names."
        )

# =====================================================
# IMPORTANT INFORMATION
# =====================================================
st.html("""
<div class="info-box">
    <strong>💡 Important Information</strong><br>
    This application provides a Machine Learning-based estimate for
    educational and informational purposes. The result is not an official
    insurance quote and does not guarantee coverage or actual premium costs.
</div>
""")

# =====================================================
# FOOTER
# =====================================================
st.html("""
<div style="text-align:center;">
    <h2>🏥 💙</h2>
    <h3>Health Insurance Cost Predictor</h3>
    <p>Powered by Machine Learning | Designed with Streamlit</p>
    <p style="font-size:12px;">
        Making insurance cost estimation simpler.
    </p>
</div>
""")