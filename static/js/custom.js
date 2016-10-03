$(document).ready(function(){
  // $('#myTable').DataTable({ 
  //   "scrollX": true, "bLengthChange": false, 
  //   "pageLength": 50, "bPaginate": false, "bInfo": false,"searching": false,
  // });
  $('.accordion-toggle').click(function(){
    $(this).find("i").toggleClass("glyphicon-plus glyphicon-minus");
  });
});

$(document).ready(function(){
  var getUrlParameter = function getUrlParameter(sParam) {
  var sPageURL = decodeURIComponent(window.location.search.substring(1)),
    sURLVariables = sPageURL.split('&'),
    sParameterName,
    i;

    for (i = 0; i < sURLVariables.length; i++) {
      sParameterName = sURLVariables[i].split('=');
      if (sParameterName[0] === sParam) {
        return sParameterName[1] === undefined ? true : sParameterName[1];
      }
    }
  };
  var search = getUrlParameter('search');
  var sort = getUrlParameter('sort');
  var filter = getUrlParameter('filter');
  if(search != undefined)
  {
    $('#search-field').val(decodeURIComponent(search.replace('+',' ')));
  }
  if(sort != undefined)
  {
    $('#sortBy').val(decodeURIComponent(sort));
  }
  if(filter != undefined)
  {
    $('#filterBy').val(decodeURIComponent(filter));
  }
  if($('#search-field').val()!='')
  {
    $('.pagination').children('li').click(function(){
      $('#page-no').val($(this).children('a').attr('href').replace('?page=',''));
      $('#search-form').submit();
      return false;
    });
  }
});
