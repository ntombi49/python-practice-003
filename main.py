def weather_graph():
    """
    This function draws a weather graph for four weeks.
    each week will be observing a specific attribute.
    WEEK 1: RAIN 🌧️ , WEEK 2: CLOUDS ☁️, WEEK 3: WIND 🍃, WEEK 4: SUN ☀️
    
    Returns:
        str: A string representation of the weather graph.
        
    i.e for RAIN: each character represents 10% of rain/attribute observed that day.
    0% - no character
    10% - 1 character
    20% - 2 characters
    ...
    
    Week 1: RAIN
    MON: 🌧️
    TUE: 🌧️🌧️🌧️🌧️🌧️
    WED: 🌧️🌧️🌧️
    THU: 🌧️🌧️🌧️🌧️
    FRI: 🌧️🌧️🌧️🌧️🌧️
    
    your task is to read data from a file 'weather.txt' and draw the graphs accordingly.
    """
     
    # Week emojis and titles
    week_emojis = ["🌧️", "☁️", "🍃", "☀️"]
    week_titles = ["RAIN", "CLOUDS", "WIND", "SUN"]
    days = ["MON", "TUE", "WED", "THU", "FRI"]

    # Reading the file
    with open("weather.txt", "r") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    weeks_data = []
    current_week = []

    # Parse the file into 4 weeks
    for line in lines[1:]: 
        if line == "---":
            if current_week:
                weeks_data.append(current_week)
                current_week = []
        else:
            number = int(line.split(":")[1].strip())
            current_week.append(number)
    if current_week:
        weeks_data.append(current_week)

    # Building the graph
    graph = ""
    for i, week in enumerate(weeks_data):
        graph += f"Week {i+1}: {week_titles[i]}\n"
        for day_index, value in enumerate(week):
            emoji_count = value // 10
            # Align day names to width 4
            graph += f"{days[day_index]:<4}: {week_emojis[i] * emoji_count}\n"
        graph += "\n"  # blank line between weeks

    return graph

print(weather_graph())
