import folium

def marker_maker(map : folium.Map, loc : list, popup : str):
    folium.Marker(
        location= loc,
        tooltip= "Click !!",
        popup= popup,
    ).add_to(map)