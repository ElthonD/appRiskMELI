from streamlit_calendar import calendar
import streamlit as st

st.set_page_config(page_title="Demo for streamlit-calendar", page_icon="📆")

st.markdown(
    "## Demo for [streamlit-calendar](https://github.com/im-perativa/streamlit-calendar) 📆"
)

mode = st.selectbox(
    "Calendar Mode:",
    (
        "daygrid",
        "timegrid",
        "timeline",
        "resource-daygrid",
        "resource-timegrid",
        "resource-timeline",
        "list",
        "multimonth",
    ),
)

#FF4B4B Rojo
#3DD56D Verde

events = [
    {
        "title": "Recuperado",
        "color": "#3DD56D", 
        "start": "2024-07-27",
        "end": "2024-07-27",
        "resourceId": "573100743",
    },
    {
        "title": "Recuperado",
        "color": "#3DD56D",
        "start": "2023-09-02",
        "end": "2023-09-02",
        "resourceId": "593191683",
    },
    {
        "title": "Recuperado",
        "color": "#3DD56D",
        "start": "2024-09-17",
        "end": "2024-09-17",
        "resourceId": "593224848",
    },
    {
        "title": "Recuperado",
        "color": "#3DD56D",
        "start": "2024-10-22",
        "end": "2024-10-22",
        "resourceId": "5A3313002",
    },
    {
        "title": "Recuperado",
        "color": "#3DD56D",
        "start": "2024-11-17",
        "end": "2024-11-17",
        "resourceId": "5B3377212",
    },
    {
        "title": "Recuperado",
        "color": "#3DD56D",
        "start": "2024-12-22",
        "end": "2024-12-22",
        "resourceId": "5C3476857",
    },
    {
        "title": "Recuperado",
        "color": "#3DD56D",
        "start": "2024-12-29",
        "end": "2024-12-29",
        "resourceId": "5C3490555",
    },
    {
        "title": "Recuperado",
        "color": "#3DD56D",
        "start": "2024-02-24",
        "end": "2024-02-24",
        "resourceId": "623632894",
    },
    {
        "title": "Consumado",
        "color": "#FF4B4B",
        "start": "2024-04-29",
        "end": "2024-04-29",
        "resourceId": "643807414",
    },
    {
        "title": "Recuperado",
        "color": "#3DD56D",
        "start": "2024-06-17",
        "end": "2024-06-17",
        "resourceId": "663942204",
    },
    {
        "title": "Recuperado",
        "color": "#3DD56D",
        "start": "2024-07-17",
        "end": "2024-07-17",
        "resourceId": "674023687",
    },
    {
        "title": "Consumado",
        "color": "#FF4B4B",
        "start": "2024-07-23",
        "end": "2024-07-23",
        "resourceId": "674040100",
    },
    {
        "title": "Recuperado",
        "color": "#3DD56D",
        "start": "2024-09-23",
        "end": "2024-09-23",
        "resourceId": "694194103",
    },
    {
        "title": "Recuperado",
        "color": "#3DD56D",
        "start": "2024-09-26",
        "end": "2024-09-26",
        "resourceId": "694201020",
    },
    {
        "title": "Recuperado",
        "color": "#3DD56D",
        "start": "2023-10-20",
        "end": "2023-10-20",
        "resourceId": "6A4263104",
    },
    {
        "title": "Recuperado",
        "color": "#3DD56D",
        "start": "2024-11-01",
        "end": "2024-11-01",
        "resourceId": "6B4291744",
    },
    {
        "title": "Recuperado",
        "color": "#3DD56D",
        "start": "2024-11-13",
        "end": "2024-11-13",
        "resourceId": "6B4320698",
    },
    {
        "title": "Recuperado",
        "color": "#3DD56D",
        "start": "2024-11-22",
        "end": "2024-11-22",
        "resourceId": "6B4346404",
    },
    {
        "title": "Recuperado",
        "color": "#3DD56D",
        "start": "2024-12-30",
        "end": "2024-12-30",
        "resourceId": "6C4443693",
    },
    {
        "title": "Recuperado",
        "color": "#3DD56D",
        "start": "2024-12-24",
        "end": "2024-12-24",
        "resourceId": "6C4432388",
    },
    {
        "title": "Recuperado",
        "color": "#3DD56D",
        "start": "2024-12-02",
        "end": "2024-12-02",
        "resourceId": "6C4373527",
    },
    {
        "title": "Recuperado",
        "color": "#3DD56D",
        "start": "2024-01-05",
        "end": "2024-01-05",
        "resourceId": "714454863",
    },
    {
        "title": "Consumado",
        "color": "#FF4B4B",
        "start": "2024-02-19",
        "end": "2024-02-19",
        "resourceId": "724574182",
    },
    {
        "title": "Recuperado",
        "color": "#3DD56D",
        "start": "2024-02-27",
        "end": "2024-02-27",
        "resourceId": "724595488",
    },
    {
        "title": "Recuperado",
        "color": "#3DD56D",
        "start": "2024-03-09",
        "end": "2024-03-09",
        "resourceId": "734622055",
    },
    {
        "title": "Consumado",
        "color": "#FF4B4B",
        "start": "2024-04-27",
        "end": "2024-04-27",
        "resourceId": "744747255",
    },
    {
        "title": "Consumado",
        "color": "#FF4B4B",
        "start": "2024-05-03",
        "end": "2024-05-03",
        "resourceId": "754761468",
    },
    {
        "title": "Recuperado",
        "color": "#3DD56D",
        "start": "2024-06-07",
        "end": "2024-06-07",
        "resourceId": "764857315",
    },
    {
        "title": "Recuperado",
        "color": "#3DD56D",
        "start": "2024-06-13",
        "end": "2024-06-13",
        "resourceId": "764876984",
    },
    {
        "title": "Consumado",
        "color": "#FF4B4B",
        "start": "2024-06-15",
        "end": "2024-06-15",
        "resourceId": "764881211",
    },
    {
        "title": "Recuperado",
        "color": "#3DD56D",
        "start": "2024-06-27",
        "end": "2024-06-27",
        "resourceId": "764914584",
    },
    {
        "title": "Recuperado",
        "color": "#3DD56D",
        "start": "2024-07-01",
        "end": "2024-07-01",
        "resourceId": "774925043",
    },
    {
        "title": "Recuperado",
        "color": "#3DD56D",
        "start": "2024-08-10",
        "end": "2024-08-10",
        "resourceId": "785029284",
    },
    {
        "title": "Recuperado",
        "color": "#3DD56D",
        "start": "2024-08-04",
        "end": "2024-08-04",
        "resourceId": "785015581",
    },
    {
        "title": "Recuperado",
        "color": "#3DD56D",
        "start": "2024-09-12",
        "end": "2024-09-12",
        "resourceId": "795119424",
    },
    {
        "title": "Recuperado",
        "color": "#3DD56D",
        "start": "2024-09-19",
        "end": "2024-09-19",
        "resourceId": "795138262",
    },
    {
        "title": "Recuperado",
        "color": "#3DD56D",
        "start": "2024-09-21",
        "end": "2024-09-21",
        "resourceId": "795141649",
    },
    {
        "title": "Recuperado",
        "color": "#3DD56D",
        "start": "2024-09-28",
        "end": "2024-09-28",
        "resourceId": "795164396",
    },
    {
        "title": "Recuperado",
        "color": "#3DD56D",
        "start": "2024-09-18",
        "end": "2024-09-18",
        "resourceId": "795135543",
    },
    {
        "title": "Recuperado",
        "color": "#3DD56D",
        "start": "2024-09-18",
        "end": "2024-09-18",
        "resourceId": "795134072",
    },
    {
        "title": "Recuperado",
        "color": "#3DD56D",
        "start": "2024-09-21",
        "end": "2024-09-21",
        "resourceId": "795141834",
    },
    {
        "title": "Recuperado",
        "color": "#3DD56D",
        "start": "2024-10-04",
        "end": "2024-10-04",
        "resourceId": "7A5178364",
    },
    {
        "title": "Consumado",
        "color": "#FF4B4B",
        "start": "2024-10-05",
        "end": "2024-10-05",
        "resourceId": "7A5181694",
    },
    {
        "title": "Recuperado",
        "color": "#3DD56D",
        "start": "2024-10-05",
        "end": "2024-10-05",
        "resourceId": "7A5181296",
    },
]
calendar_resources = [
    {"id": "573100743", "building": "Building A", "title": "Recuperado"},
    {"id": "593191683", "building": "Building A", "title": "Recuperado"},
    {"id": "593224848", "building": "Building B", "title": "Recuperado"},
    {"id": "5A3313002", "building": "Building B", "title": "Recuperado"},
    {"id": "5B3377212", "building": "Building C", "title": "Recuperado"},
    {"id": "5C3476857", "building": "Building C", "title": "Recuperado"},
    {"id": "5C3490555", "building": "Building A", "title": "Recuperado"},
    {"id": "623632894", "building": "Building A", "title": "Recuperado"},
    {"id": "643807414", "building": "Building B", "title": "Consumado"},
    {"id": "663942204", "building": "Building B", "title": "Recuperado"},
    {"id": "674023687", "building": "Building C", "title": "Recuperado"},
    {"id": "674040100", "building": "Building C", "title": "Consumado"},
    {"id": "694194103", "building": "Building A", "title": "Recuperado"},
    {"id": "694201020", "building": "Building A", "title": "Recuperado"},
    {"id": "6A4263104", "building": "Building B", "title": "Recuperado"},
    {"id": "6B4291744", "building": "Building B", "title": "Recuperado"},
    {"id": "6B4320698", "building": "Building C", "title": "Recuperado"},
    {"id": "6B4346404", "building": "Building C", "title": "Recuperado"},
    {"id": "6C4443693", "building": "Building A", "title": "Recuperado"},
    {"id": "6C4432388", "building": "Building A", "title": "Recuperado"},
    {"id": "6C4373527", "building": "Building B", "title": "Recuperado"},
    {"id": "714454863", "building": "Building B", "title": "Recuperado"},
    {"id": "724574182", "building": "Building C", "title": "Consumado"},
    {"id": "724595488", "building": "Building C", "title": "Recuperado"},
    {"id": "734622055", "building": "Building A", "title": "Recuperado"},
    {"id": "744747255", "building": "Building A", "title": "Consumado"},
    {"id": "754761468", "building": "Building B", "title": "Consumado"},
    {"id": "764857315", "building": "Building B", "title": "Recuperado"},
    {"id": "764876984", "building": "Building C", "title": "Recuperado"},
    {"id": "764881211", "building": "Building C", "title": "Consumado"},
    {"id": "764914584", "building": "Building C", "title": "Recuperado"},
    {"id": "774925043", "building": "Building A", "title": "Recuperado"},
    {"id": "785029284", "building": "Building A", "title": "Recuperado"},
    {"id": "785015581", "building": "Building B", "title": "Recuperado"},
    {"id": "795119424", "building": "Building B", "title": "Recuperado"},
    {"id": "795138262", "building": "Building C", "title": "Recuperado"},
    {"id": "795141649", "building": "Building C", "title": "Recuperado"},
    {"id": "795164396", "building": "Building A", "title": "Recuperado"},
    {"id": "795135543", "building": "Building B", "title": "Recuperado"},
    {"id": "795134072", "building": "Building B", "title": "Recuperado"},
    {"id": "795141834", "building": "Building C", "title": "Recuperado"},
    {"id": "7A5178364", "building": "Building C", "title": "Recuperado"},
    {"id": "7A5181694", "building": "Building B", "title": "Consumado"},
    {"id": "7A5181296", "building": "Building B", "title": "Recuperado"},
]

