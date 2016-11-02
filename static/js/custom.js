$(document).ready(function(){
  $('#myTable').DataTable({ 
    "scrollX": true, "bLengthChange": false, "aaSorting": [], 
    "pageLength": 50, "bPaginate": false, "bInfo": false,"searching": false,
  });
  $('.accordion-toggle').click(function(){
    $(this).find("i").toggleClass("glyphicon-plus glyphicon-minus");
  });
});

$(document).ready(function(){
  getIndustries();
  setCountries();
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
    if(filter!='country' && filter!='is_system' && filter!='industry')
      $('#search-field').val(decodeURIComponent(search.replace('+',' ')));

    $('#search-param').val(decodeURIComponent(search.replace('+',' ')));
  }
  if(sort != undefined)
  {
    $('#sortBy').val(decodeURIComponent(sort));
  }
  if(filter != undefined)
  {
    $('#filterBy').val(decodeURIComponent(filter));
    if(filter=='country')
    {
      $('.search-class').css('display','none');
      $('#country-select').css('display','block');
      $('#country-select').val(decodeURIComponent(search.replace('+',' ')));
    }
    if(filter=='industry')
    {
      $('.search-class').css('display','none');
      $('#industry-select').css('display','block');
    }
    if(filter=='is_system')
    {
      $('.search-class').css('display','none');
      $('#system-select').css('display','block');
      $('#system-select').val(decodeURIComponent(search.replace('+',' ')));
    }
    if(filter=='updated'||filter=='last_visited')
    {
      $('.search-class').css('display','none');
      $('#date-picker').css('display','block');
      $('#date-picker').val(decodeURIComponent(search.replace('+',' ')));
    }
  }
  if($('#search-field').val()!='' || filter != undefined)
  {
    $('.pagination').children('li').click(function(){
      $('#page-no').val($(this).children('a').attr('href').replace('?page=',''));
      $('#search-form').submit();
      return false;
    });
  }
  $('#filterBy').change(function(){
    if($(this).val() == 'country')
    {
      $('.search-class').css('display','none');
      $('#country-select').css('display','block');
    }
    else if($(this).val() == 'industry')
    {
      $('.search-class').css('display','none');
      $('#industry-select').css('display','block');
    }
    else if ($(this).val() == 'is_system')
    {
      $('.search-class').css('display','none');
      $('#system-select').css('display','block');
    }
    else if ($(this).val() == 'updated' || $(this).val() == 'last_visited')
    {
      $('.search-class').css('display','none');
      $('#date-picker').css('display','block');   
    }
    else
    {
      $('.search-class').css('display','none'); 
      $('#search-field').css('display','block');
    }

  });

  $('.search-class').change(function(){
    $('#search-param').val($(this).val());
  });
  
  function getIndustries()
  {
    $.ajax({
            url: "/get-all-industries/",
            type: "get",
            success: function(response) {
                var industriesHtml = '<option value="">Select Industry</option>';
                industriesArray = JSON.parse(response)
                for(var i=0;i<industriesArray.length;i++)
                {
                  industriesHtml += '<option value="'+industriesArray[i]._id.$oid+'">'+industriesArray[i].name+'</option>';
                }
                $('#industry-select').html(industriesHtml);
                if(filter=='industry')
                  $('#industry-select').val(decodeURIComponent(search.replace('+',' ')));
            }
        })
  }
  function setCountries()
  {
  var countries = ["afghanistan",
    "aland islands",
    "albania",
    "algeria",
    "american samoa",
    "andorra",
    "angola",
    "anguilla",
    "antarctica",
    "antigua and barbuda",
    "argentina",
    "armenia",
    "aruba",
    "australia",
    "austria",
    "azerbaijan",
    "bahamas",
    "bahrain",
    "bangladesh",
    "barbados",
    "belarus",
    "belgium",
    "belize",
    "benin",
    "bermuda",
    "bhutan",
    "bolivia",
    "bosnia and herzegovina",
    "botswana",
    "bouvet island",
    "brazil",
    "british indian ocean territory",
    "brunei darussalam",
    "bulgaria",
    "burkina faso",
    "burundi",
    "cambodia",
    "cameroon",
    "canada",
    "cape verde",
    "caribbean nations",
    "cayman islands",
    "central african republic",
    "chad",
    "chile",
    "china",
    "christmas island",
    "cocos (keeling) islands",
    "colombia",
    "comoros",
    "congo",
    "cook islands",
    "costa rica",
    "cote d’ivoire (ivory coast)",
    "croatia",
    "cuba",
    "cyprus",
    "czech republic",
    "democratic republic of the congo",
    "denmark",
    "djibouti",
    "dominica",
    "dominican republic",
    "east timor",
    "ecuador",
    "egypt",
    "el salvador",
    "equatorial guinea",
    "eritrea",
    "estonia",
    "ethiopia",
    "falkland islands (malvinas)",
    "faroe islands",
    "federated states of micronesia",
    "fiji",
    "finland",
    "france",
    "french guiana",
    "french polynesia",
    "french southern territories",
    "gabon",
    "gambia",
    "georgia",
    "germany",
    "ghana",
    "gibraltar",
    "greece",
    "greenland",
    "grenada",
    "guadeloupe",
    "guam",
    "guatemala",
    "guernsey",
    "guinea",
    "guinea-bissau",
    "guyana",
    "haiti",
    "heard island and mcdonald islands",
    "honduras",
    "hong kong",
    "hungary",
    "iceland",
    "india",
    "indonesia",
    "iran",
    "iraq",
    "ireland",
    "isle of man",
    "israel",
    "italy",
    "jamaica",
    "japan",
    "jersey",
    "jordan",
    "kazakhstan",
    "kenya",
    "kiribati",
    "korea",
    "korea (north)",
    "kosovo",
    "kuwait",
    "kyrgyzstan",
    "laos",
    "latvia",
    "lebanon",
    "lesotho",
    "liberia",
    "libya",
    "liechtenstein",
    "lithuania",
    "luxembourg",
    "macao",
    "macedonia",
    "madagascar",
    "malawi",
    "malaysia",
    "maldives",
    "mali",
    "malta",
    "marshall islands",
    "martinique",
    "mauritania",
    "mauritius",
    "mayotte",
    "mexico",
    "moldova",
    "monaco",
    "mongolia",
    "montenegro",
    "montserrat",
    "morocco",
    "mozambique",
    "myanmar",
    "namibia",
    "nauru",
    "nepal",
    "netherlands",
    "netherlands antilles",
    "new caledonia",
    "new zealand",
    "nicaragua",
    "niger",
    "nigeria",
    "niue",
    "norfolk island",
    "northern mariana islands",
    "norway",
    "other",
    "pakistan",
    "palau",
    "palestinian territory",
    "panama",
    "papua new guinea",
    "paraguay",
    "peru",
    "philippines",
    "pitcairn",
    "poland",
    "portugal",
    "puerto rico",
    "qatar",
    "reunion",
    "romania",
    "russian federation",
    "rwanda",
    "s. georgia and s. sandwich islands",
    "saint helena",
    "saint kitts and nevis",
    "saint lucia",
    "saint pierre and miquelon",
    "saint vincent and the grenadines",
    "samoa",
    "san marino",
    "sao tome and principe",
    "saudi arabia",
    "senegal",
    "serbia",
    "serbia and montenegro",
    "seychelles",
    "sierra leone",
    "singapore",
    "slovak republic",
    "slovenia",
    "solomon islands",
    "somalia",
    "south africa",
    "south sudan",
    "spain",
    "sri lanka",
    "sudan",
    "sultanate of oman",
    "suriname",
    "svalbard and jan mayen",
    "swaziland",
    "sweden",
    "switzerland",
    "syria",
    "taiwan",
    "tajikistan",
    "tanzania",
    "thailand",
    "timor-leste",
    "togo",
    "tokelau",
    "tonga",
    "trinidad and tobago",
    "tunisia",
    "turkey",
    "turkmenistan",
    "turks and caicos islands",
    "tuvalu",
    "uganda",
    "ukraine",
    "united arab emirates",
    "united kingdom",
    "united states",
    "uruguay",
    "uzbekistan",
    "vanuatu",
    "vatican city state (holy see)",
    "venezuela",
    "vietnam",
    "virgin islands (british)",
    "virgin islands (u.s.)",
    "wallis and futuna",
    "western sahara",
    "yemen",
    "zambia",
    "zimbabwe"];
    var countryHtml='<option value="">Select Country</option>';
    for(var i=0;i<countries.length;i++)
    {
      countryHtml += '<option value="'+countries[i]+'">'+countries[i]+'</option>';
    }
    $('#country-select').html(countryHtml);
  }


});
