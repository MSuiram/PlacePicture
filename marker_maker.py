import folium

def marker_maker(map : folium.Map, loc : list, image : str, name : str):
    folium.Marker(
        location= loc,
        tooltip= "Click !!",
        popup= f"""<div>
            <img src={image} width="230" height="172">
            <br /><span>{name}</span>
            </div>""",
    ).add_to(map)