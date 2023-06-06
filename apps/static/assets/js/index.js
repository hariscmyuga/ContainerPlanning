// Initialize and add the map
let map;

async function initMap() {
  // The location of Uluru
  const position = { lat: 24.8, lng:55.16 };
  // Request needed libraries.
  //@ts-ignore
  const { Map } = await google.maps.importLibrary("maps");
  const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

  // The map, centered at Uluru
  map = new Map(document.getElementById("map"), {
    zoom: 7,
    center: position,
    mapId: "DEMO_MAP_ID",
  });

  // The marker, positioned at Uluru
//   const marker = new AdvancedMarkerElement({
//     map: map,
//     position: position,
//     title: "Uluru",
//   });
  var locations = [
    ['Port of Jebel Ali\nTotal Empty Stock:100\nTotal Safety Stock: 20\nPort Utilization: 58%', 25.024542560551026, 55.040449148392035, 4, "http://maps.google.com/mapfiles/ms/icons/green-dot.png"],
    // ['Port Zayed', 24.519971525665348, 54.38354246641824, 5],
    ['Khalifa Port\nEmpty Stock: 1200\nTotal Safety Stock: 100\nPort Utilization: 78%', 24.775676260514004, 54.71277542386746, 3, "http://maps.google.com/mapfiles/ms/icons/red-dot.png"],
    // ['Port Rashid', 25.285433261533946, 55.275027377144, 2],
    // ['Khalid Port', 25.36101566725319, 55.37764038155965, 1],
    // ['Hamriya Port', 25.467938140217075, 55.48388005272758, 1],
    // ['Port Dibba Al-Fujairah ', 25.609366926507995, 56.2922903950612, 1],
    // ['Khorfakkan Port', 25.35276442390363, 56.36775745272349, 1],
    ['Ruwais Port\nEmpty Stock: 200\nTotal Safety Stock: 75\nPort Utilization: 45%',24.136572932018442, 52.7569834238456,5, "http://maps.google.com/mapfiles/ms/icons/green-dot.png"]
  ];
  var infowindow = new google.maps.InfoWindow();

  var marker, i;
  
  for (i = 0; i < locations.length; i++) {  
    marker = new google.maps.Marker({
      position: new google.maps.LatLng(locations[i][1], locations[i][2]),
      map: map,
      title: locations[i][0],
      icon:  locations[i][4],
      
    });}
  google.maps.event.addListener(marker, 'click', (function(marker, i) {
    return function() {
      infowindow.setContent(locations[i][0]);
      infowindow.open(map, marker);
    }
  })(marker, i));

}

initMap();