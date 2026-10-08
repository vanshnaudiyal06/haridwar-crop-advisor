import streamlit as st
import pandas as pd
import plotly.express as px
import os

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AI Crop & Rainfall Advisory",
    page_icon="🌾",
    layout="wide"
)

# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

.main-title {
    font-size: 42px;
    font-weight: 800;
    text-align: center;
    color: #16324f;
    margin-top: 10px;
    margin-bottom: 8px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #667085;
    margin-bottom: 25px;
}

.section-title {
    font-size: 26px;
    font-weight: 700;
    color: #16324f;
    margin-top: 25px;
    margin-bottom: 15px;
}

.info-card {
    background-color: white;
    padding: 20px;
    border-radius: 14px;
    border: 1px solid #e1e5ea;
    box-shadow: 0px 3px 12px rgba(0,0,0,0.05);
    margin-bottom: 15px;
}

.card-title {
    font-size: 20px;
    font-weight: 700;
    color: #16324f;
    margin-bottom: 8px;
}

.card-text {
    font-size: 16px;
    color: #555555;
    line-height: 1.6;
}

.badge {
    display: inline-block;
    padding: 7px 14px;
    border-radius: 20px;
    background-color: #e8f5e9;
    color: #2e7d32;
    font-size: 14px;
    font-weight: 600;
}

