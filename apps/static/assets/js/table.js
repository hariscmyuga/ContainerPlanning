var gridOptions = {};
var columnDefs = [];

function displayFunc(data, header)
{
    gridOptions = {
        columnDefs: header,
        rowData: data
      };
      
      
}
  // setup the grid after the page has finished loading
  document.addEventListener('DOMContentLoaded', () => {
    const gridDiv = document.querySelector('#myGrid');
    new agGrid.Grid(gridDiv, gridOptions);
}); 