var map = L.map('map');
map.setView([51.6720400, 39.1843000], 11);

L.tileLayer.provider('OpenStreetMap.Mapnik').addTo(map);

function loadJSON(elementId) {
    let element = document.getElementById(elementId);

    return JSON.parse(element.textContent);
}

let places = loadJSON('places-geojson');

L.geoJSON(places, {
    pointToLayer: function (geoJsonPoint, latlng) {
        if (geoJsonPoint.geometry.type != "Point") {
            return
        }

        let marker = L.marker(latlng, {});

        marker.bindTooltip(geoJsonPoint.properties.full_name);

        return marker;
    }
}).addTo(map);