.footer {
    text-align: center;
    color: #777777;
    margin-top: 45px;
    padding: 20px;
    line-height: 1.7;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# LANGUAGE
# =========================================================

st.sidebar.title("🌐 Language / भाषा")

language = st.sidebar.selectbox(
    "Select Language / भाषा चुनें",
    ["English", "हिन्दी"]
)


# =========================================================
# TRANSLATIONS
# =========================================================

if language == "English":

    title = "🌾 AI-Assisted Crop & Rainfall Advisory"

    subtitle = (
        "Data-driven rainfall insights and crop guidance "
        "for farmers near Haridwar"
    )

    location_badge = "Haridwar • Uttarakhand"

    dashboard = "Dashboard"
    select_year = "Select Year"
    rainfall_pattern = "Rainfall Pattern"
    rainfall_summary = "Rainfall Summary"
    crop_advisory = "Crop Advisory"
    rainfall_information = "Rainfall Information"
    view_data = "View Rainfall Data"

    average = "Average Rainfall"
    highest = "Highest Rainfall"
    lowest = "Lowest Rainfall"

    show_data = "Show complete rainfall dataset"

    wheat = "Wheat"
    rice = "Rice"
    sugarcane = "Sugarcane"

    wheat_text = (
        "Wheat is generally cultivated during the cooler season. "
        "Farmers should consider soil moisture, rainfall and local "
        "weather conditions before sowing."
    )

    rice_text = (
        "Rice requires substantial water availability. Monsoon "
        "rainfall patterns can help in planning cultivation and "
        "irrigation requirements."
    )

    sugarcane_text = (
        "Sugarcane has a long growing period and requires consistent "
        "moisture. Rainfall information can support irrigation planning."
    )

    rainfall_info_title = "About the Rainfall Data"

    rainfall_info_text = (
        "This dashboard uses historical rainfall observations to "
        "identify rainfall patterns across different months. "
        "The information can support agricultural planning by helping "
        "users understand periods of relatively higher and lower rainfall."
    )

    note = (
        "Note: This tool is intended as decision-support information. "
        "Farmers should also consider local weather forecasts, soil "
        "conditions and agricultural guidance."
    )

    location = "📍 Location: Haridwar, Uttarakhand"
    historical = "🌧️ Historical Rainfall Analysis"

    chart_title = "Monthly Rainfall Pattern"

    month_label = "Month"
    rainfall_label = "Rainfall (mm)"

    success_text = "Rainfall information for"

    footer = (
        "AI-Assisted Crop & Rainfall Advisory Tool<br>"
        "Haridwar, Uttarakhand<br>"
        "Data-driven agricultural decision support"
    )

else:

    title = "🌾 AI-सहायित फसल एवं वर्षा सलाह"

    subtitle = (
        "हरिद्वार के आसपास के किसानों के लिए वर्षा संबंधी "
        "जानकारी और फसल मार्गदर्शन"
    )

    location_badge = "हरिद्वार • उत्तराखंड"

    dashboard = "डैशबोर्ड"
    select_year = "वर्ष चुनें"
    rainfall_pattern = "वर्षा का पैटर्न"
    rainfall_summary = "वर्षा का सारांश"
    crop_advisory = "फसल सलाह"
    rainfall_information = "वर्षा की जानकारी"
    view_data = "वर्षा का डेटा देखें"

    average = "औसत वर्षा"
    highest = "सबसे अधिक वर्षा"
    lowest = "सबसे कम वर्षा"

    show_data = "पूरा वर्षा डेटा दिखाएँ"

    wheat = "🌾 गेहूँ"
    rice = "🌾 धान"
    sugarcane = "🎋 गन्ना"

    wheat_text = (
        "गेहूँ सामान्यतः ठंडे मौसम में उगाया जाता है। "
        "बुवाई से पहले किसानों को मिट्टी की नमी, वर्षा और "
        "स्थानीय मौसम की स्थिति को ध्यान में रखना चाहिए।"
    )

    rice_text = (
        "धान के लिए पर्याप्त पानी की आवश्यकता होती है। "
        "मानसून के दौरान वर्षा का पैटर्न खेती और सिंचाई "
        "की योजना बनाने में सहायक हो सकता है।"
    )

    sugarcane_text = (
        "गन्ने की फसल की अवधि लंबी होती है और इसे लगातार "
        "नमी की आवश्यकता होती है। वर्षा की जानकारी सिंचाई "
        "की योजना बनाने में सहायता कर सकती है।"
    )

    rainfall_info_title = "वर्षा डेटा के बारे में"

    rainfall_info_text = (
        "यह डैशबोर्ड अलग-अलग महीनों में वर्षा के पैटर्न को "
        "समझने के लिए ऐतिहासिक वर्षा डेटा का उपयोग करता है। "
        "यह जानकारी अधिक और कम वर्षा वाले समय को समझने तथा "
        "कृषि योजना बनाने में सहायता कर सकती है।"
    )

    note = (
        "महत्वपूर्ण सूचना: यह टूल केवल निर्णय लेने में सहायता "
        "के लिए है। किसानों को स्थानीय मौसम पूर्वानुमान, मिट्टी "
        "की स्थिति और कृषि विशेषज्ञों की सलाह को भी ध्यान में रखना चाहिए।"
    )

    location = "📍 स्थान: हरिद्वार, उत्तराखंड"
    historical = "🌧️ ऐतिहासिक वर्षा विश्लेषण"

    chart_title = "मासिक वर्षा का पैटर्न"

    month_label = "महीना"
    rainfall_label = "वर्षा (mm)"

    success_text = "वर्ष के लिए वर्षा की जानकारी"

    footer = (
        "AI-सहायित फसल एवं वर्षा सलाह टूल<br>"
        "हरिद्वार, उत्तराखंड<br>"
        "डेटा-आधारित कृषि निर्णय सहायता"
    )


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.markdown("---")

st.sidebar.subheader(dashboard)

st.sidebar.write(location)

st.sidebar.write(historical)


# =========================================================
# TITLE
# =========================================================

st.markdown(
    f'<div class="main-title">{title}</div>',
    unsafe_allow_html=True
)

st.markdown(
    f'<div class="subtitle">{subtitle}</div>',
    unsafe_allow_html=True
)

st.markdown(
    f'<div style="text-align:center;">'
    f'<span class="badge">{location_badge}</span>'
    f'</div>',
    unsafe_allow_html=True
)

st.divider()


# =========================================================
# FIND RAINFALL CSV
# =========================================================

app_folder = os.path.dirname(
    os.path.abspath(__file__)
)

csv_file = None

for filename in os.listdir(app_folder):

    if filename.lower().endswith(".csv"):

        if "rainfall" in filename.lower():

            csv_file = os.path.join(
                app_folder,
                filename
            )

            break


# If rainfall CSV isn't specifically found,
# use the first CSV available.

if csv_file is None:

    for filename in os.listdir(app_folder):

        if filename.lower().endswith(".csv"):

            csv_file = os.path.join(
                app_folder,
                filename
            )

            break


# =========================================================
# CSV ERROR
# =========================================================

if csv_file is None:

    if language == "English":

        st.error("❌ Rainfall CSV file was not found.")

        st.write(
            "Make sure rainfall.csv is inside the same "
            "folder as app.py."
        )

    else:

        st.error("❌ वर्षा की CSV फ़ाइल नहीं मिली।")

        st.write(
            "सुनिश्चित करें कि rainfall.csv, app.py के "
            "साथ उसी फ़ोल्डर में है।"
        )

    st.write("Files found:")

    st.code(
        "\n".join(os.listdir(app_folder))
    )

    st.stop()


# =========================================================
# READ CSV
# =========================================================

try:

    df = pd.read_csv(csv_file)

except Exception as e:

    if language == "English":

        st.error("❌ Could not read the CSV file.")

    else:

        st.error("❌ CSV फ़ाइल को पढ़ा नहीं जा सका।")

    st.code(str(e))

    st.stop()


# =========================================================
# CLEAN COLUMN NAMES
# =========================================================

df.columns = (
    df.columns
    .astype(str)
    .str.strip()
    .str.replace(" ", "_")
    .str.replace("-", "_")
)


# =========================================================
# IDENTIFY COLUMNS
# =========================================================

year_col = None
month_col = None
rainfall_col = None

for column in df.columns:

    name = column.lower()

    if "year" in name:

        year_col = column

    if "month" in name:

        month_col = column

    if "rainfall" in name:

        rainfall_col = column


# =========================================================
# COLUMN ERROR
# =========================================================

if (
    year_col is None
    or month_col is None
    or rainfall_col is None
):

    if language == "English":

        st.error(
            "❌ Required columns could not be identified."
        )

        st.write(
            "Columns found in your CSV:"
        )

    else:

        st.error(
            "❌ आवश्यक कॉलम नहीं मिले।"
        )

        st.write(
            "आपकी CSV में मिले कॉलम:"
        )

    st.write(list(df.columns))

    st.info(
        "Required columns: Year, Month, Rainfall"
    )

    st.stop()


# =========================================================
# CONVERT DATA
# =========================================================

df[year_col] = pd.to_numeric(
    df[year_col],
    errors="coerce"
)

df[rainfall_col] = pd.to_numeric(
    df[rainfall_col],
    errors="coerce"
)

df = df.dropna(
    subset=[
        year_col,
        month_col,
        rainfall_col
    ]
)

df[year_col] = df[year_col].astype(int)


# =========================================================
# YEAR SELECTION
# =========================================================

years = sorted(
    df[year_col].unique()
)

selected_year = st.sidebar.selectbox(
    select_year,
    years
)


# =========================================================
# SELECTED YEAR DATA
# =========================================================

year_data = df[
    df[year_col] == selected_year
].copy()


# =========================================================
# SELECT YEAR SECTION
# =========================================================

st.markdown(
    f'<div class="section-title">📅 {select_year}</div>',
    unsafe_allow_html=True
)

st.success(
    f"{success_text} {selected_year}"
)


# =========================================================
# PROFESSIONAL RAINFALL PATTERN
# =========================================================

st.markdown(
    f'<div class="section-title">🌧️ {rainfall_pattern}</div>',
    unsafe_allow_html=True
)

# Month order
month_order = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# Make a copy for chart
chart_data = year_data.copy()

# Convert month to text
chart_data[month_col] = chart_data[month_col].astype(str).str.strip()

# Check whether months are standard names
if chart_data[month_col].isin(month_order).any():

    chart_data[month_col] = pd.Categorical(
        chart_data[month_col],
        categories=month_order,
        ordered=True
    )

    chart_data = chart_data.sort_values(month_col)


# Calculate monthly rainfall
monthly_data = (
    chart_data
    .groupby(
        month_col,
        observed=False
    )[rainfall_col]
    .mean()
    .reset_index()
)


# Create chart
fig = px.bar(
    monthly_data,
    x=month_col,
    y=rainfall_col,
    text=rainfall_col,
    title=f"{chart_title} — {selected_year}",
    labels={
        month_col: month_label,
        rainfall_col: rainfall_label
    }
)


# Show rainfall values on bars
fig.update_traces(
    texttemplate="%{text:.1f} mm",
    textposition="outside"
)


# Professional chart layout
fig.update_layout(
    title={
        "text": f"{chart_title} — {selected_year}",
        "x": 0.5,
        "xanchor": "center"
    },

    height=500,

    template="plotly_white",

    margin=dict(
        l=40,
        r=40,
        t=80,
        b=80
    ),

    xaxis=dict(
        title=month_label,
        tickangle=-45
    ),

    yaxis=dict(
        title=rainfall_label,
        rangemode="tozero"
    ),

    hovermode="x unified"
)


# Display chart
st.plotly_chart(
    fig,
    use_container_width=True
)

# =========================================================
# RAINFALL SUMMARY
# =========================================================

st.markdown(
    f'<div class="section-title">📊 {rainfall_summary}</div>',
    unsafe_allow_html=True
)


col1, col2, col3 = st.columns(3)

average_value = year_data[rainfall_col].mean()

highest_value = year_data[rainfall_col].max()

lowest_value = year_data[rainfall_col].min()


with col1:

    st.metric(
        average,
        f"{average_value:.1f} mm"
    )


with col2:

    st.metric(
        highest,
        f"{highest_value:.1f} mm"
    )


with col3:

    st.metric(
        lowest,
        f"{lowest_value:.1f} mm"
    )
# =========================================================
# DATA-DRIVEN CROP ADVISORY
# =========================================================

st.markdown(
    f'<div class="section-title">🌱 '
    f'{"Crop Advisory" if language == "English" else "फसल सलाह"}'
    f'</div>',
    unsafe_allow_html=True
)

# Calculate rainfall thresholds
rainfall_values = year_data[rainfall_col]

high_threshold = rainfall_values.quantile(0.75)
low_threshold = rainfall_values.quantile(0.25)

high_months = year_data[
    year_data[rainfall_col] >= high_threshold
]

low_months = year_data[
    year_data[rainfall_col] <= low_threshold
]

moderate_months = year_data[
    (year_data[rainfall_col] > low_threshold) &
    (year_data[rainfall_col] < high_threshold)
]

high_month_names = ", ".join(
    high_months[month_col].astype(str).tolist()
)

moderate_month_names = ", ".join(
    moderate_months[month_col].astype(str).tolist()
)

low_month_names = ", ".join(
    low_months[month_col].astype(str).tolist()
)

# ---------------------------------------------------------
# Rainfall-based overview
# ---------------------------------------------------------

if language == "English":

    st.markdown(
        f"""
        <div class="info-card">

        <div class="card-title">
        🌧️ Rainfall-based Advisory — {selected_year}
        </div>

        <div class="card-text">

        <b>Higher rainfall months:</b>
        {high_month_names}

        <br><br>

        <b>Moderate rainfall months:</b>
        {moderate_month_names}

        <br><br>

        <b>Lower rainfall months:</b>
        {low_month_names}

        <br><br>

        This rainfall pattern can support crop planning,
        irrigation scheduling and monitoring of wetter periods.

        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

else:

    st.markdown(
        f"""
        <div class="info-card">

        <div class="card-title">
        🌧️ वर्षा आधारित सलाह — {selected_year}
        </div>

        <div class="card-text">

        <b>अधिक वर्षा वाले महीने:</b>
        {high_month_names}

        <br><br>

        <b>मध्यम वर्षा वाले महीने:</b>
        {moderate_month_names}

        <br><br>

        <b>कम वर्षा वाले महीने:</b>
        {low_month_names}

        <br><br>

        यह वर्षा पैटर्न फसल योजना, सिंचाई की योजना
        और अधिक वर्षा वाले समय की निगरानी में सहायता कर सकता है।

        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ---------------------------------------------------------
# Crop cards
# ---------------------------------------------------------

crop1, crop2, crop3 = st.columns(3)


# WHEAT
with crop1:

    if language == "English":

        crop_title = "🌾 Wheat"

        crop_text = """
        Generally suited to the cooler growing season.

        Monitor soil moisture and avoid excessive water
        around the crop, particularly during wetter periods.
        """

    else:

        crop_title = "🌾 गेहूँ"

        crop_text = """
        गेहूँ सामान्यतः ठंडे मौसम में उगाया जाता है।

        मिट्टी की नमी पर ध्यान दें और अधिक वर्षा वाले
        समय में खेत में अत्यधिक पानी जमा होने से बचाएं।
        """

    st.markdown(
        f"""
        <div class="info-card">

        <div class="card-title">
        {crop_title}
        </div>

        <div class="card-text">
        {crop_text}
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# RICE
with crop2:

    if language == "English":

        crop_title = "🍚 Rice"

        crop_text = """
        Rice generally requires greater water availability.

        Higher rainfall periods may support natural water
        availability, while excessive rainfall should be monitored.
        """

    else:

        crop_title = "🍚 धान"

        crop_text = """
        धान के लिए सामान्यतः अधिक पानी की आवश्यकता होती है।

        अधिक वर्षा वाले समय में प्राकृतिक जल उपलब्धता
        बेहतर हो सकती है, लेकिन अत्यधिक वर्षा पर निगरानी रखें।
        """

    st.markdown(
        f"""
        <div class="info-card">

        <div class="card-title">
        {crop_title}
        </div>

        <div class="card-text">
        {crop_text}
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# SUGARCANE
with crop3:

    if language == "English":

        crop_title = "🎋 Sugarcane"

        crop_text = """
        Sugarcane has a longer growing period and needs
        consistent moisture.

        Rainfall information can support irrigation planning
        and monitoring of excessive rainfall.
        """

    else:

        crop_title = "🎋 गन्ना"

        crop_text = """
        गन्ने की फसल की अवधि लंबी होती है और इसे
        लगातार नमी की आवश्यकता होती है।

        वर्षा की जानकारी सिंचाई की योजना बनाने और
        अत्यधिक वर्षा की निगरानी में सहायता कर सकती है।
        """

    st.markdown(
        f"""
        <div class="info-card">

        <div class="card-title">
        {crop_title}
        </div>

        <div class="card-text">
        {crop_text}
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ---------------------------------------------------------
# Important advisory note
# ---------------------------------------------------------

if language == "English":

    st.caption(
        "Note: This advisory uses historical rainfall patterns "
        "for educational and planning purposes. Actual crop "
        "decisions should also consider soil conditions, crop "
        "variety, current weather forecasts, irrigation availability "
        "and local agricultural guidance."
    )

else:

    st.caption(
        "नोट: यह सलाह ऐतिहासिक वर्षा पैटर्न का उपयोग "
        "शैक्षिक और योजना बनाने के उद्देश्य से करती है। "
        "वास्तविक फसल निर्णय लेते समय मिट्टी की स्थिति, "
        "फसल की किस्म, वर्तमान मौसम पूर्वानुमान, सिंचाई "
        "की उपलब्धता और स्थानीय कृषि सलाह को भी ध्यान में रखें।"
    )
# =========================================================
# YEAR-TO-YEAR RAINFALL COMPARISON
# =========================================================

st.markdown(
    f'<div class="section-title">📊 '
    f'{"Year-to-Year Rainfall Comparison" if language == "English" else "वर्ष-दर-वर्ष वर्षा तुलना"}'
    f'</div>',
    unsafe_allow_html=True
)

year_comparison = (
    df.groupby(year_col)[rainfall_col]
    .sum()
    .reset_index()
)

year_comparison.columns = ["Year", "Total_Rainfall"]

# ---------------------------------------------------------
# If only one year is available
# ---------------------------------------------------------

if len(year_comparison) < 2:

    if language == "English":

        st.info(
            "📌 Year-to-year comparison will become available "
            "when rainfall data for two or more years is added."
        )

        st.markdown(
            f"""
            <div class="info-card">

            <div class="card-title">
            📅 Data currently available
            </div>

            <div class="card-text">

            The dashboard currently contains rainfall data for
            <b>{selected_year}</b> only.

            <br><br>

            Add rainfall data for additional years to compare
            annual rainfall patterns and identify changes
            between years.

            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.info(
            "📌 दो या अधिक वर्षों का वर्षा डेटा जोड़ने पर "
            "वर्ष-दर-वर्ष तुलना उपलब्ध होगी।"
        )

        st.markdown(
            f"""
            <div class="info-card">

            <div class="card-title">
            📅 वर्तमान में उपलब्ध डेटा
            </div>

            <div class="card-text">

            डैशबोर्ड में वर्तमान में केवल
            <b>{selected_year}</b> का वर्षा डेटा उपलब्ध है।

            <br><br>

            अतिरिक्त वर्षों का वर्षा डेटा जोड़ने पर
            वार्षिक वर्षा पैटर्न की तुलना की जा सकेगी
            और वर्षों के बीच बदलावों को समझने में सहायता मिलेगी।

            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

else:

    selected_year_total = year_comparison[
        year_comparison["Year"] == selected_year
    ]["Total_Rainfall"].iloc[0]

    overall_average = year_comparison["Total_Rainfall"].mean()

    difference = selected_year_total - overall_average

    percentage_difference = (
        (difference / overall_average) * 100
        if overall_average != 0
        else 0
    )

    metric1, metric2, metric3 = st.columns(3)

    with metric1:
        st.metric(
            "Selected Year" if language == "English"
            else "चयनित वर्ष",
            f"{selected_year_total:.1f} mm"
        )

    with metric2:
        st.metric(
            "All-Year Average" if language == "English"
            else "सभी वर्षों का औसत",
            f"{overall_average:.1f} mm"
        )

    with metric3:
        st.metric(
            "Difference" if language == "English"
            else "अंतर",
            f"{percentage_difference:+.1f}%"
        )

    comparison_fig = px.bar(
        year_comparison,
        x="Year",
        y="Total_Rainfall",
        text="Total_Rainfall",
        title=(
            "Total Rainfall by Year"
            if language == "English"
            else "वर्ष के अनुसार कुल वर्षा"
        ),
        labels={
            "Year": "Year" if language == "English" else "वर्ष",
            "Total_Rainfall": (
                "Total Rainfall (mm)"
                if language == "English"
                else "कुल वर्षा (मिमी)"
            )
        }
    )

    comparison_fig.update_traces(
        texttemplate="%{text:.1f} mm",
        textposition="outside"
    )

    comparison_fig.update_layout(
        height=500,
        template="plotly_white",
        margin=dict(l=40, r=40, t=80, b=80),
        xaxis=dict(
            title="Year" if language == "English" else "वर्ष"
        ),
        yaxis=dict(
            title=(
                "Total Rainfall (mm)"
                if language == "English"
                else "कुल वर्षा (मिमी)"
            ),
            rangemode="tozero"
        )
    )

    st.plotly_chart(
        comparison_fig,
        use_container_width=True
    )
# =========================================================
# MONTHLY RAINFALL ANALYSIS
# =========================================================
annual_rainfall=year_data[rainfall_col].mean()
st.markdown(
    f'<div class="section-title">📅 '
    f'{"Monthly Rainfall Analysis" if language == "English" else "मासिक वर्षा विश्लेषण"}'
    f'</div>',
    unsafe_allow_html=True
)

# Find highest and lowest rainfall months
highest_month_row = year_data.loc[
    year_data[rainfall_col].idxmax()
]

lowest_month_row = year_data.loc[
    year_data[rainfall_col].idxmin()
]

highest_month = str(highest_month_row[month_col])
highest_value = float(highest_month_row[rainfall_col])

lowest_month = str(lowest_month_row[month_col])
lowest_value = float(lowest_month_row[rainfall_col])


# ---------------------------------------------------------
# Three analysis cards
# ---------------------------------------------------------

analysis1, analysis2, analysis3 = st.columns(3)

with analysis1:

    st.metric(
        "Wettest Month" if language == "English"
        else "सबसे अधिक वर्षा वाला महीना",
        highest_month,
        f"{highest_value:.1f} mm"
    )

with analysis2:

    st.metric(
        "Driest Month" if language == "English"
        else "सबसे कम वर्षा वाला महीना",
        lowest_month,
        f"{lowest_value:.1f} mm"
    )

with analysis3:

    st.metric(
        "Monthly Average" if language == "English"
        else "मासिक औसत",
        f"{annual_rainfall:.1f} mm"
    )


# ---------------------------------------------------------
# Automatic interpretation
# ---------------------------------------------------------

if language == "English":

    st.markdown(
        f"""
        <div class="info-card">

        <div class="card-title">
        🔎 What the data shows
        </div>

        <div class="card-text">

        In <b>{selected_year}</b>, the highest recorded
        rainfall was in <b>{highest_month}</b>
        ({highest_value:.1f} mm).

        <br><br>

        The lowest recorded rainfall was in
        <b>{lowest_month}</b>
        ({lowest_value:.1f} mm).

        <br><br>

        This monthly pattern can help with crop planning,
        irrigation scheduling and monitoring periods of
        higher rainfall.

        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

else:

    st.markdown(
        f"""
        <div class="info-card">

        <div class="card-title">
        🔎 डेटा क्या बताता है
        </div>

        <div class="card-text">

        <b>{selected_year}</b> में सबसे अधिक वर्षा
        <b>{highest_month}</b> में दर्ज की गई
        ({highest_value:.1f} मिमी)।

        <br><br>

        सबसे कम वर्षा <b>{lowest_month}</b> में दर्ज की गई
        ({lowest_value:.1f} मिमी)।

        <br><br>

        यह मासिक पैटर्न फसल योजना, सिंचाई की योजना
        और अधिक वर्षा वाले समय की निगरानी में सहायता
        कर सकता है।

        </div>

        </div>
        """,
        unsafe_allow_html=True
    )
# =========================================================
# RAINFALL INFORMATION
# =========================================================

st.markdown(
    f'<div class="section-title">💧 {rainfall_information}</div>',
    unsafe_allow_html=True
)


st.markdown(
    f"""
    <div class="info-card">

    <div class="card-title">
    {rainfall_info_title}
    </div>

    <div class="card-text">

    {rainfall_info_text}

    <br><br>

    <b>{note}</b>

    </div>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# VIEW DATA
# =========================================================

st.markdown(
    f'<div class="section-title">📋 {view_data}</div>',
    unsafe_allow_html=True
)


with st.expander(show_data):

    st.dataframe(
        df,
        use_container_width=True
    )
# =========================================================
# ABOUT & METHODOLOGY
# =========================================================

st.markdown(
    f'<div class="section-title">ℹ️ '
    f'{"About & Methodology" if language == "English" else "परिचय और कार्यप्रणाली"}'
    f'</div>',
    unsafe_allow_html=True
)

if language == "English":

    st.markdown(
        """
        <div class="info-card">

        <div class="card-title">
        📍 About the Project
        </div>

        <div class="card-text">

        The <b>AI-Assisted Crop & Rainfall Advisory Tool</b>
        is designed to help users understand historical rainfall
        patterns and explore how rainfall information can support
        agricultural planning near Haridwar.

        <br><br>

        The dashboard presents rainfall information in a simple,
        visual format so that patterns across months and years
        can be easier to understand.

        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="info-card">

        <div class="card-title">
        🧮 How the Dashboard Works
        </div>

        <div class="card-text">

        <b>1. Rainfall Data</b><br>
        The dashboard reads rainfall observations from the
        project's CSV dataset.

        <br><br>

        <b>2. Monthly Analysis</b><br>
        Rainfall values are grouped by month to identify
        higher, moderate and lower rainfall periods.

        <br><br>

        <b>3. Rainfall Summary</b><br>
        The dashboard calculates average, highest and lowest
        rainfall values for the selected year.

        <br><br>

        <b>4. Crop Advisory</b><br>
        The advisory uses rainfall patterns to provide simple
        planning-oriented information for wheat, rice and
        sugarcane.

        <br><br>

        <b>5. Year Comparison</b><br>
        When multiple years of data are available, the dashboard
        can compare total annual rainfall between years.

        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="info-card">

        <div class="card-title">
        ⚠️ Important Limitation
        </div>

        <div class="card-text">

        This tool is intended for <b>educational and planning
        purposes</b>. Rainfall information alone cannot determine
        the best agricultural decision.

        Soil conditions, crop variety, irrigation availability,
        current weather forecasts, pests, temperature and local
        agricultural guidance should also be considered.

        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

else:

    st.markdown(
        """
        <div class="info-card">

        <div class="card-title">
        📍 परियोजना के बारे में
        </div>

        <div class="card-text">

        <b>AI-Assisted Crop & Rainfall Advisory Tool</b>
        का उद्देश्य ऐतिहासिक वर्षा पैटर्न को समझने और
        हरिद्वार के आसपास कृषि योजना में वर्षा की जानकारी
        के संभावित उपयोग को समझने में सहायता करना है।

        <br><br>

        डैशबोर्ड वर्षा की जानकारी को सरल और दृश्य रूप में
        प्रस्तुत करता है ताकि महीनों और वर्षों के बीच
        वर्षा के पैटर्न को आसानी से समझा जा सके।

        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="info-card">

        <div class="card-title">
        🧮 डैशबोर्ड कैसे काम करता है
        </div>

        <div class="card-text">

        <b>1. वर्षा डेटा</b><br>
        डैशबोर्ड प्रोजेक्ट की CSV डेटा फाइल से
        वर्षा संबंधी आंकड़े पढ़ता है।

        <br><br>

        <b>2. मासिक विश्लेषण</b><br>
        वर्षा के आंकड़ों को महीनों के अनुसार समूहित करके
        अधिक, मध्यम और कम वर्षा वाले समय की पहचान की जाती है।

        <br><br>

        <b>3. वर्षा सारांश</b><br>
        चयनित वर्ष के लिए औसत, अधिकतम और न्यूनतम
        वर्षा की गणना की जाती है।

        <br><br>

        <b>4. फसल सलाह</b><br>
        वर्षा के पैटर्न के आधार पर गेहूँ, धान और
        गन्ने के लिए सरल योजना-आधारित जानकारी दी जाती है।

        <br><br>

        <b>5. वर्ष तुलना</b><br>
        जब कई वर्षों का डेटा उपलब्ध होगा, तब डैशबोर्ड
        अलग-अलग वर्षों की कुल वर्षा की तुलना कर सकेगा।

        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="info-card">

        <div class="card-title">
        ⚠️ महत्वपूर्ण सीमा
        </div>

        <div class="card-text">

        यह टूल <b>शैक्षिक और योजना बनाने के उद्देश्य</b>
        से बनाया गया है। केवल वर्षा की जानकारी के आधार पर
        कृषि संबंधी अंतिम निर्णय नहीं लिया जाना चाहिए।

        मिट्टी की स्थिति, फसल की किस्म, सिंचाई की उपलब्धता,
        वर्तमान मौसम पूर्वानुमान, कीट, तापमान और स्थानीय
        कृषि विशेषज्ञों की सलाह को भी ध्यान में रखना चाहिए।

        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    f"""
    <div class="footer">
    {footer}
    </div>
    """,
    unsafe_allow_html=True
)