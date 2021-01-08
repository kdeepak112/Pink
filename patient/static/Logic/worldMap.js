function updateMap() {
  fetch("https://www.trackcorona.live/api/countries")
    .then((resp) => resp.json())
    .then((api) => {
      console.log(api.data);
      var arr = api.data;
      api.data.forEach((element) => {
        latitude = element.latitude;
        longitude = element.longitude;

        cases = element.confirmed;
        if (cases > 1000000) {
          color = "rgb(252, 94, 3)";
        } else if (cases > 500000 && cases < 1000000) {
          color = "rgb(252, 157, 3)";
        } else if (cases > 100000 && cases < 500000) {
          color = "rgb(252, 186, 3)";
        } else if (cases < 100000) {
          color = "rgb(252, 252, 3)";
        }

        new mapboxgl.Marker({
          draggable: false,
          color: color,
        })
          .setLngLat([longitude, latitude])
          .addTo(map);

        map.on("mouseenter", function () {
          // Change the cursor style as a UI indicator.
          map.getCanvas().style.cursor = "pointer";
          var arr = [longitude, latitude];
          var coordinates = arr.slice();
          var description = "e.features[0].properties.description";

          while (Math.abs(longitude - coordinates[0]) > 180) {
            coordinates[0] += longitude > coordinates[0] ? 360 : -360;
          }

          popup.setLngLat(coordinates).setHTML(description).addTo(map);
        });

        map.on("mouseleave", "places", function () {
          map.getCanvas().style.cursor = "";
          popup.remove();
        });
      });
    });
}

updateMap();
