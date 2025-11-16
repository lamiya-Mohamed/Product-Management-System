import streamlit as st

st.set_page_config(page_title="Product Management System", layout="wide")

# ---------------------- تخزين البيانات ----------------------
if "users_list" not in st.session_state:
    st.session_state.users_list = []
if "user_needs_list" not in st.session_state:
    st.session_state.user_needs_list = []
if "ideas_list" not in st.session_state:
    st.session_state.ideas_list = []
if "features_list" not in st.session_state:
    st.session_state.features_list = []
if "backlog_list" not in st.session_state:
    st.session_state.backlog_list = []
if "roadmap_list" not in st.session_state:
    st.session_state.roadmap_list = {}
if "kpi_data" not in st.session_state:
    st.session_state.kpi_data = []

st.title("🚀 نظام إدارة المنتج - Product Management System")

tabs = st.tabs([
    "👤 إضافة مستخدم",
    "📌 احتياجات المستخدم",
    "💡 تحويل الاحتياجات إلى أفكار",
    "🧩 إنشاء Features",
    "⭐ ترتيب الأولويات",
    "📋 إنشاء Backlog",
    "🗺️ إنشاء Roadmap",
    "📈 متابعة KPIs",
])

# -------------------------------------------------------------
# 👤 تبويب 1 — إضافة مستخدم
# -------------------------------------------------------------
with tabs[0]:
    st.header("إضافة مستخدم جديد")

    id_user = st.number_input("رقم المستخدم", min_value=1)
    name_user = st.text_input("اسم المستخدم")
    type_user = st.selectbox("نوع المستخدم", ["Buyer", "Seller", "Admin"])
    goal_user = st.text_area("الهدف الأساسي من استخدام المنتج")

    if st.button("إضافة المستخدم"):
        st.session_state.users_list.append({
            "id": id_user,
            "name_user": name_user,
            "type_user": type_user,
            "goal_user": goal_user
        })
        st.success("✔ تم إضافة المستخدم")

    st.subheader("جميع المستخدمين")
    st.write(st.session_state.users_list)

# -------------------------------------------------------------
# 📌 تبويب 2 — احتياجات المستخدم
# -------------------------------------------------------------
with tabs[1]:
    st.header("إضافة احتياج")

    if len(st.session_state.users_list) == 0:
        st.warning("لا يوجد مستخدمون")
    else:
        selected_id = st.selectbox("اختر مستخدم", [u["id"] for u in st.session_state.users_list])
        need_text = st.text_area("وصف الاحتياج")

        if st.button("إضافة الاحتياج"):
            st.session_state.user_needs_list.append({
                "id": selected_id,
                "need_text": need_text
            })
            st.success("✔ تم إضافة الاحتياج")

    st.subheader("جميع الاحتياجات")
    st.write(st.session_state.user_needs_list)

# -------------------------------------------------------------
# 💡 تبويب 3 — تحويل الاحتياجات إلى أفكار
# -------------------------------------------------------------
with tabs[2]:
    st.header("تحويل الاحتياجات إلى أفكار")

    if len(st.session_state.user_needs_list) == 0:
        st.warning("لا توجد احتياجات")
    else:
        for need in st.session_state.user_needs_list:
            st.write("🔸 الاحتياج:", need["need_text"])
            idea = st.text_input(f"فكرة لحل الاحتياج: {need['need_text']}", key=need["need_text"])

            if st.button(f"إضافة فكرة {need['need_text']}"):
                st.session_state.ideas_list.append({
                    "need": need["need_text"],
                    "idea": idea
                })
                st.success("✔ تم إضافة الفكرة")

    st.subheader("كل الأفكار")
    st.write(st.session_state.ideas_list)

# -------------------------------------------------------------
# 🧩 تبويب 4 — تحويل الأفكار إلى Features
# -------------------------------------------------------------
with tabs[3]:
    st.header("إنشاء Features")

    if len(st.session_state.ideas_list) == 0:
        st.warning("لا توجد أفكار")
    else:
        for idea in st.session_state.ideas_list:
            st.write("💡 الفكرة:", idea["idea"])

            feature_name = st.text_input(f"اسم الميزة لفكرة '{idea['idea']}'", key=idea["idea"])
            value = st.slider("Value", 1, 10)
            cost = st.slider("Cost", 1, 10)
            impact = st.slider("Impact", 1, 10)

            if st.button(f"إضافة Feature لفكرة {idea['idea']}"):
                priority = value + impact - cost

                st.session_state.features_list.append({
                    "feature_name": feature_name,
                    "value": value,
                    "cost": cost,
                    "impact": impact,
                    "priority": priority
                })
                st.success("✔ تم إنشاء الميزة")

    st.subheader("جميع الـ Features")
    st.write(st.session_state.features_list)

# -------------------------------------------------------------
# ⭐ تبويب 5 — ترتيب الأولويات
# -------------------------------------------------------------
with tabs[4]:
    st.header("ترتيب الميزات حسب الأولوية")

    if len(st.session_state.features_list) == 0:
        st.warning("لا توجد ميزات")
    else:
        sorted_features = sorted(st.session_state.features_list, key=lambda x: x["priority"], reverse=True)
        st.session_state.features_list = sorted_features

        st.success("✔ تم ترتيب الـ Features")
        st.write(sorted_features)

# -------------------------------------------------------------
# 📋 تبويب 6 — إنشاء Backlog
# -------------------------------------------------------------
with tabs[5]:
    st.header("إنشاء Backlog")

    if len(st.session_state.features_list) == 0:
        st.warning("لا توجد ميزات")
    else:
        نصف = len(st.session_state.features_list) // 2
        st.session_state.backlog_list = st.session_state.features_list[:نصف]

        st.success("✔ تم إنشاء الـ Backlog")
        st.write(st.session_state.backlog_list)

# -------------------------------------------------------------
# 🗺️ تبويب 7 — إنشاء Roadmap
# -------------------------------------------------------------
with tabs[6]:
    st.header("إنشاء Roadmap")

    bl = st.session_state.backlog_list

    if len(bl) == 0:
        st.warning("لا يوجد Backlog")
    else:
        st.session_state.roadmap_list = {
            "Q1": bl[:1],
            "Q2": bl[1:3],
            "Q3": bl[3:5],
            "Q4": bl[5:]
        }

        st.success("✔ تم إنشاء الـ Roadmap")
        st.write(st.session_state.roadmap_list)

# -------------------------------------------------------------
# 📈 تبويب 8 — متابعة KPIs
# -------------------------------------------------------------
with tabs[7]:
    st.header("تحديث الـ KPIs")

    kpi_name = st.text_input("اسم الـ KPI")
    kpi_value = st.text_input("القيمة")

    if st.button("إضافة KPI"):
        st.session_state.kpi_data.append({"kpi": kpi_name, "value": kpi_value})
        st.success("✔ تم إضافة KPI")

    st.subheader("الـ KPIs المسجلة")
    st.write(st.session_state.kpi_data)