calendar_options = {
    "editable": "true",
    "navLinks": "true",
    "resources": calendar_resources,
}

if "resource" in mode:
    if mode == "resource-daygrid":
        calendar_options = {
            **calendar_options,
            "initialDate": "2023-07-01",
            "initialView": "resourceDayGridDay",
            "resourceGroupField": "building",
        }
    elif mode == "resource-timeline":
        calendar_options = {
            **calendar_options,
            "headerToolbar": {
                "left": "today prev,next",
                "center": "title",
                "right": "resourceTimelineDay,resourceTimelineWeek,resourceTimelineMonth",
            },
            "initialDate": "2023-07-01",
            "initialView": "resourceTimelineDay",
            "resourceGroupField": "building",
        }
    elif mode == "resource-timegrid":
        calendar_options = {
            **calendar_options,
            "initialDate": "2023-07-01",
            "initialView": "resourceTimeGridDay",
            "resourceGroupField": "building",
        }
else:
    if mode == "daygrid":
        calendar_options = {
            **calendar_options,
            "headerToolbar": {
                "left": "today prev,next",
                "center": "title",
                "right": "dayGridDay,dayGridWeek,dayGridMonth",
            },
            "initialDate": "2023-07-01",
            "initialView": "dayGridMonth",
        }
    elif mode == "timegrid":
        calendar_options = {
            **calendar_options,
            "initialView": "timeGridWeek",
        }
    elif mode == "timeline":
        calendar_options = {
            **calendar_options,
            "headerToolbar": {
                "left": "today prev,next",
                "center": "title",
                "right": "timelineDay,timelineWeek,timelineMonth",
            },
            "initialDate": "2023-07-01",
            "initialView": "timelineMonth",
        }
    elif mode == "list":
        calendar_options = {
            **calendar_options,
            "initialDate": "2023-07-01",
            "initialView": "listMonth",
        }
    elif mode == "multimonth":
        calendar_options = {
            **calendar_options,
            "initialView": "multiMonthYear",
        }

state = calendar(
    events=st.session_state.get("events", events),
    options=calendar_options,
    custom_css="""
    .fc-event-past {
        opacity: 0.8;
    }
    .fc-event-time {
        font-style: italic;
    }
    .fc-event-title {
        font-weight: 700;
    }
    .fc-toolbar-title {
        font-size: 2rem;
    }
    """,
    key=mode,
)

if state.get("eventsSet") is not None:
    st.session_state["events"] = state["eventsSet"]

st.write(state)